# BOUNTY REAPER — LayerZero current scope / impact gate receipt

**Receipt ID:** BR-20261010-LZ-SCOPE-002  
**Date:** 2026-10-10  
**Existing parcel:** `BR-20261003-024`  
**Parent technical receipt:** `BR-20261010-STATIC-001`  
**Outcome:** MATERIAL SCOPE/ELIGIBILITY NARROWING — NOT SUBMISSION-READY; keep this parcel parked at the named gates.  
**Tracker status:** `TRACKER_WRITE_BLOCKED`; no Live Tracker Runs row is claimed.

## Work performed

Reviewed the current official LayerZero Immunefi scope, information and resources pages, alongside the previously pinned immutable source `LayerZero-Labs/LayerZero-v2@9c741e7f9790639537b1710a203bcdfd73b0b9ac`.

Official sources:
- Scope (last updated 2026-10-02): https://immunefi.com/bug-bounty/layerzero/scope/
- Program information (last updated 2026-10-02): https://immunefi.com/bug-bounty/layerzero/information/
- Resources / audits and known issues: https://immunefi.com/bug-bounty/layerzero/resources/
- Immutable source `Executor.sol`: https://github.com/LayerZero-Labs/LayerZero-v2/blob/9c741e7f9790639537b1710a203bcdfd73b0b9ac/packages/layerzero-v2/evm/messagelib/contracts/Executor.sol

## Current official eligibility facts

The current published program explicitly requires a runnable PoC for every severity and an end effect meeting an in-scope impact criterion; reports already marked in LayerZero's audit repository are not reward-eligible. The program's Primacy of Impact route applies to critical/high smart-contract impacts; other impacts remain subject to its listed-asset/rules boundary. The current scope page lists 25 assets total and does not, in the material retrievable in this pass, establish an exact deployed Executor address/chain as the asset for this parcel. The official resource page also says only assets in the Assets in Scope table are considered in-scope, while the information page allows Primacy of Impact consideration where a high/critical impact is actually established. Thus exact asset eligibility must not be inferred from the repository contract alone.

## Technical evidence reconciled with the eligibility gate

At the immutable source pin, the inspected `_nativeDrop` calls each configured receiver with its requested native amount, records the low-level call success in the emitted `NativeDropApplied` event, and adds the nominal amount to `spent` irrespective of success. `nativeDropAndExecute302` then computes `msg.value - spent` and continues its separate `lzReceive` attempt. The specific sub-claim that a failed native-drop alone prevents `lzReceive` is therefore **KILLED**.

Both the relevant `nativeDrop` and `nativeDropAndExecute302` external functions are restricted by `onlyRole(ADMIN_ROLE)`. The source behavior may leave the failed amount in the Executor contract, but the current evidence does not establish:
- the exact currently deployed address, chain and implementation;
- an unprivileged attacker-controlled path to cause the loss;
- an identifiable victim and concrete funds/impact affected;
- an eligible in-scope/high-critical impact route under the current program;
- whether any separate authorized operator/off-chain workflow recovers the amount;
- dedupe against LayerZero's complete audit/prior-knowledge materials.

The earlier receipt found no matching indexed `nativeDrop` terms in the accessible audit-repository search, but its audit-PDF review was not complete. That remains **AUDIT DEDUPE NOT PASSED**; search absence is not proof the behavior is unknown to the project.

## Item disposition

- **Killed:** “failed native-drop by itself prevents `lzReceive` from being attempted.”
- **Unproven:** retained-funds/refund concern; not promoted to a confirmed vulnerability.
- **Current parcel state:** **Q3 PARKED / NOT SUBMISSION-READY**. No private report is being submitted because the asset/deployment, qualifying impact, PoC and full audit-dedupe requirements are not yet met.
- **Reopen condition:** a concrete authorized local/fork counterexample that proves an attacker/victim effect and identifies a qualifying current-program impact plus exact deployed/eligible target; full audit dedupe; all applicable program rules satisfied.
- **Next work:** unless such a concrete path can be established using lawful, bounded static/source/deployment research, continue an independent Reaper parcel rather than repeatedly revalidate this same narrowed claim.
- **Safety:** no live target or public testnet was exercised, no transaction/funds were moved, and no report was publicly disclosed.

## Tracker / persistence truth

The current runtime has no authorized Google Sheets/Drive read/write connector. The existing Live Tracker was not read, a Runs row was not written, and no independent row readback occurred. This receipt is the existing Root Intake fallback only and must retain `TRACKER_WRITE_BLOCKED`. Current Q1 remains **UNKNOWN, not zero**.

## Acceptance and remaining work

- [x] Official scope/information/resources pages re-read in this pass.
- [x] Existing immutable-source result reconciled with the official scope/impact threshold.
- [x] Overstated receive-prevention sub-claim killed.
- [x] No submission, award or payment overclaim.
- [ ] Exact deployed target/chain/implementation binding recovered if still pursued.
- [ ] Concrete qualifying impact/PoC and complete audit dedupe evidence required before any submission decision.
- [ ] Existing tracker route restored or authorized fallback retained; Q1 reconciled from current source.
- [ ] Root retrospective review of OCC-04 implementation and this item-level disposition.

**Truth boundary:** this receipt records a program-scope gate and a narrowed hypothesis, not a validated vulnerability, report submission, award, receivable or payment.
