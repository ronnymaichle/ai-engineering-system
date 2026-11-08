# Workflow: incident investigation and hotfix

1. **Triage first:** what is affected, customer/data/security consequences, urgency, incident owner and whether containment is needed. For potential active security incidents, use the approved security response route and protect evidence.
2. **Observe:** gather authorized metrics, logs and recent changes. Redact secrets/PII. Separate symptoms, confirmed facts and hypotheses; do not browse sensitive production data without approval.
3. **Bound scope:** reproduce in safe environment, identify triggering conditions and impacted components using evidence; consider recent deploy, dependency or infrastructure changes.
4. **Select mitigation:** rollback/feature-disable/traffic management or smallest safe fix; decide with authorized operational owner. Destructive operations and production access require approval.
5. **Implement and verify:** regression test for observed defect, tests for downstream impact, security/auth checks if relevant, staging/smoke check and documented rollback path. No blind production changes.
6. **Review release:** emergency process may be expedited but not self-approved by AI. Monitor actual service state after action and record unknowns.
7. **Postmortem and preventive maintenance:** detection gap, root causes (if demonstrable), safeguards, test/alert changes, ownership and recurrence evaluation. Feed Phase 8 as appropriate.

**Output:** impact, timeline of **verified** evidence, root-cause confidence, mitigation/fix status, tested behavior, follow-up owner, prevention plan.
