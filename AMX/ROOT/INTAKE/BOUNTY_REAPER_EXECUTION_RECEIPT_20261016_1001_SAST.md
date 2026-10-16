# Bounty Reaper Execution Receipt — 2026-10-16 10:01 SAST

RUN_ID: BR-20261016-1001-SAST-01
OFFICE: BOUNTY REAPER
MANDATE: AMX-MANDATE-BOUNTY-REAPER-V1
RESULT: PRODUCTIVE STATIC TRIAGE; NO Q1 ESTABLISHED; TRACKER_WRITE_BLOCKED.

## 1. Mandatory canonical pre-flight — PASS

Direct fetch from `amillimatrix-eng/CARBON-Creation-Hub`:
- `AMX/ROOT/BLUE_STATE/MANDATE_REGISTRY_V1.json`; Git blob `d3a749a48d98292a13931fd6ff8518dea03e5b20`.
- `AMX/ROOT/BLUE_STATE/BLUE_STATE_MANDATE_BINDING_AND_PREFLIGHT_V1.md`; Git blob `c70d43754a93fa2c7778baeeb6ee0bebe33e94ed`.
- Registry version/state: `1.2` / `OWNER_ACCEPTED_MERGED_BLUE_STATE`.
- Declared and independently recomputed registry root SHA-256: `6f46db56ce4b54bd4655f9e0f5e919dcdb004520d6a0acd455281841a1d7912f` — MATCH.
- Role `BOUNTY-REAPER` status `CURRENT`; mandate ID `AMX-MANDATE-BOUNTY-REAPER-V1`.
- Declared and independently recomputed canonical mandate SHA-256: `754d8fb9b6816da1bf0013940883106e0d3928b1637526ee82b38e1792c1dcd3` — MATCH; marker-bounded payload length 1,082 UTF-8 bytes.
- Existing worker/automation ID: `6abf8e6d6a188191aee2b5d3fe24a9c9`. No duplicate worker created, no scheduler mutation made.

## 2. Scheduler liveness — exact discrepancy routed

Live automation lookup at this wake returned:
- `is_enabled=false`.
- `last_run_time=2026-10-16T07:39:24.104141+00:00` (09:39:24 SAST).
- `updated_at=2026-10-16T07:40:27.683206+00:00` (09:40:27 SAST).
- The stored schedule still contains `RRULE:FREQ=HOURLY`, while `next_run_time=null`.

This current live state supersedes older receipts which recorded the worker as enabled. No enable/schedule change was made. ROOT must reconcile the single existing worker's disabled state and null next-run metadata; do not spawn a replacement.

## 3. Canonical Live Tracker — BLOCKED, Q1 remains UNKNOWN

Required canonical sink: `AMX Bounty Reaper — Live Tracker`, spreadsheet ID `1ETiK6b2YOz499OXBA5wuvgyWMjnDZoEdJIwCt2xGeCk`.

Attempted action: discover authorized Google Sheets/Drive access, then read Runs/Queue/Payouts, append the attributable Runs row, and independently read that row back.

Exact blocker: plugin discovery returned the Google Drive connector with `status=DISABLED_BY_ADMIN`, `installation_policy=NOT_AVAILABLE`, `installed=false`. This workspace does not expose an authorized Sheets/Drive read/write/readback action. No tracker read, append, readback, Queue update, or Payouts update occurred.

Fallback persisted to the existing Root Intake repository under this receipt. No replacement tracker or parallel evidence plane created. Searches of accessible Root Intake/GitHub receipts and submission artifacts did not establish a ready Q1 packet or external submission receipt, but inaccessible Runs/Queue/Drive prevents certifying Q1=0. **Q1 = UNKNOWN, NOT ZERO.**

## 4. Material parcel — Variational Arbitrum deployed source and program screen

Current official program pages:
- Scope: https://immunefi.com/bug-bounty/variational/scope/
- Information: https://immunefi.com/bug-bounty/variational/information/
- Resources: https://immunefi.com/bug-bounty/variational/resources/
- Official deployed-address documentation: https://docs.variational.io/technical-documentation/mainnet-contracts
- Official audit index: https://docs.variational.io/technical-documentation/audits

