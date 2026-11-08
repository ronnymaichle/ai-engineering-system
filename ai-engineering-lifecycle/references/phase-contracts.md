# Adaptive lifecycle — phase contracts

Use only applicable phases. Phase 0 always routes; phases 1–8 are selectable. Each phase has **trigger → minimum inputs → deliverables → exit evidence → maintenance consideration**. A phase may be `not_applicable`; revisiting is normal.

## Phase 0 — Triage, classification and routing

- **Trigger:** every engineering request.
- **Inputs:** user objective, actual environment, available tools/skills, budget, risk and permissions.
- **Deliverable:** selected phase(s), capability strategy (skill/agent/tool/harness), expected artifacts, constraints and verification.
- **Exit:** sufficient evidence to proceed or explicit blocker; unverified unknowns labeled.
- **Maintenance:** identify whether the task changes ongoing operational/support obligations.

## Phase 1 — Product discovery and requirements

- **Trigger:** new ideas, unclear requirements, changing business rules or product scope.
- **Inputs:** stakeholders/users, desired outcomes, current pain, existing behavior, legal/privacy needs, budget and success measures.
- **Deliverables:** MVP/out-of-scope boundaries, functional/nonfunctional requirements, edge cases, user journeys and acceptance criteria; priority and traceability for substantial work.
- **Exit:** objectively testable acceptance criteria and known assumptions; obtain stakeholder agreement where necessary, never fabricate it.
- **Maintenance:** support ownership, expected availability, anticipated operational cost, accessibility/i18n needs and end-of-life consideration.

## Phase 2 — Architecture, domain, threat model

- **Trigger:** foundational or meaningful architectural change; new components, integrations or failure/security boundaries.
- **Inputs:** validated requirements, existing architecture, workload, data/access classification, deployment constraints.
- **Deliverables:** domain model/bounded contexts only where needed; app/API/data/infrastructure design; dependency decisions, interfaces, threat model, alternatives and ADR for significant choices.
- **Exit:** design has a practical test and recovery strategy, explicit trade-offs, and approval of any high-impact change.
- **Maintenance:** identify observability signals, backups, migrations, rollback, resource ownership and projected review cadence.

## Phase 3 — Engineering foundation

- **Trigger:** new repo, missing guardrails, workflow automation or harness/tool integration.
- **Inputs:** design, repository inventory, platform and team preferences; permissions.
- **Deliverables:** appropriate scaffold/project config; tests and CI, branch protections, secrets patterns, docs, harness boundaries, tool availability, maintenance policy. Prefer Scaffold Kit's actual project setup when installed.
- **Exit:** locally executed checks where possible, traceable config and explicit `not_enabled` for inactive external services.
- **Maintenance:** owner, schedule proposal, alert routing and cost cap exist before production release.

## Phase 4 — Implementation and integration

- **Trigger:** approved functional change, bug fix, refactor or migration.
- **Inputs:** acceptance criteria, relevant code graph, interfaces, tests, permissions, design constraints.
- **Deliverables:** scoped diff, tests, necessary documentation, migration/recovery steps, known limitations.
- **Exit:** implementation checks executed or blocked with evidence; no surprise unrelated refactor.
- **Maintenance:** update ownership, runbooks, error alerts, dependency inventory and future operational costs when affected.

## Phase 5 — Verification and independent scrutiny

- **Trigger:** meaningful code/config/skill change or release candidate.
- **Inputs:** stated requirements, change diff, risk, test strategy, available tools.
- **Deliverables:** test results and evidence; correctness, authorization, safety, performance, accessibility/i18n, data integrity, regression and security findings as applicable; independent review for high-impact work.
- **Exit:** verified pass or documented failure/exception approved by the right person; never equate scans with security guarantees.
- **Maintenance:** can the necessary checks recur automatically or on a low-cost schedule?

## Phase 6 — Release and transition

- **Trigger:** deployment, publication, schema migration, enabling an automation or changing live user behavior.
- **Inputs:** verified candidate, changelog, approvals, environment/config, backout plan, observability.
- **Deliverables:** release checklist, approvals, compatibility and migration safety, deployment evidence, post-release checks, rollback or roll-forward decision.
- **Exit:** actual deployment verification or explicit `not_deployed`; operational handoff completed.
- **Maintenance:** live monitoring ownership, incident response, recovery targets, schedulers and budgets confirmed; do not activate unapproved costs.

## Phase 7 — Operations and project maintenance

- **Trigger:** running service, operational incident, scheduled/manual review, recurring security or reliability signals.
- **Inputs:** operational telemetry, maintenance policy, source revision, alerts, CI outcomes, budgets and permissions.
- **Deliverables:** prioritized findings, reproducible failures, issue/PR proposals, verified fixes, support/recovery actions, risk and cost trends.
- **Exit:** measurable service state and follow-up ownership; no claim of perfect coverage.
- **Maintenance:** continuous as **policy**, not magically as a running process; actual schedule/service must be configured and checked for missed runs.

## Phase 8 — Engineering system evolution

- **Trigger:** accumulated debt, repeated failures, new technology, changes in model/tool behavior, capability overlap, cost trends, postmortems, evaluation regressions.
- **Inputs:** failure records, actual outcomes, user feedback, skill/tool inventory, version and budget data.
- **Deliverables:** evidence-based improvements; ADRs, migration/deprecation plans, cost/benefit, regression scenarios and new owners.
- **Exit:** tests/evals support the selected change, or a clearly scoped proposal remains pending approval.
- **Maintenance:** improve project engineering procedures. **Changes to this skill package itself go to its separate maintainer** (not bundled here).

## Cross-cutting invariant

All phases apply proportionate security/privacy, traceability, system reliability, cost governance, context consistency, human approval for sensitive actions, and `evidence-before-claim` rules. Never require all possible artifacts for a simple change.
