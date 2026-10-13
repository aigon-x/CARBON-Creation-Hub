# Bounty Reaper — Execution Receipt

RUN_ID: BR-20261013-1055-SAST-02
OBSERVED: 2026-10-13 10:55 SAST
OFFICE: BOUNTY REAPER
PARENT_PREFLIGHT: BOUNTY_REAPER_PREFLIGHT_RECEIPT_20261013_1038_SAST.md
PARENT_PREFLIGHT_READBACK_BLOB: 29ab1cac33b6051043faef69e05d1b33b0a9081b

## Outcome summary

- Mandate pre-flight: PASS (see parent pre-flight receipt; canonical registry root and exact 1,082-byte Reaper payload digest were recomputed and matched).
- Q1 recovery: UNRESOLVED. Accessible Root Intake receipts and repository job inventory were searched. No accessible submission-ready packet or external receipt was found; this does not establish Q1=0 because the canonical tracker/Drive handoff could not be read.
- Tracker: TRACKER_WRITE_BLOCKED. The runtime tool inventory contains no authorized Google Sheets/Drive read-write/readback action for the existing Live Tracker ID 1ETiK6b2YOz499OXBA5wuvgyWMjnDZoEdJIwCt2xGeCk. The attempted action was to obtain authorized connector capability, then read Runs/Queue/Payouts, append one Runs row, and independently read it back. No Sheets API call could be invoked; no tracker read, append or readback occurred.
- Current automation owner: existing Bounty Reaper automation 6abf8e6d6a188191aee2b5d3fe24a9c9 was observed disabled by live automation lookup. Older Intake records saying enabled are stale snapshots. This run made no schedule or enable-state change.
- External lifecycle: no submission, external report ID, acceptance, award, receivable or verified payment established.

## Material work — independent program screen

### LayerZero BR-20261003-024

- Current official program information was re-read at https://immunefi.com/bug-bounty/layerzero/information/ and the current scope at https://immunefi.com/bug-bounty/layerzero/scope/ (official program last updated 2026-10-02).
- Current rules require a runnable PoC with end effect for all severities, exclude vulnerabilities marked in LayerZero-Labs/Audits, and apply Primacy of Impact to Critical/High smart-contract impacts only.
- The prior pinned-source review identifies `nativeDrop` and `nativeDropAndExecute302` as ADMIN_ROLE-gated, shows failed native drop is recorded but `lzReceive` is still attempted, and identifies an admin-only withdrawal route. The failed-drop receive-prevention and permanent-lock/no-recovery subclaims remain killed. This wake did not independently bind a deployed Executor implementation or complete audit-PDF dedupe.
- Disposition: the existing retained-funds/refund hypothesis remains NOT SUBMITTABLE on evidence available. No unprivileged attacker-controlled path, qualifying Critical/High impact, identified victim/funds at risk or compliant runnable PoC is established. Parent BR-20261003-024 remains Q3/PARKED only for a materially distinct path with exact eligible deployment, qualifying impact, complete dedupe and local/fork PoC; do not reopen the same killed subclaims.

### Stargate V2 — distinct lawful source screen

- Current official program: https://immunefi.com/bug-bounty/stargate/information/ (scope/information current page states PoC and KYC are required; completed audit reports are published by the project, and unfixed audit findings are not reward-eligible).
- Screened in-scope `FeeLibV1ETH` fee logic using public source `stargate-protocol/stargate-v2` `packages/stg-evm-v2/src/feelibs/FeeLibV1.sol`, blob `bea4e8a01305bb91e68027ef6e8afa08bc0ace31`, and its unit test `packages/stg-evm-v2/test/unitest/feelibs/FeeLibV1.t.sol`, blob `bfdb61dd9a1eaf2ba40606db36fd58f1ed303cde`.
- Candidate checked: fee formula computes floor(amount × fee / 1,000,000) + 1 for nonzero fees, so a mathematically exact multiple is charged one additional shared-decimal unit. The current test oracle explicitly encodes the same expression as expected behavior. Static disposition: A — NOT A NOVEL BOUNTY CANDIDATE on this evidence; no submission package built, and no tests were run in this wake. This is a code/test-specification observation, not proof about every deployment or a claim of user loss.
- Separately checked public Stargate V2 issue #104, https://github.com/stargate-protocol/stargate-v2/issues/104. The issue describes inability to recover a transfer to an invalid recipient; GitHub records it closed on 2026-03-02, and the maintainer response describes this as a deliberate same-chain-aligned behavior for user-supplied wrong addresses, distinct from transient receive failures. Disposition: A — known public behavior, not a novel report. Do not submit it.
- No local/fork PoC was run; no live target, testnet, transaction, funds or external submission was used.

