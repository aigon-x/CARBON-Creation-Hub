# CATEGORY A — MATRIX-WIDE INTENTION ALGORITHM INTEGRATION AUDIT
**Audit date:** 2026-10-13 SAST  
**Classification:** Category A — shared Matrix behavior, interpretation integrity, and conversion capability  
**Route:** Existing ROOT Intake and existing GitHub issue #18 (Search → Marketplace → Media actions → Matrix continuity)  
**Status:** INVESTIGATION SUBMITTED; MATRIX-WIDE ACCEPTANCE NOT PROVEN; ROOT DISPOSITION REQUIRED  
**Authority effect:** Evidence and implementation-readiness report. This file does not itself alter mandates, Blue State, registry hashes, permissions, runtime configuration, or merge authority.

## 1. Executive disposition

The Owner-designated originating intention system is **partially integrated, not proven integrated throughout AMX and all its tentacles**.

Three materially different states must not be conflated:

1. **Canonical semantics and governance exist.** The originating-intention receipt, V1 contract, 35-gate acceptance contract, thin-adapter architecture, and an additive Blue State application are present and mutually consistent.
2. **A shared CARBON° Search / INTELLAGENT engine is source-evidenced.** Earlier verified deployment/CI receipts and the POSTRUN-05 correction establish that the Search engine exists in its own runtime source lineage. Issue #16 remains CLOSED for the bounded first cycle. That does not certify all consumers.
3. **Matrix-wide consumer integration and current runtime acceptance remain OPEN.** The current Marketplace draft branch now contains a real shared-engine adapter and fail-closed route, superseding older source claims that only a keyword adapter existed. However, the current branch is still PR #14 OPEN / DRAFT / UNMERGED / NOT MERGEABLE, the exact current head has no workflow-run evidence returned by the GitHub read, and no same-head deployed query/session/outcome readback was established in this audit.

**Conclusion:** Do not report the algorithm as absent; do not report it as Matrix-wide integrated. Its semantic and core implementation foundations exist. Cross-tentacle runtime adoption, original formula lineage, same-version deployment, consumer-by-consumer receipts, and measured downstream consequence remain unaccepted.

This audit corrects an old over-broad Marketplace conclusion where newer source supersedes it, while preserving the still-valid acceptance and deployment blockers. It does not reopen Search V1 issue #16.

## 2. Intentions for this investigation and derived outcomes

