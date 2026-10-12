# CATEGORY B — CROSS-MODEL RUNTIME, CANON AND ANTI-OVERWRITE CAUTION
**Date:** 2026-10-12  
**Intake ID:** ROOT-20261012-CATB-CROSS-MODEL-RUNTIME-ANTI-OVERWRITE  
**Status:** SUBMITTED FOR ROOT / T-GOV CLASSIFICATION — BLUE STATE AMENDMENT REQUESTED  
**Requested disposition:** MERGE into the existing Blue State / Matrix Ecosystem Recovery & Anti-Dilution control. Do not create a competing framework, runtime, worker, queue or scheduler.

## 1. Executive caution

The Owner clarifies that the applications are running, while the repository snapshots reviewed in the prior pass and their UI/UX are stale and out of canon for implementation. The product surfaces need to reflect the current storyline and intended Matrix interconnection.

**Treat the source revisions reviewed during the prior James/HOBO pass as forensic evidence only—not implementation authority—until Owner/ROOT binds each live runtime to its exact source, revision, data plane and deployment receipt.** This includes the assistant-created James-Bot recovery branch and draft PR #1. Preserve for provenance; do not merge, copy from, or describe passing local tests as a live fix.

This is a governance caution and source-selection proposal. It does not authorize a direct Blue State edit, production overwrite, shared-bucket/database change, deployment move, or JAM3S V1 change.

## 2. Evidence requiring the guardrail

### A. James/JAM3S source copies are highly similar
Inspected repository main heads:
- `BullRulez/James-Bot`: `97bb4637670dd116b45206b0a5aacc0a51527d09`, dated 2026-04-28.
- `BullRulez/AMB-HOBO-AI-`: `3f59971cedf2db4b92f9cfdfe2ad426796675adf`, dated 2026-06-15.
- `BullRulez/JAM3S_BOT`: `078576d4a86dc4c3f3ae532183b89a6dabf1e084`, dated 2026-07-22.
- `BullRulez/Unchained_AmillimatriX-`: `38c2f603c4e1349918945b0947845ff135e0d0d2`, dated 2026-06-27.

The following files are similar, not independent proof of separate live runtimes:
- `James-Bot/james_bot.py`: blob `afbf1883ac672ed3fd1cee4d903ae1f38bff4d57`, 1,403 lines.
- `JAM3S_BOT/james_bot.py`: blob `c1a40657dd2e437edc5c9e0005ac2a0a629611b3`, 1,454 lines; normalized-line comparison found 94.7% Jaccard overlap with the James-Bot copy.
- `JAM3S_BOT/app/applet/james_bot.py`: blob `f3e17b3a3fb61d0872a02ee7480b292dca54f914`, 1,521 lines; also highly similar to the other copies.

This establishes duplicated/similar source artifacts, **not** the number of active services or which file runs in production. The existing Matrix manifest already holds James-Bot/JAM3S code-level reconciliation. Do not silently select a winner, copy one file over another, or call each copy a separate authoritative runtime.

### B. HOBO and H0B° Unchained share Firebase identifiers
Readback of `firebase-applet-config.json` in `AMB-HOBO-AI-` and `Unchained_AmillimatriX-` shows the same Firebase project ID, app ID, auth domain and Storage bucket identifier, while their Firestore database IDs differ:
- HOBO database ID: `ai-studio-fe1f1030-15b2-4f6f-9cec-0849aae24a06`.
- H0B° Unchained database ID: `ai-studio-841e0ae8-e66a-4c34-94da-840a9520e282`.

The Owner reports that this is the same Europe bucket. The reviewed GitHub config confirms the same bucket identifier but this pass did **not** independently verify its location/region through the cloud control plane. The differing database IDs may be intentional. Do not normalize, swap or “fix” IDs by guesswork. Do not alter bucket contents, Firebase config, Firestore rules, auth, webhooks or secrets without an approved plan, backup/provenance and explicit authority.

### C. Product/storyline direction exists, but is not final canon by assumption
The existing intake candidate `AMX/ROOT/INTAKE/H0B_JAM3S_ONE_STREAMLINED_WHOLE_2026-10-04.md` states the intended whole: **H0B° is the face, voice, humor and cultural gravity; JAM3S records memory, rules, evidence, timestamps, state and receipts.** Its card journey is:
`FIND / EARN → HOLD → SHARE → RECEIVE → PASS → ACCUMULATE JOURNEY → UNLOCK → PRESERVE RECEIPT`.

