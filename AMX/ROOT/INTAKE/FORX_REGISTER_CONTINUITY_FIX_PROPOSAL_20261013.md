# FORX continuity repair proposal — register/Index divergence

**Status:** PROPOSED FOR ROOT REVIEW; NOT MERGED; NO MAIN-BRANCH MUTATION  
**Prepared:** 2026-10-13  
**Review branch:** `proposal/forx-flight-register-continuity-20261013`  
**Existing Root route:** [Issue #31](https://github.com/amillimatrix-eng/CARBON-Creation-Hub/issues/31)  
**Controlling rule:** Blue State Category A — Dynamic Flight Path Continuity. The mandate/registry are binding; this document creates no authority or runtime.

## Finding

The current durable state does not prove a registered launch for `FORX-20261013-1646Z-01`. The report/index artifacts for segments 02–04 exist, but the current append-only register contains only the separately registered Matrix continuity flight `AMX-FLT-20261012-DSYNC-145440-9fb44f0c`.

Direct main readback before this proposal:

- Blue State blob: `cda4da372801a91debf3a9c71b8c8ebbf33b4114`.
- Registry blob: `d3a749a48d98292a13931fd6ff8518dea03e5b20`; root remains `6f46db56ce4b54bd4655f9e0f5e919dcdb004520d6a0acd455281841a1d7912f`.
- Register blob: `2fa89004db22bb50580d899e5d37516178c6d6b3`, 39 JSONL events; no event carries FORX flight ID `FORX-20261013-1646Z-01`.
- Index blob: `e0133b2710a0f4287a2751197f8bfd67d5bba17d`; its “Latest continuity checkpoint” claims event `AMX-FLT-20261012-DSYNC-145440-9fb44f0c:CHECKPOINT:SEGMENT-05:INTAKE-RECOVERY-20261013` and register blob `ca100baca17c99b0964e0ad172b0a7f2698822eb`, but neither matches the fetched current register.
- Last register event is the active segment-11 RESUME event. No valid segment-12 checkpoint existed at inspection time.
- Historical register also contains some incomplete optional linkage fields. They are preserved as historical evidence; this proposal does not rewrite prior lines.

## Proposed repair in this review branch

1. Append one current-time CHECKPOINT event to the already registered Matrix continuity flight, segment 12, linked to the exact prior segment-11 event and its existing authorization. This is a checkpoint about observed drift and recovery ownership—not a fabricated launch, not a new FORX flight, and not proof that FORX segment 02–04 was authorized.
2. Update the Index’s *latest checkpoint* pointer to that proposed event and the exact Git blob SHA of the resulting register.
3. Preserve the segment 02–04 report artifacts, but label their `FORX-20261013-1646Z-01` identity as an **unregistered historical claim / continuity anomaly** pending ROOT/T-GOV disposition. Do not delete reports, backdate LAUNCH, or silently adopt their flight ID.
4. Add a read-only, standard-library Python validator plus unit tests and a PR/push-only GitHub Actions check. The check validates JSONL/event IDs, one registered launch per referenced flight, links where present, the current checkpoint event/blob anchor, and Index claims labelled “Existing flight”. It performs no write, has no schedule/worker, and does not touch graph, staging or weights.

## Why not backfill the FORX LAUNCH?

Blue State says a launch must precede material work and missing/mismatched launch identity is a continuity anomaly. A retroactive LAUNCH would assert a fact not present in the current durable evidence. The repair therefore preserves the reports and records the anomaly instead of inventing authorization. ROOT/T-GOV must decide whether those report artifacts should be treated as provenance-only, rejected as invalid flight execution, or reconciled using independently available authorization evidence.

## Acceptance criteria for Root

- [ ] Independently read the proposed register and Index on the PR head.
- [ ] Verify the segment-12 checkpoint references the prior registered segment-11 event and existing authorization.
- [ ] Verify the Index blob value equals the Git blob SHA for the register bytes on the same PR head.
- [ ] Run the validator tests and inspect the CI result.
- [ ] Confirm the Index no longer represents the missing FORX launch as a registered active flight.
- [ ] Decide the proper disposition for the historical FORX reports; preserve provenance and do not backdate.
- [ ] Confirm mandate payload hashes and Registry v1.2 root remain unchanged.
- [ ] Merge only if the corrected truth state and guard satisfy Canon; otherwise request changes or reject.

## Directive 23 — itemized record

- **Expected outcome:** stale checkpoint pointer removed and missing FORX registration treated as an explicit anomaly; future stale/missing flight anchors fail verification.
- **Owner:** ROOT/T-GOV for authority/disposition; MASTER/LIBRARIAN for continuity validation; T-COD for technical gate review; FORX retains its discovery/weighted-continuation mandate.
- **Required action:** review this PR, independently test, then merge or reject through the existing governance path.
- **Dependency/blocker:** no authenticated historical launch evidence for the FORX ID; canonical launch may not be fabricated; repository API exposes no fork-creation operation, so this submission uses a separate review branch in the canonical repository rather than claiming to be a fork.
- **Acceptance evidence:** append-only segment-12 event, aligned Index pointer, fail-closed validator and synthetic regression tests, PR CI result.
- **Persistence/readback:** remains proposed until PR readback/CI, Root disposition, and any authorized merge.
- **Safety/preservation:** no branch-to-main bypass, no duplicate runtime/worker/scheduler/graph/store, no mutation of weights/manifest, no changes to canonical mandates or registry, no backdating/deletion.
- **Item disposition:** durable fix **PROPOSED, NOT ACCEPTED**; current registration anomaly OPEN until Root adjudication and accepted readback.
- **Remaining work:** ROOT review, review-CI, merge/reject decision, post-merge independent readback, and any further authorized runtime propagation proof.