| ID | Investigation intention | Action and evidence examined | Derived outcome | Disposition |
|---|---|---|---|---|
| I-01 | Resolve the controlling meaning of INTENTION before judging implementations. | Read the canonical originating-intention receipt and 35-gate V1 acceptance contract; checked the current Blue State and the 2026-10-13 Category A directive. | INTENTION is runtime behavior: continuous, evidence-bound orientation toward the best defensible resolution of Measured Intent. Explicit signals, Measured Intent, latent hypotheses and unknowns must remain distinct. Correction rolls back only affected derived state, reweights and continues. | PASS — canonical semantics found. |
| I-02 | Determine whether the shared engine exists, without mistaking a retrieval endpoint or UI for it. | Read the canonical Search contract and the POSTRUN-05 source correction; reviewed the recorded Search runtime lineage. | Shared Search / INTELLAGENT source and versioned intent/session endpoints are evidenced in the recorded deployed-revision lineage. Deterministic Evidence House search alone is not the engine. Prior first-cycle acceptance remains issue #16 CLOSED. | SOURCE / HISTORICAL DEPLOYMENT EVIDENCE — not a claim that all present callers are accepted. |
| I-03 | Establish whether Marketplace actually calls that one shared engine. | Fetched current PR #14 metadata and source at head 2c720b2c0aa7b5e24a0bf39cc38811d764803634; inspected backend/marketplace.py, backend/marketplace_discovery.py, and tests/test_marketplace_intent_discovery.py. | The newer branch has IntentEngineDiscoveryAdapter, posts public listing candidates to the shared /api/search/intent contract, reads the resulting session ranking, marks query as verified only after response/session readback, excludes private seller references from candidate payloads, and fails closed instead of silently falling back to keyword search. Mocked acceptance tests express those checks. | SOURCE-LEVEL REPAIR PRESENT; current-head CI, same-head deploy, and live behavior NOT VERIFIED. |
| I-04 | Establish if the current Marketplace revision is accepted/deployed. | Read live PR metadata and requested workflow runs for the exact current head. | PR #14 remains OPEN, DRAFT, UNMERGED and NOT MERGEABLE. The exact current head is 2c720b2c0aa7b5e24a0bf39cc38811d764803634; its workflow-run lookup returned an empty list. Older CI/preview evidence for 1ce15e2… or 249ec519… is historical and cannot certify this head. | OPEN — exact-head CI and same-revision runtime readback required. |
| I-05 | Determine whether every Matrix tentacle has an evidenced adapter/receipt. | Compared the Category A consumer inventory and acceptance requirements with reachable repo searches, issue #18, the current audit trail, and the known iSCOPE/PRI, HTML Matrix, public/client and positioning routes. | The architecture and test requirements call for those consumers; this audit did not recover per-consumer source + current deployed result + receipt proving their adoption of the shared core. Mentions, saved prompt wording, task timestamps and documents do not prove runtime consumption. | OPEN — build and verify a per-consumer integration register. |
| I-06 | Recover the Owner-designated original algorithm, including reported additional mathematical formulas containing π, without inventing or approximating them. | Searched the existing Category A directive, Search source/acceptance artifacts, the associated 2026-10-13 governance incident, connected Notion results for “π”, “Euler” and algorithm wording, and the Library-held AMX transcript provenance ledger for exact π/intention-algorithm/formula terms. | The canonical CARBON° intention definition and EIF expression are located. The specific additional Owner-authored π-bearing formula/source artifact is NOT LOCATED by this bounded search. The transcript ledger yielded no π or exact “intention algorithm” match; this is not proof that the artifact does not exist or is not held elsewhere. | OPEN — source-lineage recovery owner and broader source census required; no formula may be reconstructed from memory. |
| I-07 | Check whether buying, selling, job positioning and conversion retain the Owner's actual objective rather than substituting a convenient narrative. | Read GOVERNANCE_ISCOPE_COMMERCIAL_HISTORY_AND_INTENT_DRIFT_20261013.md and the Category A directive. | A current recorded incident already identifies context/chronology truncation, tactical cash-bridge interpreted as long-term career change, owner-authorship attenuation, and non-consumption of the Owner-designated anti-misunderstanding algorithm as distinct failures. This audit found no fresh end-to-end runtime regression result proving those routes now consume the algorithm and pass the stated cases. | OPEN — run regression vectors through actual authorized consumers; preserve internal/public separation. |
| I-08 | Route the findings through existing ROOT governance without creating duplicate machinery. | Prepared this audit for the existing INTAKE path and existing issue #18. | The appropriate next step is an explicit ROOT/T-GOV disposition followed by bounded authorized implementation, per-consumer tests and readback. No new worker, scheduler, core, CRM, queue, issue or authority is warranted. | SUBMITTED FOR ROOT DISPOSITION; completion must be read back. |

## 3. Canonical semantics and control boundary

The current canonical sources are:

- Originating semantics: https://github.com/amillimatrix-eng/CARBON-Creation-Hub/blob/main/house/search/CARBON_SEARCH_ORIGINATING_INTENTION_RECEIPT_V1.md (blob f2482fb67e358bc5795609d2d2063e012ab1ee64).
- V1 acceptance contract: https://github.com/amillimatrix-eng/CARBON-Creation-Hub/blob/main/house/search/CARBON_SEARCH_ACCEPTANCE_V1.json (blob 31407f9b1f05c058eb7ed44a28767dd4483479f9).
- Existing Matrix-wide integration directive: https://github.com/amillimatrix-eng/CARBON-Creation-Hub/blob/main/AMX/ROOT/INTAKE/CATEGORY_A_MATRIX_WIDE_INTENTION_ENGINE_INTEGRATION_DIRECTIVE_20261013.md (blob ff953355dd12b8dac12f508176dedc881e95fad4).
- Search / Marketplace source-scope correction: https://github.com/amillimatrix-eng/CARBON-Creation-Hub/blob/main/AMX/ROOT/INTAKE/MATRIXWIDE_DEEP_SYNC_POSTRUN05_SEARCH_ENGINE_SCOPE_CORRECTION_20261011.md (blob 332472bda3787e3e91124bd362dbbabacf039172).
- Existing iSCOPE commercial-history / Owner-intent incident: https://github.com/amillimatrix-eng/CARBON-Creation-Hub/blob/main/AMX/ROOT/INTAKE/GOVERNANCE_ISCOPE_COMMERCIAL_HISTORY_AND_INTENT_DRIFT_20261013.md (blob 6dc6b66a249b0f0355e0768573ca04ad9d7130c2).
- Existing acceptance/convergence route: https://github.com/amillimatrix-eng/CARBON-Creation-Hub/issues/18.

