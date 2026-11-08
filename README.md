# AI Engineering Lifecycle — installable skill

**Version:** 1.0.0  
**Status:** Installable reference implementation and workflow package; no background maintenance is activated simply by installing it.

This is a unified, phase-routed engineering orchestration skill for Claude Code and other agents that support the `SKILL.md` convention. It pairs with [ronnymaichle/scaffold-kit](https://github.com/ronnymaichle/scaffold-kit) without copying or replacing it. The package was derived from the supplied **AI Software Engineering System Builder** master prompt and the proposed lifecycle/maintenance design.

## Install

**Claude Code, project scope:** copy the `ai-engineering-lifecycle/` folder into `<repo>/.claude/skills/ai-engineering-lifecycle/`, retaining `SKILL.md`, `references/`, `workflows/`, `assets/` and other subdirectories. Commit it if your team should share the skill. In supported Claude Code sessions, invoke `/ai-engineering-lifecycle` or describe a relevant engineering task. If auto-activation does not occur, invoke explicitly.

**Claude Code, personal scope:** copy to `~/.claude/skills/ai-engineering-lifecycle/` so the skill is available across your repos. Project and personal installations are alternative scopes.

**Dedicated skill repository:** put the skill folder in a GitHub repo, then copy/symlink the folder to a location the target AI client recognizes. Merely putting a `SKILL.md` in an arbitrary Git repository does not make it automatically active; installation and runtime support depend on the client.

**Other AI agent systems:** load `SKILL.md` as the entry point and provide access to its relative references. Adapt activation and tools to the target platform; don't assume Claude-only hooks exist.

## Optional companion

Install `scaffold-project` separately if you want the scaffold-kit templates and scripts. When available, the lifecycle skill delegates the *project foundation* to it. It must not silently clone and execute an unreviewed repository. Pin a reviewed scaffold-kit release and follow the project's own approval/security workflow.

The user plans to author a **separate maintainer skill for this skill package**. That maintainer is **not provided here**. Its interface, ownership and suggested test/release contract are documented in `references/maintainer-handoff.md`. Project maintenance is still a primary responsibility of this lifecycle skill.

## Test this package

From the `ai-engineering-lifecycle/` folder:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
python3 scripts/repo_health.py --root . --output /tmp/ai-lifecycle-health.md
```

The first two commands check structure, references, templates and scenario fixtures; they are *not* model-based evaluations. The third provides a deterministic, read-only repository metadata report. The package includes human/agent evaluation cases that must still be executed in the target model/runtime before declaring behavioral reliability.

## Safe example schedule

`examples/weekly-maintenance.yml` demonstrates a low-privilege weekly GitHub Actions check. Nothing runs until the user decides to copy it to `.github/workflows/` in an actual project and commits it. It does not call paid AI, push changes, open PRs, or deploy. Scheduled checks are best-effort: do not treat them as a production availability monitoring service.

## Contents

- `SKILL.md`: concise agent-facing entry point and routing.
- `references/`: authoritative decisions, phase contracts, governance, maintenance policy, and specialist engineering standards.
- `workflows/`: executable step sequences for common engineering intents.
- `assets/`: copy-and-adapt project artifacts and report templates.
- `examples/`: opt-in GitHub Actions checkup example.
- `scripts/`: stdlib-only validation and read-only repository health report.
- `evals/`: scenario-based behavioral evaluation fixtures.
- `tests/`: structural tests of the package.

## Limits

Skills are instructions, not guaranteed tool access, persistent background agents, security policy engines or active schedulers. The provided source does not install any live job, service, agent, monitoring integration, security scanner, or production pipeline. Some standards and tools change; verify current source material before adopting decisions.
