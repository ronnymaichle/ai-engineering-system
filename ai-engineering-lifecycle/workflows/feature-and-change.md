# Workflow: feature, refactor or integration

1. **Route:** identify business goal, affected users and acceptance criteria; classify change as local, cross-cutting or high-risk. A feature should not force full project rescheduling.
2. **Read the code:** inspect existing implementations, symbols, public contracts, tests, integration calls, config and documented constraints; estimate blast radius. Do not build a new architecture if current one is fit.
3. **Design minimum change:** files to modify, approach, data/API compatibility, error/failure states and tests. Consider security, privacy, accessibility, localization and performance only where implicated.
4. **Select collaborators:** existing skills/tools; agent investigator or independent reviewer only if worthwhile. Prevent multiple agents from editing the same files concurrently.
5. **Implement:** focused code changes, regression/unit/integration/contract tests, safe migrations and docs/runbook updates. Preserve existing conventions.
6. **Validate:** run relevant checks; if blocked, disclose and keep status `blocked` or `not_tested`. Independent review required by risk/organization rather than for every trivial edit.
7. **Decide release/maintenance:** specify deployment impact, feature flag/rollback if relevant, telemetry, support owner and future check adjustments. Do not deploy without authorization.

**Output:** implementation summary, diff/test evidence, unresolved risk and project maintenance implications. **Avoid:** broad unrequested refactoring and new skills for a one-time feature.