The operating sequence is:

SIGNAL → MEASURE INTENT → FORM HYPOTHESES → CHECK MANDATE/SCOPE → SEARCH/EXECUTE → EVIDENCE + EXPECTED REGRET → SELECT WEIGHTED NEXT ACTION → PERSIST → READ BACK → RECORD OUTCOME/WEIGHT CONSEQUENCE → INTAKE DELTA → CONTINUE.

The intention model may rank only from evidence-backed probabilities and utility inputs. Unsupported hypotheses remain hypotheses; absent signal does not become an asserted preference. Mandate, safety, permission, privacy, financial and governance limits govern what may be done even when an action appears high utility. Numeric EIF/Intent Delta must not be fabricated where inputs are missing. Expected Regret and decision stability govern stop/continue; the diagnostic ΔI is not a shortcut to acceptance.

The current 35-gate V1 acceptance contract remains frozen. It includes measured-intent boundaries, latent hypotheses, posterior update, permission scopes, provenance/contradictions, EIF/Expected Regret, truthful HOLD, provider-failure discipline, outcome learning, Marketplace scenario, privacy isolation, audit receipt, deployment readback, Matrix-wide caller, surface parity, correction/rollback, dynamic focus, primary resolution and bounded same-session pivots. All mandatory gates and same-build deployed readback remain required for the corresponding build-grade claim.

## 4. What is integrated, and how far the evidence reaches

### 4.1 Canonical law / governance — PRESENT

The canonical semantic definition, acceptance contract, one-shared-core architecture and an additive Blue State intent-driven application exist. The governance law itself says document presence or prompt/wake timestamps do not prove behavior. Mandate and role boundaries are not expanded by this report.

**Derived outcome:** preserve the current semantic law and current Search V1 history. Do not create duplicate intent math in worker prompts or claim the whole Matrix is complete because the rule is written.

### 4.2 CARBON° Search / INTELLAGENT — SOURCE-VERIFIED IN RECORDED REVISION; CURRENT MATRIX-WIDE ACCEPTANCE OPEN

The POSTRUN-05 correction identifies the deployed-revision Search entry point as backend/search_app.py and the intent component as backend/intent, including intent API, engine, ranker and provider modules. The report identifies the typed versioned intent/search/session/pivot/feedback/action paths and their design for evidence-scoped candidate resolution, Measured Intent/hypotheses, EIF/Expected Regret, decision stability, session persistence and correction continuity.

The current repository default-branch fetch in this audit did not resolve the historical engine source files by path. Accordingly, the POSTRUN-05 source blobs/recorded revision are retained as historical source evidence, not silently represented as currently checked-out source. A fresh deployed contract/health/query receipt for this audit was not captured.

**Derived outcome:** Search's existence and bounded first-cycle acceptance are not denied; issue #16 remains CLOSED. Acceptance of the additional post-build fidelity upgrade and current caller-by-caller rollout still require their own governance, test and runtime receipts.

### 4.3 Marketplace — MATERIAL SOURCE PROGRESS; ACCEPTANCE NOT YET PROVEN

Current PR #14 head 2c720b2c0aa7b5e24a0bf39cc38811d764803634 includes:

- a thin IntentEngineDiscoveryAdapter in backend/marketplace_discovery.py;
- environment configuration for an HTTPS shared intent endpoint and client-surface token;
- public candidate typing and CARBON_MARKETPLACE scope;
- POST intent submission followed by GET session readback before recording QUERY_VERIFIED;
- private seller-reference exclusion from the shared candidate request;
- fail-closed production behavior if the shared engine cannot be configured/reached, instead of silently branding substring matching as intent search;
- test source that mocks the intent/session path and asserts ranking order, authorization header, scope, privacy exclusion and 503 behavior when the endpoint is unconfigured.

This is sufficient to correct the stale source claim that the current branch contains only a local substring adapter. It is **not** sufficient to claim this exact revision passed CI, was deployed, was configured with valid live credentials/provider state, or returned a current live decision/session. GitHub returned no workflow runs associated with the current head. PR #14 remains draft and unmerged.

**Derived outcome:** retain #18 as OPEN. Preserve the adapter implementation and test source. Current authorized T-COD/CARBON° action is exact-head test execution, then same-revision deployment and live query/session readback. Do not merge the draft or treat its branch test source as a passing test result.

### 4.4 HTML Matrix / other first-party callers — NOT DEMONSTRATED

