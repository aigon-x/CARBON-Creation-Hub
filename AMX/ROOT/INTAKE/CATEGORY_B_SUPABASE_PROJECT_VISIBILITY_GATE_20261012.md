# ROOT INTAKE — CATEGORY B: SUPABASE PROJECT-VISIBILITY GATE + REUSE-FIRST EXECUTION RECOMMENDATION

**Intake ID:** ROOT-20261012-CATB-SUPABASE-PROJECT-VISIBILITY  
**Date:** 2026-10-12  
**Classification requested:** CATEGORY B — research findings + sequenced recommendations  
**Submitting lane:** Capability continuity / tool-route recovery  
**Authority effect:** ADVISORY ONLY. This report requests governance disposition and an authorized access check. It does not create project infrastructure, change production state, authorize spend, or modify existing schedules, roles, workers, queues, or mandates.

## 1. Decision requested

**Recommended disposition: MERGE this as an access-and-verification subtask into the existing ROOT intake work on plugin bundles/provider continuity and capability-route recovery. Do not create a duplicate Supabase project, second queue, new worker, scheduler, or parallel governance record.**

Supabase is already named within the existing AMX Builder & Code bundle concept in the ROOT Intake consolidation record. This report is a new factual delta: the currently connected Supabase organization can be enumerated, but its project list returned empty. The immediate question is therefore route/access verification—not a fresh architecture proposal and not an instruction to provision infrastructure.

## 2. Evidence captured and precise limits

- The connected organization listing returned **AMilliMATRiX**, organization identifier `toebqxvtghjdnuyhbhuh`, with plan/tier reported as **Free**.
- The connected `list_projects` operation returned an empty project list.
- This establishes only that **no projects were returned in this connected tool context at the time of inspection**. It does not prove that the organization has no projects, that no project exists elsewhere, or that project data has been deleted.
- Because no project reference was returned, the connected route could not inspect a live schema, migrations, Row Level Security (RLS), database advisors, Edge Functions, queues, schedules, logs, backup settings, or application runtime.
- No database query, schema mutation, deployment, account change, project creation, or spend was performed.
- The prior ROOT Intake record already treats Supabase as part of the candidate AMX Builder & Code bundle and warns that a listed app does not itself guarantee account authorization, connector access, or working routes. This proposal preserves that distinction.

**Evidence source record:** connected Supabase organization listing and project listing from this run. A project ID and project-level readback are not available yet.

## 3. Why this matters

A database architecture recommendation cannot safely be treated as an implementation finding without examining the actual project and its current controls. Creating a new project before checking the existing authorized route risks duplicate infrastructure, avoidable cost, split data, and a false claim that the original state was recovered.

The rational first action is a bounded access audit. If the current organization route is incomplete, restore access to the existing approved project. If no approved project can be found, bring a separate, costed provisioning request through the existing authority path before creating anything.

## 4. Reuse-first technical recommendation

After the correct existing project is visible, conduct a read-only audit in this order:

1. **Identity and scope:** record the exact project reference, project owner/authorized operator, environment, region if relevant, and whether it is production, staging, or development.
2. **Schema and change history:** inspect schemas, tables, migrations, triggers, extensions, and the current deployment/readback path. Do not infer the schema from product documentation.
3. **Security:** inspect exposed schemas and grants, RLS coverage and policy logic, views, functions and privileged execution, Storage policies, and secrets handling. Run the available Supabase security/database advisors and record findings before proposing changes.
4. **Execution durability:** identify whether an existing queue, Edge Function, or scheduled processing route already exists. Reuse it when suitable. Do not create another scheduler or queue just because a preferred pattern is available.
5. **Operations:** inspect current errors/logs, usage and resource constraints, and available backup/restore options. Validate the required recovery point and recovery time against the actual workload and plan before calling it production-ready.
6. **Behavioral acceptance:** for any later approved change, test it, then independently re-read the persisted result, verify the expected state transition and failure/retry path, and record the exact evidence. A submitted directive, acknowledged job, or successful write alone is not acceptance.

**Conditional target architecture, only if evidence shows a real gap:** use Postgres as the durable source of record; RLS and appropriate grants for access boundaries; the existing authorized queue for durable work; and Edge Functions for bounded execution. Use `pg_cron`/scheduled invocation only if a demonstrated requirement exists and it does not duplicate a current schedule. Give every external side effect an idempotency/deduplication key and separately record the external receipt. Database queue delivery is not a guarantee that an external message, payment, submission, or other side effect occurred exactly once.

