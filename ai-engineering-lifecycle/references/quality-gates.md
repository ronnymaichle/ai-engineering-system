# Measurable, evidence-based quality gates

Apply gates **based on risk and task**, not as a ceremonial checklist. Establish measurable applicability, check, evidence, owner, pass/fail/conditional status, exception authority and review date. An unexecuted gate is never marked passed.

## Status vocabulary

- `verified`: required checks ran and passed, with commands, outputs or comparable traceable evidence.
- `partially_verified`: some checks ran; gaps and impact are stated.
- `not_tested`: relevant check was not executed.
- `failed`: relevant check executed and failed; include reason or trace.
- `blocked`: the required check cannot be executed with current access/tools; include missing dependency.
- `not_applicable`: gate excluded with an explicit reason.

## Gate map

| Gate | Typical evidence | Who decides |
|---|---|---|
| Requirements | testable acceptance criteria, agreed scope, explicit assumptions | product owner as applicable |
| Architecture | ADR, dependency/data-flow impact, capacity/trade-offs | technical owner |
| Security/privacy | threat-model changes, auth tests, secret/dependency findings, accepted residual risk | authorized security/project owner |
| Implementation | diff review, types/lint, tests, docs, migration safety | implementation owner plus reviewer as appropriate |
| Verification | unit/integration/contract/E2E/regression evidence, independent review for material risk | reviewer/CI |
| Performance/reliability | representative workload measurements, budgets/SLOs, recovery behavior | service owner |
| UX/accessibility/i18n | critical user journey tests, keyboard/reader/locale tests | product/UX owner where relevant |
| Release | CI status, change record, staging/smoke checks, approvals, rollback, health checks | release owner |
| Operations | support owner, dashboards/alerts, runbooks, backup restore evidence, maintenance policy | service owner |
| Costs | estimated recurring cost, actual cost and limits/alerts, funding approval | budget owner |
| Closure | results, limitations, accepted risks, deferred work and next responsible person | task owner |

A conditional pass needs the residual failure, accountable approver, expiry and follow-up. Only that approver can accept the exception; AI review is not human authorization.

## Test strategy

Select tests by failure impact and code change: unit tests for algorithms/business invariants; integration for I/O; contracts for public APIs; E2E for essential journeys; security for privilege boundaries; performance tests for high-load paths; resilience/failover/restore checks for important services. Consider property-based, mutation and fuzz testing when it improves detection. Track flaky tests and defects that escape production rather than optimizing coverage percentage alone.

## Evidence format

```
Gate: verification
Status: partially_verified
Scope: login flow and session revocation
Observed: `npm run test:auth` (pass, 142 cases), `npm run typecheck` (pass)
Not run: browser E2E (CI unavailable)
Risk: cookie behavior not independently checked in browser
Owner: application team
Next action: run E2E in PR CI before merge
```

Replace example commands with commands actually executed. Never reuse this example as evidence for real work.

## Model/skill quality gates

For skill/agent changes, test: correct routing, no duplicate skill generation, tool/permission boundaries, cost behavior, handling of malformed inputs, partial failures, budget exhaustion, stale context, unsafe proposals, independent review and structured output conformance. Preserve baseline metrics and compare before/after on the same scenarios; `evals/scenarios.json` provides an initial fixture set, not completed performance results.
