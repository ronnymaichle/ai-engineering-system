# Workflow: release, change of live environment or enabling automation

1. Confirm requested target, authorization, accountable release owner, environments, source revision, version and release window.
2. Check requirements and acceptance criteria, CI status, security/privacy, tests, migration compatibility, artifact/dependency integrity and applicable quality gates.
3. Prepare rollout plan: configuration/secrets/IAM impact, data backup/restore checks when relevant, canary/blue-green or straightforward rollout based on real risk, and alert thresholds.
4. Prepare **rollback or roll-forward** path, database migration compatibility, feature flags, expected user changes, communications and support ownership.
5. Request explicit go/no-go authorization for production or public publication. Agent must not approve itself. Record any accepted exceptions and approvers.
6. Execute only permitted deployment actions; verify actual health using endpoints/metrics/logs and essential user journeys; observe for regressions.
7. Report `deployed`, `not_deployed`, `failed` or `blocked` with evidence; never claim release solely because build or test passed.
8. Handoff to operations: on-call/support contact, runbooks, monitoring, maintenance schedule/status, security alerts, known issues, projected ongoing costs and next review.

Note: Creating a GitHub Actions workflow file does **not** guarantee that the schedule is active. Confirm default branch, permissions, repo settings, notification route, and an observed successful run after enabling it.