The current scope page was retrieved with `Last Updated 15 October 2026`, maximum bounty USD 100,000, PoC required, and KYC required. It expressly covers exploitable quoting, pricing, execution, margin, liquidation, funding, accounting, or settlement logic only where an eligible impact such as unauthorized funds loss/theft or protocol insolvency is demonstrably established. The scope also excludes attacks requiring privileged addresses unless additional privilege modification is involved.

Read-only source binding via Blockscout:
- Network: Arbitrum One, chain ID `42161`.
- Official docs list Settlement Pool Factory `0x0F820B9afC270d658a9fD7D16B1Bdc45b70f074C` and Oracle `0x84BE56470d45b7f6629A66A219a38681F6BA6172`.
- Factory metadata identifies `SettlementPoolFactory`, fully verified, Solidity compiler `0.8.28+commit.7893614a`, verified timestamp `2025-10-20T10:24:36.711698Z`, source tree including `src/SettlementPoolFactory.sol` and `src/SettlementPool.sol`; constructor arguments include USDC address `0xaf88d065e77c8cc2239327c5edb3a432268e5831` and implementation association `0x8db6c8B7a085C3839e93EB8DaD45b93FB1ef5836`.
- Oracle metadata identifies verified contract `Oracle`, compiler `0.8.28+commit.7893614a`, verified timestamp `2026-01-10T10:03:43.173039Z`, with source tree including `src/Oracle.sol` and settlement/treasury libraries.
- This was source/metadata retrieval only. No live contract calls, transaction, token movement, signature, or fund operation was performed. The retrieved metadata/source was not independently compared against raw deployed runtime bytecode in this run; no claim of executable reproduction is made.

### 4A. Factory-switch / old-pool registry loss — A / PUBLIC AUDIT PRIOR ART

The deployed `src/Oracle.sol` source has `setSettlementPoolFactory(address)` restricted to `DEFAULT_ADMIN_ROLE` and replaces the `factory` pointer. Several paths consult `factory.getPool(poolUuid)` for existing pools. This exact pattern matches the high-risk finding titled `factory cannot be updated without causing a DOS to existing pools in core Oracle functions` in the public Cantina/Spearbit Variational review, printed page 4, context `Oracle.sol#L392-L399`.

Primary report: https://docs.variational.io/technical-documentation/audits (Spearbit_Variational_Report_PUBLIC.pdf; 5 pages). The report explicitly marks the finding `Variational: Acknowledged` and `Cantina Managed: Acknowledged`. This is known audit prior art and the path is admin-gated. **A — DUPLICATE / NOT SUBMITTABLE.** Do not repackage the acknowledged factory-switch denial-of-service issue.

### 4B. SettlementPoolDeployer access control — A / NOT THE REVIEWED DEPLOYMENT PATH

The same public review documents a separate historical high-risk issue for `SettlementPoolDeployer.deploy` lacking access control. The verified `SettlementPoolFactory.createPool` source retrieved for this deployment requires `msg.sender == owner() || msg.sender == address(oracle)` before pool creation. The `SettlementPoolDeployer.sol` path does not appear in the retrieved current factory source tree. Do not claim the historical deployer issue against this source without exact in-scope deployed code proving that path remains active. No separate submission candidate established.

### 4C. Single-sided atomicDeposit with parentQuoteUuid zero — B / HYPOTHESIS HELD, NOT PROMOTED

Static path reviewed in verified `src/Oracle.sol` and `src/SettlementPool.sol`:
- `Oracle.atomicDeposit(...)` is `onlyRole(PROVIDER_ROLE)`. On the one-sided path (`partyOneAmountRequested > 0 && partyTwoAmountRequested == 0`), the function checks `atomic_deposits_processed[parentQuoteUuid]`, transfers USDC from the party to Oracle then to the pool, and records the idempotency flag only when `parentQuoteUuid != 0`.
- `SettlementPool.depositUSDCAtomic(...)` has the same one-sided branch and emits/returns before its later `require(parentQuoteUuid != 0)` statement.
- Therefore the static code permits the zero UUID value on this one-sided path and does not mark zero as processed. Repeated calls still transfer actual USDC from the specified party under the provider's authority and allowance; this is not evidence of a free transfer or direct theft.

