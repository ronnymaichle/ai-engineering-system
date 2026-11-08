# Workflow: improve AI engineering capabilities (phase 0 → 8, and 3/5 as needed)

1. **Specify the pain:** repeated task failures, high context cost, unsafe autonomy, tool errors, poor routing, stale docs, low-quality agent review, excessive token spend, slow CI, incompatible providers.
2. **Measure baseline:** representative cases, observed time/cost, false positives, success rate, security/permission findings, human review burden. Collect only privacy-permitted telemetry.
3. **Inventory existing capability owners:** skills, agents, hooks, deterministic tests, tool integrations, model routers, runtime scheduler, project policies, Scoutfold Kit if relevant. Don't duplicate roles.
4. **Choose component:** skill change for reusable procedure; harness for real execution enforcement, persisted state or scheduling; tool for deterministic external function; agent for bounded independent analysis; policy/CI for mandatory checks.
5. **Compare options:** reuse/configure/refactor vs create, cost, reliability, maintenance, exposure, portability, migration and rollback. Use small reversible trials for uncertain tools/models.
6. **Propose scoped change:** interfaces, activation, permissions, inputs/outputs, owner, error states, compatibility and regression tests.
7. **Implement only within current authority:** do not grant tool rights, expand secrets, install new paid providers or publish a new skill version without explicit approval.
8. **Evaluate:** rerun baseline+edge scenarios; check correctness, cost, latency, safety, context integrity and tool-use traces. Record regressions, unresolved risk and next measurement.
9. **Ownership rule:** if the requested change affects this `ai-engineering-lifecycle` skill package, output a proposal using `references/maintainer-handoff.md` for the user's **separate future maintainer skill**. Do not impersonate it. If it affects Scaffold Kit, hand off to `scaffold-kit-maintainer` where available.

**Output:** evidence, component decision, minimal change, migration/eval plan, owner and expected measurable benefit.
