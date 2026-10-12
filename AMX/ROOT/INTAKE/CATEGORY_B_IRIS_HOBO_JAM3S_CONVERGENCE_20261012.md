# CATEGORY B — IRIS / H0B° / JAMES–JAM3S CONVERGENCE RECOVERY
Date: 2026-10-12
Intake ID: ROOT-20261012-CATB-IRIS-HOBO-JAM3S-CONVERGENCE
Requested governance disposition: **MERGE** into the existing Matrix ecosystem recovery / anti-dilution workstream; retain item-level HOLDs where source, lineage, deployment, or approval evidence is missing.
Current implementation state: **PARTIAL — James landing stability proposal isolated; not merged or deployed.**
Authority state: **Submitted to canonical ROOT Intake by durable repository write; ROOT classification/acknowledgment not confirmed.**

## 1. Why this is being taken

The Owner asked for the latest commits and a safe path to bring IRIS / MyCase, HOBO / H0B° Unchained, and James / JAM3S current as the branches converge. The existing Matrix recovery controls already define this as a source-lineage and anti-dilution problem. Reuse those controls instead of creating a second architecture, worker, queue, or design system that erases ecosystem boundaries.

**Decision:** recover each source, preserve identity and capability, implement only low-risk changes on an isolated branch, and require evidence before merging, deploying, moving value, or claiming runtime continuity.

## 2. Current-source findings

