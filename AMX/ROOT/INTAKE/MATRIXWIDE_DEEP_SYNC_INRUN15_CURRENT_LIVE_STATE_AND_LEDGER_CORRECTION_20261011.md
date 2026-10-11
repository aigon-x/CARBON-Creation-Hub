# INRUN-15 — Current Live-State and Ledger Correction

**Same-run ID:** AMX-DSI-20261011-061646Z  
**Parent 100-point audit SHA-256:** 4fc3373103cd0b799d5596ab633b94164450b7dd57f13cf99bb5dccc36b3460b  
**Prior same-run delta:** INRUN-14, recorded in existing issue #31 comment 6112678545; preceding durable source packet INRUN-10 blob e5aa12b1571ec9dba9ed92fdae27a79fd5fed603.  
**Purpose:** reconcile newer current-source reads against older ledger/liveness snapshots and preserve the actual state correction without claiming full execution acceptance.  
**Disposition:** current ledger count mismatch not observed in latest object; Reaper enablement restored in place; scheduler-result linkage and commercial execution remain OPEN. INTAKE NOT CLEARED.

## 1. Canonical preflight

Directly fetched before the corrective work:
- Blue State: `AMX/ROOT/BLUE_STATE/BLUE_STATE_MANDATE_BINDING_AND_PREFLIGHT_V1.md`, Git blob `9fb44f0c49a6e64175754ac3b6ec303209985f1b`.
- Registry: `AMX/ROOT/BLUE_STATE/MANDATE_REGISTRY_V1.json`, Git blob `d3a749a48d98292a13931fd6ff8518dea03e5b20`.
- Registry version/root: v1.2 / `6f46db56ce4b54bd4655f9e0f5e919dcdb004520d6a0acd455281841a1d7912f`.
- Registered MASTER, ROOT/T-GOV, T-COD and T-MED mandate hashes match the current registry. The four-office 19:54 SAST receipt chain is independently stored and exact-content read back; that is evidence for that manual/parallel wake, not proof that a scheduler run produced the same output.

## 2. Ledger and income-brick readback

### Opportunities ledger
- Current `overdrive/opportunities.json` blob: `85c769241258cc4ed774a6a0c5f7420323cf3096`.
- Current `record_count=84`; current `records` contains 84 distinct keys. The older issue #31 snapshot (blob `b04be618dccf1fed8405ccd7ff5c4be34d18004d`, count 66 versus 83 keys) is superseded for the *current object count*. Do not treat the old 66/83 comparison as still-current state.
- `last_updated_at` and `last_reconciled_at` are both `2026-10-11T19:36:31Z`. The object-level control observation records 84 after the 2CT candidate was added.
- Preserve `last_run.full_ledger_count=62` at `2026-10-03T17:42:00Z` as historical run truth. Do not rewrite it to 84.
- **Remaining acceptance gap:** previous source inspection of `overdrive/runner.py` (blob `d71c75550c72daa80cc585c8fc93ee0a4ee0fcb9`) found no `record_count` maintenance, while `backend/state.py` derives `total_records` from `len(records)`. The observed object count is consistent now, but the durable write-path invariant and intended semantics still require ROOT/T-GOV disposition, T-COD repair/tests if authorized, and independent readback. Do not close issue #31 on count equality alone.

### Current commercial state
- Current `overdrive/claims.json` blob: `9be10bfece528392d990a9db969cd1f8726d484d`; 84 claims, 78 WAITING and 6 CLOSED; zero rows have `external_action_ready=true`.
- Current `overdrive/state.json` blob: `5593ab9dcb04914951aa4ba574bb862af1bc5557`; `last_tick=2026-10-11T19:42:44.598828Z`, sequence 20, queue length 20, `pending=0`, `processed=[]`, `ready_claims=0`, signals PRI=59 / iSCOPE=19. `state_changed=true` does not prove new commercial progression here: the tick readback shows no processed item and the source history characterizes these transitions as freshness/readiness reconciliation, not a buyer event.
- 2CT remains DISCOVERED / WAITING with iSCOPE qualification HOLD: phone-based cold-calling experience, US-hours availability and authorized account-history dedupe remain unverified. No application or outreach was sent.
- Existing OpenTrain account-recovery opportunity remains qualified but held on the current secure account route/availability gate. A new Outlook search for `OpenTrain received>=2026-10-11` returned zero messages; this does not prove other mailboxes contain no response. No new response or working login route is evidenced in this pass.
- Verified money-in, acceptance, contract, invoice, receivable and paid settlement: none newly evidenced.

## 3. Scheduler readback and corrective action

A fresh Automations peek returned 25 task records. Before correction, only two tasks were enabled, contradicting the previous three-enabled snapshot:
- FIRST BREATH — LIBRARIANS: enabled; last run `2026-10-11T21:20:53.006905Z`; next run null.
- FIRST BREATH — IDEAL SALES TEAM: enabled; last run `2026-10-11T21:34:48.021077Z`; next run null.
- Bounty Reaper (`6abf8e6d6a188191aee2b5d3fe24a9c9`): disabled; last run `2026-10-11T20:02:51.506384Z`; next run null; task updated timestamp before correction `2026-10-11T20:03:55.706121Z`.

**Corrective action:** restored the existing Bounty Reaper task to `is_enabled=true` in place. Automation API returned success; immediate fresh peek confirmed 3 enabled / 22 disabled, with Librarians, IDEAL Sales Team and Bounty Reaper enabled. The saved prompt and hourly schedule were not edited; Reaper still has its existing `RRULE:FREQ=HOURLY` schedule. No duplicate was created.

