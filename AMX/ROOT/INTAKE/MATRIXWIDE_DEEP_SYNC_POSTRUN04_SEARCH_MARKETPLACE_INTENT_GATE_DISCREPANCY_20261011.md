# POSTRUN-04 — SEARCH / MARKETPLACE INTENT-GATE IMPLEMENTATION DISCREPANCY

**Run ID:** AMX-DSI-20261011-061646Z  
**Parent audit SHA-256:** 4fc3373103cd0b799d5596ab633b94164450b7dd57f13cf99bb5dccc36b3460b  
**Source time:** 2026-10-11, current accessible repository readback.  
**Priority recommendation:** material semantic/acceptance discrepancy; ROOT/T-GOV to classify.  
**Disposition:** NOT CLOSED. This finding is based on exact source revisions and design gates; direct HTTP response was unavailable through the current endpoint reader.

## 1. Deployed Search source — what is actually implemented in the inspected endpoint

The current Render configuration points to service `srv-db4etm1srm7s73at90gg`, latest returned live deploy `dep-db4f2tjtqb8s73f2eu00`, commit `69834610dfb0945490b5d6f8047c8d99a0f83477`.

At that exact commit:
- `backend/app.py` exposes `POST /api/evidence/search`. It calls `store.search(req.query, req.limit * 2)`, filters by the HOUSE/PUBLIC visibility boundary, truncates to the limit, and returns fields `query`, `supported`, `results`, `count`, `gap`, and `retrieval`.
- That response explicitly labels retrieval as **“SQLite FTS5 / deterministic local search”**.
- `backend/store.py` tokenizes the query into OR'ed token-prefix FTS expressions and ranks matches with SQLite `bm25(evidence_fts)`; its fallback checks for the literal normalized query substring in evidence JSON.
- In the inspected API/store implementation, the returned Search contract does not expose a measured-intent snapshot, latent hypothesis set/probabilities, evidence-backed utility inputs, EIF, Expected Regret, stop/continue reason, decision-stability evidence, correction/pivot session state or next action.

This is not an accusation about motive and does not prove that no intent-aware code exists anywhere in a different service. It is a concrete mismatch between the inspected deployed Search endpoint implementation and the full CARBON Search design/acceptance contract. The direct Render endpoint could not be independently queried in this run; this is exact-commit source evidence paired with the deployment record, not a claimed fresh HTTP response.

## 2. Marketplace preview — current Search route does not call the shared intent engine

PR #14 is still DRAFT / OPEN / UNMERGED at current recorded head `249ec519b25526ed4336f82ecea6f51580898995`. Its preview deployment `dep-db4u77vlot8c73d1mnl0` is LIVE on that same commit; exact-head combined-status lookup returned no CI entries.

At that commit:
- `backend/marketplace.py` implements `GET /api/carbon/search` by calling `discovery.search(q, store.list_listings())`.
- The default `LocalDiscoveryAdapter` in `backend/marketplace_discovery.py` declares `external_search_connected = False` and `external_marketplace_connected = False`.
- Its actual ranking/filtering operation is substring matching against listing `title`, `description`, `seller_intent`, and `negotiability`. It does not call the shared CARBON Search / INTELLAGENT engine or compute posterior hypotheses, EIF or Expected Regret.
- `/api/carbon/bootstrap` describes the product as “the marketplace where intent has weight”, but this descriptive thesis is not executable acceptance evidence.
- Marketplace evidence tests do enforce valuable boundaries: unknown buyer/seller evidence remains neutral (`score: null`), participant evidence is factual, bond does not buy priority, commitments are bilateral, and time expiry does not imply breach. Those transaction-state rules are not the same thing as intent-weighted search/ranking.

## 3. Acceptance-contract contradiction also needs reconciliation

