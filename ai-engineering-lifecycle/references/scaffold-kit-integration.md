# Integration with ronnymaichle/scaffold-kit

Source reviewed: <https://github.com/ronnymaichle/scaffold-kit> (public `main` and the source skill as available on 2026-11-08). Re-verify contents, tags, script contracts and available versions before use; this integration does **not** vendor or fork the kit.

## Real component ownership

| Existing kit component | This skill's relationship |
|---|---|
| `skill/scaffold-project/SKILL.md` | Invoke when user wants a new project foundation or upgrade existing repo standards |
| `references/` | Authoritative full engineering standards used by that kit; avoid duplicating them in project docs |
| `templates/` | Project instructions, checklists, GitHub CI/config, Claude agents, progress, ADR and scaffolding assets |
| `scripts/quality/` | Tested deterministic checks copied into projects by scaffold-project as appropriate |
| `tests/`, `evals/` | Existing kit's script tests and planning evaluations; reuse the applicable ones |
| `skill/scaffold-kit-maintainer/SKILL.md` | Maintains **Scaffold Kit** itself, **not** this lifecycle skill |

Scaffold Kit has `lean`, `standard` and `strict` profiles and new-project vs. existing-repo upgrade modes. Keep those meanings when delegating a scaffold task. The kit uses tagged releases and project-owned copies, so upgrades require a deliberate review and migration; a central release does not magically update existing applications.

## Integration procedure

1. Inventory whether `scaffold-project` is actually installed and whether a local/tagged kit is already present. If absent, this lifecycle skill still works and can propose a simple non-kit foundation; do not claim Scaffold Kit was executed.
2. When appropriate, recommend or invoke existing `scaffold-project` for phases 1–3 (requirements, stack selection, foundation) or its **upgrade mode**, rather than recreating its rules, copied templates or scripts here.
3. Before fetching external code, get required authorization and use a vetted, pinned release or trusted local copy. Do not run unreviewed install scripts; verify source and checks in the target environment.
4. Merge lifecycle-specific planning into the existing project's project instructions and appropriate `docs/` files without overwriting customized configuration or duplicating documentation.
5. Treat current Scaffold Kit quality scripts and agent guard hooks as existing controls; inspect `quality.config.json`, `.claude/settings.json`, root `CLAUDE.md` and CI before adding new hooks. **Runtime enforcement remains dependent on the actual installed hook configuration.**
6. Add a project **maintenance policy** as a small linked document or append to existing `docs/OPERATIONS.md` if already authoritative; avoid competing sources of truth.
7. For feature/hotfix/release tasks, preserve Scaffold Kit's project-local Feature/Hotfix/Release workflow and overlay only missing lifecycle gates, budget policy and operation/evaluation requirements.
8. Validate with kit's documented test commands *if installed*, then document what was actually run. Don't claim check success based on the kit's README.

## Boundary with future maintainer skill

- `scaffold-kit-maintainer`: owns changes to scaffold-project and scaffold-kit repository.
- **Future `ai-engineering-lifecycle-maintainer`** (user-created; not included): owns changes to THIS package, its evaluation fixtures and compatibility mapping.
- `ai-engineering-lifecycle`: coordinates engineering work and software-project maintenance. It can submit a documented suggestion for its own future improvements, but does not autonomously edit/version/publish itself.

If both systems offer an opinion, first use target project instructions and established kit rules for project scaffolding details; use this skill for phase routing, cross-system architecture, maintenance planning and decisions about components. Escalate contradictory policy instead of silently overwriting.