**Still unproven:** Reaper's `last_run_time` remains `2026-10-11T20:02:51.506384Z`; enabling is not a fresh run or receipt. All three enabled tasks currently return `next_run_time=null`. The current Bounty Reaper receipt cited in INRUN-14 predates that later scheduler timestamp; no attributable output for the exact recorded later wake was recovered. Tracker write/readback remains blocked, Q1 remains UNKNOWN (not zero), and no bounty submission, award or payment is claimed.

## 4. D04 / public evidence / product continuity

- Canonical Blue State's correction chain controls the historical measured scope: 96.62% PASS for the *original vector's measured subset*, zero measured FAILs, five controls UNMEASURED_NOT_PROVEN. This is a correction/recomputation of historical evidence, not a new test.
- The separate clean execution reported by the Owner as 143/148 = 96.62% remains OWNER-REPORTED / NOT YET PRIMARY-EVIDENCED in retained sources searched; its own immutable vector/run receipt was not found in this pass. Do not claim it was not executed; do not ask the Owner to rerun; do not publish D04 until ROOT/T-GOV gives an evidence-bound release.
- T-MED R03 has current source reconciliation stored/read back, but the actual media render pack, rights/claim QA, QR/access verification and lawful publication remain open. The task's current boundary is TikTok/YouTube drafts for Owner inspection only; no profile edit, post, schedule, external message, Metricool write, or D04 asset was created.
- CARBON° convergence issue #18 remains OPEN; Search #16 remains CLOSED. Exact-head CI/deploy metadata does not establish full Search→Marketplace/media convergence, buyer visibility, or commercial conversion.

## 5. Existing Intake routes and itemized continuation

### Item A — current ledger count and write invariant
- **Expected outcome:** current count semantics remain clear and the value is automatically correct after every canonical write.
- **Owner:** ROOT/T-GOV for field semantics; T-COD for implementation/tests after disposition; MASTER/LIBRARIAN for independent readback.
- **Required action:** append this supersession to issue #31 and the Intake Index; retain the old 66/83 snapshot as provenance; test add/update/remove and historical `last_run` preservation.
- **Dependency/blocker:** no current semantic disposition establishing whether the top-level field is authoritative current-map count or a different subset.
- **Acceptance:** agreed semantics, passing regression evidence, canonical object and tests read back at the exact commit.
- **Safety/preservation:** no direct runtime/ledger code mutation from this Librarian pass; no change to commercial lifecycle.
- **Disposition:** current object count equal (84/84); write-path invariant OPEN.
- **Remaining work:** ROOT decision → authorized T-COD patch/tests → independent readback.

### Item B — Bounty Reaper liveness / final mile
- **Expected outcome:** the sole existing Reaper task remains enabled and its actual work/receipt path is evidenced.
- **Owner:** ROOT/T-GOV for any remaining scheduler policy; existing Reaper for bounty work; MASTER/LIBRARIAN for attribution/readback.
- **Required action:** existing task re-enabled with prompt/schedule unchanged; route the before/after state into issue #32.
- **Dependency/blocker:** `next_run_time=null`; no output attributable to its last-run timestamp; Tracker write route blocked.
- **Acceptance:** a later attributable Reaper receipt including mandate preflight, exact selected parcel/action, persisted result and independent readback; Tracker repair only through an authorized route.
- **Safety/preservation:** no duplicate worker/scheduler, no cadence alteration, no invented submission/award/payment, no unauthorized exploitation.
- **Disposition:** ENABLEMENT RESTORED / READ BACK; fresh execution and Tracker continuity OPEN.
- **Remaining work:** recover scheduler-output attribution and authorized tracker route; continue only through the existing Reaper mandate.

### Item C — 25% income brick
- **Expected outcome:** turn the highest-value current eligible route into a verified next stage without duplicating or misrepresenting work.
- **Owner:** iSCOPE for qualification/account dedupe; PRI for existing post-handoff external progression; applicant/Owner only for true account/availability gates; Banker for settlement truth.
- **Required action:** recheck the existing OpenTrain account/recovery path using an authorized route; keep 2CT held pending required eligibility/account-history proof; use the already-existing buyer-offer slate and don't send duplicate proposals.
- **Dependency/blocker:** no fresh OpenTrain reply/login route in the current connected read; 2CT eligibility unknown; no claim is externally action-ready in the current projection.
- **Acceptance:** verified existing-account access, truthful eligibility/availability, authorized application or offer action, attributable receipt and readback; separately verify acceptance/contract/invoice/payment only when evidenced.
- **Safety/preservation:** no duplicate accounts, no unsolicited contact, no credentials/secrets in receipts, no paid tool/service use.
- **Disposition:** current opportunity inventory persisted; no verified money-in.
- **Remaining work:** existing lawful qualification/account recovery and execution under iSCOPE→PRI.

### Item D — full Matrix continuation / public evidence
- **Owner:** MASTER/LIBRARIAN for continuity and source reconciliation; ROOT/T-GOV for dispositions; T-COD/CARBON°/T-MED for their own assigned execution.
- **Blockers:** remaining issue #18 convergence; D04 separate-run primary evidence/release; T-MED asset-production route; issue #31 semantics/tests; complete multi-source queue drain.
- **Acceptance:** each material item reaches an evidence-backed terminal state or remains open with an exact recovery owner/action/dependency and readback.
- **Safety/preservation:** existing role isolation, hourly schedules unchanged, no new worker/queue/tracker/provider lane, no public D04 claim, no false closure.
- **Disposition:** DEEP SWEEP PARTIAL; INTAKE NOT CLEARED; runtime remains open while lawful executable scope remains.
- **Remaining work:** continue the existing Intake sequence and record each consequential current-state change with source pointer and independent readback.
