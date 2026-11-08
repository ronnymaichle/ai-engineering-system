# Engineering capability registry

> Use only once an ecosystem has enough skills/agents/tools to justify a registry. One owner per capability; the actual platform/tool state remains authoritative.

| Name | Kind (skill/agent/tool/harness/hook/CI) | Purpose and activation | Input/output contract | Owner/version | Permission boundary | Dependencies | Evidence/evals | Deprecation/retirement |
|---|---|---|---|---|---|---|---|---|
| `scaffold-project` | skill | new repo or upgrade foundation | repo and choices → project-local scripts/docs | Scaffold Kit / `<observed tag>` | approved project writes | `scaffold-kit` | kit's tests | review on major changes |
| `ai-engineering-lifecycle` | skill | phase routing, engineering coordination | objective/context → decision/plan/verification | separate lifecycle maintainer / `1.0.0` | no inherent runtime permissions | current agent runtime | scenarios + reports | replace on audited successor |

If a capability is unavailable, do not mark it installed or active because it appears in this example.
