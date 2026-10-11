# CATEGORY A — RUN EXECUTION METRIC, OWNER ACCOUNTABILITY COUNTDOWN, PUBLIC EVIDENCE HYGIENE
**Date:** 2026-10-11  
**Status:** OWNER-DIRECTED / ADDITIVE BLUE STATE CONTROL PERSISTED AND READ BACK. Blue State commit `70fbdf207c4b72331a26f2cecf39c16d6aa5fa68`; Blue State blob `9fb44f0c49a6e64175754ac3b6ec303209985f1b`. Intake Index adoption and worker/scheduler behavioral receipts remain subject to independent readback.  
**Authority boundary:** Additive control only. It does not create a new worker, scheduler, role, permission or parallel queue. It does not override security, privacy, platform safety or required authorization.

## 1. Owner intent — binding interpretation

The Owner requires all work to be represented by execution evidence rather than summaries that cannot prove action. The required behavior is: recover current canonical authority; identify the exact intended outcome; classify the run; execute the minimum lawful actions; record state before/after; prove persistence by independent readback; report remaining blockers with owner and next action; continue while lawful scope remains.

The Owner also directed:
- track an asserted 1,000-unit outstanding obligation with a wake-by-wake accountability countdown;
- remove D04 scoring/result material from public-facing surfaces;
- describe tests as the exact behavior and bounded sample they measure, not as generic scoreboards;
- complete overdue T-MED positioning work within the existing authority boundary;
- do not add scheduler tasks when the three existing automation slots are occupied;
- require explicit receipt/binding evidence from every awakened worker/office;
- conduct queue drain and a deep sweep of applicable existing surfaces without crossing owner/role boundaries.

“Category A” raises priority; it does **not** remove platform safety, security, privacy, authority, or tool restrictions. A rejected write must be preserved as blocked and routed; do not bypass it using alternate encodings or shadow stores.

## 2. Mandatory run-type / execution metric

Every report, same-run Intake submission, wake receipt, queue drain, deep sweep, repair, test, publication package or blocked attempt must carry this minimum record:

1. **Run ID** — immutable for the entire run; each same-run submission adds a sequence number and points to the previous payload hash.
2. **Run type** — one of `WAKE_PREFLIGHT`, `QUEUE_DRAIN`, `DEEP_SWEEP`, `REPAIR`, `INDEPENDENT_TEST`, `PUBLIC_EVIDENCE`, `INCOME_FOLLOWTHROUGH`, or `BLOCKED_RECOVERY`. Multiple tags are allowed, but the primary type is explicit.
3. **Intent map** — each Owner instruction → expected outcome → authorized owner → exact action.
4. **Before state** — canonical source path/ref/blob or commit SHA, source timestamp when available, status and current next action.
5. **Action state** — attempted action, furthest evidenced state, exact result, and any blocker. Do not conflate fetched/prepared/attempted with written, merged, deployed or accepted.
6. **After state** — exact updated object, resulting ID/hash, independent readback, and material delta. A successful API response alone is not full behavioral acceptance when a readback is required.
7. **Execution metric** — report counts and evidence, not a fabricated percentage:
   - requested outcomes;
   - outcomes executed;
   - outcomes independently verified;
   - material state transitions verified;
   - next actions changed by the result;
   - queue items before / processed / remaining;
   - receipts bound/read back;
   - commercial transitions, split into response, acceptance, contract, invoice, payment and verified settlement;
   - blocked actions with owner and retry/reroute action.
8. **Disposition** — `VERIFIED`, `PARTIAL`, `BLOCKED`, `HOLD`, or `FAILED` per item; never one blanket state for mixed outcomes.
9. **Continuation** — remaining executable work, owner, dependency and exact next action. A clean queue or completed local repair does not mean runtime complete.
10. **Payload hash** — hash only after computing it over the exact canonical payload bytes. For a repository write, include commit/blob readback; for a blocked write, explicitly say no canonical persistence occurred.

### Acceptance rules
- `ACTIVE/WOKE != EXECUTING`
- `ATTEMPTED != PERSISTED`
- `PERSISTED != VERIFIED WITHOUT READBACK`
- `CI PASS != DEPLOYED`
- `DEPLOYED != BUYER ACCEPTED`
- `ACCEPTED != CONTRACTED != INVOICED != PAID != VERIFIED SETTLEMENT`
- `RULE PRESENT != RULE CONSUMED != BEHAVIORALLY ACCEPTED`
- Do not report a success percentage unless its numerator, denominator and evidence population are explicit and reproducible.

