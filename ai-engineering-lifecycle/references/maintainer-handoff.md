# Interface to the separate lifecycle-skill maintainer (not included)

The user intends to build a **distinct maintainer skill** for `ai-engineering-lifecycle`. Do not create one here, install an imagined agent, or claim it is running. This document is a **handoff contract** for that future component.

## Ownership distinction

- **This skill**: project lifecycle planning and execution routing; proactive design of app maintenance; sanctioned checkups of codebase, infrastructure, security and AI features; evidence-based recommendations.
- **Future maintainer skill**: review, improve, test, version and release **this skill package** (`SKILL.md`, `references/`, `workflows/`, `assets/`, `examples/`, `scripts/`, `evals/`, `tests/`).
- **Scaffold Kit maintainer**: maintains the separate scaffold-kit repository and its two skills.

## Proposed handoff schema

When a change to **this package** is desired, produce a handoff with:

```yaml
handoff_kind: lifecycle_skill_change_proposal
package: ai-engineering-lifecycle
observed_version: 1.0.0
request: "..."
reason_and_evidence: "..."
source_paths: ["..."]
impact: ["activation", "workflow", "policy", "security", "cost", "platform", "eval"]
risk: low # low | moderate | high
breaking_change: false
expected_behavior: "..."
regression_scenarios: ["..."]
requested_tests: ["scripts/validate_skill.py", "tests/"]
user_approval: pending # pending | granted | denied
proposed_version_bump: minor # patch | minor | major
migration_and_rollback: "..."
```

This is an example **schema**, not a claim that a maintainer accepted or executed it. Redact private project information and secrets from handoffs.

## Suggested maintainer quality/release policy

- Read current source and user intent; classify whether the issue is project maintenance versus skill maintenance.
- Own one authoritative file for each rule; avoid circular references or conflicting ownership with Scaffold Kit.
- Update behavior and evaluation fixtures together; run structural checks plus **model/runtime-based** scenario tests.
- Use PR/review, semver and changelog; check frontmatter compatibility, links, scripts, permissions and documentation.
- Use migration notes, explicit breakage flags and rollback steps for changed activation, contracts or tool requirements.
- Never self-approve risky external actions; no automatic release/publication by default.

## Minimum acceptance criteria for future maintainer

1. Can handle a user request like "Improve the lifecycle skill's routing when a project has no CI" without modifying unrelated application code.
2. Can identify its own repo files, compare baseline scenarios and add regressions.
3. Can distinguish this package from Scaffold Kit and its dedicated maintainer.
4. Can propose an audited version bump, changelog, migration and rollback with evidence.
5. Can hand control back without making an unapproved release.