### IRIS / MyCase
- Repository: [BullRulez/IRIS-My-Case](https://github.com/BullRulez/IRIS-My-Case), default branch `main`.
- Latest repository commit found: [2524b03c3c257e7bc9d87835a40391b54687ee59](https://github.com/BullRulez/IRIS-My-Case/commit/2524b03c3c257e7bc9d87835a40391b54687ee59), “Initial commit,” 2026-08-29. Repository reports size 0 and contains only a 53-byte README. It is not the current editable implementation.
- A retained historical HTML artifact, `02.08 About IRIS.html`, confirms the core purpose: a living evidence layer helping participants evaluate evidence and make better-informed decisions before committing. It explicitly says IRIS does not score, rank, or determine human suitability; the decision remains human.
- The retained AMX manifest references `IRIS_v0_1_Package.zip` as a historical source seed and explicitly records a current-source gap. A search of available Library file listings did not surface the ZIP itself. This is **not** proof that the artifact is deleted; custody remains unresolved.
- Do not rebuild IRIS from memory or equate the `IRIS-My-Case` repository slug with the current runtime. Evidence-backend ownership and placement remain HOLD until the current architecture/source is recovered.

### HOBO / H0B° Unchained
- Character/app repository: [BullRulez/AMB-HOBO-AI-](https://github.com/BullRulez/AMB-HOBO-AI-), `main`, latest commit [3f59971cedf2db4b92f9cfdfe2ad426796675adf](https://github.com/BullRulez/AMB-HOBO-AI-/commit/3f59971cedf2db4b92f9cfdfe2ad426796675adf), 2026-06-15. This is the React / Gemini / Firebase / Telegram codebase; source is present, but the current deployment/runtime receipt is not verified.
- The repository's `AGENTS.md` preserves H0B°'s gritty, street-authentic, high-execution terminal style and explicitly forbids unsolicited SDKs and mock APIs that pretend to represent real balances or transactions.
- The separate published surface [H0B° unchAIned](https://hobo-unchained.amillimatrix.chatgpt.site/) currently presents faction sprints, participation, INTEL, and a JAM3S-verified task adapter. Its visible truth labels say INTEL is earned status, not cash, and real-value rewards require external verification. Do **not** assume this published ChatGPT Site is built from `AMB-HOBO-AI-` or merge their source without lineage evidence.
- A third codebase, [BullRulez/Unchained_AmillimatriX-](https://github.com/BullRulez/Unchained_AmillimatriX-), has a later latest commit [38c2f603c4e1349918945b0947845ff135e0d0d2](https://github.com/BullRulez/Unchained_AmillimatriX-/commit/38c2f603c4e1349918945b0947845ff135e0d0d2), 2026-06-27, and includes MatrixOrbit / SignalScan work. This is additional source lineage to compare, not permission to collapse the HOBO products into one app.
- **Disposition:** preserve HOBO's canon and separate source lineages. Recover a runtime/deployment receipt and identify which app the Owner intends to update before a visual redesign is merged.

### James / JAM3S
- [James-Bot](https://github.com/BullRulez/James-Bot) latest `main` commit: [97bb4637670dd116b45206b0a5aacc0a51527d09](https://github.com/BullRulez/James-Bot/commit/97bb4637670dd116b45206b0a5aacc0a51527d09), 2026-04-28. This contains the Telegram Web App UI, a separate Python bot file, a large React screen, and a Puppeteer smoke test.
- [JAM3S_BOT](https://github.com/BullRulez/JAM3S_BOT) latest `main` commit found: [078576d4a86dc4c3f3ae532183b89a6dabf1e084](https://github.com/BullRulez/JAM3S_BOT/commit/078576d4a86dc4c3f3ae532183b89a6dabf1e084), 2026-07-22. Its `AGENTS.md` explicitly freezes JAM3S V1, requires implementation in isolation, and says not to deploy without an explicit `RUN IT`, `DEPLOY TO PRODUCTION`, or `SHIP V1` approval.
- Existing Matrix recovery rules establish JAM3S as the reputation / trust / verified-participation / accountable-record ecosystem. `James-Bot` and `JAM3S_BOT` are related candidates but their exact code-level lineage remains HOLD. Do not copy one repo over the other or treat the UI as proof of the bot's durable trust/ledger behavior.
- Source inspection found direct unguarded `localStorage` access in the James UI's React state initializer. In a browser context where storage access throws, that can prevent the component from mounting. The old Puppeteer test navigates to a retired Netlify preview URL and does not verify the primary CTA or successful transition into the app.
- The current public `https://jam3sbot.netlify.app/` returned boot text through text extraction. The old preview `https://69ec3c128f1a22d4ec8777b8--jam3sbot.netlify.app/` returned 404. A live browser test could not start because the connected TinyFish wallet is below zero; therefore the exact production crash was not reproduced in a browser.
- The James UI also contains simulated activity/balance/reward values. Those must remain clearly labelled as simulation and must not be represented as authoritative, persistent or externally settled Matrix state.

## 3. Changes actually made

A recovery branch was created in `BullRulez/James-Bot`:
- Branch: `recovery/james-landing-stability-20261012`
- [Draft PR #1 — Guard Matrix landing startup in restricted browsers](https://github.com/BullRulez/James-Bot/pull/1)
- Commits:
  - [f281aed79b4bf4c5b471416dd7d5a0b686a796f5](https://github.com/BullRulez/James-Bot/commit/f281aed79b4bf4c5b471416dd7d5a0b686a796f5) — guard storage reads/writes.
  - [78aaef34bfd28e68e8fc5c36e9b0c5caabdefe61](https://github.com/BullRulez/James-Bot/commit/78aaef34bfd28e68e8fc5c36e9b0c5caabdefe61) — make MatrixRain cleanup/reactivity respect the `active` prop.
  - [75ea2f42bdcd7bd4faf5e393abdb5ce04aad28a0](https://github.com/BullRulez/James-Bot/commit/75ea2f42bdcd7bd4faf5e393abdb5ce04aad28a0) — replace the stale smoke test with local landing-flow tests for normal and denied storage.
- PR remains **open, draft, unmerged**. The source changes are persisted in GitHub, but the build and browser test have **not** been run in this environment. No production deployment, bot/database mutation, reward change, or merge was made.
- This is a targeted stability correction, **not** a claim that the whole James experience has been repaired or visually converged.

## 4. Capability / provider checks

- GitHub source reads and writes succeeded under the BullRulez account; source commits and branch/PR were returned by the connector.
- Vercel returned no projects matching James/JAM3S and the team context has no linked Git projects. Vercel is not evidenced as the active deploy route for these sources.
- Linear searches for James/JAM3S, HOBO, and IRIS returned no relevant project work items; only generic workspace onboarding issues surfaced. No duplicate tracking issue was created.
- TinyFish could extract the published pages, but its live browser automation was not started due to insufficient wallet balance. Do not treat a text extraction as interaction-level verification.
- Render listed a workspace called “My Workspace,” but its service API explicitly requires the user to select a workspace before service inspection. No workspace was selected and no Render service was inspected or changed.
- Blockscout chain metadata was available after session initialization, but no contract address / chain mapping was recovered from the inspected product sources. No on-chain state was queried or claimed.

## 5. Recommended Matrix visual convergence — additive, not flattening

Apply a shared **Matrix interaction language**, not a shared identity:
1. Black / obsidian base; deliberate green signal and gold provenance accents; crisp hierarchy and purposeful motion; readable mobile layout; consistent focus, loading, empty, error, and success states.
2. Common state vocabulary across products: `SOURCE`, `SYNC`, `VERIFIED`, `PENDING`, `BLOCKED`, `UNKNOWN`. Only show `VERIFIED` when a durable evidence source supports it.
3. IRIS remains evidence-first, accessible, neutral, and human-decision preserving; no ranking people or gamifying evidence.
4. HOBO keeps its rough-edged, street-authentic tone and its explicit INTEL-versus-cash distinction.
5. JAM3S remains trust-through-verified-participation, not a simulated balance dashboard. Telegram bot, web UI, and durable record remain distinct surfaces.
6. Share visual tokens and interaction/accessibility patterns only after source lineage and product-specific canon are documented. Do not introduce another runtime, queue, scheduler, database, provider or shadow architecture merely to make screens look aligned.

## 6. Category B Directive 23 acceptance checklist

| # | Expected outcome / owner | Required action | Dependency / blocker | Acceptance evidence | Persistence / readback | Safety / preservation | Item disposition | Remaining work |
|---|---|---|---|---|---|---|---|---|
| 1 | Current source lineage — Continuity owner + ROOT | Compare IRIS seed/site/repo; HOBO AI, Unchained and published surface; James-Bot, JAM3S_BOT and package | IRIS seed ZIP and exact runtime source not located; HOBO deployment receipt absent; JAM3S code lineage unresolved | Per-source commit, file/package hash, branch, deploy receipt and explicit lineage edges | Commit this report and update canonical Intake Index; independently re-read both | No overwrite/copy across repos; preserve unknowns as HOLD | **HOLD** pending evidence | Locate IRIS ZIP/current source; recover HOBO deployment; reconcile James/JAM3S and package |
| 2 | James landing stability — James-Bot maintainer | Review and run PR #1; test primary CTA with normal and denied storage; fix any reproducible crash | Browser/build execution not available here; TinyFish wallet insufficient | Passing build/lint plus Puppeteer output with no uncaught page errors | PR branch and files exist; read back commit SHAs and PR state | Draft only; no merge/deploy; no reward or backend change | **MODIFY proposed** in draft PR | Run checks in a controlled environment; inspect actual production crash logs |
| 3 | Matrix design convergence — Product/design owner + ROOT | Establish shared tokens and state semantics; apply product-specific treatments only after source selection | Product Design audit workflow unavailable in this standard chat; deployment/source targets differ | Approved source-to-screen comparison, responsive/a11y checks, interaction tests | Record tokens and product-specific deltas in canonical design/source record | No generic reskin; preserve IRIS neutrality, HOBO canon, JAM3S trust boundaries | **HOLD** | Continue in Product Design Work tab; identify authoritative HOBO surface and current IRIS source |
| 4 | HOBO runtime and truth — HOBO owner | Verify live deployment and reconcile AI app with H0B° Unchained site without collapsing them | Render workspace requires explicit selection; TinyFish live interaction blocked | Exact deployment URL, source SHA, runtime/build receipt, UI behavior and state-source map | Read deployment metadata and source SHA into existing recovery manifest | No simulated value presented as real; no unrequested SDKs | **HOLD** | Owner selects Render workspace; recover actual deploy provider/source |
| 5 | JAM3S trust and integration — JAM3S owner | Reconcile UI, Telegram runtime, package, durable DB and any deployment; remove false authority claims before release | V1 freeze; no lineage merge evidence; no verified current runtime readback | Source/package hash comparison, database backup receipt, tests, runtime health and authenticated flow evidence | Update existing Matrix manifest only with read-back evidence | Preserve frozen V1; no deployment without explicit approval | **HOLD** | Code-level lineage analysis; verify backend truth, test suite and runtime |
| 6 | IRIS living evidence — IRIS owner + ROOT | Recover current source; map case/MiCase and evidence backend; audit presentation and access controls | Current editable/runtime source and evidence-backend ownership unknown | Source hash, architecture map, evidence provenance/access tests, human-decision guardrails | Preserve historical HTML and ZIP references; update manifest after proof | Do not rank people, redefine IRIS, or infer backend ownership | **HOLD** | Locate source seed and current Sites/repository artifacts |
| 7 | Deployment/provider route — capability continuity owner | Reuse actual provider; verify Vercel/Render/Netlify/AI Studio route rather than assume | Vercel has no linked projects; Render workspace not selected; Netlify preview is 404 | Provider project/service ID, commit-linked deployment, health/readback | Record provider and immutable deployed SHA in existing manifest | No new project, service, spend, scheduler, or runtime without evidence/approval | **HOLD** | User confirms Render workspace if that route is to be inspected; inspect other exact deployment receipts |
| 8 | Intake disposition — ROOT / existing Intake owner | Classify as MERGE/MODIFY/REJECT/ALREADY-SUBSUMED/HOLD in the existing recovery lane | Direct parent notification route unavailable; no ROOT acknowledgment received | Explicit item-level disposition in canonical index and attributable acknowledgment | Read back report and index after writes | No false queue drain; submitted does not equal accepted/implemented | **MERGE recommended; pending ROOT disposition** | Obtain ROOT classification/readback; continue only source-supported actions |

## 7. Final disposition

- **What was taken:** one isolated, low-risk James landing stability patch plus a two-mode browser test.
- **Why:** browser storage exceptions are a credible startup failure mode, and the existing smoke test checks a retired URL without testing the landing transition.
- **What was not taken:** no bulk branch sync, cross-repo copy, UI-wide redesign, production deploy, database change, or claim that IRIS/HOBO/JAM3S are now current.
- **Canonical route:** merge this recovery report into the existing Matrix ecosystem recovery / anti-dilution workstream. No new worker, queue, schedule, provider, or shadow architecture.
- **State:** James patch persisted in a draft PR; IRIS, HOBO runtime and James/JAM3S lineage remain explicit HOLDs. The Matrix convergence is **not complete** until the acceptance evidence above is read back.
