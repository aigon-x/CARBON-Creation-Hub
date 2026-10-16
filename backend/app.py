from __future__ import annotations

import fcntl
import hashlib
import hmac
import json
import os
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel, Field

from .state import aggregate_state
from overdrive.payment_truth import payment_state
from .store import EvidenceStore, SCHEMA_VERSION, T10_FIELDS, T10_SCHEMA


class SearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=500)
    limit: int = Field(default=8, ge=1, le=50)


class ProposalChangeRequest(BaseModel):
    selected_modules: list[str] = Field(default_factory=list, max_length=20)
    message: str = Field(default="", max_length=1200)
    contact: str = Field(default="", max_length=120)
    action: str = Field(default="REQUEST_CHANGE", pattern="^(REQUEST_CHANGE|REQUEST_CALLBACK)$")


class EvidencePayload(BaseModel):
    evidence_id: str
    capability: str
    artifact: str
    authoritative_source: str
    source_pointer: str | None = None
    date_version: str | None = None
    role_contribution: str | None = None
    acceptance_test: str | None = None
    durable_receipts: list[str] = Field(default_factory=list)
    durable_receipt: str | None = None
    artifact_hash: str | None = None
    source_hash: str | None = None
    status_freshness: str
    interview_safe_explanation: str
    T10_JOB: str
    T10_ACTUAL: str
    T10_EVIDENCE: str
    T10_CHANGE: str
    T10_REMAINING_GAP: str
    T10_PASS: str = Field(pattern="^(PASS|HOLD|FAIL|UNKNOWN)$")
    inspect_route: str | None = None
    visibility: str = "PRIVATE"
    tags: list[str] = Field(default_factory=list)



CARBON_BUSINESS_SEARCH_HEALTH_URL = "https://carbon-search-intention-v1.onrender.com/api/search/health"
CARBON_BUSINESS_MARKET_BOOTSTRAP_URL = "https://carbon-intent-marketplace-v1-preview.onrender.com/api/carbon/bootstrap"

