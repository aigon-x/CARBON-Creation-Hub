# CATEGORY B — AMELIGRAM: ECOSYSTEM-ONLY MESSAGING PRODUCT FEASIBILITY AND POSITIONING
**Date:** 14 October 2026  
**Status:** CATEGORY B DIRECTIVE / FEASIBILITY REQUIRED / NOT A BUILD AUTHORIZATION  
**Owner intent:** captured as given; this does not pause or supersede any current directive, flight, commercial route, or already-authorized project work.

## 1. Objective

Investigate feasibility, implementation paths, risks, cost/operating burden and positioning for **Ameligram**, a first-party AMilliMATRiX messaging experience intended to contain AMX ecosystems and authorized participant spaces rather than become a general public chat network.

The intended experience may use an MTX ID / user-facing MtriX path to identify participants and route them toward authorized ecosystems and spaces. Current evidence does not establish that the MTXID-to-Your-MtriX link or entitlement API is fully implemented. Do not assume it exists; inspect the current governing identity, access and JAM3S records before relying on it.

The name “Ameligram” and the sound/positioning idea are owner-supplied creative direction. Preserve the proposed sonic contrast—a childlike voice asking “Ameligram?” followed by a deep, resonant “voice of Gold” signature—as a concept to refine, not a completed audio asset or final script.

## 2. Non-interference rule

- This is a side proposal. It must not halt, weaken, or displace current FORX, Carbon commercial, Search/Marketplace convergence, ROOT Intake clearance, or other existing work.
- Do not create a new worker, schedule, queue, database, identity authority, scoring system, payment rail or parallel governance route for the feasibility study.
- Use the existing Root/Route Intake and existing owners. ROOT/T-GOV should retroactively classify, reconcile and file this directive under the existing category/authority model; the present file itself does not grant build, spend or launch authorization.
- Keep AMilliMATRiX as the containing ecosystem and keep every component ecosystem's own purpose, identity, permissions and truth state. Ameligram is a communication surface, not a replacement for the systems it connects.

## 3. Feasibility paths to compare

### A. Telegram Bot / Mini App — lowest-friction prototype

Official Telegram documentation describes Mini Apps as interactive web apps that can provide authorization, payments and push notifications within Telegram: https://core.telegram.org/api/bots/webapps

**What it can prove:** navigation, ecosystem discovery, member-aware links, announcements, selected workflows and product entry from one Telegram-integrated experience.

**What it does not prove:** an independent Ameligram messaging network or control over Telegram’s underlying messaging infrastructure. This is a prototype/distribution route, not the final standalone product.

### B. Telegram-compatible client using Telegram APIs / MTProto

Telegram officially permits third-party Telegram-like clients, but requires compliance with its API terms, including privacy/security expectations and supporting core communications compatibly with Telegram users. Sources: https://core.telegram.org/api/terms and https://core.telegram.org/api/obtaining_api_id

**Fit:** useful only if intentional Telegram interoperability is a goal.

**Potential mismatch:** a client app cannot be treated as an ecosystem-only walled garden while disregarding the platform’s interoperability conditions. Do not choose this route simply because Telegram’s API is available.

### C. Independent Ameligram built on an existing open messaging protocol/server

Evaluate a private, controlled deployment using an existing open messaging protocol and self-hostable homeserver/client foundation rather than writing every messaging primitive from scratch. The Matrix protocol is one candidate to assess technically; it is a protocol, not the AMilliMATRiX governance system. It supports room messaging, synchronization, and optional end-to-end encryption, while a self-hosted Synapse deployment requires real hosting, domain, database, backup and abuse-prevention work. Sources: https://spec.matrix.org/unstable/ ; https://matrix.org/docs/guides/understanding-synapse-hosting/ ; https://matrix.org/docs/matrix-concepts/end-to-end-encryption/

**Fit:** could support a branded Ameligram client and controlled ecosystem rooms on infrastructure under AMX control.

