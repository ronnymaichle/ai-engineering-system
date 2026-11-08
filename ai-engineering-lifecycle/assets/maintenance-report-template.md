# Project maintenance checkup — `<project>`

- Run ID: `<id>`
- Started (UTC/timezone): `<timestamp>`
- Mode: `<manual/scheduled/event>`
- Repo and revision: `<repo + commit>`
- Maintenance policy: `<path + version>`
- Operator/agent/tools: `<names + versions>`
- Status: `<verified/partially_verified/not_tested/failed/blocked>`
- Last successful scheduled run: `<timestamp or unknown>`
- Spend: `<CI minutes / AI tokens or calls / cost; unknown if not measured>`

## Executive result

`healthy_for_checks_run` / `findings` / `incomplete` / `incident_escalated`.

## Evidence table

| Domain | Check/tool | Command or source | State | Evidence and limits |
|---|---|---|---|---|
| Tests | `<...>` | `<...>` | `not_tested` | `<...>` |
| CI/build | `<...>` | `<...>` | `not_tested` | `<...>` |
| Dependencies | `<...>` | `<...>` | `not_tested` | `<...>` |
| Security/privacy | `<...>` | `<...>` | `not_tested` | `<...>` |
| Runtime/infra | `<...>` | `<...>` | `not_tested` | `<...>` |
| Database/backup | `<...>` | `<...>` | `not_tested` | `<...>` |
| API/integration | `<...>` | `<...>` | `not_tested` | `<...>` |
| AI components | `<...>` | `<...>` | `not_tested` | `<...>` |
| Docs/debt/cost | `<...>` | `<...>` | `not_tested` | `<...>` |

## Findings and actions

| ID | Evidence | New/known | Severity | Impact and recommended change | Owner | Issue/PR | Due/review |
|---|---|---|---|---|---|---|---|
| `<...>` | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` | `<...>` |

## Escalations / approvals / risks

- Critical escalations: `<none or authorized recipient and status>`
- Changes proposed or performed: `<include tests and PR; no fabricated actions>`
- Open/accepted risks: `<owner, date and expiry>`
- Checks not run and why: `<explicit blind spots>`
- Scheduler and notification health: `<observed or not_verified>`
- Next review trigger and owner: `<...>`