That file is explicitly an **INTAKE MERGE CANDIDATE**, not proof ROOT froze every detail as final canon. Preserve the locked H0B° character file and 47-line quote vault, the JAM3S V1 freeze/approval gate, and the distinction between private records and public journey proof. New UI/UX should represent the latest Owner-approved storyline and use existing authorized Matrix interfaces. Do not fabricate live metrics, balances, payouts, validation cycles or trust state, or create a parallel ledger.

## 3. Proposed Blue State guardrail — model-to-model non-overwrite protocol

ROOT/T-GOV is asked to classify and, if accepted, add these rules to existing canonical governance:

1. **Canon first; predecessor work second; code third.** Every incoming model/session reads current Blue State, Matrix manifest, required-state gate, current Intake decisions, latest Owner instructions, and previous model/PR/branch receipts before proposing a change. First deliverable: what the previous model actually changed, what is valid/reusable, what is stale/out of canon, what failed or remains untested, and the smallest safe improvement. Never restart from partial chat memory.
2. **Bind the live target before editing.** Record product/identity, owner, canonical source repo/package, branch and immutable source SHA, production URL/service ID, deployed SHA/build receipt, runtime/database identity, storage/bucket/project/region, auto-deploy path, current UI/storyline and integration contract. If any essential binding is missing or conflicting, mark `UNKNOWN/HOLD`; read-only discovery only.
3. **Label stale targets `OUT-OF-CANON-FOR-IMPLEMENTATION`.** Keep them as history/forensic evidence; do not delete or rewrite history. This label concerns use as an implementation target, not the identity or continuation of HOBO, H0B° Unchained, JAM3S or any Matrix ecosystem.
4. **One accountable implementation owner and one active change set per bound runtime/scope.** Search existing branches, PRs, hotfixes and other model activity. Review the diff and evidence before starting. Where work overlaps, coordinate through the existing Intake; do not create parallel fixes for competing guesses of the same app.
5. **Compare-and-swap; never blind overwrite.** Read current branch/head and exact content hashes immediately before a write. Use a narrow diff on an isolated branch/PR and the existing review route. If head/hash moved, stop and reconcile; never force-push, reset, replace an entire file from a stale snapshot, or silently choose one model's conflict resolution. After writing, independently read back commit, file SHAs, deployed SHA and relevant runtime state.
6. **Shared dependencies are preservation boundaries.** Shared project/bucket/app identifiers alongside app-specific database IDs do not grant permission to merge data. Preserve object/file provenance and backup state first. No object deletion/rename, location change, database-ID swap, permission/rules change, credential/webhook change or migration without explicit authority and rollback.
7. **Design integration is not authority integration.** Align UI/UX with approved story while preserving each ecosystem identity and access boundary. State labels must reflect the authorized source of truth: `LIVE`, `DEMO`, `PENDING`, `BLOCKED`, or `UNKNOWN`. JAM3S remains the evidence/record function; HOBO remains the character/front-of-house function. Do not expose private Matrix internals to consumers.
8. **Source-copy count is not runtime count.** Similar files indicate lineage/overwrite risk, not proof of multiple production services. Verify active deployment IDs/routes, health, deployed source revision and data store before consolidation or retirement.
9. **CI is scoped evidence, not live acceptance.** Passing tests on a stale repository or assistant-generated branch prove only what that exact branch/test exercised. Never propagate the result into live release status without source-to-deployment SHA match and tests against the intended release.
10. **Handoff must be comparative and useful.** Every successor model reviews prior outputs and produces a delta review: prior actions/claims and SHAs; valid reusable work; stale/out-of-canon work; gaps and untested claims; proposed improvement; affected surfaces/dependencies; preservation and rollback; acceptance tests; readback evidence; unresolved items. No repetitive summary-only handoff or duplicate architecture.

## 4. Controlled implementation sequence

