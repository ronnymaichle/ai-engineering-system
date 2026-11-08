# Workflow: new project (phases 0 → 1 → 2 → 3 → 4/5/6 as authorized)

1. **Identify outcome.** Describe the problem, users, success measure, budget, team skill, deployment target and earliest useful scope. Capture age/PII, payments, public content and accessibility/locale requirements when relevant.
2. **Define MVP.** Requirements with testable acceptance criteria, constraints, assumptions, outside-scope list and change-management owner. For unclear product needs, resolve only material blockers.
3. **Choose architecture.** Recommend the simplest fitting application, API, data/auth, deployment and observability stack. Evaluate security, scale, availability, recovery, vendor lock-in, compatibility, maintenance overhead and estimated cost; research live pricing/versions when possible. Generate an ADR for consequential choices.
4. **Maintenance-by-design.** Decide operational owner, basic health metrics, alert thresholds, incident contact, backups/restore RTO/RPO if needed, security alerts, scheduled/manual checkup cadence, AI usage budget and release rollback.
5. **Choose foundation capability.** If installed, invoke `scaffold-project` from Scaffold Kit for its step-by-step project setup and vetted templates. Respect its profile/mode and existing user preferences. Do not silently overwrite files, clone unreviewed code or pretend its scripts ran when absent.
6. **Implement an end-to-end thin slice.** Prefer validated vertical slice and tests over a massive speculative scaffold. Use only approved credentials and infrastructure.
7. **Verify.** Code/tests/CI/security/UX/contract/docs checks relevant to scope. Report executed vs. pending.
8. **Release only with authorization.** Stage/migrate/monitor/rollback and confirm actual health before calling it released. A new project can stop after architecture/foundation when that is the user request.
9. **Handoff.** Create/update a short maintenance policy with owner, cadence, trigger, budget, approval and review date; store where the project already owns operations docs.

**Outputs:** scoped requirements, architecture decision(s), populated repo if authorized, actual validation evidence, release status and project maintenance policy. **Avoid:** designing Kubernetes/microservices/sharding for speculative traffic, new skills for normal app capabilities, or pretending a schedule exists because it was proposed.