## Current parcel inventory and queue truth

- Accessible prior receipts also classify the narrow Sei Giga abort hypothesis as killed; XOXNO stale/non-returned-position claim as not reproduced; sBTC nonce-response behavior as public prior art; Veda request-integrity, Axelar origin and OpenBridge stale-vote subclaims as killed/narrowed; vesting arithmetic as an unpromoted signal without established bounty eligibility or practical impact.
- The accessible BLACK/jobs inventory contains historical Reaper LayerZero and XOXNO job files; this inventory and the receipt search did not establish a ready Q1 packet. Because Runs/Queue/Payouts and Drive are inaccessible, Q1 remains UNKNOWN, NOT ZERO.
- No qualifying live Q2/Q1 finding was established in this wake. The LayerZero parent remains Q3/PARKED for a distinct future path. The separate Stargate screen produced two dispositions that should not be resubmitted.

## Durable receipt / fallback

TRACKER_WRITE_BLOCKED: the required existing Tracker read → append Runs row → independent row readback could not be invoked because this runtime exposes no authorized Sheets/Drive connector. This receipt is the same-run fallback in existing Root Intake, not a replacement tracker. It must be fetched back after commit; Queue/Payouts remain untouched.

## Directive 23 itemized addendum

1. Expected outcome: canonical mandate bound. Owner: Bounty Reaper. Action: reuse the immediately preceding digest-verified pre-flight. Dependency: canonical Registry/Blue State. Acceptance evidence: parent receipt and canonical hashes match. Persistence/readback: parent receipt independently fetched and matched. Safety: no authority expansion. Disposition: PASS. Remaining: repeat each wake.
2. Expected outcome: completed Q1 work drained. Owner: Bounty Reaper + ROOT/authorized connector owner. Action: read Runs/Queue/Payouts and Root Drive/handoff, submit any eligible Q1 through official route and preserve external receipt. Dependency/blocker: Tracker/Drive read access unavailable. Acceptance: actual queue reconciliation and official external receipt, not absence of local files. Persistence/readback: this fallback receipt only; no Tracker row. Safety: no inference that Q1=0. Disposition: HOLD / UNKNOWN. Remaining: restore authorized connector and reconcile Q1.
3. Expected outcome: advance or kill live Q3. Owner: Bounty Reaper. Action: reconcile exact LayerZero source semantics and current impact rules. Dependency: exact deployed implementation, distinct eligible actor/impact, full audit dedupe and local/fork PoC absent. Acceptance evidence: pinned-source prior receipts plus current official program information. Persistence/readback: this execution receipt. Safety: static/research only. Disposition: current native-drop hypothesis NOT SUBMITTABLE; parent remains Q3/PARKED only for a materially distinct path. Remaining: do not repeat killed subclaims; reopen only with new evidence.
4. Expected outcome: use other executable work rather than idle at one gated parcel. Owner: Bounty Reaper. Action: screen separate Stargate V2 fee-rounding and failed-recipient candidates. Dependency: public source/test and public issue state. Acceptance evidence: current fee test encodes +1 as expected; issue #104 closed with deliberate behavior response. Persistence/readback: this receipt. Safety: no live interaction or submission. Disposition: both candidates A / NOT SUBMITTABLE as novel reports. Remaining: continue to another distinct source/asset when an actionable candidate is identified.
5. Expected outcome: lifecycle and payment truth preserved. Owner: Bounty Reaper / ROOT. Action: distinguish research from submission, award and settlement. Dependency: no external receipt or award evidence. Acceptance: external lifecycle evidence required. Persistence/readback: this receipt. Safety: no payout inference. Disposition: no submission/award/payment claimed. Remaining: submit only a complete, eligible packet through the official program route.
6. Expected outcome: single-worker/runtime liveness reconciled. Owner: ROOT / existing automation owner. Action: reconcile why existing automation is disabled despite old enabled receipts and restore a permitted existing cadence after acceptance controls pass. Dependency: scheduler owner authority and confirmed Tracker/readback route. Acceptance: live task state readback and fresh attributable worker result. Persistence/readback: current live automation lookup recorded in parent preflight receipt. Safety: no duplicate worker or scheduler, and this run makes no schedule change. Disposition: OPEN / ROOT ACTION REQUIRED. Remaining: reconcile and authorize.

