# Bounty Reaper Execution Receipt — 2026-10-15 20:56 SAST

RUN_ID: BR-20261015-2056-SAST-01
OFFICE: BOUNTY REAPER
MANDATE: AMX-MANDATE-BOUNTY-REAPER-V1
STATUS: PRODUCTIVE STATIC/SCOPE ADVANCEMENT; TRACKER_WRITE_BLOCKED; Q1 UNKNOWN, NOT ZERO.

## Mandatory canonical pre-flight — PASS

Directly fetched from `amillimatrix-eng/CARBON-Creation-Hub`:
- Registry: `AMX/ROOT/BLUE_STATE/MANDATE_REGISTRY_V1.json`; Git blob `d3a749a48d98292a13931fd6ff8518dea03e5b20`.
- Binding: `AMX/ROOT/BLUE_STATE/BLUE_STATE_MANDATE_BINDING_AND_PREFLIGHT_V1.md`; Git blob `c70d43754a93fa2c7778baeeb6ee0bebe33e94ed`.
- Registry version/state: `1.2` / `OWNER_ACCEPTED_MERGED_BLUE_STATE`.
- Registry root SHA-256: declared and independently recomputed `6f46db56ce4b54bd4655f9e0f5e919dcdb004520d6a0acd455281841a1d7912f` — MATCH.
- Role: `BOUNTY-REAPER`; mandate: `AMX-MANDATE-BOUNTY-REAPER-V1`; status `CURRENT`.
- Exact marker-bounded canonical payload: 1,082 UTF-8 bytes. Independently recomputed SHA-256 `754d8fb9b6816da1bf0013940883106e0d3928b1637526ee82b38e1792c1dcd3` — MATCH.
- Existing owner identity observed in prior durable Reaper receipts: `6abf8e6d6a188191aee2b5d3fe24a9c9`. No scheduler change or duplicate worker created in this run.
- Live automation lookup at 2026-10-15 20:56 SAST: the one existing task is `is_enabled=true`; `last_run_time=2026-10-15T18:54:53.824764Z` (20:54:53 SAST); `next_run_time=null` despite its stored hourly schedule. No enable/schedule mutation was made. Preserve this as an open scheduler-observability/liveness discrepancy for ROOT to reconcile; do not spawn a duplicate.

## Canonical tracker / Q1 drain

Canonical sink: `AMX Bounty Reaper — Live Tracker`, spreadsheet ID `1ETiK6b2YOz499OXBA5wuvgyWMjnDZoEdJIwCt2xGeCk`.

- Intended actions: obtain authorized Sheets/Drive access; read current Runs, Queue and Payouts; reconcile completed Q1 work; append one attributable Runs row; independently read the new row back.
- Exact blocker: this runtime exposes no authorized Google Sheets/Drive read-write/readback action for the canonical spreadsheet.
- Outcome: no tracker read, append, row readback, Queue update or Payouts update occurred. This Root Intake record is the required fallback, not a tracker replacement.
- Current Q1: **UNKNOWN, NOT ZERO**. Accessible GitHub jobs and prior Root Intake receipts did not establish a submission-ready packet, but inaccessible Runs/Queue/Drive mean this cannot certify Q1=0.

## Material parcel advancement — LayerZero BR-20261003-024

### Target binding recovered

Current published official LayerZero Ethereum deployment documentation identifies:
- Network: Ethereum Mainnet, chain ID 1.
- LayerZero Endpoint ID: 30101.
- Executor target: `0x173272739Bd7Aa6e4e214714048a9fE699453059`.
- Source: https://docs.layerzero.network/v2/deployments/chains/ethereum

This closes the missing **documented target/chain/address association** for the Ethereum Executor. Etherscan's indexed proxy page links this proxy to implementation address `0xfe9ab78ed4f9f3dbb168d9f5e5213d78605c9805`. However, the retrieved Etherscan page was crawled months earlier and the direct implementation page returned HTTP 403; the current on-chain implementation slot and implementation-source/bytecode equivalence were not independently read in this run. Treat the implementation pointer as a useful lead, not a verified current source binding.

### Pinned source and semantics

Pinned public source:
- `LayerZero-Labs/LayerZero-v2` commit `9c741e7f9790639537b1710a203bcdfd73b0b9ac`.
- `Executor.sol` blob `7e64f06b4fca2cc7052b764014a919a639abe82e`.
- `WorkerUpgradeable.sol` blob `e261c667376028ac97a606419422ef738bfe318d`.

