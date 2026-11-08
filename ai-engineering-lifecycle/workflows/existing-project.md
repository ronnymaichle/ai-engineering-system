# Workflow: existing repository, assessment and upgrade

1. **Inventory without changing:** repo/branch/status, instructions, stack/lockfile, build/tests, CI hooks, deployed environments, database/API contracts, docs, source folders, security status, maintenance policies and existing skills/tools.
2. **Assess project reality:** purpose, currently working features, critical user journeys, open incidents and technical debt. Use language-aware navigation and dependency/impact analysis, not only README claims.
3. **Compare to risk-based baseline:** requirements, architecture, auth/privacy, tests, CI, deployment, backup/restore, observability, costs, agent/tool guardrails and scheduling. Mark `present/partially_present/missing/not_applicable/not_verified` and evidence per item.
4. **Choose strategy:** targeted remediation, Scaffold Kit **upgrade mode** if appropriate, migration to supported stack or minimal policies. Never scaffold over existing code. Preserve app behavior and customized conventions.
5. **Rank gaps:** severity × likelihood × operational/user impact, then effort and cost. Separate immediate security/reliability issues from optional engineering quality improvements.
6. **Propose safe increments:** small branches/PRs, first tests to lock behavior, idempotent migrations, rollback points and compatibility. Request approval for config rewrite, paid services, production changes or large refactors.
7. **Execute agreed increments:** don't combine all upgrades into one risky batch. Use existing tools and Scaffold Kit's own scripts only if present and reviewed.
8. **Verify and report:** exact commands, outcomes, docs/ADR updates, remaining risks and next recommended iteration; design/adjust maintenance policy.

**Output:** evidence-based gap matrix, ordered migration plan, verification report, project maintenance owner/cadence. **Avoid:** generic 100-point audits disconnected from actual repository, automatically creating duplicate docs, or asserting a vulnerability exists without scanner/proof.