1. **Read-only runtime inventory:** resolve the actual running URLs/service identities and source/deployed SHAs for HOBO, H0B° Unchained and JAM3S/James. Inspect the existing GCloud/Europe environment and bucket metadata through authorized cloud access. Do not infer the provider or source from a README, repo existence, previous model summary, or a provider inventory that is not the active host.
2. **Lineage diff:** compare active runtime source with repo/package copies; identify duplicated files, divergent changes, generated assets and owner-authorized canon. Give each artifact one explicit disposition: `KEEP-CANON`, `KEEP-HISTORICAL`, `MERGE`, `REPLACE-AFTER-APPROVAL`, `OUT-OF-CANON-FOR-IMPLEMENTATION`, or `UNKNOWN/HOLD`.
3. **UI/story review:** map each live screen to approved product story and Matrix integration. List stale UI/UX behavior, missing journey stages, incorrect source-of-truth reads, false state labels, mobile/accessibility issues and obsolete interactions before editing.
4. **Propose one narrow change set per confirmed target:** exact files/endpoints, expected behavior, migration/no-migration statement, dependencies, rollback, tests and explicit no-touch surfaces. Route material changes through the existing ROOT/Intake path; respect JAM3S V1 release authorization.
5. **Isolated implementation after binding only:** use a named branch and one accountable implementer. No production edits while lineage remains unresolved.
6. **Validation and reconciliation:** build, lint, relevant unit/integration/browser tests, responsive UI checks, deployed SHA match, and end-to-end state/receipt behavior. Re-read canonical records and runtime after any change. ROOT/Owner makes the release decision; submission or CI alone is not acceptance.

## 5. Immediate item dispositions requested

- James-Bot recovery branch / [draft PR #1](https://github.com/BullRulez/James-Bot/pull/1): **HOLD / forensic only / do not merge as the live fix**. Branch tests passed for that branch but it is not bound to the Owner-identified running runtime.
- James-Bot vs JAM3S_BOT source copies: **HOLD — lineage and duplicate-source reconciliation required**. Active runtime count remains unknown.
- HOBO / H0B° Unchained Firebase linkage: **PRESERVE — shared dependency; no config/data/rules migration** pending live cloud readback.
- H0B° × JAM3S product storyline: **current Intake direction only; not final canon by assumption** until ROOT/Owner confirms the governing version.
- Current live UI/UX refresh and Matrix interconnection: **proposed work; implementation HOLD** until runtime-source binding and an approved design delta are recorded.
- Blue State: **ROOT/T-GOV classification/merge requested**; this caution is not itself canonical Blue State authority.

## 6. Category B Directive 23 — itemized addendum

- **Expected outcome:** future models inspect prior work, correctly bind canonical/live targets, improve existing work without overwriting, and preserve shared runtime/data dependencies.
- **Owner:** ROOT/T-GOV for Blue State classification; existing ecosystem/source owners for runtime binding, canon and release; one current implementation owner per bounded change.
- **Required action:** adjudicate this caution; bind running apps to immutable source/deploy evidence; resolve duplicate sources; document UI/storyline deltas; implement only accepted changes.
- **Dependency/blocker:** active GCloud/Europe service/bucket metadata and deployment SHAs have not been read back from the authorized cloud control plane; the story file remains an Intake merge candidate; exact source-to-runtime lineage remains unresolved.
- **Acceptance evidence:** Blue State merge/readback; active service IDs/routes and deployed SHAs; source-to-runtime diff and artifact dispositions; approved UI/UX delta; passing tests against intended release SHA; no unauthorized shared-data/config changes.
- **Persistence/readback:** index this caution in the canonical Intake Index, post it to the existing ROOT issue thread and independently read back artifact, index pointer and comment.
- **Safety/preservation:** no production deploy, branch merge, data migration, shared-bucket operation, secret/config/rules edit, bot/ledger/reward mutation or lineage erasure. Retain old model outputs and commits as provenance.
- **Item-level disposition:** caution = submitted for ROOT/T-GOV classification; stale snapshots = out of canon for implementation pending binding; duplicate source copies = reconciliation HOLD; shared bucket = preserve; UI/storyline refresh = proposed / target-binding HOLD; Blue State acceptance = pending.
- **Remaining work:** ROOT/T-GOV decision; read current GCloud/Europe service/bucket and deployed source details; confirm approved story canon; complete comparative prior-model review; bind one target per app; then design, test and release through the existing route.