Static review/readback confirms:
- `nativeDrop` and `nativeDropAndExecute302` are `onlyRole(ADMIN_ROLE)`.
- `_nativeDrop` records low-level transfer success, but increments the nominal `spent` amount even when a receiver call fails.
- `nativeDropAndExecute302` then calculates `msg.value - spent` and still attempts `lzReceive`; a failed native drop alone does not prevent that receive attempt.
- Inherited `WorkerUpgradeable.withdrawToken(address(0), to, amount)` is also admin-only and supports native-currency withdrawal. The source does not prove a permanent lock with no authorized recovery path.

### Official eligibility and dedupe gates

Current official program pages:
- Information: https://immunefi.com/bug-bounty/layerzero/information/
- Scope: https://immunefi.com/bug-bounty/layerzero/scope/
- Resources/audits: https://immunefi.com/bug-bounty/layerzero/resources/

The official information page says a runnable PoC with end-effect is required for all severities and vulnerabilities marked in LayerZero's audit repository are ineligible. Primacy of Impact is only for Critical/High smart-contract impacts. No qualifying attacker-controlled path, identifiable victim/funds at risk or Critical/High impact has been established.

The public audit repository directory lists, among other relevant material:
- `MessageLib-Paladin-15DEC2023-Initial.pdf`
- `MessageLib-Paladin-11JUN2026-Diff.pdf`

The PDF content was not readable through the available retrieval route in this run. Their existence and filenames are evidence that audit material exists, not evidence of its contents. **AUDIT DEDUPE remains NOT PASSED.** Prior receipts describe the 2023 Paladin MessageLib report as thematic prior art concerning upfront Executor fees/native airdrops; exact identity with this narrowed failure path is not established.

### Parcel disposition

- Failed-drop prevents `lzReceive`: **A — KILLED**.
- Permanent-lock/no-recovery subclaim: **A — KILLED on reviewed source**, due to the inherited admin-only withdrawal path.
- Existing parent parcel: **Q3 / PARKED — NOT SUBMISSION-READY**, only for a materially distinct path with a proven eligible target/implementation, attacker/victim impact, compliant local/fork PoC and complete audit/prior-art dedupe.
- No report package created or submitted. No Immunefi report ID, acceptance, award, receivable or verified payment established.
- No live-target exploitation, mainnet/public-testnet testing, transaction, fund movement, spend, credential expansion, KYC bypass or public disclosure.

## Separate candidate screen — 0x Settler

This wake continued beyond the LayerZero audit gate and screened a distinct, current Immunefi program/source without opening another worker or external submission:
- Program scope: https://immunefi.com/bug-bounty/0x/scope/ (published scope says last updated 2026-09-21; includes 0x Settler and lists direct theft/permanent freeze among eligible impact classes; PoC and KYC are required).
- Immutable reviewed repository snapshot: `0xProject/0x-settler@275cf8ce398bcc862753deee7ff043764c1e27b9`.
- Hypothesis screened: alleged function-level reentrancy through re-entry into `execute()` from external pool/action callbacks, publicly described in issue #646 on 2026-09-07: https://github.com/0xProject/0x-settler/issues/646. The issue is public and marked closed/completed, so it is not a fresh/private report.
- Exact source: `src/core/Permit2Payment.sol` blob `96318212668d40355ff34628f28edfef8d96c737`. `takerSubmitted` calls `TransientStorage.setPayer(msgSender)`; `setPayer` checks `_PAYER_SLOT` and reverts `ReentrantPayer(address)` when a payer is already set. `setOperatorAndCallback` also explicitly documents the payer slot as the implicit entrypoint reentrancy guard. This directly contradicts the issue's core assumption that nested `execute()` can run before the original slippage check.
- Additional screened callback gate: `_setOperatorAndCall` stores a specific target + selector + callback, calls that target, then requires the callback slot to have been consumed; `getAndClearCallback` checks caller and selector and clears before callback execution. The Uniswap V4 call path selects the manager from chain-specific code, not a public caller-supplied target in the exposed action.
- Disposition: **A — KILLED / PUBLIC PRIOR ART / NO BOUNTY CANDIDATE** for the claimed general `execute()` reentrancy gap. No local exploit test or live-target test was run; conclusion is bounded to the claim against the reviewed source. The public issue's no-pause/best-practice and cross-chain-replay assertions were not promoted.
- Outcome: no candidate package, external submission, report ID, acceptance, award or payment. This screen is recorded as a kill, not as a vulnerability discovery.

## Additional reward-route and current-program screening

### Sablier — reward route closed

