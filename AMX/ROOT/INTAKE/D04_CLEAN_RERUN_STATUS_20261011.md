# D04 CLEAN-RUN STATUS — CURRENT SOURCE READBACK — 2026-10-11

Run ID: AMX-LIBRARIAN-20261011-1408SAST-01  
Submission sequence: 02  
Status: **HOLD — NO NEW BENCHMARK SCORE PRODUCED IN THIS SUBMISSION**

## Frozen test boundary

- Test: `AMX-D04-ENTERPRISE-CORPORATE-CONTROLS-V1`
- Frozen criteria: `AMX/ROOT/DEMONSTRATORS/D04/D04_ENTERPRISE_CORPORATE_CONTROLS_V1.json`
- Frozen criteria Git blob: `b392cb16ba15bef38d3f281c5144852a355b59b0`
- Scope remains 88 controls across 11 domains; no criteria, weights, criticality or pass-rule changes are authorized.
- This status file is a correction of a stale execution-status note. Its prior revision remains available in Git history; no historical test artifact or control vector has been deleted or rewritten.

## Corrected direct observations

### 1. The stale external-ready code repair is present

- Current `overdrive/runner.py` blob: `d71c75550c72daa80cc585c8fc93ee0a4ee0fcb9`.
- Current `tests/test_overdrive_claims.py` blob: `80515dd8db88dfe4095ff870b5026ec27813180d`.
- The fetched runner clears `external_action_ready` whenever a claim's current status is not `READY`, recomputes `external_ready_count`, and derives `executable_order` from the current claim statuses.
- The fetched regression test includes stale `READY` → `WAITING` coverage: the flag clears, both counters go to zero, and the executable order empties. It also covers a completed claim retaining a stale flag.
- PR #28 is merged. Head SHA: `74cc1b963c5344c34639679df618cfbe05f189ee`; merge commit: `8233184a1ee8cb186739a38fc14ed15d084464d3`.
- **Correction to prior status:** it was inaccurate to say the current default-branch runner still lacked this guard. The guard and regression-test source are present in the current branch readback.

### 2. Exact-head CI is still not verified

- The commit-status readback for PR #28's head and merge SHA exposes a Vercel failure linking to a build-rate-limit/plan-upgrade gate. That is a deployment/build-capacity result, **not evidence that the Python regression tests failed**.
- The connected GitHub workflow-run read returned no PR-triggered run receipt for the PR head SHA or merge SHA. No exact-head regression-suite PASS receipt was recovered in this submission.
- Existing workflow: `.github/workflows/overdrive-recovery.yml`, blob `9bfdb4940d4150e2f39246b26584da75ff81a12e`. It defines an existing 5-minute schedule and `workflow_dispatch`; no new workflow or worker is required.
- The connected GitHub integration exposes read/status and rerun-failed-job operations but no workflow-dispatch operation. I did not mutate source/state simply to manufacture a trigger.

### 3. Queue state — distinguish completed adapter history from current claims

- Current `overdrive/state.json` blob: `08f0a61ddd947fd09f4a657ba89b705270ec550f`.
- It reports `adapter_status=OPERATIONAL`, sequence 20, and 20 queue entries. A direct parse shows **20/20 entries are COMPLETED and each has a durable receipt**. They are retained history, not 20 pending jobs.
- The latest persisted tick is `2026-10-10T18:57:59.949295+00:00`; its result reports `pending=0`, `processed=[]`, and `ready_claims=1`.
- Current `overdrive/claims.json` blob: `1181368e78903b501de695eda44254e3781ebe2d`. Its generated timestamp is `2026-10-10T18:57:59.947710+00:00`; it reports `ready_count=1`, `external_ready_count=0`, and executable order containing `PRI|callforceoutsourcing.com|marketing-lead|south-africa`. The matching claim has `external_action_ready=false`.
- **Disposition:** the adapter queue is drained, but the overall current-claims gate is not cleared because a READY internal claim remains and no fresh tick/readback was available in this submission. No buyer-facing send or application is authorized by this observation.

### 4. Ledger reconciliation remains open