The architecture requires the Owner/HTML Matrix, public/client, authorized non-CARBON worker and other first-party callers to invoke the same versioned core through thin adapters, with scope/perms/disclosure adjusted by caller. This search did not produce a complete consumer register with a source path and current observed runtime result for every caller. A broad lexical search that returns no code hit is not an exhaustive proof that no integration exists.

**Derived outcome:** record each consumer as UNKNOWN/NOT DEMONSTRATED until its live/source evidence is attached; do not label all consumers missing based only on search absence. Inventory the HTML Matrix and every current first-party consumer from route/build/mandate sources; then test each actual invocation.

### 4.5 iSCOPE / PRI / commercial conversion — GOVERNANCE FAILURE CLASS KNOWN; RUNTIME ADOPTION NOT PROVEN

The current 2026-10-13 governance incident explicitly identifies Owner-intent interpretation/objective inversion, whole-chronology truncation and failure to consume the Owner-designated anti-misunderstanding algorithm. It makes the distinction that a temporary cash-flow option must not be substituted for the Owner's long-term objective, and internal strategic context must not be copied into an external application or profile by default. The same durable directive requires actual commercial lifecycle states to remain distinct through response, acceptance, contract, invoice and settlement.

This is strong evidence that the relevant failure modes have been encountered and documented. It is not evidence that the current iSCOPE/PRI runtime invokes a shared intent API or has passed fresh regression cases. The audit did not find item-attributable end-to-end output proving shared-core usage changes qualification/selection, progresses a conversion-critical action, and feeds the observed result into a later selection.

**Derived outcome:** preserve role ownership: iSCOPE qualifies; PRI owns authorized post-handoff commercial writing/progression; Banker retains settlement truth. Use shared-intent behavior only through an authorized caller/contract. Test full chronology-to-requirement mapping, tactical bridge vs long-term objective, role/audience-specific copy, inbound no-delay and actual lifecycle/state transitions. No shadow CRM/ledger, repeated outreach or assumed payment.

### 4.6 Additional Owner-authored mathematical formulas / π — SOURCE RECOVERY OPEN

The canonical Search EIF expression has been located: EIF(x) = Σᵢ P(Iᵢ | S,E) × U(x,Iᵢ), with Expected Regret as a separate continuation/stop control and ΔI = 1 − EIF(best) as diagnostic only.

The Category A directive separately says the Owner refers to additional authored formulas, including formulae containing π, and explicitly prohibits inventing or reconstructing them from memory. This audit searched the relevant GitHub directive/Search documents and the existing Notion/Library query paths; exact π and Euler searches returned no matching Notion pages, and the provenance ledger had no exact π or “intention algorithm” match. This is a bounded source census, not global proof of non-existence.

**Derived outcome:** keep original formula lineage OPEN. ROOT/Master recovery must enumerate remaining authorized Owner/source repositories, transcripts, attached artifacts and code locations; record exact source/version/hash plus authorship/provenance and accepted consumer. Only after that inventory may ROOT decide whether a formula is already represented in current canon or requires a versioned amendment. Do not invent equivalent math and claim it is the Owner's formula.

## 5. Tentacle status register

| Consumer / surface | Evidence in this audit | Correct status |
|---|---|---|
| Canonical intention law / originating receipt | Current canonical file read and blob identified | VERIFIED PRESENT |
| 35-gate Search V1 contract | Current canonical JSON read; frozen gates | VERIFIED PRESENT; no new 35-gate certification made |
| Search / INTELLAGENT core | Recorded deployed-revision source and prior acceptance references; no fresh live query receipt here | SOURCE-VERIFIED IN RECORDED REVISION; CURRENT RUNTIME READBACK OPEN |
| Marketplace thin adapter | Current PR #14 source and mocked test file read | SOURCE-VERIFIED ON DRAFT HEAD; CI/deploy/live acceptance OPEN |
| HTML Matrix invocation | Requirement in architecture; no caller-specific live invocation receipt found | NOT DEMONSTRATED / INVENTORY REQUIRED |
| Non-CARBON Matrix worker invocation | Requirement in architecture; no caller-specific receipt found | NOT DEMONSTRATED / INVENTORY REQUIRED |
| iSCOPE qualification / intent routing | Existing incident records intent drift; no fresh shared-core runtime regression receipt | OPEN / BEHAVIORAL RETEST REQUIRED |
| PRI progression / buyer conversion | Existing commercial authority path identified; no attributable intent→conversion outcome join shown | OPEN / BEHAVIORAL RETEST REQUIRED |
| Professional positioning / T-MED | Current intent/objective/privacy incident is recorded; correct external-audience selection on a fresh run not evidenced | OPEN / REGRESSION REQUIRED |
| Buyer and seller dual-sided context | V1 contract and Marketplace concepts support separate contexts; current exact-head CI/live acceptance absent | CONTRACT PRESENT / ACCEPTANCE OPEN |
| Tender, pilot and paid-work routes | Required by Category A directive; no specific deployed consumer receipt attached | NOT DEMONSTRATED |
| Other first-party / future-compatible surfaces | Need source and runtime census; do not assume exhaustive search coverage | UNKNOWN UNTIL INVENTORIED |
| Original additional π-bearing Owner formula(s) | Not located in the bounded sources searched | SOURCE-RECOVERY OPEN |