The pre-existing unbound vesting-arithmetic signal was checked against Sablier as one possible vesting ecosystem, without assuming the old signal originated there.
- Sablier's own bounty page states the program was deprecated effective **2026-05-01**: https://sablier.notion.site/bug-bounty
- Sablier's EVM repository security policy also states that it does not operate a bounty and reports are not eligible for rewards: https://github.com/sablier-labs/evm-monorepo/security
- Disposition for a Sablier payout route: **A — NOT REWARD-ELIGIBLE under the retrieved current policy**. No vulnerability was claimed, no private submission or direct contact was made, and no external report/award/payment exists.
- The older generic vesting-arithmetic B signal remains **B — UNBOUND SIGNAL**; there is not enough evidence to attribute it to Sablier or promote it to a live, in-scope target.

### SP1 — current live program; public candidate triage

Official current program:
- Information/reward route: https://immunefi.com/bug-bounty/sp1/information/
- Current scope: https://immunefi.com/bug-bounty/sp1/scope/
- Program was live from 2026-09-21, last updated 2026-10-13, maximum reward $100,000. The scope requires a runnable PoC and limits eligible proof-system impacts to specified soundness/completeness failures in production configurations; it excludes several experimental/debug paths and requires latest-release reproducibility.

Three already-public issue reports were checked against the current scope and candidate novelty gate:
1. **#2927 — BLS12-381 decompression infinity/subgroup handling**: https://github.com/succinctlabs/sp1/issues/2927. Its own description marks the finding dormant because the relevant precompile is decommissioned and expressly says it is not an SP1 proof-system soundness issue. **A — KILLED / NOT AN ELIGIBLE LIVE IMPACT.**
2. **#2926 — Weierstrass decompression wrappers panic**: https://github.com/succinctlabs/sp1/issues/2926. Public since 2026-08-04, before the bounty launch; the author states no execution was performed and the affected precompiles have no active executor/AIR implementation. The report is about disabled wrapper behavior, not demonstrated false-proof acceptance or a qualifying production proof verifier impact. **A — PUBLIC PRIOR ART / NOT SUBMISSION-READY.**
3. **#2922 — deferred proof verification setting**: https://github.com/succinctlabs/sp1/issues/2922. Public since 2026-08-03, before bounty launch. Its own report says the proof mismatch is caught in compression and it is not a soundness problem; the requested improvements are documentation and execute-time testing. **A — PUBLIC PRIOR ART / NON-QUALIFYING IMPACT.**

These issue reports were screened as prior art, not repackaged. No candidate survived for a private bounty submission. No report package, report ID, acceptance, award, receivable or payment was produced. The screen does not establish that the entire SP1 codebase is exhausted; any further SP1 path must be reviewed against the latest release, official known-issue/audit lists and a runnable local PoC before promotion.

## Accessible inventory and continuation

The current accessible `BLACK/jobs` inventory contains historical Reaper LayerZero and XOXNO job files. Prior Reaper receipts classify the current Symbiosis helper-balance signal as outside the listed asset/impact boundary; the sampled Stargate 100%-fee claim as killed; Sei Giga narrow abort, Veda request-integrity, Axelar origin and OpenBridge stale-vote hypotheses as killed/narrowed; XOXNO stale-position as not reproduced; sBTC nonce behavior as public prior art; and vesting arithmetic as a B signal with no identified project/source, eligible impact or PoC. No alternative ready Q1 package was recovered.

This run materially advanced the LayerZero parcel by recovering the documented Ethereum target association and re-confirming the exact gates that prevent a valid submission. The remaining implementation/audit gates are specific and evidenced; do not repeat the killed subclaims as new findings. Tracker recovery is a separate open obligation.

## Recovery assignment

- **Owner:** ROOT / authorized Google Sheets-Drive connector owner.
- **Next action:** restore authorized read/write/readback access to the existing canonical Live Tracker; read Runs/Queue/Payouts and Root Drive/handoff; reconcile Q1 before treating the queue as empty; append this run's Runs row and independently read it back.
- **Acceptance:** canonical queue is read, row content is independently verified, and any eligible completed packet enters its official program with an external receipt/report ID.
- **Persistence here:** existing Root Intake fallback only; no shadow tracker or parallel evidence plane created.

RUN_RESULT: PRODUCTIVE — LAYERZERO TARGET ASSOCIATION BOUND; FAILED-DROP CLAIMS REMAIN KILLED; PARENT Q3 PARKED.
TRACKER: TRACKER_WRITE_BLOCKED.
Q1: UNKNOWN, NOT ZERO.
EXTERNAL SUBMISSION / ACCEPTANCE / AWARD / PAYMENT: NONE ESTABLISHED.
SAFETY: STATIC / PUBLIC-SOURCE REVIEW ONLY.