- Current `overdrive/opportunities.json` blob: `b04be618dccf1fed8405ccd7ff5c4be34d18004d`.
- Top-level `record_count=66` while `records` contains 83 distinct keys; `last_updated_at=2026-10-09T13:05:00Z`, and `last_run.run_at=2026-10-03T17:42:00Z`.
- This is an unresolved counter/currentness invariant, already raised in Intake issue #31. Do not manually alter the count or historic run snapshot until the existing T-COD/ROOT disposition defines its semantics and tests the invariant.

## Separate test evidence search and clean-input rule

- The Owner reports having run a distinct clean execution with the same frozen standards. This submission does not dispute that report.
- Searches of the current Intake/repository, connected Notion search, and accessible Library did not recover that execution's own raw control vector and immutable run receipt.
- An older 96.62% recomputation artifact surfaced in PR #28's deletion diff; its own text says it recomputed a prior vector. It is **not** the Owner-reported separate execution and is excluded from any new score calculation.
- No historical score, status vector, or score-recomputation output is used as the scoring input for a new run. No third test was executed in this submission because the exact-head regression result and current runtime/claims readback are not available. **No score is being invented to fill that gap.**

## Required execution path

1. **T-COD — exact-head test acceptance.** Use the existing `overdrive-recovery.yml` workflow path through an authorized workflow-dispatch/scheduler route. Capture workflow run ID, tested SHA, regression-suite output and final status. Do not add a parallel workflow or change the frozen D04 criteria.
2. **Existing OVERDRIVE executor/runtime owner — fresh tick and readback.** Run the existing authorized tick path; read back `state.json`, `claims.json`, `opportunities.json` and receipts at the same run boundary. Reconcile the one internal READY claim under current route/state rules. Do not send duplicate buyer contact or promote a lifecycle state without attributable evidence.
3. **T-COD + ROOT/T-GOV — current-ledger invariant.** Disposition issue #31's `record_count` versus 83-key discrepancy and retain `last_run` as historical. Fix through the existing canonical write/reconciliation path only after its intended semantics and tests are accepted.
4. **MASTER/LIBRARIAN — clean D04 execution.** After the exact-head test and fresh readback gates pass, assess all 88 frozen controls from the then-current evidence, persist a new immutable control vector/run receipt, recompute the score, and read back that exact artifact. The missing prior separate test must not be substituted with another run or a recomputation.

## Itemized Directive 23 disposition

- **New clean D04 result** — Owner: MASTER/LIBRARIAN. Required action: perform the same frozen 88-control assessment only after the current-run gates are met. Dependency: exact-head regression result plus fresh claims/state/opportunity readback. Acceptance evidence: immutable 88-row vector, frozen criteria reference, weighted arithmetic, verdict-gate evaluation and independent readback. Persistence/readback: not yet satisfied. Safety: prior vectors are not scoring inputs; no criteria edits. Item disposition: **OPEN / HOLD**. Remaining work: authorized workflow execution and fresh runtime readback.
- **Runner state-guard repair** — Owner: T-COD. Required action: retain and verify the already-merged fix rather than re-implementing it. Evidence: current runner and regression-test blobs above; PR #28 merge commit. Persistence/readback: source readback PASS. Safety: no second patch or duplicate worker. Item disposition: **CODE PRESENT / TEST RECEIPT UNVERIFIED**. Remaining work: exact-head CI receipt.
- **Adapter queue** — Owner: existing OVERDRIVE executor. Required action: preserve the 20 completed receipts and obtain a fresh current tick. Evidence: state blob and receipt-bearing entries above. Persistence/readback: historical tick exists; fresh readback absent. Safety: do not misclassify completed receipts as pending jobs and do not manually rewrite the state. Item disposition: **ADAPTER PENDING=0 / CLAIMS GATE OPEN**. Remaining work: fresh tick and treatment of the one READY internal claim.
- **Opportunity-ledger counter/currentness** — Owner: T-COD with ROOT/T-GOV disposition. Required action: resolve intended `record_count` semantics and update through the existing writer with regression tests. Dependency: issue #31 decision; current map has 83 keys. Acceptance evidence: exact-SHA tests and fresh readback confirming the count invariant without rewriting the 3 October run snapshot. Safety: preserve every record and lifecycle; no shadow ledger. Item disposition: **OPEN**. Remaining work: governed fix and acceptance.
- **Separate Owner-reported test** — Owner: MASTER/LIBRARIAN evidence recovery. Required action: continue searching retained source/session evidence; do not ask the Owner to rerun or defend it. Evidence: current accessible Intake/Repository/Notion/Library search produced no primary vector/receipt. Persistence/readback: not recovered. Safety: do not replace it with the old recomputation artifact. Item disposition: **PRIMARY EVIDENCE NOT FOUND IN ACCESSIBLE SOURCES; EXECUTION REPORTED BY OWNER IS NOT DISPUTED**. Remaining work: recover its own receipt, or rely on the authorized new clean execution after prerequisites pass.