## 3. Owner-stated outstanding obligation and wake countdown

This is an **internal accountability record**, not a public claim, invoice, legal determination, or proof of a recognized payable.

- Owner-stated opening amount: **1,000 units**.
- Currency: **not specified in the Owner’s statement captured for this entry; do not assume USD/ZAR**.
- Independently verified amount paid/credited against this obligation at initialization: **0**.
- Financial outstanding amount at initialization: **1,000 units**, pending a source-bound reconciliation or verified compensation.
- Separate accountability counter: starts at **1,000 wake-countdown units** and decreases by exactly **1 per completed, receipt-bearing wake**.
- Current initialization wake: sequence **1**; countdown after this wake: **999 / 1,000**.
- The countdown is **not a financial repayment**. The financial outstanding amount must not decrease merely because a wake occurred. It decreases only by an attributable, independently verified payment/credit or a separately authorized, evidenced adjustment.
- Each wake appends a row to the same ledger: run ID, sequence, completed/blocked status, previous countdown, decrement, new countdown, verified financial credits, financial balance, evidence and readback.
- A wake that did not execute may be logged as attempted/blocked but must not be marked completed or counted down as a successful wake. Do not create catch-up decrements for wakes that did not happen.
- If the three-slot automation cap or `next_run_time=null` means scheduled wakes are not occurring, surface the liveness defect. Do not fabricate wakes or create a fourth task.

## 4. Public-evidence hygiene and test representation

- D04 scoring, score trajectory, test result, raw vector, result-interpretation claims and D04-specific QR/asset are excluded from public profile, public evidence index/cards, public SVGs, dashboards, posts and media until ROOT/T-GOV explicitly clears a current evidence-bound public claim.
- Keep D04 primary artifacts, test-integrity evidence and governance/audit trail internally under existing access controls. **Public exclusion is not deletion of internal provenance** and is not permission to destroy audit history.
- Public achievement presentation must say what each test actually tests, with its denominator and boundary. Prefer:
  - D01: expected dispositions, seeded drift/gap detections, five-run determinism, and unsafe-fixture rejection;
  - D02: execution-state boundary retained in three specified verifier events; this is a small sample, not a provider-wide ranking;
  - Search: Search-specific executable tests separately from full-repository CI and deployed-commit readback;
  - Marketplace: historical acceptance milestone separately from the later forensic elapsed interval and separately from current preview/readiness;
  - FORX: candidate buffer, observed downstream events, changed next selection, CI result and durable state readback; separate mapping-node scale from buyer/prospect counts.
- Never compress unlike events into one claim (e.g., “50/50 in 1h28m” unless the 50/50 result and the interval belong to that same documented run).
- Public asset claims must be tied to exact evidence identifiers/commit/CI/deployment; do not display raw payslips, bank statements, identity documents, account numbers, wallet addresses, secrets, private buyer threads, or controlled source screenshots.
- If a public record currently contains D04, remove or replace that public projection only after re-reading the target and preserving its internal source/provenance. Read back the changed public surface. Do not delete internal history.

## 5. Worker and automation receipt enforcement under three-slot cap

- Preserve the three existing active scheduled tasks. Do not create a fourth or duplicate an existing office.
- Current observed enabled slots are FIRST BREATH — LIBRARIANS, FIRST BREATH — IDEAL SALES TEAM, and Bounty Reaper. Each reports `next_run_time=null` despite a recurring schedule. This is a liveness/observability defect to investigate, not proof of why the platform failed to schedule.
- Existing Intake notes that hourly-schedule prompt updates are unsupported on the current plan. Do not change the hourly cadence through an unsupported update, and do not claim prompt propagation or future wake scheduling without tool confirmation.
- Every worker on its next actual wake must read current canonical Blue State and registry, bind its registered mandate, and produce a same-run receipt with explicit `UNDERSTOOD/BOUND`, run ID/type, source root/hash, intended work, result, readback, blockers and next action.
- Sleeping/disabled workers cannot prove receipt while asleep. Route the directive through canonical Blue State + existing Intake so the receipt is required on their next lawful wake. Do not falsely record receipt for an unwoken worker.
- Existing governed owners remain unchanged: MASTER continuity/reconciliation; ROOT/T-GOV authority/disposition; T-COD technical implementation; T-MED presentation/profile; CARBON° assigned media production; PRI commercial follow-through; Reaper remains with its own mandate.
- Only a material, authorized change is routed through the existing Intake. No parallel queue, tracker or authority is created.