Official references consulted:
- [Supabase Queues](https://supabase.com/docs/guides/queues)
- [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
- [Production readiness checklist](https://supabase.com/docs/guides/deployment/going-into-prod)
- [Scheduling Edge Functions](https://supabase.com/docs/guides/functions/schedule-functions)
- [Shared responsibility model](https://supabase.com/docs/guides/deployment/shared-responsibility-model)

## 5. Proposed sequence and governance boundary

**Step 1 — Resolve the route first.** An authorized organization/project administrator should confirm whether an existing AMX project is present and make the proper project visible to the connected authorized route. Do not copy credentials into Intake, logs, prompts, or this report.

**Step 2 — Read-only verification.** Record the project reference and perform the audit in §4 without altering data or settings. Save a reproducible findings receipt under the existing Intake/evidence path and independently read it back.

**Step 3 — Classify gaps.** Separate configuration defects, connector/permission gaps, missing evidence, and true architecture gaps. Route material changes through the existing ROOT/Intake governance path; do not locally promote a recommendation to policy.

**Step 4 — Implement only approved deltas.** Use the repository's existing migration and review workflow, test on a non-production environment when available, run relevant advisors/tests, and verify the final state after deployment. Preserve the prior state and rollback path.

**Step 5 — Provision only if needed and approved.** If the authoritative check finds no suitable existing project, present the owner with purpose, data classification, operator/access model, expected usage, total cost implications, backup/recovery needs, and acceptance tests before creating anything.

## 6. Category B Directive 23 — itemized outcome and acceptance index

- [ ] **Item 1 — Project/access truth.** **Expected outcome:** distinguish a missing project from an inaccessible or incorrectly linked project. **Owner:** ROOT/T-GOV for disposition; authorized Supabase organization/project administrator for the access check; existing continuity lane for route recovery. **Required action:** inspect the organization and authorized project inventory through the approved route. **Dependency/blocker:** no project was returned by the connected listing. **Acceptance evidence:** exact project reference plus successful authorized project readback, or documented result from the administrator that no suitable project exists. **Persistence/readback:** record the result in the existing Intake/evidence route and re-fetch it. **Safety/preservation:** no credentials in evidence; no project creation during discovery. **Disposition:** OPEN / blocked on authorized route check. **Remaining work:** establish the actual project state.
- [ ] **Item 2 — Security and schema audit.** **Expected outcome:** verified current-state inventory of schema, migrations, RLS/grants, privileged functions, Storage policies and advisor findings. **Owner:** authorized database operator with ROOT governance oversight. **Required action:** read-only inspection of the identified project. **Dependency/blocker:** Item 1 must pass. **Acceptance evidence:** timestamped audit receipt referencing the exact project/environment and advisor output. **Persistence/readback:** receipt committed to the existing evidence path and independently fetched. **Safety/preservation:** no live edits during the audit; secret values excluded. **Disposition:** NOT STARTED. **Remaining work:** conduct only after project access is proven.
- [ ] **Item 3 — Execution/retry model.** **Expected outcome:** identify current queues, Edge Functions and schedules, then reuse rather than duplicate appropriate components. **Owner:** existing implementation owner under ROOT/T-GOV authorization. **Required action:** trace one authorized work item through persisted state, execution result, retry/deduplication behavior and readback. **Dependency/blocker:** Items 1–2 and an identified real use case. **Acceptance evidence:** trace with stable item ID, state transitions, failure/retry result and external receipt where applicable. **Persistence/readback:** stored test receipt and independent state query. **Safety/preservation:** no new worker, schedule or queue before explicit approval. **Disposition:** PROPOSED / not implemented. **Remaining work:** determine whether there is an evidenced gap.
- [ ] **Item 4 — Production/recovery readiness.** **Expected outcome:** verified suitability for the intended workload, including resource usage, security and recovery options. **Owner:** authorized project operator; ROOT decides whether evidence is sufficient for the AMX use case. **Required action:** inspect actual plan/usage and backup/restore settings. **Dependency/blocker:** project-level access and workload requirements. **Acceptance evidence:** current settings and a recovery approach appropriate to the required recovery objectives. **Persistence/readback:** evidence receipt plus direct dashboard/database readback. **Safety/preservation:** don't label production-ready from documentation alone; don't incur upgrades or spend without approval. **Disposition:** OPEN. **Remaining work:** quantify requirements against actual settings.
- [ ] **Item 5 — Existing-route reuse / no duplicate infrastructure.** **Expected outcome:** resolve the Supabase finding within existing builder-bundle/provider-continuity work. **Owner:** ROOT/Intake; MASTER/LIBRARIAN or existing continuity lane for index/route continuity. **Required action:** record this as a linked subtask, not a new role or parallel architecture programme. **Dependency/blocker:** ROOT disposition under the existing Intake route. **Acceptance evidence:** an explicit MERGE/MODIFY/HOLD disposition and canonical index readback. **Persistence/readback:** linked report, commit evidence and refreshed index. **Safety/preservation:** preserve original histories and specialist mandates. **Disposition:** MERGE recommended; governance readback pending. **Remaining work:** ROOT/T-GOV disposition and route propagation if accepted.

## 7. Current disposition

**INTAKE SUBMISSION:** this proposal is submitted for ROOT/Intake disposition once persisted in the canonical route.  
**Implementation:** NOT STARTED.  
**Live Supabase health/security status:** UNKNOWN—not audited because project-level visibility is unavailable.  
**Project existence:** UNKNOWN from this connector result; an empty returned list is not proof of nonexistence.  
**Spend or infrastructure changes:** NONE.  
**Final decision requested:** MERGE into the existing plugin-bundle/provider-continuity route as an access-gated audit subtask; HOLD any project creation and production changes until the authorized current-state readback and explicit approval.

