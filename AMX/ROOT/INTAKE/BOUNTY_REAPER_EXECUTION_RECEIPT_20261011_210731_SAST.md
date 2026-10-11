# Bounty Reaper execution receipt

Run ID: BR-20261011-190845-SAST-02  
Observed: 2026-10-11 21:07:31 SAST  
Sequence: 5  
Revision note: this revision replaces the initial draft's mismatched digest entry; payload below is sealed to its marker-bounded UTF-8 bytes. The original write was commit 8823e25def9758d54a7ebe598e9eeffa4f5ddc87.
Payload SHA-256: `d5ecdad160c213dfaa7d100a6a0c495902a292363969d7700ac61d464f93d5d9`  
Hash input: exact UTF-8 bytes between `BEGIN_EXECUTION_PAYLOAD` and `END_EXECUTION_PAYLOAD`, excluding marker lines and including the final newline before the end marker.

BEGIN_EXECUTION_PAYLOAD
RUN_ID: BR-20261011-190845-SAST-02
SEQUENCE: 5
RUN_TYPE: LAYERZERO_NATIVE_DROP_SCOPE_IMPACT_PROOF_KILL
OFFICE: BOUNTY REAPER
OBSERVED: 2026-10-11 21:07:31 SAST
PREFLIGHT: PASS; canonical registry v1.2 root 6f46db56ce4b54bd4655f9e0f5e919dcdb004520d6a0acd455281841a1d7912f; mandate AMX-MANDATE-BOUNTY-REAPER-V1 CURRENT with SHA-256 754d8fb9b6816da1bf0013940883106e0d3928b1637526ee82b38e1792c1dcd3.
TRACKER: TRACKER_WRITE_BLOCKED; no authorized Google Sheets/Drive read/write/readback action; Q1 UNKNOWN, NOT ZERO.
SOURCE: LayerZero-Labs/LayerZero-v2 Executor.sol pinned commit 9c741e7f9790639537b1710a203bcdfd73b0b9ac, blob 7e64f06b4fca2cc7052b764014a919a639abe82e; WorkerUpgradeable.sol blob e261c667376028ac97a606419422ef738bfe318d.
KILL: _nativeDrop records each low-level native send success but increments spent by nominal amount even when sent=false; nativeDropAndExecute302 subtracts nominal amount from msg.value before lzReceive. The asserted permanent-lock/no-recovery subclaim is false: WorkerUpgradeable has admin-only withdrawToken(address(0), to, amount), which can recover retained native balance. nativeDropAndExecute302 is onlyRole(ADMIN_ROLE), not permissionless. Static evidence shows no theft or permanent end-user fund loss; no runnable PoC was executed.
PRIOR_ART: Paladin LayerZero MessageLib Final Report Issue #03, page 20/62, already discusses up-front executor/verifier fees regardless of execution and uses a large native airdrop as the example; disposition ACKNOWLEDGED / LOW SEVERITY. LayerZero Immunefi excludes issues marked in LayerZero-Labs/Audits, requires runnable PoC for all severities, and prohibits mainnet/public-testnet testing. Current public scope lists 25 assets; exact eligible deployed Executor target/address remains unbound.
PARCEL: BR-20261003-024 remains C/Q3 PARKED as a parent parcel, but failed native-drop receive-prevention and permanent-lock/no-recovery are explicitly KILLED. No Q2/Q1 promotion. Only resume if a distinct claim has exact eligible deployment, independent impact, complete audit dedupe, and compliant local-fork PoC.
RESULTS: new qualifying finding=0; submissions=0; external report IDs=0; awards=0; verified payments=0; tracker row readback unavailable.
SAFETY: public-source static review only; no deployed target call, local-fork PoC, transaction, spend, public disclosure or submission.
NEXT: continue another executable existing Reaper parcel; restore authorized existing Live Tracker access through governance; no new tracker or wallet top-up.
ITEMIZED_DIRECTIVE_23:
1. Expected outcome: kill permanent-loss claim. Owner: Bounty Reaper. Action: verify nativeDrop/spent logic and recoverability. Dependency: pinned source. Acceptance: source blobs and official code readback. Persistence: corrected receipt in existing Root Intake; tracker still unavailable. Safety: static only. Disposition: REJECT subclaim. Remaining work: none on this narrow claim.
2. Expected outcome: preserve true parent status. Owner: Bounty Reaper. Action: keep BR-20261003-024 parked; mark only this subclaim killed. Dependency: exact eligible Executor deployment, a separate qualifying impact, complete current audit dedupe, and local-fork PoC. Acceptance: these gates remain open. Persistence: Root Intake fallback only, no tracker row. Safety: no live/public-testnet tests. Disposition: MODIFY / HOLD Q3. Remaining work: test only a distinct claim, otherwise close after all hypotheses dispositioned.
3. Expected outcome: reconcile Q1. Owner: ROOT / authorized tracker connector owner. Action: read canonical Runs, append this run as needed, and independently read back. Dependency: no authorized Sheets/Drive tool is exposed to this runtime. Acceptance: actual tracker row plus readback. Persistence: TRACKER_WRITE_BLOCKED. Safety: do not infer Q1=0. Disposition: HOLD. Remaining work: authorize existing sheet access; continue other work meanwhile.
END_OF_PAYLOAD
END_EXECUTION_PAYLOAD

Evidence pointers:
- Pinned Executor source: https://github.com/LayerZero-Labs/LayerZero-v2/blob/9c741e7f9790639537b1710a203bcdfd73b0b9ac/packages/layerzero-v2/evm/messagelib/contracts/Executor.sol
- Pinned Worker recovery source: https://github.com/LayerZero-Labs/LayerZero-v2/blob/9c741e7f9790639537b1710a203bcdfd73b0b9ac/packages/layerzero-v2/evm/messagelib/contracts/upgradeable/WorkerUpgradeable.sol
- LayerZero Immunefi rules: https://immunefi.com/bug-bounty/layerzero/information/
- LayerZero official scope: https://immunefi.com/bug-bounty/layerzero/scope/
- Paladin MessageLib audit PDF (Issue #03, page 20, acknowledged / Low): https://paladinsec.co/assets/audits/20231215_Paladin_LayerZeroMessageLib_Final_Report.pdf
- Live Tracker is not replaced by this fallback receipt; tracker access/readback remains blocked.
