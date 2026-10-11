# POSTRUN-05 — Search-engine scope correction

**Run ID:** AMX-DSI-20261011-061646Z  
**Parent audit SHA-256:** 4fc3373103cd0b799d5596ab633b94164450b7dd57f13cf99bb5dccc36b3460b  
**Corrects:** POSTRUN-04, commit f86a34a2b6e94e71a8f874a65fc7e48f12cadcb2, blob 748a93eccf530627a7b4393e2f0ad6cc3726a8f3.  
**Disposition:** Search engine code exists; the outstanding gap is its actual Marketplace integration and runtime-provider readback.

## 1. Explicit correction

POSTRUN-04 inspected the evidence sub-endpoint in backend/app.py and store.py but did not account for the Search service entry point. Its conclusion must not be read as saying the whole CARBON° Engine of Intent is absent. The evidence endpoint itself is deterministic FTS/BM25 retrieval; the production entry point mounts the separate intent engine.

## 2. Deployed-revision code evidence

The live Render service record identifies commit 69834610dfb0945490b5d6f8047c8d99a0f83477.

At that exact revision:
- Dockerfile (blob ec664fb00118824d40cc8754f74fc9a85e45e434) starts backend.search_app:app.
- backend/search_app.py (blob 00b8e76eef012ef3b0845e98b98ad1debfa2f312) mounts backend.intent via mount_search.
- backend/intent/api.py (blob 189422b99f3680d63fc5f3156a8d70de124d3840) exposes the versioned contract, health, intent search, session/evidence retrieval, pivot, feedback and action routes with surface-specific authorization.
- backend/intent/engine.py (blob e1870892562fb7b74042b09db895260ac3741ba2) separates measured criteria from hypotheses, collects scoped candidates, ranks them, computes Expected Regret/decision stability, persists session state and supports same-session correction/pivots.
- backend/intent/ranker.py (blob 79645b5fd6609e3a649029abe8234ab2d77dd87c) records measured-intent and hypothesis contributions. Its EIF combines measured score and hypothesis score; Expected Regret combines margin, hypothesis and hidden-variable risk.
- backend/intent/providers.py (blob 9c57845d1c504634f340c6f9fb3382ceba87b324) makes external-search and Marketplace-signal providers environment-configured. Marketplace signals require AMX_MARKETPLACE_SIGNAL_PATH; external retrieval uses CARBON_SEARCH_EXTERNAL_URL. Code presence does not prove these are configured in the live environment.

This confirms the intent engine and its calculation mechanics exist in the deployed-revision source. Direct live endpoint output could not be retrieved in this run, so provider/configuration state remains UNKNOWN until authorized health/contract readback.

## 3. Marketplace integration gap remains

At PR #14 head 249ec519b25526ed4336f82ecea6f51580898995, backend/marketplace.py implements GET /api/carbon/search by calling discovery.search(q, store.list_listings()). Its LocalDiscoveryAdapter in backend/marketplace_discovery.py has both external-search and external-marketplace flags false and filters by substring matching across title, description, seller intent and negotiability. This route does not call the shared Search intent endpoint in the inspected revision.

The Search engine has a separate optional file-based Marketplace-signal provider, but its live configuration was not independently verified. Marketplace participant/commitment/bond/time and unknown-neutral evidence safeguards remain valuable; they are not proof of intent-weighted Search invocation.

## 4. Acceptance count wording

The Search acceptance JSON has 35 mandatory-gate objects and the Search API contract reports 35 gates. The JSON's build_law wording says “100/100 mandatory gates”, while the commissioning contract and first-cycle Intake record specify a frozen 35/35 target. ROOT/T-COD must reconcile this wording/scope without silently changing the historical acceptance count.

## 5. Corrected acceptance and ownership

- Search intent-engine implementation: SOURCE-VERIFIED in deployed-revision code.
- Live provider/environment configuration: UNKNOWN, pending direct authorized readback.
- Marketplace route invoking the same intent engine: NOT DEMONSTRATED.
- Exact-head Marketplace CI and same-revision end-to-end action/outcome/weight/readback: OPEN.
- Issue #16: keep its historical CLOSED state; this correction does not reopen it.
- Issue #18: keep OPEN until same-engine Marketplace integration, exact-head CI and deployed-runtime outcome evidence are verified.

**Owners:** T-COD for integration/tests; CARBON° for product semantics; ROOT/T-GOV for acceptance-count/scope disposition; MASTER/LIBRARIAN for source readback and Intake continuity.

**Acceptance:** demonstrate intent/posterior/EIF/Expected-Regret and scope/provider-failure/session-correction behavior on the deployed Search revision, then show Marketplace calls that same versioned core and that an action outcome is durably reflected in the next selection. Preserve UNKNOWN where configuration or live behavior is unverified.

**Safety/preservation:** no code, provider environment, worker, tracker, schedule, mandate or frozen acceptance target changed in this report.  
**Terminal disposition:** INTAKE NOT CLEARED; POSTRUN-04 corrected; Marketplace integration and live behavior remain open.