Disposition: `B — SOURCE-LEVEL IDEMPOTENCY EDGE / NOT PROMOTED`. The entry point requires the privileged `PROVIDER_ROLE`, and no attacker-controlled path bypassing that role, qualifying funds-loss impact, or safe local PoC was established. Current program exclusions on privileged-address-dependent attacks apply on the evidence available. Do not submit. Reopen only if a distinct non-privileged reachable path or a concrete in-scope impact is established with runnable local PoC and full audit/known-issue dedupe.

## 5. Independent live-program parcel — SP1 build issue screen

Current official scope/information retrieved this wake:
- Scope: https://immunefi.com/bug-bounty/sp1/scope/
- Information: https://immunefi.com/bug-bounty/sp1/information/

The SP1 program was live and last updated 13 October 2026, with a runnable PoC requirement. Its current scope limits eligibility to production proof soundness or protocol-level completeness failures, requiring the latest release and production circuits/verification keys, and explicitly excludes prover/service availability failures.

Public issue #3004, `sp1-recursion-gnark-ffi fails to build: github.com/consensys/gnark-ignition-verifier was deleted`, reports a Go dependency/build failure from a clean module cache; the report proposes a dependency-source workaround. This is a public build/reproducibility issue, not evidence of false-proof acceptance or a qualifying deterministic proof-verification completeness flaw. Under current program scope, disposition is **A — PUBLIC BUILD ISSUE / NON-QUALIFYING IMPACT / DO NOT SUBMIT**. No build reproduction was run and no claim of a security vulnerability is made.

Public reference: https://github.com/succinctlabs/sp1/issues/3004

## Lombard BasculeV1 threshold/replay hypothesis — public audit prior-art kill

Continuation after the receipt's first independent candidate screen; this section was added during the same open Bounty Reaper run.

### Current program and target
- Official current scope: https://immunefi.com/bug-bounty/lombard-finance/scope/ — last updated 15 October 2026, PoC required, KYC required, and **a non-refundable report submission fee is required for every report**.
- In-scope mainnet asset: BasculeV1 `0xc750eCAC7250E0D18ecE2C7a5F130E3A765dc260` (Ethereum chain ID 1), directly bound by official `lombard-finance/evm-smart-contracts/mainnet.json`, blob `125c071bc6adef7055e55ff033437d37214091b7`.
- Pinned source: `lombard-finance/evm-smart-contracts@7fe83e56f2265c0c281747c8dd3bb141d3022c46`; `contracts/bascule/Bascule.sol`, blob `e6fb296037bc3e6185786d07c38c40842f54a58b`.

### Hypothesis originally screened
`Bascule.validateWithdrawal()` allows an unreported withdrawal below `validateThreshold()` without setting `depositHistory[depositID]` to `WITHDRAWN`; if a bridge calls it as a gate and threshold is nonzero, a repeated below-threshold use of the same deposit ID may pass the Bascule check repeatedly. The source comments state threshold defaults to zero and requires privileged `VALIDATION_GUARDIAN_ROLE` to raise it; `validateWithdrawal()` itself is role-gated to `WITHDRAWAL_VALIDATOR_ROLE`.

### Exact prior art — same issue already documented
- Public report: Sherlock, Lombard June 2025 audit issue #337, **“Issue L-5: Validation threshold should never be set as non zero.”** Reference: https://github.com/sherlock-audit/2025-06-lombard-june-23rd/issues/337 and report mirror https://resources.cryptocompare.com/asset-management/20731/1758551907204.pdf.
- The report describes the same two mechanics: a raised threshold allows below-threshold withdrawals without Bascule validation, and the original Bascule path fails to mark those deposits as withdrawn in `depositHistory`. It states that the issue was **acknowledged but not fixed at that time**.
- Bascule's own `contracts/bascule/README.md`, blob `db1d6491f295484859a9db599a7cf44f10a7557f`, also explicitly warns that nonzero threshold depends on the bridge passing the correct withdrawal amount and that reporting zero can bypass validation. This is prior public documentation, not a novel finding.
- A separate past Immunefi audit report #38102 also covers a different equality-boundary issue in BasculeV2 (`>=` versus `>`), which is not being conflated with this BasculeV1 replay hypothesis: https://reports.immunefi.com/lombard/38102-sc-insight-due-to-incorrect-design-in-basculev2-validatewithdrawal-valid-transactions-will-be.