RUN_RESULT: MATERIAL STATIC SCREENING; NO SUBMISSION-READY PACKAGE ESTABLISHED
TRACKER: TRACKER_WRITE_BLOCKED
Q1: UNKNOWN, NOT ZERO
SUBMISSIONS: NONE ESTABLISHED
AWARDS/PAYMENT: NONE ESTABLISHED
SAFETY: NO LIVE EXPLOITATION, PROHIBITED TESTING, FUND MOVEMENT, SPEND, CREDENTIAL EXPANSION, OR PUBLIC DISCLOSURE

## Post-commit ROOT routing attempt

- Attempted to deliver a model-visible parent/ROOT notification referencing this receipt and the Tracker/scheduler blockers.
- Result: `NOT_FOUND: HTTP error prior to action invocation; HTTPException 404: Action not found`.
- Truth boundary: no direct parent notification was delivered. The existing Root Intake receipt and Intake Index remain the persisted fallback. ROOT recovery is still required; do not infer connector restoration, queue reconciliation or scheduler reactivation.

## Continuation slice — Stargate FeeLib boundary check (2026-10-13 11:09 SAST)

- The same `_calculateFee` expression was evaluated at the valid owner-configured boundary `feeMill = FEE_DENOMINATOR = 1,000,000`. For every positive amount, integer-division result is the amount itself and the appended `+ 1` yields `amount + 1`; `applyFeeView` then attempts `amountInSD - fee`, which underflows/reverts (apart from uint64 conversion boundary behavior).
- The contract permits a 100% fee configuration, but `setFeeConfig` is `onlyOwner`. The relevant unit test explicitly assumes away inputs for which `expectedFee > _amountInSD` and comments that underflow can occur in real life; it uses the same formula as the expected oracle.
- Disposition: B — configuration edge recorded / NOT PROMOTED. This is owner-configuration-dependent and no unprivileged actor path, affected production config, qualifying user-funds impact, or bounty-eligible exploit was established. It is not a report package. If later public deployment evidence shows an active in-scope path set to 100%, reassess only with authorized local/fork PoC and current program scope.
- Source blobs: FeeLibV1.sol `bea4e8a01305bb91e68027ef6e8afa08bc0ace31`; FeeLibV1.t.sol `bfdb61dd9a1eaf2ba40606db36fd58f1ed303cde`.

## Continuation slice — Stargate shared-decimal dust path (2026-10-13 11:10 SAST)

- Reviewed current public source in `StargatePool.sol`, `StargatePoolNative.sol`, `StargateBase.sol` and the `StargateOFT` variant.
- For ERC-20 `StargatePool._inflow`, the source computes `amountSD = _ld2sd(_amountLD)` then transfers only `_sd2ld(amountSD)` from the sender: non-representable local-decimal dust is not transferred in the first place. The pool deposit returns/mints the normalized amount, so no loss of the dust to the pool was established.
- For native deposits, `StargatePoolNative._assertMsgValue` requires `msg.value == _amountLD` and `_amountLD == _sd2ld(_ld2sd(_amountLD))`; inputs carrying non-representable dust revert. For native send paths, `_assertMessagingFee` explicitly treats any value above normalized amount plus quoted fee as extra messaging fee; source comment states that dust may remain in `msg.value`. This is explicit handling, not evidence of a novel stuck-dust loss.
- StargateBase `_ld2sd` floors by `convertRate`, but the concrete ingress/validation paths were the decisive checks. Disposition: A — DUST-LOSS HYPOTHESIS KILLED / NOT SUBMITTABLE on the inspected paths. Scope/deployment source remains current public main rather than a verified deployed immutable target; this static pass does not assert unrelated security.
- Static-only; no local/fork test, live contract call, transaction or fund movement. Source locations: `stargate-protocol/stargate-v2/packages/stg-evm-v2/src/StargatePool.sol` (notably `_inflow` and `deposit`), `StargatePoolNative.sol` (`_assertMsgValue`, `_assertMessagingFee`), `StargateBase.sol` (`_ld2sd` / `_sd2ld`).

## Additional Directive 23 disposition

7. Expected outcome: test the fresh shared-decimal dust hypothesis through the concrete ingress paths. Owner: Bounty Reaper. Action: trace ERC-20 pool ingress, native deposit validation and native send fee handling. Dependency: current public source and tests. Acceptance evidence: transfer amount normalization, native input dust rejection, and explicit messaging-fee adjustment. Persistence/readback: this appended receipt and refreshed Intake Index pointer. Safety: static only, no live/fork interaction. Disposition: A / KILLED for the narrow dust-loss hypothesis. Remaining: no work on this sub-claim absent contradictory in-scope deployed-source evidence.