Current `house/search/CARBON_SEARCH_ACCEPTANCE_V1.json` has a top-level `build_law` value of **“100/100 mandatory gates or NOT_MATRIX_GRADE”**, while its `mandatory_gates` array contains **35 gates**. The linked commissioning contract says **35/35 mandatory acceptance gates** are the frozen first-cycle target. ROOT/T-COD must reconcile the JSON count/build-law language and identify the exact scope of the milestone closed under issue #16; this report does not silently edit or reinterpret the frozen contract.

The 35 listed gates include:
- G01–G03: typed measured intent, latent-intent plurality and posterior update;
- G11–G12: probability-weighted EIF and Expected Regret stop control;
- G15: provider failure must not silently downgrade to keyword Search;
- G21: Marketplace resolves demand/supply signals through the same intent engine;
- G23/G25–G26: per-search audit receipt, same-revision deployed-runtime readback and a Matrix-wide shared callable capability;
- G29–G35: surface parity, canonical entity directory, correction/rollback, dynamic intention focus, decisive primary result, bounded pivots and same-session pivot continuation.

The inspected endpoint/adapter code described above does not itself demonstrate those behaviors.

## 4. Required ROOT/T-GOV / T-COD / CARBON disposition

**Expected outcome:** an unambiguous statement whether issue #16 closed only a bounded deterministic evidence-search first slice, or whether it was intended to certify the full Engine of Intent contract. The current evidence does not substantiate the latter claim through the inspected live/deployed source.

**Owners:**
- ROOT/T-GOV: classify the conflicting gate count and reconcile the scope/meaning of issue #16's completed status with the controlling 35-gate commissioning contract.
- T-COD: implementation, tests and same-revision deployment/runtime evidence for the shared intent engine and Marketplace adapter.
- CARBON°: product truth and the Search → Marketplace → capability action → outcome-learning contract.
- MASTER/LIBRARIAN: preserve source snapshots, route the exact delta and verify readback; do not claim technical acceptance on T-COD's behalf.

**Acceptance test (must remain evidence-gated):**
1. Demonstrate the deployed Search endpoint returns typed Measured Intent, hypotheses/probability provenance, evidence/claim pointers, lawful scope, EIF/utility inputs where calculable, Expected Regret/continue decision, stop reason and authorized action/HOLD. Missing calibration must stay UNKNOWN, never fabricated.
2. Demonstrate the Marketplace route invokes the *same versioned* Search core, not a second local substring scorer; preserve the current commitment/bond/time/participant-evidence protections.
3. Test ambiguous intent with multiple hypotheses, an evidence update that changes weights without restart, a decision-sensitive uncertainty that keeps search going, a wrong-entity correction that invalidates only dependent state, provider failure without silent keyword downgrade, and a pivot that preserves the same session/furthest valid state.
4. Resolve the JSON 100/100 vs 35-gate count explicitly under ROOT; run every gate in the accepted scope and read back the exact same deployed commit/config. Deployment status alone is not acceptance.
5. Preserve issue #16's history. Do not automatically reopen it or move its frozen target. Keep the remaining semantic integration/open acceptance tracked in the existing issue #18 and Intake until ROOT records the scope/disposition.

**Dependency/blocker:** current-head Marketplace CI is not evidenced; endpoint HTTP readback was inaccessible; intent-aware implementation is not demonstrated by the inspected Search API and Marketplace local adapter; the gate-count wording is contradictory.

**Safety/preservation:** no code, schedule, worker, mandate digest, provider, tracker or authority layer is changed by this report. No buyer, private source, external search or payment claim is invented.

**Item-level disposition:** deployed deterministic evidence retrieval = SOURCE-VERIFIED; Marketplace local substring adapter = SOURCE-VERIFIED; shared intent-engine execution through both endpoints = NOT DEMONSTRATED; acceptance-scope/count = ROOT RECONCILIATION REQUIRED; Marketplace integration = OPEN.

**Remaining work:** ROOT/T-GOV source/scope disposition; T-COD/CARBON implementation and tests under existing authority; exact-head CI and same-revision endpoint readback; update issue #18/Intake with the resulting source hashes and test receipts. INTAKE NOT CLEARED.
