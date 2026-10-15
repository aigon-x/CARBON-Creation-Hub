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

The 2023 Paladin final PDF was recovered from its public publisher and text inspected: https://paladinsec.co/assets/audits/20231215_Paladin_LayerZeroMessageLib_Final_Report.pdf. Its Issue #03 (pp. 19–20) explicitly states that executor/verifier fees are paid upfront whether or not they do the destination work; it gives a large native airdrop as an example where an executor can collect the fee then abandon delivery. The resolution is ACKNOWLEDGED, recommending that applications choose reliable providers. This is confirmed, material prior art for the economic premise of an Executor getting paid despite non-execution, so the current claim cannot be submitted as a novel version of that general issue. The exact implementation-specific path may differ, but no eligible, materially distinct impact has been proven. The 2026 diff PDF MessageLib-Paladin-11JUN2026-Diff.pdf remains unread through the available connector route. AUDIT DEDUPE: the 2023 thematic prior art is confirmed; complete current audit dedupe is NOT PASSED.

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

## SP1 latest-release spot check — no promotion

Follow-on static review was pinned to SP1's official latest-release tag available at this check:
- Release: `v6.9.0`, signed release commit `b8387fa61e1361d90ee7de49f551863418ca0f08` (released 2026-10-10): https://github.com/succinctlabs/sp1/releases
- Scope reference requires the latest release, production verifier/configuration and a runnable proof of concept on Apple M3-class hardware or similar within ten minutes: https://immunefi.com/bug-bounty/sp1/scope/
- The earlier decommissioned-Weierstrass-precompile issue is still non-live in the latest-release syscall/AIR mapping: `BLS12381_DECOMPRESS`, `SECP256K1_DECOMPRESS`, and `SECP256R1_DECOMPRESS` return `None` from both `as_air_id()` and `as_air_id_user()` in `crates/core/executor/src/syscall_code.rs` at tag `v6.9.0` (blob `c26459782b05320c0b63d64de6c4e0d9122f0369`). This corroborates the existing dormant/no-impact kill; do not reframe it as a live proof-system flaw.
- Checked the changed logic in merged PR #2993, “perf(gpu): simplify zerocheck constraint evaluation” (merged 2026-10-05; public source diff: https://github.com/succinctlabs/sp1/pull/2993). The bounded static review found algebraic identity folding (multiply by zero/one, add/subtract zero, negate zero), constant-multiply lowering, liveness pruning and register reuse. The diff explicitly retains every original root assertion and alpha index and adds a test asserting this for repeated/constant roots. No specific false-proof or qualifying deterministic completeness counterexample was established from this static pass.
- Local execution environment check: `rustc` and `cargo` are not installed; `nvidia-smi` is unavailable. The required current-release runnable PoC / production-circuit reproduction was therefore **not** built or executed in this runtime. This is a concrete test gate, not evidence of a vulnerability. Do not submit the PR as a finding or imply the bounty's PoC gate was met.
- Disposition: `B — STATIC SCREEN ONLY / NO SUBMISSION CANDIDATE PROMOTED`. Continue only with a new, specific source-level inconsistency that can be deduplicated against the official audit/known-issue lists and validated in a suitable lawful local environment.

## LayerZero audit dedupe delta — 2023 primary PDF recovered

Source: Paladin Blockchain Security, Smart Contract Security Assessment for LayerZero (MessageLib), final report dated 2023-12-15. Public publisher PDF: https://paladinsec.co/assets/audits/20231215_Paladin_LayerZeroMessageLib_Final_Report.pdf.

The report's Issue #03 (printed pages 19–20) is titled “Message lib lacks direct on-chain incentive for executors and verifiers to actually do their part, as the fee is collected at the source chain when a transaction is sent out.” It states that fees are paid upfront regardless of whether an executor/verifier does its part, specifically gives the example of a large native airdrop where an executor can collect a fee and then never execute the destination message, and records the resolution as ACKNOWLEDGED. The stated resolution asks applications to select providers based on reliability metrics. This confirms material thematic prior art, not just a filename-level hint.

Disposition update for BR-20261003-024: the generic “Executor can retain/collect compensation while native airdrop/destination execution fails” premise is A — PUBLIC AUDIT PRIOR ART / NOT NOVEL FOR SUBMISSION under the program's published audit-exclusion rule. The source-specific low-level failed-call/refund semantics remain a code observation, not an eligible finding without a distinct qualifying impact; no such impact or compliant PoC is established. The prior claim that the 2023 audit's contents were unreadable is superseded by this source recovery. The 2026 MessageLib diff audit remains unread, therefore full dedupe is still not passed. Do not submit the generic native-drop premise.
## 1inch latest-tag / order-announcement edge screen — not promoted

Official active program screen: https://immunefi.com/bug-bounty/1inch-SmartContracts/scope/ and https://immunefi.com/bug-bounty/1inch-SmartContracts/information/. The scope was updated 2026-10-14, requires a PoC and KYC, expressly limits the program to the latest tag/releases, excludes theoretical attacks without demonstrated business impact, prohibits mainnet/public-testnet testing (local forks only), and prohibits submitting AI-generated reports.

Bounded hypothesis screened: whether a third party registering a valid signed order before its maker could unduly anchor the order's start time after the new timestamp feature was introduced.