## Cross-system recheck — Vercel, Render, Notion — 2026-10-11

- **Vercel portal deployments:** the deployment for Intake commit `cd35fdc6488d201d5ddbe26564d215e4b5fdc960` is READY and its commit status is success; the later deployment for Intake-index commit `e2155155eee1b2f816dd56ea1c68c7b722db90ab` is also READY/status success. This confirms the status/readback surface was deployed. It does **not** constitute a D04 regression-test receipt.
- **Runner merge commit:** `8233184a1ee8cb186739a38fc14ed15d084464d3` still reports a Vercel status failure linking to the build-rate-limit/upgrade gate. This is a deployment-provider status, not a Python test failure. No exact-head automated test result was recovered by this check.
- **Render:** the existing `amx-evidence-house` service is live on commit `a4ddb9bb2e7be00a8be794384b774e5acb1f8bfc` (message: distinguish Owner-reported new D04 test from original recomputation). The existing backend is live on commit `767bc444dc5029b0ad891f361cc49bd01715aa2f`. Deployment success confirms the services deployed; it does not show that they executed or stored the Owner-reported clean D04 vector. A filtered Render-log query did not recover a D04-specific vector/receipt.
- **Notion conflict:** the current fetched page “D04 COUNTING INTEGRITY — CLEAN RERUN REQUIRED; 90.51 / 96.62 HISTORICAL ONLY” was last fetched with source timestamp 2026-10-10T15:56:33Z. It explicitly says the primary 96.62 vector was not recovered and that its arithmetic recomputation is not a fresh run; a separate section/related governance copy describes 96.62 as PASS. Treat those as conflicting/stale governance statements, not as a substitute for a raw control vector. Current GitHub Intake remains the operative status pointer and preserves the Owner-reported separate execution without disputing it.
- **Disposition:** no new D04 run or score was produced in this recheck. Frozen criteria, historical artifacts and the Owner's report remain preserved. The clean result remains blocked on a valid execution path that produces all 88 current control rows, exact criteria/run references, weighted arithmetic, critical gates and immutable persisted readback.

### Additional Directive 23 items
- **Vercel/CI distinction** — Owner: T-COD / existing deployment owner. Action: obtain a successful exact-SHA regression receipt through the authorized workflow path; do not treat a Vercel rate-limit status as a test failure. Dependency: available authorized workflow trigger. Acceptance: run ID, tested SHA, regression output and terminal result. Persistence/readback: deployment status read back; test receipt still absent. Safety: no new workflow or paid-plan change assumed. Disposition: OPEN.
- **Evidence House cross-system check** — Owner: existing Evidence House/runtime owner. Action: query its persisted D04 artifacts and read back any matching receipt using the existing service path. Dependency: access to the application's actual artifact store/route. Acceptance: artifact ID/hash and complete 88-control vector. Persistence/readback: deployments verified, D04-specific receipt not recovered. Safety: no service redeploy or data mutation initiated. Disposition: OPEN.
- **Notion/GitHub contradiction** — Owner: ROOT/T-GOV, with MASTER/LIBRARIAN. Action: reconcile the stale Notion page and any 96.62 PASS statement against the current Intake and primary-vector inventory. Dependency: recover primary receipt or explicitly retain UNVERIFIED. Acceptance: consistent current pointer, with old page/history preserved and readback. Persistence/readback: conflict identified; correction not applied in Notion in this pass. Safety: no historical page or benchmark artifact deleted. Disposition: OPEN.
