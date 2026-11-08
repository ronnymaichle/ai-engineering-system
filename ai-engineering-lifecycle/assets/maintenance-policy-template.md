# Project maintenance policy

> Copy into the project's authoritative operations documentation or link it from there. Replace all placeholders. **This document does not activate jobs or grant permissions.**

## Scope and ownership

- Project / repo: `<name and location>`
- Environment(s): `<dev/staging/prod>`
- Product/service owner: `<role/person>`
- Security/incident contact: `<role/contact>`
- Budget approver: `<role/person>`
- Review/expiry date: `<date>`
- Critical user/data exposure: `<none/PII/payments/regulated/etc>`
- Risk profile: `<lean/standard/strict>` (risk, independent of cost)
- Budget profile: `<manual/scheduled-low-cost/event-driven/managed-continuous>`

## Schedules, triggers and verification

| Check or job | Why / scope | Trigger and timezone | Runner/platform | Owner | Evidence/alert destination | Max spend | Activation state |
|---|---|---|---|---|---|---|---|
| Repository health | tests/docs/CI/dependency signals | manual or weekly | local/CI | `<owner>` | `<issue/report>` | `<cap>` | `not_enabled` |
| Security advisories | vulnerable dependency notification | event-driven if supported | `<provider>` | `<owner>` | `<channel>` | `<cap>` | `not_verified` |
| Application health | service errors/availability | continuous telemetry if justified | `<provider>` | `<owner>` | `<channel>` | `<cap>` | `not_enabled` |
| Backups/restore | data recovery objectives | `<cadence>` | `<runner>` | `<owner>` | `<report>` | `<cap>` | `not_enabled` |
| AI feature evals | quality/safety/model drift | `<cadence/event>` | `<runner>` | `<owner>` | `<report>` | `<cap>` | `not_enabled` |

Allowed activation states: `not_enabled`, `configured_not_verified`, `verified_active`, `failed`, `disabled`.

## Permissions and guardrails

- Default automation privilege: `<read-only>`; write/PR permissions: `<none until explicitly approved>`.
- Allowed services and token scopes: `<minimal list; NEVER store actual secrets here>`.
- Human sign-off required: `<production deploy, destructive data, IAM/secrets, external publication, spending, high-risk fixes>`.
- Isolation and artifact/log redaction: `<rules>`.
- Change method: `<branch + PR + CI + reviewer>`.

## Cost and execution limits

- Monthly maintenance budget: `<currency amount, or zero paid AI>`.
- Per-run CI/API/agent cap: `<cap>`; AI calls/tokens/context limit: `<cap>`.
- Max concurrency and retries: `<values>`; timeout: `<duration>`.
- On budget exhaustion: `stop paid AI calls; keep deterministic read-only checks; report blocker; request approval`.
- Cost measurement source and alert threshold: `<provider + mechanism>`.
- Run record retention: `<duration>`; privacy/data minimization: `<rules>`.

## Incident and missed-run response

- Critical escalation threshold: `<risk/action/signal>`; owner response expectation: `<duration>`.
- Signals that must not wait for routine review: `<security compromise, major outage, data integrity failure, critical auth regression, etc>`.
- Failed/missed schedule detection: `<last_success + monitor + fallback/manual alert>`.
- Recovery/runbook locations: `<links>`; RTO/RPO where relevant: `<targets>`.

## Definition of a completed review

A report with source revision, time, checks actually run, tool status/evidence, new findings vs. known issues, risk and owner, AI/CI cost, unresolved blind spots, and next scheduled/manual review. `No findings` never implies zero bugs.

## Explicit approvals

- Policy approved by: `<owner / date or pending>`
- Schedule enabled by: `<owner / date or not_enabled>`
- Permission/budget change approved by: `<owner / date or pending>`