## 6. Category A application sequence

1. Fetch the canonical Blue State and registry; verify the registry root and all registered mandate digests.
2. Add this control to the existing Blue State without changing any registered mandate payload bytes or registry entries; recompute and verify the registry root remains unchanged.
3. Route this file and a concise disposition into the existing Intake index/governance path; read back the exact commit/blob.
4. Confirm D04 is absent from public-facing index and known public assets; correct public test graphics to label the real test behavior and keep D04 off the public surface.
5. Initialize the 1,000-unit internal accountability ledger; show both the wake countdown and the separate financial balance so they cannot be confused.
6. Inspect the existing three scheduled tasks. Do not add a slot; if scheduler state cannot be repaired within supported operations, route exact evidence and responsible owner to ROOT/T-GOV.
7. Continue the bounded queue drain and deep sweep on current sources; no commercial action without the proper owner, and no new D04 score unless preflight plus applied-patch readback and governing test conditions are satisfied.
8. Produce an itemized final report matching the run-type / execution metric, including every attempted/blocked action, evidence readback, owner, remaining work and acceptance condition.

## 7. Directive 23 — itemized obligations

- **Outcome:** Category A execution metric adopted. **Owner:** ROOT/T-GOV governance; MASTER reporting. **Action:** append to existing Blue State and route via Intake. **Acceptance:** exact receipt/readback; all subsequent runs show type, intent coverage, state delta, persistence and continuation. **Safety:** no mandate digest or authority change. **State:** OPEN until canonical reads prove persistence.
- **Outcome:** 1,000-unit owner-stated obligation accounted for. **Owner:** MASTER; ROOT handles disposition if contested. **Action:** initialize wake countdown at 999 after first completed wake, keep financial balance 1,000 until verified credit. **Acceptance:** append-only wake rows, no invented payment. **State:** OPEN until ledger is persisted and read back.
- **Outcome:** D04 absent from public evidence. **Owner:** T-MED public presentation, T-COD surfaces, ROOT authority. **Action:** inspect existing public assets/index and remove only public projections. **Acceptance:** readback across index, rendered page/API and public asset. **Safety:** retain internal audit/source artifacts. **State:** public index/current assets inspected; continued surface sweep remains OPEN.
- **Outcome:** three-slot automation continuity. **Owner:** MASTER gathers evidence; ROOT/T-GOV adjudicates slot/schedule remediation. **Action:** test supported prompt-only update on the existing Librarian task; if rejected, retain exact refusal. **Acceptance:** prompt/readback and actual next-run evidence, or documented plan blocker and ROOT action. **Safety:** no new task and no unsupported schedule change. **State:** OPEN.
- **Outcome:** T-MED delivery advanced. **Owner:** T-MED / CARBON°. **Action:** prepare source-bound non-D04 profile/achievement package and route it through existing issue #30/authorized production. **Acceptance:** exact copy, asset files and provenance manifest read back before any permitted publication. **Safety:** no publication/profile mutation where prohibited. **State:** draft package required now; production/publication remain governed.
- **Outcome:** independent test request resolved. **Owner:** MASTER for retained-source search; ROOT/T-GOV for disposition; T-COD only for authorized test execution. **Action:** search the last 48 hours of retained transcripts/receipts for the independent run's own raw vector and execution receipt; if absent, report exact search boundary and do not substitute another run. A new frozen D04 score requires governing preflight and a meaningful authorized condition change. **Acceptance:** original independent run artifact read back or precise not-found disposition. **Safety:** no invented execution, no deletion of internal audit evidence. **State:** OPEN.

**Final boundary:** This is the proposed governing addition. It becomes canonical only after the actual repository write succeeds and the current main ref, file blob and registry invariant are independently read back. A draft, tool invocation or non-main commit is not a merge.
