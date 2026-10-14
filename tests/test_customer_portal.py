import hashlib
import json
from pathlib import Path

from fastapi.testclient import TestClient

from backend.app import create_app


def portal_client(tmp_path: Path, monkeypatch) -> TestClient:
    (tmp_path / "evidence").mkdir(parents=True)
    (tmp_path / "house/remediation").mkdir(parents=True)
    (tmp_path / "evidence/index.json").write_text(json.dumps({"records": []}), encoding="utf-8")
    (tmp_path / "house/remediation/proposal.html").write_text("<html>proposal</html>", encoding="utf-8")
    private_registry = tmp_path.parent / (tmp_path.name + "-private-proposals.json")
    monkeypatch.setenv("AMX_PROPOSAL_REGISTRY_PATH", str(private_registry))
    private_registry.write_text(json.dumps({
        "schema": "AMX_CARBON_CUSTOMER_PORTAL_V1",
        "proposals": {
            "test-token": {
                "proposal_ref": "TEST-001",
                "opportunity_key": "test-opportunity",
                "thread_id": "original-thread",
                "customer_id": "verified-customer",
                "business_name": "Test Business",
                "status": "DRAFT",
                "issued_at": None,
                "validity_hours": 24,
                "modules": [
                    {"id": "SOCIAL", "name": "SOCIAL°", "selected": True},
                    {"id": "PLACE", "name": "PLACE°", "selected": False},
                ],
            }
        },
    }), encoding="utf-8")
    (tmp_path / "overdrive").mkdir()
    (tmp_path / "overdrive/opportunities.json").write_text(json.dumps({"records": {"test-opportunity": {"execution_owner": "PRI", "state": "SUBMITTED", "thread_id": "original-thread"}}}))
    return TestClient(create_app(tmp_path, tmp_path / "data/test.db"))


def test_draft_quote_does_not_start_validity_clock(tmp_path, monkeypatch):
    c = portal_client(tmp_path, monkeypatch)
    r = c.get("/api/proposals/test-token")
    assert r.status_code == 200
    body = r.json()
    assert body["quote_status"] == "DRAFT_NOT_ISSUED"
    assert body["valid_until"] is None
    assert body["validity_hours"] == 24


def test_customer_portal_route_and_unknown_token(tmp_path, monkeypatch):
    c = portal_client(tmp_path, monkeypatch)
    r = c.get("/proposal/test-token")
    assert r.status_code == 200
    assert "proposal" in r.text

    missing = c.get("/proposal/nope", follow_redirects=False)
    expected_ref = hashlib.sha256(b"nope").hexdigest()[:12].upper()
    assert missing.status_code == 307
    assert missing.headers["location"] == f"/house/?ref={expected_ref}"
    assert "nope" not in missing.headers["location"]
    assert c.get("/api/proposals/nope").status_code == 404


def test_revoked_and_cancelled_portal_pages_recover_without_token_leak(tmp_path, monkeypatch):
    c = portal_client(tmp_path, monkeypatch)
    registry_path = tmp_path.parent / (tmp_path.name + "-private-proposals.json")
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    base = registry["proposals"]["test-token"]
    registry["proposals"]["revoked-token-secret"] = {**base, "status": "REVOKED"}
    registry["proposals"]["cancelled-token-secret"] = {**base, "status": "CANCELLED"}
    registry_path.write_text(json.dumps(registry), encoding="utf-8")

    for token in ("revoked-token-secret", "cancelled-token-secret"):
        page = c.get(f"/proposal/{token}", follow_redirects=False)
        expected_ref = hashlib.sha256(token.encode("utf-8")).hexdigest()[:12].upper()
        assert page.status_code == 307
        assert page.headers["location"] == f"/house/?ref={expected_ref}"
        assert token not in page.headers["location"]
        assert c.get(f"/api/proposals/{token}").status_code == 404


def test_expired_quote_has_neutral_recovery_and_keeps_old_quote_nonbinding(tmp_path, monkeypatch):
    c = portal_client(tmp_path, monkeypatch)
    registry_path = tmp_path.parent / (tmp_path.name + "-private-proposals.json")
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    registry["proposals"]["test-token"]["status"] = "ISSUED"
    registry["proposals"]["test-token"]["issued_at"] = "2020-01-01T00:00:00Z"
    registry_path.write_text(json.dumps(registry), encoding="utf-8")

    response = c.get("/api/proposals/test-token")
    assert response.status_code == 200
    body = response.json()
    assert body["quote_status"] == "EXPIRED"
    assert body["recovery_url"] == "/house/"
    assert body["valid_until"] is not None

    root = Path(__file__).resolve().parents[1]
    page = (root / "house/remediation/proposal.html").read_text(encoding="utf-8")
    script = (root / "house/remediation/proposal.js").read_text(encoding="utf-8")
    assert 'id="recoveryLink"' in page
    assert 'id="recoveryNote"' in page
    assert "$('recoveryLink').href" in script
    assert "$('recoveryNote').classList.remove('hidden')" in script


def test_change_request_is_non_binding_and_filters_unknown_modules(tmp_path, monkeypatch):
    c = portal_client(tmp_path, monkeypatch)
    r = c.post("/api/proposals/test-token/request-change", json={
        "selected_modules": ["SOCIAL", "UNKNOWN"],
        "message": "Add PLACE later.",
        "contact": "customer@example.com",
        "action": "REQUEST_CHANGE",
    })
    assert r.status_code == 200
    body = r.json()
    assert body["received"] is True
    assert body["binding"] is False
    receipt_path = tmp_path / "data/proposal_requests.jsonl"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8").splitlines()[-1])
    assert receipt["selected_modules"] == ["SOCIAL"]
    assert receipt["binding"] is False
    assert "does not automatically" in receipt["note"]
