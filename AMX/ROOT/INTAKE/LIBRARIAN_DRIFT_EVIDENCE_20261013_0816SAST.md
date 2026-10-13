# LIBRARIAN DRIFT EVIDENCE — ROOT INTAKE
**Observed:** 2026-10-13 08:16 SAST (06:16 UTC)  
**Classification:** Category A runtime/continuity drift + stale-source/supersession drift  
**Existing flight:** `AMX-FLT-20261012-DSYNC-145440-9fb44f0c`, segment 04, IN_FLIGHT  
**Purpose:** Evidence and governed recovery actions only. This artifact does not itself change mandates, allocations, scoring rules, owners, public-release status, commercial state or scheduler configuration.

## 1. Canonical preflight

Direct current-main reads:
- `AMX/ROOT/BLUE_STATE/BLUE_STATE_MANDATE_BINDING_AND_PREFLIGHT_V1.md`: blob `e7219b643f257dd3c59b86c1b56c8c91f97f8ee4`
- `AMX/ROOT/BLUE_STATE/MANDATE_REGISTRY_V1.json`: blob `d3a749a48d98292a13931fd6ff8518dea03e5b20`
- `AMX/ROOT/INTAKE/INTAKE_INDEX.md`: blob before this report `ac6ef9a97199ecd71757d611677b76f31b107b02`
- Registry v1.2 root recomputed as `6f46db56ce4b54bd4655f9e0f5e919dcdb004520d6a0acd455281841a1d7912f`, exactly matching the declared root.
- Mandate payload bytes independently re-hashed from the canonical Blue State markers. All four registered roles matched their registry digests and `CURRENT` status:
  - MASTER-LIBRARIAN: `f127bec771d398c7c2c3a1e746734619568b5641c91d6f810514d08f7f76b4f8`
  - ROOT-TGOV: `d92852d15f66168990290aece801b8c8573d48037b88765a081a26d58e10b120`
  - T-COD: `67a9fc18adc6323ea93f86bc70bb677b7e063b5f6f6a8218d1ec2713c4f0e9b3`
  - T-MED: `3204cb5d8dfcfbc1e904a4a23f0077959bb9371152a2ef32be48e7e858d148f1`

## 2. Drift A — stale D04 instruction versus current supersession

The supplied cached envelope says 90.51% / FAIL is the current plateau. That statement conflicts with the newer canonical supersession record.

The current Blue State states that the correction chain `ecafad6… → 78d0473… → 99adcea… → 5aa034c…` established the **96.62% PASS / zero measured FAIL interpretation for the original historical vector**. It explicitly classifies a later T-MED block that resurrected 90.51% / FAIL as separate stale-result reversion drift. The existing governance evidence is `AMX/ROOT/INTAKE/GOVERNANCE_D04_9051_STALE_RESULT_REVERSION_DRIFT_20261010.md`.

Separate from that historical recomputation, the current Intake Index records an Owner-reported, distinct clean execution of 143/148 = 96.62%; its own primary vector/run receipt has not yet been located in retained repository sources. The Index says not to deny that execution occurred, not to ask the Owner to rerun it, and not to claim an independently verified current PASS until that execution's own primary evidence is located and read back.

**Finding:** cached instructions and the supplied envelope are stale for D04 source ordering. The remedy is canonical-source consumption and evidence-bound representation, not another benchmark run and not a new scoring standard.

**Disposition:** preserve historical artefacts; no fresh score generated; public D04 release remains gated on the separate clean execution's primary evidence and ROOT/T-GOV release disposition.

## 3. Drift B — ROOT issue #31 body retains an obsolete ledger projection

Current source readback:
- `overdrive/opportunities.json`, blob `22b61245999586669982844ecd50d7ec0df6232f`: `record_count=86`; actual distinct keys = 86.
- `overdrive/claims.json`, blob `042ff62943557578594637d0a65fae9662605435`: 86 claims; `ready_count=0`; `external_ready_count=0`.
- `overdrive/state.json`, blob `a1d40b8ddcb5d28fd8b6b9edcf9209dcc6b57244`: sequence 20; last recorded tick `2026-10-12T01:12:34.099363+00:00`; queue length 20; last recorded `processed=[]`.
- The `last_run.full_ledger_count=62` field belongs to its historical `2026-10-03T17:42:00Z` run and must not be rewritten to imitate the current map.