### Disposition
**A — KILLED / PUBLIC PRIOR ART / NOT SUBMITTABLE.** Do not repackage the threshold-bypass/replay behavior. The exact live `validateThreshold()` value and every deployed integration gate were not independently read during this source-only screen, so no claim is made that the issue is currently exploitable. Regardless, the exact core behavior is pre-disclosed and the current program charges a non-refundable submission fee; no submission, fee, transaction, or funds movement was made.

## 6. Carried-forward queue and prior-art state

- LayerZero `BR-20261003-024`: retain prior receipt state. Generic failed native-drop/non-execution economics are confirmed thematic prior art in Paladin's 2023 MessageLib audit Issue #03; the current source-only failed-drop and permanent-lock claims remain killed. The 2026 diff audit remains unread through current retrieval paths, so full audit dedupe is incomplete. Parent remains parked only for a materially distinct eligible path; do not submit the generic native-drop premise.
- XOXNO liquidation-credit stale-position hypothesis: prior source-bound receipt remains a bounded kill; the property test was not executed because the runtime lacks Rust toolchain/clone access.
- 0x Settler nested `execute()` reentrancy: prior receipt remains `A — KILLED / PUBLIC PRIOR ART`; the payer transient-slot guard prevents the reviewed nesting claim.
- 1inch order announcement timestamp: prior receipt remains `A — NO PROMOTION`; exact latest-tag binding/eligible impact not established.
- Enzyme Onyx zero-share-price redemption: prior receipt remains `A — PUBLIC QA PRIOR ART`; do not resubmit the acknowledged zero-share-value claim.
- Symbiosis MetaRouter balance helper: prior receipt remains `B — SCOPE-GATED / NOT SUBMITTABLE`; no attack path to the currently listed MetaRouterGateway assets has been established.
- Lombard BasculeV1 threshold/replay hypothesis: `A — KILLED / PUBLIC PRIOR ART`; the same nonzero-threshold below-threshold repeat-without-consuming condition was documented in Sherlock 2025 issue L-5 and acknowledged. No submission fee paid.

## 7. Run outcome and truth boundary

PRODUCTIVE ACTION: Recovered current mandate digest; exposed the current disabled/null-next-run scheduler discrepancy; recovered a live program's verified Arbitrum factory and Oracle source; killed an audit-acknowledged factory-switch claim; narrowed a separate provider-gated zero-UUID idempotency edge; and killed a separate public SP1 build issue against current scope.

Q1_DRAIN: UNRESOLVED, because canonical Runs/Queue/Payouts and Drive handoff are inaccessible. No READY_FOR_SUBMISSION packet established from accessible evidence. This is not proof the queue is empty.
TRACKER: `TRACKER_WRITE_BLOCKED` — Google Drive connector disabled by administrator / installation unavailable.
Q1: UNKNOWN, NOT ZERO.
EXTERNAL SUBMISSION / REPORT ID / ACCEPTANCE / AWARD / VERIFIED PAYMENT: NONE ESTABLISHED.
SAFETY: PUBLIC SOURCE/STATIC REVIEW ONLY; no live exploitation, prohibited testing, transaction, spend, fund movement, credential expansion, KYC bypass, or public disclosure.

## 8. Recovery actions

1. ROOT / connector administrator: restore authorized read/write/readback access to the existing Live Tracker; read Runs/Queue/Payouts and Root Drive handoff; reconcile Q1; append this run's Runs row and independently read it back. Acceptance is the actual tracker row/readback, not this fallback receipt.
2. ROOT: reconcile the one existing Bounty Reaper automation: currently `is_enabled=false`, stored hourly schedule, `next_run_time=null`. Do not create a duplicate worker.
3. Bounty Reaper: continue with a distinct current, eligible public program/source and promote only on exact scope, privilege model, novelty/audit dedupe, qualifying impact and runnable PoC evidence.