CARBON_BUSINESS_SERVICES: list[dict[str, Any]] = [
    {
        "id": "website-presence",
        "name": "Website & Digital Presence",
        "family": "Build and convert",
        "readiness": "SCOPED / PILOT",
        "summary": "Create or improve a business website, landing page, catalogue, enquiry path or customer-facing digital experience.",
        "deliverable": "A scoped brief, page structure and visual direction; implementation and launch terms are agreed before work is promised.",
        "current_limit": "Self-service payment, automated mockup acceptance and an instantly provisioned interactive trial are not yet verified for this service.",
        "route": "/business/services/website-presence",
        "product_url": "",
        "action_label": "Request a scope by email",
        "action_url": "mailto:amillimatrix@gmail.com?subject=CARBON%20Website%20%26%20Digital%20Presence%20Scope",
    },
    {
        "id": "quick-technical-review",
        "name": "Quick Technical Review",
        "family": "Fixed-scope review",
        "readiness": "AVAILABLE",
        "summary": "A concise written review of one public repository URL or a non-sensitive code/config excerpt of up to 100 lines.",
        "deliverable": "Key findings, up to three prioritized recommendations, and one concrete example fix where the supplied evidence supports it.",
        "current_limit": "No live penetration testing, production access, secrets handling, implementation work or guarantee that a vulnerability exists. Follow-up material must exclude secrets and private customer data.",
        "route": "/business/services/quick-technical-review",
        "product_url": "https://amx-evidence-house.onrender.com/house/#micro-matrix-offer",
        "action_label": "Buy the fixed-scope review — US$4.99",
        "action_url": "https://buy.stripe.com/9B6eVd7hfeTCaYh62eaR200",
    },
    {
        "id": "brand-communications",
        "name": "Brand & Communications",
        "family": "Look professional",
        "readiness": "SCOPED / PILOT",
        "summary": "Refine business positioning, brand presentation, typography, messaging, signage, menus, price lists and reusable assets.",
        "deliverable": "A scoped set of brand or communication recommendations and agreed assets, using the customer's brand as the lead.",
        "current_limit": "Availability, deliverables, rights, revisions and price must be confirmed for the specific engagement.",
        "route": "/business/services/brand-communications",
        "product_url": "",
        "action_label": "Request a scope by email",
        "action_url": "mailto:amillimatrix@gmail.com?subject=CARBON%20Brand%20%26%20Communications%20Scope",
    },
    {
        "id": "social-campaigns",
        "name": "Social Presence & Campaigns",
        "family": "Get found",
        "readiness": "SCOPED / PILOT",
        "summary": "Improve social profiles and plan useful content, promotions, publishing support and performance reporting.",
        "deliverable": "An agreed campaign or content package sized to the business goal and supplied assets.",
        "current_limit": "Live account integrations, publishing permissions, recurring campaign operations and performance access are confirmed individually; none is implied by this listing.",
        "route": "/business/services/social-campaigns",
        "product_url": "",
        "action_label": "Request a scope by email",
        "action_url": "mailto:amillimatrix@gmail.com?subject=CARBON%20Social%20Presence%20%26%20Campaigns",
    },
    {
        "id": "customer-sales-journey",
        "name": "Customer & Sales Journey",
        "family": "Sell and serve",
        "readiness": "SCOPED / PILOT",
        "summary": "Improve enquiries, bookings, ordering, digital menus, product catalogues, customer follow-up and after-sales journeys.",
        "deliverable": "A mapped customer path and an agreed set of practical changes or digital assets.",
        "current_limit": "Third-party messaging, commerce and payment integrations require individual route, permission and end-to-end checks before they can be promised.",
        "route": "/business/services/customer-sales-journey",
        "product_url": "",
        "action_label": "Request a scope by email",
        "action_url": "mailto:amillimatrix@gmail.com?subject=CARBON%20Customer%20%26%20Sales%20Journey",
    },
    {
        "id": "workflow-automation",
        "name": "Workflow Automation & Integration",
        "family": "Run better",
        "readiness": "SCOPED / PILOT",
        "summary": "Identify repetitive work and scope forms, internal dashboards, APIs or supported platform integrations.",
        "deliverable": "A scoped workflow design and a tested implementation where the needed access, runtime and provider capability are available.",
        "current_limit": "No integration is treated as connected until credentials/permissions, successful execution, failure handling and durable readback are proven.",
        "route": "/business/services/workflow-automation",
        "product_url": "",
        "action_label": "Request a scope by email",
        "action_url": "mailto:amillimatrix@gmail.com?subject=CARBON%20Workflow%20Automation%20Scope",
    },
    {
        "id": "stock-operations",
        "name": "Stock & Operations Intelligence",
        "family": "Run better",
        "readiness": "SCOPED / PILOT",
        "summary": "Review authorized stock, sales and customer-demand data for stock rotation, reorder prompts, wastage and operational friction.",
        "deliverable": "Recommendations or a scoped operational workflow based on data the business is authorized to share.",
        "current_limit": "No live POS, supplier, inventory or customer-data integration is implied. Data source, access, and rights must be checked first.",
        "route": "/business/services/stock-operations",
        "product_url": "",
        "action_label": "Request a scope by email",
        "action_url": "mailto:amillimatrix@gmail.com?subject=CARBON%20Stock%20%26%20Operations%20Scope",
    },
    {
        "id": "apps-portals",
        "name": "Apps, Portals & Customer Tools",
        "family": "Build digital capability",
        "readiness": "SCOPED / PILOT",
        "summary": "Scope lightweight web apps, installable PWAs, customer portals and internal tools when they solve a clear business problem.",
        "deliverable": "A defined user flow, implementation scope and release/hosting plan.",
        "current_limit": "The automatic quote-to-payment-to-interactive-trial path is not yet verified for this service; hosting, persistence, access control and delivery conditions must be agreed.",
        "route": "/business/services/apps-portals",
        "product_url": "",
        "action_label": "Request a scope by email",
        "action_url": "mailto:amillimatrix@gmail.com?subject=CARBON%20App%20or%20Portal%20Scope",
    },
    {
        "id": "intent-search",
        "name": "CARBON° Search / INTELLAGENT",
        "family": "Find the right next step",
        "readiness": "SCOPED / PILOT",
        "summary": "An intent-led Search interface designed to interpret a need, compare relevant evidence and route to a useful next action.",
        "deliverable": "The current public Search interface is reachable; live external search coverage must be checked separately.",
        "current_limit": "External search-provider integrations are not currently verified as connected.",
        "route": "/business/services/intent-search",
        "product_url": "https://carbon-search-intention-v1.onrender.com/search",
        "action_label": "Open Search",
        "action_url": "https://carbon-search-intention-v1.onrender.com/search",
    },
    {
        "id": "marketplace",
        "name": "CARBON° Marketplace",
        "family": "Match a need with an offer",
        "readiness": "SCOPED / PILOT",
        "summary": "A live Marketplace interface for listing, discovery and intent-based matching where eligible listings and connected sources exist.",
        "deliverable": "The current interface is reachable and shows an honest empty state; no external listings are promised.",
        "current_limit": "External listing providers are not verified as connected, and the current Marketplace money adapter reports that no real money moves through it.",
        "route": "/business/services/marketplace",
        "product_url": "https://carbon-intent-marketplace-v1-preview.onrender.com/market",
        "action_label": "Open Marketplace",
        "action_url": "https://carbon-intent-marketplace-v1-preview.onrender.com/market",
    },
    {
        "id": "studios",
        "name": "CARBON Studios",
        "family": "Create and fulfil",
        "readiness": "SCOPED / PILOT",
        "summary": "The creation and production layer for agreed brand assets, copy, listings, images and selected media deliverables.",
        "deliverable": "A defined brief, preview/review step and a scoped deliverable where the required production route is available.",
        "current_limit": "A populated, buyer-ready searchable Studios catalogue and a fully automated preview-to-trial workflow are not yet verified.",
        "route": "/business/services/studios",
        "product_url": "",
        "action_label": "Discuss a scoped brief",
        "action_url": "mailto:amillimatrix@gmail.com?subject=CARBON%20Studios%20Production%20Brief",
    },
]