The body of open ROOT issue #31 still presents the older count of 66 declared records / 83 distinct keys. Later comments on the same issue already report current 86/86. Preserve the old body as historical evidence; use a dated additive comment and index cross-reference for the current derived count instead of silently rewriting provenance.

**Finding:** this is stale ROOT Intake projection drift, not a current ledger cardinality defect. Current ledger invariant is satisfied.

## 4. Drift C — current state and attributable execution must be joined

The state snapshot remains sequence 20 and has no processed events in its latest recorded tick. A successful automation/workflow invocation by itself is not proof of commercial conversion or a durable state transition.

No current-cycle application, buyer acceptance, contract, invoice, payment or verified settlement is established by the state readback in this artifact. Keep `SUBMITTED`, `ACCEPTED`, `CONTRACTED`, `INVOICED`, `PAID` and `SETTLED` distinct.

Issue #3 remains open until a fresh current cycle demonstrates reconcile → persist → readback → continued material action. Issue #24 remains closed. FORX #12/#17 and CARBON Search #16 remain closed; CARBON convergence #18 remains open. No no-contact restriction was relaxed.

## 5. Exact recovery chain

1. **ROOT/T-GOV — D04 source/order:** reconcile the canonical Blue State, current Intake Index, and the separate reported clean-run record. Locate and read back that run's own vector/receipt if retained; otherwise record the exact search scope and “primary evidence not found in retained sources.” Bind an explicit release decision. Do not request a third test.
2. **MASTER/LIBRARIAN + ROOT/T-GOV — issue #31:** add an additive comment linking this evidence and the current 86/86 ledger readback; update the existing Index additively with this path/hash only after the file has been read back. Do not rewrite historical snapshots.
3. **MASTER + current runtime owner — commercial continuity:** reconcile the next authorized runtime tick against opportunities, claims, state and action receipts at one boundary. Any external action remains owned by its current office and requires its gates.
4. **T-COD:** resume the existing Evidence House acceptance obligation. Verify the live route with an authorized low-cost request, exact request/response, record IDs, privacy and freshness behavior. Do not infer service health from deployment metadata alone.
5. **T-MED + existing CARBON° owner:** use the existing authorized production route for non-D04 assets, then verify real files, hashes, rights, claim pointers and access. Keep profile/publication and all D04 assets gated pending ROOT disposition.

## 6. Directive 23 itemized acceptance addendum

- **Expected outcome:** drift is durable in existing ROOT Intake with no authority or evidence mutation.
- **Owners:** ROOT/T-GOV (governance and D04 release); MASTER/LIBRARIAN (continuity, Index and receipt chain); T-COD (technical acceptance); T-MED/CARBON° (assets); existing commercial owners (buyer route).
- **Required actions:** persist this artifact; link it in issue #31; add Index cross-reference; carry out each bounded recovery action above.
- **Dependencies/blockers:** supported repository-write route; separate clean-run primary evidence; authorized live test access; enabled and authorized production route.
- **Acceptance evidence:** successful create/commit response, fetched artifact content+blob; issue-comment ID and readback; Index new blob and matching cross-reference; exact runtime/test receipts.
- **Persistence/readback:** not asserted until each write is fetched after mutation and matches.
- **Safety/preservation:** no prompt-over-canon selection; no score change, re-test, mandate/allocation mutation, external contact, publication, credential/billing change, no-contact relaxation or duplicate worker/task.
- **Per-item disposition:** D04 = OPEN/HOLD; issue #31 current projection = additive correction required; commercial progression = OPEN; Evidence House = OPEN; media = OPEN; flight landing = NOT CLAIMED.
- **Remaining work:** complete the persistence/readback chain and each office's authorized execution. This report is not a flight landing.