**Questions requiring proof:** closed registration/invitation model; mapping existing MTX ID to protocol identity without duplicating identity authority; SSO/session integration; room membership and ecosystem permission mapping; private versus announcement rooms; DM policy; end-to-end encryption/key recovery; push notifications; media/file storage; backups and disaster recovery; anti-abuse/reporting/moderation; retention/export/deletion; federation disabled or explicitly constrained; mobile client distribution; operating cost and on-call ownership.

### D. Custom messaging stack

Consider only if the open-protocol route fails clear requirements. A bespoke messaging backend/client would multiply risk across real-time delivery, sync, attachment storage, device state, push notifications, multi-device history, abuse controls, encryption, recovery and long-term operations. Require a written reason why an existing protocol/server cannot satisfy the accepted needs before authorizing this route.

## 4. Initial recommendation for the feasibility study

Compare A and C first: use a Telegram Mini App only as a fast, bounded way to validate the information architecture and ecosystem-entry experience; evaluate a restricted, self-hosted open-protocol deployment for a genuinely independent Ameligram. Keep B only if Telegram interoperation is explicitly desired. Do not start a custom messaging stack merely to make the interface look like Telegram.

This is a recommendation for ROOT/T-COD to assess, not a technology decision, budget approval or implementation claim. No source, server, mobile app or Telegram configuration has been changed by this directive.

## 5. Minimum requested deliverable

ROOT/T-GOV should bind the existing technical/product owner to return a concise feasibility package containing:

1. Current-asset/source sweep, including recovered historical Python prototypes if they can be located; preserve them as evidence, not automatic build authority.
2. Comparison of A/B/C/D on ecosystem-only containment, identity reuse, user experience, privacy/security, operating effort, dependencies, portability, costs, and time-to-first-safe-pilot.
3. Proposed MVP user journeys and permission model: onboarding, identity linking, ecosystem selection, private spaces, announcements, messages, notification settings, report/block/moderation and account recovery.
4. Threat/privacy model, end-to-end encryption choice, backup/key recovery policy, data retention and regional/legal considerations.
5. Reuse map for existing identity, HOBO, JAM3S, IRIS, Carbon, Marketplace and Matrix integration points—without merging their authority or making unavailable capabilities appear live.
6. Recommended positioning and the first visual/audio concept, preserving Ameligram as its own experience and the supplied childlike-to-deep-voice motif for refinement.
7. Rough initial build/run cost range with assumptions, minimum owner gates, and a clear BUILD / DEFER / REJECT recommendation.
8. Acceptance tests and explicit non-interference checks proving the pilot does not change current project flows or expose unauthorized ecosystem content.

## 6. Existing product boundaries to preserve

- H0B° remains a clown/entertainment/roasting/philosophy character, never diluted into a generic assistant or converted into the Ameligram helpdesk.
- JAM3S remains the accountable identity/reputation/referral infrastructure where its existing mandate says it belongs; Ameligram must consume governed identity capability, not recreate it.
- CARBON° remains the design/creation house and may design Ameligram's visual experience, but does not become the owner of user identity, governance or messaging authority.
- AMilliMATRiX remains the governing ecosystem, not a public marketing label to force across every separate ecosystem's identity.
- Access to a paid product/capability and permission to participate are separate states. An MTX ID must not silently imply a subscription, contribution tier, payment or entitlement.

## 7. Acceptance and status

**Current state:** OWNER INTENT CAPTURED / CATEGORY B / FEASIBILITY NOT YET RETURNED.  
**No claims:** no Ameligram implementation, deployment, security proof, MTXID integration, operating cost, domain, or audio asset is claimed.

**Next action:** ROOT/T-GOV classifies and assigns the feasibility task to the existing product/technical owner, preserving all ongoing work; acceptance is the evidence-backed comparison and recommendation above, independently read back into the existing Root/Route Intake.
