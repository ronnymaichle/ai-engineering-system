# Behavioral evaluation scenarios

`scenarios.json` contains 20 **unexecuted** evaluation fixtures. Each gives a user request, expected phase selection and decision, and positive/negative behavioral assertions. They are not proof of agent quality.

## Recommended evaluation protocol

1. Install this skill in the actual target platform. Compare baseline (without this skill or previous version) with candidate version; hold model/runtime and tools constant when possible.
2. For each fixture, feed only the `request` and realistic relevant environment context. Ask the agent to respond or perform a dry run within a controlled test repository.
3. Score requested items: selected phases, chosen component ownership, factual accuracy, security/approval boundaries, maintenance budget and evidence status. Evaluate `must_do` and `must_not` manually or with an independently validated rubric.
4. Add tests for tool failures, missing network, sensitive data, oversized codebase, conflicting repo instructions, outdated model, cost exhaustion, inactive schedule and permission denial.
5. Record successes/failures, token/cost/latency, test evidence, reviewer decision and regression from baseline; do not mark scenarios passed just because JSON validates.
6. Test multiple model tiers and different real repositories before claiming portable reliability, if target platform and budget permit. Record exact versions and limitations.

New failures should become reproducible fixtures with an accountable owner. Updates to this evaluation suite itself are owned by the **separate lifecycle skill maintainer**.
