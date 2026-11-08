# Continuous maintenance engine — software projects, not this skill's source

This policy is **cross-cutting** Phases 1–8. During design, determine how the eventual product will be maintained; during foundation/release, configure checks with authorization; during operations, run and verify; during evolution, assess outcomes and improve. **The user will create a separate maintainer skill to update this lifecycle skill's own source.** Do not conflate these owners.

## Core maintenance contract

Every substantial project should define:

- **Owner(s):** responsible engineer/team, escalation contact, budget approver and secondary owner where necessary.
- **Assets:** source code, test/build pipelines, dependencies/supply chain, data/privacy, auth/IAM/secrets, APIs, infrastructure, deployment, backups, observability, documentation, and project-specific AI features/agents/models.
- **Review cadence:** manual, scheduled, event-driven or continuously monitored; per-domain severity overrides routine cadence.
- **Signals:** actual CI failures, tests, SCA/vulnerabilities, errors/SLIs, user reports, service status, billing/usage alerts, data integrity, backup restore evidence, provider/model changes, stale docs and change risk.
- **Response:** detect → triage → prioritize → reproduce/diagnose → propose → verify → authorize → apply → observe → document/learn.
- **Authority:** read-only by default; PR proposals only with repository authorization; changes to production, IAM, secrets, sensitive data and budgets require a designated approver.
- **Evidence:** run identifier, date, source revision, tools/scans actually executed, findings by severity, owner, costs, check status, issue/PR references and next planned action.
- **Limits:** expected spend, per-execution caps, concurrency, rate limits, timeout, token ceilings, retries, notifications, retention and safe stop conditions.

Do not promise an agent will *always* find new bugs. No maintenance schedule can prove absence of vulnerabilities, defects or regressions. Continuous monitoring and event alerting complement—do not replace—scheduled reviews.

## Select the cheapest sufficient delivery mechanism

| Mechanism | Use when | Trade-offs / guardrail |
|---|---|---|
| **Manual review** | hobby/personal/limited budget, non-critical | no recurring job; human must trigger, record last review; critical security alerts need separate owner |
| **Scheduled CI (weekly/monthly)** | repository health, dependency/status summary, tests with modest runtime | good low-cost baseline; jobs may be delayed/missed; no persistent runtime, no always-on protection |
| **Event-driven** | failed CI, dependency advisory, error-rate spike, incident, SLA breach | faster triage, fewer periodic AI calls; deduplicate and rate-limit alerts |
| **Backend cron/queue worker** | app maintenance tasks like cleanup, cache, synchronization, data validation | use idempotency, lease/locking, checkpointing, concurrency/timeout budgets; never let LLM choose dangerous prod queries autonomously |
| **Managed scheduled service** | reliable recurring operations across multiple apps, audited ownership | provider fees, permissions, monitoring; enforce least privilege and runbook |
| **Always-on telemetry/on-call** | material uptime/data integrity requirements | staffed response and reliable alerts; not equivalent to running an AI agent continuously |
| **AI-assisted periodic analysis** | many nontrivial findings need interpretation, issue synthesis, code impact and proposed PRs | read-only first, selective invocation, cost limits and reviewed changes; do not send secrets/log PII to model |

Avoid default Kubernetes, microservices, persistent AI workers or large paid SaaS subscriptions. Compare current hosting, Git provider features and operational simplicity. Account for CI minutes/storage, paid API calls, AI tokens, inference latency, human review and alert fatigue. Quote costs only when checked against current pricing/plan.

## Budget-first tier examples (not fixed prices)

- **Lean/manual:** developer runs a manual weekly or monthly checklist and local tests; repository security advisories if available. AI only on demand. Report gaps; keep a next-review reminder outside the skill only when authorized.
- **Standard/weekly:** limited scheduled CI metadata/test summary; dependency alerts; AI triggered on meaningful failures or review requests; open issues/PRs only with permission; cap calls and time.
- **Strict or operationally critical:** event/telemetry-based incident alerts, more frequent verification, periodic restore exercises, independent security/release review; use dedicated scheduling/on-call based on actual risk, not an arbitrary subscription.

**Rigor and spending are separate axes.** A sensitive low-budget project may require stronger controls or reduced scope rather than quietly skipping security requirements.

## Maintenance check domains and frequency guidance

| Area | Cheap default | Escalation trigger |
|---|---|---|
| Regression/code | CI on changes + periodic critical journey tests | failed CI, crash, customer impact |
| Dependencies/supply chain | version alerts/lockfile review | exploited vulnerability or package compromise |
| Security/privacy/IAM | PR checks and periodic access review | leak, auth bypass, new exposure |
| Data and database | integrity checks, migration safety, backups | integrity alert, failed restore, replication lag |
| Infrastructure | health/resource/backup signal checks | saturation, security misconfiguration, downtime |
| API/clients | compatibility and contract monitoring | broken consumer, unexpected provider change |
| UX/i18n/a11y | critical journey checks following changes | high-impact usability/accessibility defect |
| AI features/agents | eval regression, model/tool version tracking, prompt-injection tests | provider deprecation, safety/quality regression |
| Docs/debt/cost | periodic backlog/doc drift and budget review | stale runbook, cost alert, repeated failures |

## Operational safety controls

1. **Install is not activation:** ask for approval before creating/enabling schedules, credentials, notifications, paid APIs or deployments. Generate configuration for review when lacking access.
2. **Minimum permissions:** scheduled read-only jobs get `contents: read`; no write token by default. AI suggestion jobs cannot force push, merge, change branch rules or deploy.
3. **Untrusted CI events:** don't expose high-privilege secrets to untrusted pull requests. No direct execution of arbitrary code generated by an LLM without review.
4. **Idempotent jobs:** stable run IDs, de-duplication, concurrency limits, retry backoff and dead-letter/failure state if needed; avoid conflicting writers.
5. **Detect missed runs:** track expected/actual run timestamps and scheduler health. GitHub Actions schedules run on the default branch and can be delayed or disabled; do not treat their existence as continuous monitoring.
6. **Privacy:** filter logs and artifacts, use retention policies, minimize external model/tool transfers; access only relevant project data.
7. **Budget stop:** hard/soft thresholds, API/agent quotas, alert on overruns, terminate gracefully before further calls; retain a deterministic read-only fallback.
8. **Validation before changes:** reproduce in appropriate environment; tests/authorization/regression; submit PR with risk and rollback. Human approves high-impact changes.
9. **Audit:** keep findings, severity, evidence, accepted risks, owners and follow-up; do not mark `fixed` until independently verified.
10. **Exception management:** reason, approving person, expiration and review trigger; no indefinite silent deferment of critical issues.

## Example weekly lifecycle

- Monday schedule (or manual request) starts read-only repository check, basic tests/status, dependency-alert review if access permits, plus current error/incident signals when connected.
- A deterministic policy filters duplicate/known findings, chooses severity and checks per-run budget.
- Optionally invoke AI to interpret *sanitized* findings, narrow code impact and draft a plan. Use specialized agents for significant security/reliability cases, not by default.
- Produce a report with **verified** evidence, unknowns, prioritized changes, owners and no-change result when healthy.
- If allowed, create a branch/PR with a scoped fix, tests and rollback note. **Never auto-merge or auto-deploy a generated fix by default.**
- Evaluate whether the check itself ran on time and provided value; tune cadence, sources and spending.

## Critical distinction

Project AI components and their behavior **are** reviewed under this policy. The **source of this orchestration skill** is maintained only by the separate future maintainer skill and released through a distinct process. See `references/maintainer-handoff.md`.