No count of integrated consumers is reported because a complete consumer denominator has not yet been established. “Not demonstrated” is intentionally not equivalent to “does not exist.”

## 6. Required corrective sequence through existing authority

### A. ROOT / T-GOV — disposition before material contract/code change

**Action:** Explicitly ACCEPT / MODIFY / REJECT / ALREADY-SUBSUMED / HOLD the existing Category A matrix-wide directive and the existing post-build intention-fidelity patch through issue #18. Reconcile this audit with the current Blue State, frozen V1 contract, current #14 branch, earlier POSTRUN-04/05 reports and the 2026-10-13 iSCOPE incident.

**Output required:** controlling disposition, exact upgrade/version boundary, owners, dependencies, NEXT_ACTION and DUE, preservation of #16 as CLOSED, and an acceptance/readback contract for the remaining consumer rollout.

**Owner:** ROOT/T-GOV.  
**Blocker:** explicit current governance disposition and confirmation of exact source/upgrade scope.  
**Acceptance evidence:** durable ROOT issue/Intake decision read back; no contradicting stale projection left controlling.

### B. T-COD + CARBON° — Marketplace current-head behavior

**Action after authorized scope:** test commit 2c720b2c0aa7b5e24a0bf39cc38811d764803634 on its exact head; run the existing test suite including test_marketplace_intent_discovery.py, all frozen regressions and the real shared Search provider contract. Do not settle for mocked tests. If a current failure is reproduced, repair the smallest affected state and preserve unaffected valid evidence.

**Acceptance:**
1. exact-head mandatory CI passes;
2. the permitted public listing candidates are sent through the shared versioned intent endpoint with the correct scope/client authorization;
3. live response is followed by the session/ranked-candidate readback;
4. response records core/contract version, intent status/session, scope and evidence pointers;
5. provider failure returns a truthful HOLD/503 and never falls through to keyword-only ranking under the Search label;
6. the same exact passing SHA is deployed, and a non-costly authorized live query returns a matching deployed-revision receipt;
7. observed item/action outcome is persisted and read back where outcome learning is in scope.

**Owner:** T-COD + CARBON°; MASTER/LIBRARIAN for evidence/readback; ROOT for gate/authority scope.  
**Blocker:** exact-head CI and same-head live configuration/deployment are currently not evidenced.  
**Acceptance evidence:** immutable commit and workflow run ID, test artifacts, same-SHA deployment ID, query/session receipt and independent source/state readback.  
**Preservation:** do not change the frozen Search V1 35-gate target, merge solely to clear status, expose secrets, enable real-money movement or reopen issue #16.

### C. Matrix-wide callers — inventory, bind and verify each individually

**Action:** build an additive consumer register inside existing #18/Intake evidence, not a new queue. Enumerate all current first-party callers from code/route/deployment/membership sources and record, for each: named consumer, owner/mandate, adapter and source path, core/contract version, permission/scope and audience, exact code/deploy revision, test vector, actual observed runtime output, receipt/audit link, correction behavior, outcome consequence and blocker/next action.

Priority sequence from current Category A authority:
1. HTML Matrix and current first-party surfaces.
2. Authorized non-CARBON worker caller.
3. iSCOPE qualification and PRI conversion path.
4. Professional positioning / audience-specific fact-base selector.
5. Marketplace (once exact-head/current-deploy acceptance passes).
6. Remaining first-party consumers; third-party/client use only after separate permission/data-scope review.

**Owner:** T-COD plus each existing surface/office owner; ROOT governs material behavior or scope changes.  
**Acceptance:** actual per-consumer call and readback against the shared contract; no consumer passes solely because its saved prompt contains intent terminology.  
**Preservation:** do not clone intent math into worker prompts, silently widen ACLs or create a second CRM/pipeline.

