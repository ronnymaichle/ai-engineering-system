# Workflow: on-demand or scheduled project health check

Use for "weekly checkup", "audit my app", "what bugs are new?" and similar. Never claim you can continuously watch the repo unless an actual authorized automation exists.

1. **Load policy and baseline:** read current project maintenance policy and last report, owner, repo revision, last successful checks, issues/PRs, allowed tools, per-run budget and mode (`manual` or `scheduled`). If absent, default to read-only on-demand assessment and propose a policy.
2. **Run cheap evidence first:** existing tests/linters/type check/security tools, Git status, CI outcomes and dependency advisories **only when available and permitted**. Start with `python3 scripts/repo_health.py --root <repo>` if this package is installed. That utility is metadata-only, not a bug/vulnerability scanner.
3. **Check live signals if connected:** errors/SLOs/alerts, API failures, background queues, backups/restore status, cost anomalies and incidents. If not connected, say `not_checked` rather than marking healthy.
4. **Review AI components as needed:** provider/model/tool version changes, eval regression, privacy/safety behavior, tool permission drift, prompt-injection exposure, budget overrun. Do not export private logs to a model without authorization.
5. **Deduplicate and triage:** distinguish new vs known issues, observable failures vs inferred risks, exploitability/customer impact, remediation effort, owner, required response time.
6. **Selective AI diagnosis:** only if evidence is nontrivial and budget permits. Narrow code search, generate a reproducible hypothesis and test plan; independent review for high-impact changes.
7. **Propose or implement fix based on authority:** report-only default. If explicitly enabled, create scoped branch/PR with code/tests and reviewer; no auto-merge or production patching.
8. **Generate report:** `assets/maintenance-report-template.md` including checks actually run, evidence, untested domains, cost, failure/missed run status, issues, owner and next check.
9. **Improve the check itself:** measure alert quality, false positives, coverage gaps, CI minutes, AI spend and missed scheduler executions. Adjust only with authorized change control.

### Critical escalation

Suspected data breach, active exploitation, auth bypass, irreversible data loss or material production outage → stop regular backlog batching; invoke incident response and notify accountable owner promptly. A weekly cadence never justifies waiting for the next review.

### Truthful result states

`healthy_for_checks_run` means no relevant problem found by the **checks actually executed**, not the app has zero bugs. `not_checked`/`blocked` must remain visible for missing telemetry, scanners or providers.