- Latest published repository release found: `4.3.4`, published 2026-09-24: https://github.com/1inch/limit-order-protocol/releases/tag/4.3.4. Its `contracts/helpers/OrderRegistrator.sol` blob is `c16e30831f6c44c88b4e1e7ece8f560c9301922e` and contains signature/extension validation plus the `OrderRegistered` event, but no `announcedAt` mapping.
- Main-branch `contracts/helpers/OrderRegistrator.sol`, blob `0317e58286e438d246a95c742851797b51a655ec`, does add `announcedAt[orderHash]`, records only the first timestamp, and rejects later registration with `OrderAlreadyRegistered`. The feature arose in merged PR #435, commit `e92c8bd3336d6bceb7bcba67d4f0c32ec73b6da5`: https://github.com/1inch/limit-order-protocol/pull/435.
- The scope table added several assets on 2026-10-14 under generalized labels, but the fetched extraction did not provide exact address/source-version mapping for this helper. Latest-release eligibility and this helper's exact in-scope deployment are therefore **UNVERIFIED**.
- Even on current branch, permissionless registration is signed-order relay; first registration is write-once and requires a valid order signature. No deterministic attack path causing direct theft, freezing, or another listed economic impact was established from this feature alone. No local PoC was built or executed.

Disposition: **A — NO PROMOTION / NO REPORT** for this specific front-running hypothesis. This is a narrow kill for the speculative timestamp-front-run claim, not a declaration that all 1inch assets are safe. Do not submit: exact eligible deployed implementation and qualifying impact are unproven; program prohibits AI-generated reports. No code, external report, report ID, acceptance, award, or payment resulted.
## XOXNO INV-ACCT-10 recovery — reviewed liquidation-credit path killed

Recovered the existing frozen job source `XOXNO/rs-lending-xlm@a2486b255b974ef8432ce44de014931f51552f4b` and continued the exact stale-account-position hypothesis. This is a bounded static disposition, not a whole-repository proof.

### Exact source evidence

- `docs/reference/invariants.md`, blob `a03076080ec1f34b1ec8632751998d2ba472fff5`, defines `INV-ACCT-10`: pool keeps market totals, trusts controller-provided scaled positions, and controller is responsible for reconciliation. The document explicitly says the property test `prop_accounting_conservation` checks the supply and debt equalities within four token units after every operation.
- `contracts/controller/src/positions/liquidation/plan.rs`, blob `f14ca6f3ff969aa95cdcec85ab9c46690dda1427`: the plan computes risk totals and derives seizure entries from the passed account's own `supply_positions`; liquidation plan validation occurs before application.
- `contracts/controller/src/positions/liquidation/math.rs`, blob `8acaee358492426cf806da32da7603c0869242b7`: `calculate_seized_collateral` iterates current account positions and derives shares against the same cached supply index. A full close carries the exact stored `position.scaled_amount`; partial seizure converts down and caps against the held position. Under-delivery only scales planned seizures down against measured repayment.
- `contracts/controller/src/positions/liquidation/mod.rs`, blob `891333a89d6d332d2f3b40e03b1f5a3cf255d7a7`: `process_liquidation` loads the account, builds and validates the plan, applies measured repayments, trims seizures to received value, then applies transfer or share-credit mode in the same call.
- `contracts/controller/src/positions/liquidation/apply.rs`, blob `0bedd96acfd5955ae599636fba4db49ff3920605`: share-credit mode fetches the debtor's current in-memory supply position and uses checked subtraction of gross seizure shares; over-seizure reverts. Receiver credit adds only net shares. Only fee shares are sent to the pool for reclassification as revenue; seizure and receiver allocations are asserted to conserve shares.
- `contracts/pool/src/ops/seize.rs`, blob `9d487a302fbc055fdeaeb0829100b3cc4e941270`: deposit-side `PoolSeizeEntry` reclassifies the provided shares as revenue; it does not move cash.
- `contracts/controller/tests/positions/liquidation_seize_modes.rs`, blob `98dcbb3c87cb34329c61bed55214e5d0f05b3b30`: tests exercise exact fee-plus-liquidator conservation, under-delivery scaling, fee bounds, full-close exact shares at a non-unit index, and the partial-seizure bound. `tests/test-harness/tests/controller/liquidation_seize_modes.rs`, blob `81b4c9d0d71fc63c78ca14079c47234a73a2ef4c`, contains end-to-end credit-mode scenarios and tests that pool supplied shares and cash remain unchanged, with only revenue changing.
- Searches through the connected GitHub source for `INV-ACCT-10`, `PoolSeizeEntry` and liquidation/accounting issue text surfaced no matching public issue or matching commit result. This is bounded connector search evidence, not exhaustive proof of no prior art.

### Disposition and gate

**A — KILLED FOR THE REVIEWED LIQUIDATION CREDIT / SEIZURE PATH.** No concrete stale-position write was found in this path; the data flow follows the documented invariant and includes checked subtraction and allocation-conservation assertions. Do not promote the previous generic stale-account hypothesis as a vulnerability based only on the pool trusting its controller.

Scope limit: other controller mutation paths were not exhaustively audited, so this is not a global proof that `INV-ACCT-10` can never fail. The whole-repository property test `prop_accounting_conservation` was not run. The execution runtime has no `cargo` or `rustc`; an attempted local public clone fails because this runtime cannot resolve `github.com`. Static source was therefore read through the authorized GitHub connector, but executable reproduction remains blocked by the local Rust toolchain / clone transport. No source-changing action, live test, transaction, external submission, report ID, award or payment occurred.

Next lawful advancement if executable infrastructure becomes available: run the exact pinned checkout's existing `prop_accounting_conservation` and focused liquidation-credit tests, then inspect other account mutation paths only if a specific non-returned/stale-position source can be isolated. Do not label this bounded kill as a Q1 submission.

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
