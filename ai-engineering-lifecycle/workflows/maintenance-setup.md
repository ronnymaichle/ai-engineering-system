# Workflow: configure budget-aware project maintenance

## Step 1 — project inventory and risk

Assess deployed status, repo host/plan, CI, cloud/hosting, dependencies, data sensitivity, user impact, criticality, uptime expectations, existing telemetry, backup/restore and current alerts. Identify human owner and the user's **maximum monthly and per-checkup spend**. A zero-paid-AI budget is a valid target.

## Step 2 — choose controls and cadence

Compare manual, scheduled CI, security/event-triggered checks, backend scheduled workers, managed schedulers or an always-on monitoring service. Match actual need rather than selecting the most autonomous. Distinguish:

- **Repository/code maintenance:** test failures, security/dependency alerts, outdated docs/ADR/debt, agent/model eval regression. Often CI/manual jobs.
- **Application maintenance tasks:** queue retries, TTL deletion, aggregation, integrity/cleanup, recurring integrations. Often audited app workers/managed scheduler with idempotency/locking.
- **Production incident detection:** availability/errors/security signals requiring prompt alerts and accountable on-call response. Do **not** replace with weekly AI report.

Configure each check with `name, owner, trigger/cadence/timezone, inputs, tool permissions, expected outputs, severity, response owner, expiry, budget cap, notification route, retry limit, missed-run signal, evidence retention`.

## Step 3 — cost and permission design

Estimate: CI minutes × runner price + AI calls × measured tokens and current provider pricing + storage/egress + third-party APIs + alerts + human review. Model per-task budget caps, cost alerts, tool rate limits and a deterministic fallback. Keep read-only jobs at minimal repo permissions. Proposed PR-writing automation must require opt-in, a scoped credential, independent tests and protected-branch review. No direct autonomous prod fixes.

## Step 4 — deliver configuration and approval request

Populate `assets/maintenance-policy-template.md`; if suitable provide *reviewable* `examples/weekly-maintenance.yml` and `scripts/repo_health.py`, which provide only a deterministic repo check. Do not claim security scanners, AI agents, notifications or live scheduled jobs exist without installing/configuring them. Prefer existing project CI rather than duplicate CI files. Request approval for installation, external access, tokens, paid jobs and alerting.

## Step 5 — verify active automation

Once explicitly authorized and installed, verify scheduler status, default branch, first successful run, artifact/alerts, failed-run notification and budget. Test at least one controlled failure path where safe. If no scheduler tools/access: give exact next steps and mark state `not_enabled`.

## Step 6 — operational handoff

Owner, backups/incident runbooks, review interval, severity response, budget/alerts, retention and review/retirement date. The existence of a workflow file is not proof that a scheduled job ran. Report exact activation state.