### D. Buyer, seller, job, tender and commercial regressions

**Required vectors:** resolve the user's requested objective before optimizing adjacent work; separate explicit signal/Measured Intent/hypothesis/unknown; do not infer budget or readiness from title/click; resolve buyer and seller goals separately; route the highest-value lawful next conversion action; map the full professional chronology to actual requirements; do not turn a tactical cash bridge into a new long-term objective; do not disclose internal strategy to a public/buyer-facing audience by default; keep inbound offers outside the sourcing allocation; preserve discovered/submitted/accepted/contracted/invoiced/paid/settled as distinct evidence states.

For every material action, retain request → evidence/scope → decision/HOLD → action/output → state transition → readback → next action/owner/due → later outcome/weight change. The later selection change must be actually observed and joined to its prior outcome; two independent records do not prove causal integration without the join.

**Owners:** existing iSCOPE, PRI, Banker, positioning/T-MED and product/build owners within their mandates; ROOT for scope and governance.  
**Acceptance:** fresh-runtime regression receipt plus real permitted state/action evidence, not retrospective wording only.

### E. Original formula lineage recovery

**Action:** continue the source census of the Owner-authorized source custody. Record each attempted corpus/query, result, version/hash, provenance and next recovery route. Keep the canonical EIF/Expected Regret implementation distinguishable from any additional proprietary Owner-created formulae. ROOT classifies recovered formulas as existing canon, additive implementation detail, or material semantic upgrade before changing acceptance/engine behavior.

**Owner:** MASTER/LIBRARIAN for source lineage and receipt; ROOT/T-GOV for authoritative provenance/supersession; T-COD only for authorized implementation after classification.  
**Blocker:** exact π-bearing source artifact has not been identified in this audit.  
**Acceptance:** exact source file/turn/artifact and version/hash recovered or documented corpus census with an explicit remaining recovery owner; no reconstructed formula is falsely represented as the Owner’s original.

## 7. Acceptance rule and closure boundary

The Category A audit is not closed by writing this file, issue acknowledgement, a successful code search, one adapter, a prompt change, or a build passing local mocked tests.

The integration may be represented as accepted only when:
- ROOT has dispositioned the existing governance route and exact version boundary;
- the originating formula/source lineage is reconciled or explicitly left as a governed provenance HOLD with a recovery owner;
- the per-consumer register covers the verified current consumer set;
- each applicable consumer invokes the same authorized versioned core or holds with a recorded lawful reason;
- exact revision CI and same-revision runtime readback pass relevant frozen regression vectors;
- correction/rollback preserves unaffected evidence and continues from the furthest valid state;
- each material action has a receipt and state readback;
- commercial outcomes remain correctly separated, and any claimed outcome→weight→next-selection causal chain has an evidenced join;
- new source, consumer, deploy and behavioral receipts are linked back through existing #18 and the ROOT Intake index/receipt route.

Until then, use **PARTIAL SOURCE INTEGRATION / MATRIX-WIDE ACCEPTANCE OPEN**. Do not state “fully integrated throughout AMX,” “all tentacles use the algorithm,” or MATRIX_GRADE on the strength of this investigation.

## 8. Category A disposition request

ROOT/T-GOV is requested to:

1. classify this as a continuation and evidence reconciliation of the existing 2026-10-13 Category A directive, not a duplicate initiative;
2. acknowledge the current Marketplace adapter as a source-level correction to the prior source claim, while retaining exact-head CI/deployment/runtime acceptance as OPEN;
3. set owner, dependency, NEXT_ACTION and DUE for each item in Sections 6A–6E;
4. retain issue #16 CLOSED, issue #18 OPEN / EXECUTION, and the frozen 35-gate Search V1 contract;
5. order a verified per-consumer register plus original formula source-lineage recovery;
6. require readback of the ROOT disposition and subsequent actual consumer outcomes before any matrix-wide completion statement.

## 9. Directive 23 itemized acceptance index

