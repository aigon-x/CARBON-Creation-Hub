# BOUNTY REAPER — sBTC nonce-response prior-art dedupe receipt

**Receipt ID:** BR-20261010-SBTC-PRIOR-ART-001  
**Date:** 2026-10-10  
**Existing Reaper lineage:** `RUN-20261002-1837`; immutable commit `3e16c056fd7bc595522fb904dd4d3fcd4cb7795a` in `stacks-sbtc/sbtc`  
**Disposition:** **PUBLICLY DOCUMENTED / MERGED BEHAVIOR — DO NOT SUBMIT AS A NEW FINDING.** Any materially different hypothesis requires its own concrete evidence.  
**Scope:** Prior-art/eligibility dedupe only; no claim that the entire current sBTC codebase is safe.

## 1. Why this parcel was revisited

The existing Matrix truth record identifies Reaper's latest previously evidenced material run as `RUN-20261002-1837`, with source pin `stacks-sbtc/sbtc@3e16c056fd7bc595522fb904dd4d3fcd4cb7795a`, and says exact program/scope binding remained on HOLD. It was therefore appropriate to re-resolve the current official bounty scope and the source commit's public history before considering further promotion.

## 2. Direct primary-source readback

- Immutable source commit: https://github.com/stacks-sbtc/sbtc/commit/3e16c056fd7bc595522fb904dd4d3fcd4cb7795a
- Public pull request #2135: https://github.com/stacks-sbtc/sbtc/pull/2135
- Public issue #2133: https://github.com/stacks-sbtc/sbtc/issues/2133
- Current sBTC bug-bounty scope: https://immunefi.com/bug-bounty/sbtc/scope/

The fetched commit title is **“feat: cache nonce responses and use them (#2135)”**, dated before this receipt. Its description states that it caches `NonceResponse` values in the signer state machine, uses them to construct signature-share responses, and caches nonce responses during DKG verification. The current public PR is **merged** and explicitly closes issue #2133. Issue #2133 already describes the intended behavior: use each signer's directly received and authenticated nonce responses rather than copies supplied in a signature-share request; cache them; reject mismatched responses; and treat duplicate nonce requests as retransmissions.

The current official sBTC program page was last updated **2026-10-07** and includes the “sBTC signer implementation” among in-scope assets. Its out-of-scope rules exclude publicly disclosed/known findings, including issues and pull requests in the sBTC repository, while requiring a functional PoC for any report. Thus the general behavior explicitly described by issue #2133 and merged PR #2135 cannot be treated as a new undisclosed bounty finding.

## 3. Precise disposition

**Killed as a standalone bounty claim:** “The nonce-response cache/verification behavior introduced by commit `3e16c056fd7bc595522fb904dd4d3fcd4cb7795a` is itself a new undisclosed vulnerability.” The central behavior is already publicly described in issue #2133 and implemented by merged PR #2135.

**Not established:** that every path in the sBTC signer, DKG verification, WSTS nonce handling, or newer code is safe. This check was not a full security audit, did not execute tests, and did not attempt exploitation.

**Reopen condition:** identify a materially distinct defect with exact affected function/path, attacker preconditions, a reproducible local/regtest PoC, impact meeting the current official program, and dedupe against all relevant current public issues/PRs/advisories/audits. A rephrasing of the merged behavior, a test/log observation already described by the PR, or a generic hypothesis is insufficient.

**Next lawful action:** do not spend further Reaper cycles trying to submit the public feature/fix itself. Continue to a different independent, potentially eligible Reaper parcel; preserve any separate concrete nonce/round/ownership mismatch only if new evidence distinguishes it from the known implementation and demonstrates current eligible impact.

## 4. Safety and tracker truth

No live target, transaction, public testnet or fund movement was used. No report was submitted and no acceptance, award, receivable or payment is claimed.

The current runtime still has no authorized Google Sheets/Drive read/write connector. This is an Intake fallback receipt only: **no Live Tracker Runs row is claimed**, tracker state remains `TRACKER_WRITE_BLOCKED`, and Q1 remains **UNKNOWN, not zero** until the current queue is reconciled through an authorized source.

## 5. Category B Directive 23 — itemized acceptance checklist

- [x] **Outcome:** the exact prior-art candidate is identified and not promoted as a fresh finding.
- [x] **Owner:** Bounty Reaper remains the specialist owner; ROOT/T-GOV retains governance disposition; Commercial Manager coordinates priority and continuity.
- [x] **Required action:** stop pursuing the publicly described/merged behavior as novel and advance a distinct lawful parcel.
- [x] **Dependency/blocker:** public issue/PR prior art is established for the general nonce-response cache behavior; the current Tracker read/write route remains blocked.
- [x] **Acceptance evidence:** exact source commit fetched; issue #2133 and merged PR #2135 fetched directly; current official sBTC scope page checked.
- [ ] **Persistence/readback:** receipt must be read back from canonical main and indexed. Live Tracker row is not written; preserve the exact fallback marker.
- [x] **Safety/preservation:** no live testing, no exploit, no duplicate external submission, no claim that adjacent code is safe.
- [x] **Item-level disposition:** general nonce-response cache behavior = PUBLIC PRIOR ART / DO NOT SUBMIT; distinct unproven adjacent hypothesis = UNKNOWN, only reopen with new evidence; current sBTC program = current source confirms it is in-scope at program level; exact claim eligibility remains subject to its own gates.
- [ ] **Remaining work:** index/read back this receipt; proceed to another eligible parcel; recover Tracker access/Q1 truth; keep Root retrospective OCC-04 review open.

**Truth boundary:** this receipt kills only the standalone public behavior claim. It does not claim a complete audit, test execution, bounty submission, award or payment.
