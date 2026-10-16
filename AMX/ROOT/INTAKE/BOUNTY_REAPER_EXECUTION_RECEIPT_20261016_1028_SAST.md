# Bounty Reaper — continuation receipt 2026-10-16 10:28 SAST

RUN_ID: BR-20261016_1028-SAST-01
PARENT_RECEIPT: AMX/ROOT/INTAKE/BOUNTY_REAPER_EXECUTION_RECEIPT_20261016_1001_SAST.md
OFFICE: BOUNTY REAPER
MANDATE: AMX-MANDATE-BOUNTY-REAPER-V1
RESULT: PRODUCTIVE STATIC TRIAGE; ONE PUBLIC UUID-ZERO CLAIM KILLED; OTHER VARIATIONAL HYPOTHESES NOT PROMOTED
TRACKER: TRACKER_WRITE_BLOCKED
Q1: UNKNOWN, NOT ZERO
EXTERNAL_SUBMISSIONS / REPORT_IDS / AWARDS / VERIFIED_PAYMENTS: NONE ESTABLISHED

## 1. Canonical mandate and current worker truth

The existing same-day 10:01 SAST receipt was recovered and read in full before this continuation. It is the parent, so this record does not replace its already-recorded Variational and SP1 work.

Pre-flight readback (unchanged current canonical sources):
- Registry: `AMX/ROOT/BLUE_STATE/MANDATE_REGISTRY_V1.json`, blob `d3a749a48d98292a13931fd6ff8518dea03e5b20`; version 1.2; state `OWNER_ACCEPTED_MERGED_BLUE_STATE`.
- Registry root SHA-256: `6f46db56ce4b54bd4655f9e0f5e919dcdb004520d6a0acd455281841a1d7912f`; recomputed from the 12 sorted `ROLE_KEY=MANDATE_SHA256\n` rows: MATCH.
- Mandate binding: `AMX/ROOT/BLUE_STATE/BLUE_STATE_MANDATE_BINDING_AND_PREFLIGHT_V1.md`, blob `c70d43754a93fa2c7778baeeb6ee0bebe33e94ed`.
- Role `BOUNTY-REAPER`, mandate ID `AMX-MANDATE-BOUNTY-REAPER-V1`, status CURRENT. Marker-bounded payload: 1,082 UTF-8 bytes; recomputed SHA-256 `754d8fb9b6816da1bf0013940883106e0d3928b1637526ee82b38e1792c1dcd3`: MATCH.

The one existing Reaper automation was re-read live:
- ID `6abf8e6d6a188191aee2b5d3fe24a9c9`
- `is_enabled=false`
- `last_run_time=2026-10-16T07:39:24.104141+00:00`
- `next_run_time=null`
- `updated_at=2026-10-16T07:40:27.683206+00:00`
- Stored schedule remains the original hourly VEVENT (`DTSTART;TZID=Africa/Johannesburg:20261008T224500`, `RRULE:FREQ=HOURLY`).

No scheduler mutation, enable action, immediate-run request, duplicate worker, or duplicate schedule was made. The 10:01 SAST receipt already records the currently observed worker as disabled with null next-run time. That remains a ROOT liveness/reconciliation item. Manual research continues independently; the scheduler stays untouched while the existing worker is at rest.

## 2. Current Variational program gates

The official Immunefi scope page was freshly retrieved at this continuation:
- https://immunefi.com/bug-bounty/variational/scope/
- https://immunefi.com/bug-bounty/variational/information/
- The official deployed-address document: https://docs.variational.io/technical-documentation/mainnet-contracts
- The official audit index: https://docs.variational.io/technical-documentation/audits

Scope page states a maximum bounty of USD 100,000; live since 16 March 2026; last updated 15 October 2026; PoC and KYC required. It includes qualifying unauthorized loss/theft or permanent freeze of funds and protocol insolvency, but excludes attacks requiring privileged addresses absent additional modification of privilege. The submission gate is therefore not satisfied by a role-gated operational edge alone.

The official audit index links the public Cantina-managed/Spearbit Variational report, completed February–March 2026:
https://docs.variational.io/technical-documentation/audits
The report itself:
https://3617648257-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FmoFQRSZ6KLfe4tnHIWRJ%2Fuploads%2Fin03zKRaj1ZCcTYLfaUn%2FSpearbit_Variational_Report_PUBLIC.pdf?alt=media&token=75976e59-fc34-481b-802f-db56af537ee3

The report's page 4 records two high-risk findings as acknowledged by both Variational and Cantina Managed: (1) switching the Oracle's factory causes denial of service for existing pools when the old factory no longer serves their pool registry; (2) missing access control in a historical `SettlementPoolDeployer.deploy` path. These are public prior art, not fresh bounty claims.

## 3. Material continuation — third-party UUID-zero withdrawal claim killed

Public hypothesis source reviewed:
- Sidecar test blob `e41938cb17de13a4a09a1b0f10e32bff97a77433`, `tradewife/night-shift-security/foundry/test/VariationalFalsifier.t.sol`:
  https://github.com/tradewife/night-shift-security/blob/main/foundry/test/VariationalFalsifier.t.sol