- **Expected outcome:** controlling intention semantics retained. **Owner:** ROOT/T-GOV. **Action:** disposition and bind the existing Category A route. **Dependency/blocker:** current formal ROOT decision. **Acceptance evidence:** durable disposition read back. **Persistence/readback:** this record plus #18; governance readback pending. **Safety/preservation:** no new authority or duplicate system. **Disposition:** OPEN.
- **Expected outcome:** Marketplace actually invokes the shared core on its accepted deployment. **Owner:** T-COD + CARBON°. **Action:** exact-head CI → live POST/session readback → same-SHA deployment → outcome readback. **Dependency/blocker:** current PR head has no returned workflow run and no fresh live receipt. **Acceptance evidence:** workflow ID, deployment ID, session receipt and output/state join. **Persistence/readback:** PR #14/#18 receipts. **Safety/preservation:** fail closed, no credential disclosure, no real-money action. **Disposition:** SOURCE FIX PRESENT; ACCEPTANCE OPEN.
- **Expected outcome:** every applicable AMX tentacle uses one versioned engine appropriately. **Owner:** T-COD and existing consumer owners; ROOT controls semantic/permission change. **Action:** enumerate and test callers one at a time. **Dependency/blocker:** no complete current consumer denominator/per-consumer runtime receipts. **Acceptance evidence:** each caller's exact revision, scope, test, observed output and receipt. **Persistence/readback:** register via #18 and Intake index. **Safety/preservation:** no cloned engine or ACL widening. **Disposition:** OPEN.
- **Expected outcome:** Owner-authored original formula lineage is preserved. **Owner:** MASTER/LIBRARIAN + ROOT/T-GOV. **Action:** continue authorized source census. **Dependency/blocker:** exact additional π-bearing artifact not found in bounded search. **Acceptance evidence:** source/version/hash or explicit bounded corpus census with recovery owner. **Persistence/readback:** provenance link in #18/Intake. **Safety/preservation:** do not invent or reconstruct the Owner’s formula. **Disposition:** OPEN.
- **Expected outcome:** Owner objective and evidence survive buyer/job/profile contexts. **Owner:** existing iSCOPE/PRI/positioning owners. **Action:** run chronology, bridge-vs-goal, dual-intent, privacy/audience and conversion-lifecycle regression cases. **Dependency/blocker:** no fresh end-to-end consumer receipt proving uptake. **Acceptance evidence:** current runtime results and material state transitions read back. **Persistence/readback:** existing commercial ledger/receipt and ROOT Intake. **Safety/preservation:** private strategy stays private; financial states remain distinct. **Disposition:** OPEN.
- **Expected outcome:** runtime/source status is not mistaken for behavioral completion. **Owner:** MASTER/LIBRARIAN. **Action:** reconcile current records and only claim verified states with attributable receipts. **Dependency/blocker:** cross-consumer evidence and current live outcomes. **Acceptance evidence:** independent readback and evidenced joins. **Persistence/readback:** link subsequent receipts here and to #18. **Safety/preservation:** no false pass or unsupported Matrix-wide claim. **Disposition:** OPEN.

**Final status:** Investigation evidence prepared for the existing ROOT Intake path. The report itself has no authority to declare integration accepted; ROOT disposition, implementation/rollout and subsequent behavioral acceptance remain open.


---

## 10. Post-audit runtime readback — 2026-10-13 SAST

This section supersedes only the dated status claims in Sections 6 and 9 that exact-head CI and same-revision deployment/runtime had not yet been verified. All earlier observations remain historical provenance.

### Executed and verified

