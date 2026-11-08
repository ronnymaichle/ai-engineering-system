# Phase 0 — Triage and decision engine

Read when deciding how to solve an engineering request. Routing is adaptive and can revisit previous phases. Never infer platform permissions from user requests alone.

## Preflight (proportionate to task)

1. **Understand:** goal, desired artifact, constraints, user impact, delivery deadline, risk and definition of done.
2. **Inspect available context:** repo root and status; `CLAUDE.md`/`AGENTS.md` or equivalent; framework/language/dependencies; tests; CI; deployment/observability; project-specific governance; skills, tools, services and agents actually available.
3. **Classify repository:** new, established, legacy, regulated/sensitive, or unknown; decide if a feature is local or architectural.
4. **Assess:** data sensitivity, user exposure, external effects, operational criticality, reversibility, security impact, failure consequences, team capacity and monthly/per-run budget.
5. **Determine authority:** read-only analysis, code changes in a branch, creating PRs, changing CI, changing infra, deploying. Never silently infer approval to publish, spend or deploy.
6. **Select route:** minimal applicable phases, capability owners, quality gates and evidence.
7. **Record gaps:** facts unknown/unavailable and whether they block work; ask at most the questions truly needed, otherwise use explicit defaults and proceed with reversible work.

## Capability selection hierarchy

Prefer in this order **when it solves the problem**: existing project behavior/configuration → existing skill/workflow/tool → focused change to existing skill/tool → small automation/hook/CI control → new bounded skill → specialist agent → harness/runtime feature → combination. Do not force this sequence when a permission/security control requires deterministic enforcement from the outset.

| If the need is... | Choose | Why / acceptance |
|---|---|---|
| Repeatable domain procedure, clear inputs/outputs | Skill | Can be invoked independently and tested with scenarios |
| Existing procedure already covers it | Use/configure/improve existing skill | Reuse one authoritative owner; avoid copy-paste policy drift |
| Runtime scheduling, execution loop, durable state, enforced permissions, sandbox | Harness / external service / CI job | Markdown cannot guarantee execution or enforcement |
| Independent investigation, specialist scrutiny, parallelism, context isolation | Bounded subagent | Explicit scoped tools, max budget, result contract and reviewer independence |
| Known integration need satisfied by mature tool | Tool or MCP integration | Verify license, permissions, ongoing maintenance, security and actual capabilities |
| Code convention enforced on every PR | Linter/test/CI/hook | Deterministic, reproducible check rather than reminder |
| Traceability, context, state, ADR, ownership issue | Documentation/knowledge-system improvement | Link to existing source of truth; prefer generated indexes |
| Several independent requirements | Combined solution | Name exactly why each component is necessary and who owns it |
| Unclear or tiny problem | No new component | Direct fix/explanation with tests where relevant |

Before recommending a new tool or multi-agent system, compare **existing coverage, complexity, verification, tokens/compute, vendor dependency, long-term operations and total cost**. Do not create an agent for every specialty or a file for every concern.

## Phase selection examples

- New SaaS: 0 → 1 → 2 → 3 → 4 → 5 → 6; design maintenance before 6; use 7/8 after launch.
- Existing repository to modernize: 0 → 1/2 only if needed → 3 upgrades → 5, with staged rollout.
- Local feature: 0 → 4 → 5; briefly recheck requirements/architecture if cross-cutting.
- Reliability regression: 0 → 7 observation → 4 hotfix → 5 → 6, then 8 post-incident improvements.
- New codebase intelligence tool: 0 → 8 system assessment → 3 harness/tool integration → 5 evaluation.
- Weekly maintenance check: 0 → design policy → 7 checkup → 5 verification → 8 prioritized backlog; do not run an inactive schedule.

## Risk levels and response scaling

- **Low:** localized, easily reversible, non-sensitive. Lightweight plan, focused tests, normal code review.
- **Moderate:** cross-module, API/data changes, new dependencies, exposure. Impact map, broader tests, security review, rollback plan.
- **High:** authentication/authorization, payments, minors' data, regulated data, secrets, production infrastructure, irreversible or multi-tenant changes. Explicit approval, threat model, independent review, recovery exercise as applicable; no autonomous deployment.

Profiles for engineering rigor: **lean**, **standard**, **strict** (as in Scaffold Kit), selected by actual risk. A lean budget never waives required security safeguards. A strict profile does not mandate unnecessary infrastructure.

Budget profile is separate from rigor: **manual**, **scheduled-low-cost**, **event-driven**, **managed/continuous**. Record AI tokens/calls/timeout caps, CI minutes, storage, external API costs, notification burden and stopping rules, not just model price.

## Default recommendation report

`Problem / Evidence inspected / Options / Recommended classification / Phases / Why this is sufficient / Scope / Risks and approval / Budget / Verification / Maintenance owner / Next action`. Cite actual repo paths and command results when available. Mark assumptions explicitly.