- Sidecar source copy blob `64a140bb950cded4180cc5985b0e8c5aa8cab056`, `foundry/src/variational/src/SettlementPool.sol`.
- The public test labels `test_PROP_014b_batch_overdeposit_with_uuid0_freeze_exploit` as evidence that a first withdrawal with `transferUuid=0` succeeds and a second withdrawal fails, permanently freezing the other party's funds.

The claim fails against the verified deployed source already recovered in the parent receipt. In `SettlementPool._withdrawUSDCOnBehalf(...)`, the source requires:
`require(transferUuid != 0, "must provide non-zero transferUuid");`
before checking/marking `transfers_processed` or transferring USDC. Both `withdrawUSDCNoEvent` and `withdrawUSDC` call this internal method. Therefore a withdrawal with zero UUID cannot be the first successful withdrawal described by that test. `Oracle.processTreasuryManagementWithdrawals` catches item failures, so an outer successful batch call would not make the failed item a successful withdrawal. The test's claimed “first UUID-zero withdrawal succeeds” is contradicted by the source; the alleged UUID-zero permanent-freeze exploit is **A — KILLED / NOT REPRODUCED BY SOURCE**. No deployed call, test transaction, live probe, or fund movement was made.

Related zero-ID deposit path:
- The verified source permits a zero UUID to remain unmarked in `_depositUSDCOnBehalf`, but the relevant treasury route is only callable through Oracle paths with `PROVIDER_ROLE`. That demonstrates a provider-controlled repeat-deposit/idempotency edge, not theft or an unprivileged way to take funds. Under the current official scope's privilege exclusion and with no qualifying outsider impact established, it is **B — PRIVILEGED PATH / NOT PROMOTED**.
- `Oracle.transferFromOLPToPool` can route a supplied pool address without checking it against the pool registry in source, but it is likewise gated by `PROVIDER_ROLE`; no independent privilege-escalation vector was established. **A/B — PRIVILEGED OPERATING PATH; NO BOUNTY CANDIDATE.**
- The public sidecar's “creator overdeposit per batch item” claim depends on treating a batched item list with distinct `parentQuoteUuid` values as if the creator contribution should be paid only once. The public interface documents `parentQuoteUuid` as the UUID associated with an individual quote, and each batch item holds its own UUID. This static read does not establish that per-item creator contribution is incorrect under intended semantics, nor a qualifying loss. **B — SPECIFICATION/IMPACT NOT ESTABLISHED; NOT PROMOTED.** The sidecar was read as public prior art, not as AMX-owned work. No local Foundry tests were run by this wake.

## 4. Consolidated Variational dispositions after this continuation

- Factory-pointer switch: **A — KILLED AS PUBLIC AUDIT PRIOR ART; ACKNOWLEDGED.**
- Historical `SettlementPoolDeployer.deploy` access control: **A — NOT THE REVIEWED FACTORY DEPLOYMENT PATH.** The current verified `SettlementPoolFactory.createPool` source gates caller to owner or configured Oracle; do not transfer the historical finding onto this path without exact evidence that the vulnerable path remains active.
- UUID-zero withdrawal / permanent-freeze sidecar claim: **A — KILLED BY EXPLICIT NONZERO-WITHDRAWAL GUARD.**
- UUID-zero treasury deposit/repeatability: **B — PROVIDER-ROLE GATED; NO ELIGIBLE UNPRIVILEGED IMPACT ESTABLISHED.**
- Batch creator “overdeposit” premise: **B — INTENDED PER-ITEM SEMANTICS / QUALIFYING IMPACT NOT ESTABLISHED.**
- Arbitrary pool routing from `transferFromOLPToPool`: **A/B — PROVIDER-ROLE GATED; NOT A SUBMISSION CANDIDATE UNDER CURRENT SCOPE.**

No candidate survived the exact privilege, impact, novelty/audit-dedupe and runnable-PoC gates. No bounty report was prepared or submitted.

## 5. Queue/tracker truth and outstanding work

The authoritative `AMX Bounty Reaper — Live Tracker` spreadsheet remains unread and unwritten. Connected workspace lookup in the parent receipt established that Google Drive is `DISABLED_BY_ADMIN`, with installation unavailable. That is a narrow ROOT/admin route issue; it does not block current static research. Do not claim a Runs row or queue readback.

- Tracker status: `TRACKER_WRITE_BLOCKED`.
- Queue Q1: `UNKNOWN, NOT ZERO`.
- External submission/report IDs/acceptance/award/receivable/verified payment: none established.
- Existing automation: remains disabled as currently observed; do not enable or spawn a duplicate in this continuation.
- Next lawful action: continue with another distinct, current-scope candidate that has a plausible unprivileged impact path and a runnable local PoC route; skip the killed public claims above. ROOT/admin retains responsibility to restore authorized Sheets/Drive read-write/readback and reconcile the one existing scheduler.

RUN_RESULT: PRODUCTIVE — VARIATIONAL UUID-ZERO WITHDRAWAL/FREEZE CLAIM KILLED AGAINST VERIFIED SOURCE; PROVIDER-GATED UUID-ZERO DEPOSIT EDGE AND BATCH OVERDEPOSIT PREMISE NOT PROMOTED; PUBLIC AUDIT DEDUPE PRESERVED; NO Q1 CANDIDATE OR PAYMENT ESTABLISHED.
TERMINAL: NO — execution obligation remains open.
