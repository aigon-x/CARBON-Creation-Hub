# INRUN-10 — OpenTrain route evidence and latest worker liveness

**Same-run ID:** AMX-DSI-20261011-061646Z  
**Parent 100-point report SHA-256:** 4fc3373103cd0b799d5596ab633b94164450b7dd57f13cf99bb5dccc36b3460b  
**Prior correction packets:** INRUN-08 blob 0b37bc8d270b4d72190421e0390287251d7c78a5; INRUN-09 blob 2ddcf0dece0c32980b244d2e8ec5fe4dbc43be37.  
**Disposition:** latest source checked; commercial route remains HOLD for existing-account recovery; INTAKE NOT CLEARED.

## 1. Latest scheduler readback

The current connected Automations peek still returns 25 records, 3 enabled and 22 disabled.

| Existing task | last_run_time UTC | SAST equivalent | next_run_time |
|---|---|---|---|
| FIRST BREATH — LIBRARIANS | 2026-10-11T18:18:44.113672Z | 2026-10-11 20:18:44 | null |
| FIRST BREATH — IDEAL SALES TEAM | 2026-10-11T17:40:23.974065Z | 2026-10-11 19:40:23 | null |
| Bounty Reaper | 2026-10-11T17:58:58.933845Z | 2026-10-11 19:58:58 | null |

A same-day Librarian receipt chain exists under the *separate* run `AMX-LIBRARIAN-20261011-1954SAST-01`. It independently read back four office receipts with matching Registry v1.2 and mandate digests, and its follow-up item 06 posted/read back existing issue comments. Those are real continuity and governance receipts. The run explicitly labels the 19:54 SAST time as reported runtime context, not a scheduler timestamp; the scheduler's newest Librarian timestamp is 20:18:44 SAST. A receipt attributable to that exact latest timestamp was not found in the present search. The Sales and Reaper results tied to their respective latest timestamps also remain unlocated. No schedule was changed or duplicate run requested to compensate for a missing result channel.

## 2. Verified OpenTrain route — genuine opportunity, not earned income

**Official listing:** [Python Backend Developer for AI Agent Data](https://www.opentrain.ai/jobs/python-backend-developer-for-ai-agent-data--cmutoopjw000306mwfvbs4c88/)  
**Listing ID:** `cmutoopjw000306mwfvbs4c88`  
**Source readback:** retrieved 2026-10-11, official OpenTrain page shows posted 2026-10-04 and “open worldwide”.

The listing states a four-week remote contractor engagement paying **USD 300 per approved task**, with at least **20 hours per week** and **one approved task per day**. Requirements include at least three years of backend development experience, strong Python and a framework such as FastAPI, Flask or Django, REST APIs/microservices, Git, Docker, testing/code quality, and daily AI coding-assistant use. The page says account creation on OpenTrain is free and the applicant is sent to a hiring site to complete the application.

This establishes a live published application path and explicit eligibility/availability gates. It does **not** establish acceptance, a guaranteed task, the exact client payout rail, a completed task, an approved task, or money received.

## 3. Existing commercial record and blocked next action

Current repository record `overdrive/opportunities.json`, blob `d839a401ac8f8f649a89a42af3527e42e7e1fb96`, includes:
- key: `opentrain.ai|python-backend-developer-ai-agent-data|cmutoopjw000306mwfvbs4c88`;
- state: `QUALIFIED`;
- execution_readiness: `HOLD_ACCOUNT_RECOVERY`;
- capital direction: `INBOUND / FREE APPLICATION`;
- reward: USD 300 per approved task;
- required next step: restore the existing account through a secure current login/recovery route; verify truthful 20+ hours/week and one approved task/day availability; no duplicate account.

The corresponding `overdrive/claims.json` blob `2236acb32ce3c1c3ef0132a34f4a4db81358ccc9` marks the same opportunity `QUALIFIED / WAITING`, `external_action_ready=false`, routing reason `HOLD_ACCOUNT_RECOVERY`. Its current next action still requires the existing account recovery route. A prior password-reset message and support-recovery request are recorded, but the source states no inbound support reply supplied a current fresh secure recovery/direct-application route as of its last thread read. Do not infer that an account login works merely because a password-reset email exists. Do not create another OpenTrain account or claim application submission.

**Current opportunity-ledger invariant:** the same opportunities blob declares `record_count=66` while the records map has 83 keys; historical `last_run.full_ledger_count=62` is tied to 2026-10-03T17:42:00Z. Preserve historical fields. The current route remains blocked and no ledger mutation was made by this continuation.

## 4. OVERDRIVE tick acceptance boundary

The most recent inspected tick commit is `2ede2e84120a442636e06bbe887b53c0ecf28a04`, with state blob `2b0fc2dac3fa7b2e7baf8c76cc28fbd98a36641f`. The state is sequence 20, `last_tick=2026-10-11T18:06:48.535779+00:00`, `processed=[]`, `pending=0`, `state_changed=true`, and queue length 20. The tick diff refreshes freshness timestamps and signals. It does not prove a new external action or commercial state transition. The one READY claim remains internal monitoring only: 83 claims, `ready_count=1`, `external_ready_count=0`, and the CallForce READY row has `external_action_ready=false`.

## 5. Category B Directive 23 — itemized disposition

- **Expected outcome:** establish whether a current no-upfront paid route exists, state the precise gating conditions, and preserve the latest scheduler/receipt evidence.
- **Owner:** existing PRI for post-handoff progression and the existing OpenTrain thread/account path; applicant/Owner for any credential/account-only step; ROOT/T-COD for ledger/readiness invariant; MASTER/LIBRARIAN for receipts and continuity.
- **Action performed:** rechecked official OpenTrain listing; compared the listing with current opportunities and claims rows; refreshed the 25-task scheduler peek; reviewed the separate Librarian 19:54 receipt chain and its issue-comment readback.
- **Dependencies/blockers:** existing OpenTrain account/recovery route not freshly verified; applicant availability/experience gates must be truthfully confirmed; exact payout rail and actual task approval are not yet known; latest scheduler-output linkage remains incomplete.
- **Acceptance evidence:** official listing URL; current opportunities blob `d839a401ac8f8f649a89a42af3527e42e7e1fb96`; claims blob `2236acb32ce3c1c3ef0132a34f4a4db81358ccc9`; current Automation peek; Librarian receipt commits cited in INRUN-09.
- **Persistence/readback:** keep this as a same-run evidence delta; link from the existing GitHub ROOT Intake Index, existing Notion ROOT receipt index, and issue #3/#31. Read back each pointer.
- **Safety/preservation:** no application submitted, no external message sent, no credential request, no duplicate account, no paid product/plan, no bond or wallet spend, and no income inferred. No state/ledger change was made.
- **Item-level disposition:** OpenTrain role = VERIFIED PUBLISHED / QUALIFIED RECORD / ACCOUNT RECOVERY HOLD; scheduler last-runs = RECORDED / exact outputs not all attributed; OVERDRIVE tick = FRESHNESS UPDATE / 0 ITEMS PROCESSED; income = NOT VERIFIED.
- **Remaining work:** obtain a legitimate current login/recovery route; verify applicant eligibility/availability; proceed only through the existing application route with user/office authorization; persist any resulting application/task/approval evidence and payout confirmation; resolve the ledger count and READY-vs-external-ready semantics through issue #31.

**Disposition:** source-backed opportunity preserved; no submission or revenue claim. **INTAKE NOT CLEARED.**