- **Current source head:** `2c720b2c0aa7b5e24a0bf39cc38811d764803634`, PR #14, branch `build/carbon-intent-marketplace-v1`.
- **Exact-head CI:** GitHub Actions run [38202721580](https://github.com/amillimatrix-eng/CARBON-Creation-Hub/actions/runs/38202721580), “Evidence House Backend Tests”, completed SUCCESS on that exact SHA; its `test` check completed SUCCESS.
- **Same-SHA preview deployment:** Render deployment `dep-db76623rjlhs73a2hifg` is LIVE on `2c720b2c0aa7b5e24a0bf39cc38811d764803634` at [Marketplace preview](https://carbon-intent-marketplace-v1-preview.onrender.com). This is the existing preview service only; PR #14 remains OPEN / DRAFT / UNMERGED.
- **Live route readback:** `GET /api/health`, `GET /api/carbon/bootstrap`, `GET /openapi.json`, and `GET /api/carbon/search` responded. OpenAPI advertises the Marketplace Search route plus 52 total routes.
- **Shared Search health:** after one transient HTTP 503 on the first probe, repeat reads of [Search health](https://carbon-search-intention-v1.onrender.com/api/search/health) and [Search contract](https://carbon-search-intention-v1.onrender.com/api/search/contract) succeeded. The live contract still reports `CARBON_SEARCH_V1`, `INTELLAGENT`, and 35 mandatory gates; `external_provider` and `marketplace_provider` remain `UNCONFIGURED`.

### Acceptance still fails at live consumer integration

- Marketplace bootstrap reports `discovery.name=LOCAL_CARBON_MARKET`, `external_search_connected=false`, `external_marketplace_connected=false`, `demo_mode=true`, `money_moved=false`, and `production_provider_connected=false`.
- The live `GET /api/carbon/search` response likewise reports `discovery.name=LOCAL_CARBON_MARKET` and a provider-selection remainder. Therefore the newly deployed revision is live, but its effective runtime is **not yet invoking the shared intent endpoint** for Marketplace search.
- At this source revision, `IntentEngineDiscoveryAdapter.from_env()` selects the shared engine only if `CARBON_SEARCH_INTENT_URL` or `CARBON_SEARCH_CLIENT_TOKEN` is configured. With neither configured, explicit preview demo mode selects the local adapter. The effective runtime configuration therefore does not yet supply the shared Search endpoint/client-token pair. No secret value was retrieved or exposed during this pass.
- The adapter implementation in `backend/marketplace_discovery.py` expects an HTTPS endpoint ending in `/api/search/intent` plus a client-surface token matching Search's `AMX_SEARCH_CLIENT_TOKEN`; a successful qualified query must POST to Search, receive a session ID, GET the session and observe ranked candidates before reporting `QUERY_VERIFIED`.
- The marketplace currently has zero listings. The shared adapter can be configured, but full behavioral acceptance still needs a safe, explicit preview fixture (or existing verified public candidate) and a query proving event → session readback → ranking/output consequence. Do not treat route presence, healthy status, or a local empty result as shared-engine acceptance.
- Search suffered a single initial 503 on this pass; two later health/contract probes succeeded. Classify the one 503 as **transient observed, not a persistent service failure** unless fresh regression evidence appears.
- Sandbox boundary preserved: the live Marketplace still reports `SANDBOX_NO_MONEY_MOVED` and `money_moved=false`. No real payment, settlement, production provider, or credential change was performed.

### Next action / owner disposition

- **T-COD / existing CARBON runtime owner:** bind the currently stored Render environment configuration to the existing shared Search endpoint and approved client-token value, without exposing secrets in source/transcripts; do not rotate a shared token until its consumers and impact are reconciled.
- **MASTER/LIBRARIAN:** read back the effective runtime adapter state and exact deployment SHA after the configuration change.
- **FORX + ROOT/T-GOV:** produce/reconcile the full per-consumer denominator and formal Category A disposition through existing issue #18. Keep #18 OPEN / EXECUTION, PR #14 DRAFT/UNMERGED, #16 CLOSED, and 35-gate Search V1 frozen until behavior has been read back. If the existing runtime secret cannot be securely recovered, record the exact owner/action/gate instead of guessing or using a dummy credential.

### Directive 23 itemized delta

- **Expected outcome:** source commit proven on a hosted Marketplace preview. **Owner:** T-COD / CARBON runtime. **Action:** deploy exact head. **Dependency:** existing preview service. **Acceptance evidence:** CI run 38202721580 + deployment dep-db76623rjlhs73a2hifg on SHA 2c720b2. **Persistence/readback:** GitHub run and Render deployment readback. **Safety:** preview/sandbox only; no money moved. **Disposition:** PASS for same-SHA CI/deployment only.
- **Expected outcome:** Marketplace invokes shared intent runtime. **Owner:** T-COD/CARBON runtime; ROOT governs authority. **Action:** provide the current endpoint and client token at runtime, then verify live POST/session readback and result ordering. **Dependency/blocker:** effective adapter is LOCAL_CARBON_MARKET; environment pair not configured and no listings present. **Acceptance evidence:** `QUERY_VERIFIED`, session ID, ordered candidate IDs and durable readback on the exact deployed SHA. **Persistence/readback:** this audit and #18. **Safety:** do not expose/rotate secrets without consumer check; sandbox money remains disabled. **Disposition:** OPEN / FAIL acceptance, recovery path identified.
- **Expected outcome:** matrix-wide original intention algorithm acceptance. **Owner:** ROOT/T-GOV + existing consumer owners. **Action:** enumerate and test each current consumer; recover original formula lineage. **Dependency/blocker:** consumer denominator, per-consumer receipts and formula origin still unresolved. **Acceptance evidence:** exact revision and behavioral receipt per consumer plus source/hash for the formula or bounded provenance census. **Persistence/readback:** existing #18 / ROOT Intake. **Safety:** preserve roles, privacy and frozen contract; no duplicate engine. **Disposition:** OPEN.