def _fetch_public_json(url: str, timeout: float = 2.0) -> dict[str, Any]:
    """Read a fixed public health/bootstrap endpoint without propagating its failure."""
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "AMX-CARBON-Business-Readiness/1.0",
            "Cache-Control": "no-cache",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
            if not isinstance(payload, dict):
                return {"reachable": False, "http_status": getattr(response, "status", 200), "data": {}, "failure": "INVALID_RESPONSE"}
            return {
                "reachable": 200 <= int(getattr(response, "status", 200)) < 300,
                "http_status": int(getattr(response, "status", 200)),
                "data": payload,
                "failure": None,
            }
    except urllib.error.HTTPError as exc:
        return {"reachable": False, "http_status": exc.code, "data": {}, "failure": "HTTP_ERROR"}
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, UnicodeError):
        return {"reachable": False, "http_status": None, "data": {}, "failure": "CONNECTION_OR_RESPONSE_ERROR"}


def create_app(repo_root: Path | None = None, db_path: Path | None = None) -> FastAPI:
    root = Path(repo_root or os.getenv("AMX_REPO_ROOT") or Path(__file__).resolve().parents[1]).resolve()
    db = Path(db_path or os.getenv("AMX_DB_PATH") or root / "data/amx_evidence.db").resolve()
    store = EvidenceStore(db)
    seed_stats = store.import_seed(root / "evidence/index.json")

    app = FastAPI(title="AMilliMATRiX Evidence + House Control Backend", version="2.0.0")
    app.state.repo_root = root
    app.state.store = store
    app.state.seed_stats = seed_stats

    def house_visible(record: dict[str, Any]) -> bool:
        return str(record.get("visibility", "PRIVATE")).upper() in {"HOUSE", "PUBLIC"}

    def visible_evidence() -> list[dict[str, Any]]:
        return [r for r in store.list() if house_visible(r)]

    def t10_contract(records: list[dict[str, Any]]) -> dict[str, Any]:
        return {
            "schema": T10_SCHEMA,
            "fields": list(T10_FIELDS),
            "rule": "Activity is not outcome. A hypothesis is not a finding. A remediation action is not a verified fix until the original condition is retested.",
            "coverage": store.t10_coverage(records),
        }

    origins = [o.strip() for o in os.getenv("AMX_CORS_ORIGINS", "").split(",") if o.strip()]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins or [],
        allow_credentials=False,
        allow_methods=["GET", "POST", "PUT"],
        allow_headers=["Content-Type", "X-AMX-Admin"],
    )

    def require_admin(x_amx_admin: str | None = Header(default=None)) -> None:
        secret = os.getenv("AMX_ADMIN_TOKEN")
        if not secret:
            raise HTTPException(status_code=503, detail="admin writes disabled: AMX_ADMIN_TOKEN is not configured")
        if not x_amx_admin or not hmac.compare_digest(x_amx_admin, secret):
            raise HTTPException(status_code=401, detail="invalid admin credential")

    @app.get("/", include_in_schema=False)
    def public_entry():
        if not (root / "house/remediation/index.html").is_file():
            raise HTTPException(status_code=503, detail="House interface unavailable")
        return RedirectResponse(url="/house", status_code=307)

    @app.get("/api/health")
    def health() -> dict[str, Any]:
        records = visible_evidence()
        return {
            "status": "CONNECTED",
            "backend": "provider-neutral/local",
            "schema_version": SCHEMA_VERSION,
            "state_source": "LOCAL_SNAPSHOT",
            "seed_import": app.state.seed_stats,
            "t10": t10_contract(records),
        }

    @app.get("/api/t10", dependencies=[Depends(require_admin)])
    def t10_status() -> dict[str, Any]:
        state = aggregate_state(root)
        records = visible_evidence()
        return {
            **t10_contract(records),
            "operator": state.get("t10"),
            "truth_screen": state.get("system_truth_t10"),
        }

    @app.get("/api/evidence")
    def list_evidence() -> dict[str, Any]:
        records = visible_evidence()
        return {
            "records": records,
            "count": len(records),
            "state_source": "LOCAL_DB",
            "t10": t10_contract(records),
        }

    @app.get("/api/evidence/{evidence_id}")
    def get_evidence(evidence_id: str) -> dict[str, Any]:
        record = store.get(evidence_id)
        if record is None or not house_visible(record):
            raise HTTPException(status_code=404, detail="evidence record not found")
        return record

    @app.get("/api/evidence/{evidence_id}/versions", dependencies=[Depends(require_admin)])
    def get_evidence_versions(evidence_id: str) -> dict[str, Any]:
        if store.get(evidence_id) is None:
            raise HTTPException(status_code=404, detail="evidence record not found")
        versions = store.versions(evidence_id)
        return {"evidence_id": evidence_id, "versions": versions, "count": len(versions)}

    @app.post("/api/evidence/search")
    def search_evidence(req: SearchRequest) -> dict[str, Any]:
        results = [r for r in store.search(req.query, req.limit * 2) if house_visible(r)][:req.limit]
        return {
            "query": req.query,
            "supported": bool(results),
            "results": results,
            "count": len(results),
            "gap": None if results else "No governed evidence matched this query. UNKNOWN/HOLD over inference.",
            "retrieval": "SQLite FTS5 / deterministic local search",
        }

    @app.put("/api/evidence/{evidence_id}", dependencies=[Depends(require_admin)])
    def put_evidence(evidence_id: str, payload: EvidencePayload) -> dict[str, Any]:
        body = payload.model_dump()
        if body["evidence_id"] != evidence_id:
            raise HTTPException(status_code=400, detail="path evidence_id must match payload evidence_id")
        try:
            record, changed = store.upsert(body)
        except ValueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        return {"record": record, "changed": changed}

    @app.post("/api/evidence/export", dependencies=[Depends(require_admin)])
    def export_evidence() -> dict[str, Any]:
        target = root / "evidence/export.json"
        payload = store.export_projection(target)
        return {
            "path": str(target.relative_to(root)),
            "count": len(payload["records"]),
            "generated_at": payload["generated_at"],
            "t10": payload["t10"],
        }

    @app.get("/api/operator/state", dependencies=[Depends(require_admin)])
    def operator_state() -> dict[str, Any]:
        return aggregate_state(root)

    @app.get("/api/neural/proof", dependencies=[Depends(require_admin)])
    def neural_proof() -> dict[str, Any]:
        from neural.router import exercise
        return exercise(root)

    @app.get("/api/opportunities", dependencies=[Depends(require_admin)])
    def opportunities() -> dict[str, Any]:
        return aggregate_state(root)["opportunities"]

    @app.get("/api/opportunities/{record_key:path}", dependencies=[Depends(require_admin)])
    def opportunity(record_key: str) -> dict[str, Any]:
        import json
        path = root / "overdrive/opportunities.json"
        payload = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"records": {}}
        record = payload.get("records", {}).get(record_key)
        if record is None:
            raise HTTPException(status_code=404, detail="opportunity not found")

        record = dict(record)
        record["state"] = payment_state(record, record_key)
        if record["state"] == "PAYMENT_UNVERIFIED":
            record.pop("t10", None)
            record.pop("T10", None)
        native_t10 = record.get("t10") or record.get("T10")
        if isinstance(native_t10, dict) and all(str(native_t10.get(field, "")).strip() for field in T10_FIELDS):
            outcome = {field: native_t10[field] for field in T10_FIELDS}
        else:
            evidence_items = record.get("evidence", [])
            evidence_count = len(evidence_items) if isinstance(evidence_items, list) else 0
            outcome = {
                "T10_JOB": str(record.get("next_action") or "Preserve and verify the current commercial outcome without inferring closure."),
                "T10_ACTUAL": (
                    f"Current durable state={record.get('state', 'UNKNOWN')}; "
                    f"execution_owner={record.get('execution_owner', 'UNKNOWN')}; "
                    f"last_action_at={record.get('last_action_at', 'UNKNOWN')}."
                ),
                "T10_EVIDENCE": f"overdrive/opportunities.json::records/{record_key}; embedded evidence items={evidence_count}",
                "T10_CHANGE": "This read exposes the latest durable ledger state only; it does not infer a newer conversion, acceptance, payment, or closure outcome.",
                "T10_REMAINING_GAP": (
                    "This opportunity record does not yet carry native T10 outcome fields. "
                    f"Current next action: {record.get('next_action') or 'not explicitly recorded; closure remains unproven.'}"
                ),
                "T10_PASS": "HOLD",
            }
        return {"record_key": record_key, "record": record, "t10": outcome}

    def proposal_registry() -> dict[str, Any]:
        configured = os.getenv("AMX_PROPOSAL_REGISTRY_PATH", "")
        if not configured:
            raise HTTPException(status_code=404, detail="customer portal disabled")
        path = Path(configured).resolve()
        if path.is_relative_to(root):
            raise HTTPException(status_code=503, detail="proposal registry must be private runtime storage outside the repository")
        if not path.exists():
            return {"schema": "AMX_CARBON_CUSTOMER_PORTAL_V1", "proposals": {}}
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise HTTPException(status_code=503, detail="proposal registry unavailable") from exc
        if not isinstance(payload, dict) or not isinstance(payload.get("proposals"), dict):
            raise HTTPException(status_code=503, detail="proposal registry invalid")
        return payload

    def proposal_projection(portal_token: str) -> dict[str, Any]:
        record = proposal_registry()["proposals"].get(portal_token)
        if not isinstance(record, dict):
            raise HTTPException(status_code=404, detail="proposal not found")

        if str(record.get("status", "")).upper() in {"REVOKED", "CANCELLED"}:
            raise HTTPException(status_code=404, detail="proposal not found")
        public_fields = {"proposal_ref", "business_name", "status", "issued_at", "validity_hours", "full_proposal_url",
                         "headline", "subhead", "visual_note", "visuals", "market_context", "offer", "modules", "sources"}
        projected = {k: v for k, v in record.items() if k in public_fields}
        issued_at = projected.get("issued_at")
        validity_hours = int(projected.get("validity_hours") or 24)
        status = str(projected.get("status") or "DRAFT").upper()
        valid_until = None

        if status in {"REVOKED", "CANCELLED"}:
            quote_status = status
        elif not issued_at:
            quote_status = "DRAFT_NOT_ISSUED"
        else:
            try:
                issued = datetime.fromisoformat(str(issued_at).replace("Z", "+00:00"))
                if issued.tzinfo is None:
                    issued = issued.replace(tzinfo=timezone.utc)
                valid_until_dt = issued.astimezone(timezone.utc) + timedelta(hours=validity_hours)
                valid_until = valid_until_dt.isoformat().replace("+00:00", "Z")
                quote_status = "ACTIVE" if datetime.now(timezone.utc) < valid_until_dt else "EXPIRED"
            except ValueError:
                quote_status = "UNKNOWN"

        projected["portal_token"] = portal_token
        projected["quote_status"] = quote_status
        projected["valid_until"] = valid_until
        projected["validity_hours"] = validity_hours
        return projected

    @app.get("/api/proposals/{portal_token}")
    def customer_proposal(portal_token: str) -> dict[str, Any]:
        return proposal_projection(portal_token)

    @app.post("/api/proposals/{portal_token}/request-change")
    def customer_proposal_change(portal_token: str, payload: ProposalChangeRequest) -> dict[str, Any]:
        proposal = proposal_projection(portal_token)
        allowed = {str(item.get("id")) for item in proposal.get("modules", []) if isinstance(item, dict)}
        selected = sorted({module for module in payload.selected_modules if module in allowed})
        association = proposal_registry()["proposals"][portal_token]
        opportunity_key = association.get("opportunity_key")
        ledger_path = root / "overdrive/opportunities.json"
        ledger = json.loads(ledger_path.read_text()) if ledger_path.exists() else {}
        record = ledger.get("records", {}).get(opportunity_key, {})
        if (record.get("execution_owner") != "PRI" or not record.get("thread_id")
                or association.get("thread_id") != record["thread_id"] or not association.get("customer_id")):
            raise HTTPException(status_code=503, detail="verified PRI customer/thread association required")
        identity = {"opportunity_key": opportunity_key, "thread_id": record["thread_id"],
                    "customer_id": association["customer_id"], "proposal_ref": proposal["proposal_ref"],
                    "action": payload.action, "selected_modules": selected,
                    "message": payload.message.strip(), "contact": payload.contact.strip()}
        request_id = "CPR-" + hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()[:24].upper()
        receipt = {
            "request_id": request_id,
            "received_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "proposal_ref": proposal.get("proposal_ref"),
            **identity,
            "quote_status_at_request": proposal.get("quote_status"),
            "action": payload.action,
            "selected_modules": selected,
            "message": payload.message.strip(),
            "contact": payload.contact.strip(),
            "binding": False,
            "note": "Customer portal request only. It does not automatically modify, accept, invoice, or pay the quote.",
        }
        target = Path(os.getenv("AMX_CUSTOMER_REQUEST_PATH", str(root / "data/proposal_requests.jsonl")))
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("a+", encoding="utf-8") as handle:
            fcntl.flock(handle, fcntl.LOCK_EX)
            handle.seek(0)
            existing = [json.loads(line) for line in handle if line.strip()]
            if not any(r.get("request_id") == request_id for r in existing):
                handle.seek(0, 2)
                handle.write(json.dumps(receipt, ensure_ascii=False) + "\n")
                handle.flush()
                os.fsync(handle.fileno())
        return {"request_id": request_id, "received": True, "binding": False}

    @app.get("/api/customer-requests/{request_id}", dependencies=[Depends(require_admin)])
    def private_customer_request(request_id: str) -> dict[str, Any]:
        target = Path(os.getenv("AMX_CUSTOMER_REQUEST_PATH", str(root / "data/proposal_requests.jsonl")))
        if target.exists():
            with target.open() as handle:
                fcntl.flock(handle, fcntl.LOCK_SH)
                for line in handle:
                    request = json.loads(line)
                    if request.get("request_id") == request_id:
                        return request
        raise HTTPException(status_code=404, detail="customer request not found")

    @app.get("/api/house/bootstrap")
    def house_bootstrap() -> dict[str, Any]:
        state = aggregate_state(root)
        evidence = visible_evidence()
        gallery = [
            r for r in evidence
            if "carbon" in str(r.get("capability", "")).lower()
            or "production" in str(r.get("capability", "")).lower()
        ]
        return {
            "backend": {
                "status": "DEGRADED" if state.get("adapter_errors") else "CONNECTED",
                "state_source": state["state_source"],
                "refreshed_at": state["refreshed_at"],
                "adapter_errors": state.get("adapter_errors", []),
            },
            "operator": {"state_source": state["state_source"], "refreshed_at": state["refreshed_at"]},
            "evidence": {"count": len(evidence), "records": evidence},
            "gallery": gallery,
            "t10": t10_contract(evidence),
            "controls": {
                "no_false_live_state": True,
                "unknown_hold_over_inference": True,
                "full_ledger_not_routing_subset": True,
                "model_not_matrix": True,
                "t10_outcome_truth": True,
                "activity_not_outcome": True,
                "remediation_requires_original_condition_retest": True,
            },
        }

    @app.get("/api/business/services")
    def carbon_business_services() -> dict[str, Any]:
        # The health checks are read-only and parallel so the service directory never
        # depends on either product being up. A failed check is a defined recovery state.
        with ThreadPoolExecutor(max_workers=2) as pool:
            search_future = pool.submit(_fetch_public_json, CARBON_BUSINESS_SEARCH_HEALTH_URL)
            market_future = pool.submit(_fetch_public_json, CARBON_BUSINESS_MARKET_BOOTSTRAP_URL)
            search_probe = search_future.result()
            market_probe = market_future.result()

        search_data = search_probe.get("data", {})
        market_data = market_probe.get("data", {})
        search_reachable = search_probe.get("reachable") is True and search_data.get("status") == "CONNECTED"
        discovery = market_data.get("discovery") if isinstance(market_data.get("discovery"), dict) else {}
        market_reachable = market_probe.get("reachable") is True and market_data.get("product") == "CARBON°"
        listings = market_data.get("listings") if isinstance(market_data.get("listings"), list) else []
        external_search = discovery.get("external_search_connected") is True
        external_marketplace = discovery.get("external_marketplace_connected") is True
        money_adapter = str(market_data.get("money_adapter") or "NOT_VERIFIED")
        money_moved = market_data.get("money_moved") is True

        if not search_reachable:
            search_message = "The latest live check could not confirm the Search route. Check the route before promising availability."
        elif str(search_data.get("external_provider") or "UNCONFIGURED").upper() == "UNCONFIGURED":
            search_message = "The Search interface is reachable, but external search providers are not connected."
        else:
            search_message = "The Search interface is reachable. The current provider configuration still needs a live query and result-readback test."

        if not market_reachable:
            marketplace_message = "The latest live check could not confirm the Marketplace backend. Check the route before promising availability."
        elif not external_search and not external_marketplace:
            marketplace_message = f"The Marketplace interface is reachable with {len(listings)} current listing(s), but external search and listing sources are not connected."
        else:
            marketplace_message = f"The Marketplace interface is reachable with {len(listings)} current listing(s). Any connected source still requires result-level verification."

        services = [dict(item) for item in CARBON_BUSINESS_SERVICES]
        for service in services:
            if service["id"] == "intent-search":
                service["current_limit"] = search_message
                service["runtime_state"] = "CONNECTED" if search_reachable else "CHECK_FAILED"
            elif service["id"] == "marketplace":
                service["current_limit"] = marketplace_message
                service["runtime_state"] = "CONNECTED" if market_reachable else "CHECK_FAILED"
                service["listing_count"] = len(listings)
                service["real_money_moved_in_current_bootstrap"] = money_moved
                service["money_adapter_state"] = (
                    "NO_REAL_MONEY_MOVED"
                    if money_adapter == "SANDBOX_NO_MONEY_MOVED" and not money_moved
                    else "SEPARATE_VERIFICATION_REQUIRED"
                )

        return {
            "checked_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "services": services,
            "runtime": {
                "search": {
                    "state": "CONNECTED" if search_reachable else "CHECK_FAILED",
                    "message": search_message,
                },
                "marketplace": {
                    "state": "CONNECTED" if market_reachable else "CHECK_FAILED",
                    "message": marketplace_message,
                    "listing_count": len(listings),
                    "external_search_connected": external_search,
                    "external_marketplace_connected": external_marketplace,
                    "money_moved": money_moved,
                    "money_adapter_state": (
                        "NO_REAL_MONEY_MOVED"
                        if money_adapter == "SANDBOX_NO_MONEY_MOVED" and not money_moved
                        else "SEPARATE_VERIFICATION_REQUIRED"
                    ),
                },
            },
            "personal_referral": {
                "state": "NOT_CONNECTED",
                "message": "Direct service links can be shared now. Personal referral attribution and referral-credit tracking are not active until the existing canonical identity/referral route is verified.",
            },
        }

    house_dir = root / "house/remediation"
    if house_dir.exists():
        @app.get("/house/assets/{asset}")
        def public_asset(asset: str):
            if asset == "config.js":
                from fastapi.responses import Response
                return Response('window.AMX_API_BASE = "";', media_type="application/javascript")
            if asset not in {"house.css", "house.js", "proposal.css", "proposal.js"}:
                raise HTTPException(status_code=404, detail="asset not found")
            path = house_dir / asset
            if path.is_symlink() or not path.is_file():
                raise HTTPException(status_code=404, detail="asset not found")
            return FileResponse(path)

        @app.get("/proposal/{portal_token}")
        @app.get("/proposal/{portal_token}/")
        def customer_proposal_page(portal_token: str):
            proposal_projection(portal_token)
            return FileResponse(house_dir / "proposal.html")

        @app.get("/business")
        @app.get("/business/")
        def carbon_business_index():
            path = house_dir / "business.html"
            if path.is_symlink() or not path.is_file():
                raise HTTPException(status_code=503, detail="CARBON Business directory unavailable")
            return FileResponse(path)

        @app.get("/business/services/{service_slug}")
        def carbon_business_service(service_slug: str):
            allowed_slugs = {item["id"] for item in CARBON_BUSINESS_SERVICES}
            if service_slug not in allowed_slugs:
                raise HTTPException(status_code=404, detail="Carbon service not found")
            path = house_dir / "business.html"
            if path.is_symlink() or not path.is_file():
                raise HTTPException(status_code=503, detail="CARBON Business directory unavailable")
            return FileResponse(path)

        @app.get("/house")
        @app.get("/house/")
        def house_index():
            return FileResponse(house_dir / "index.html")

    return app


app = create_app()
