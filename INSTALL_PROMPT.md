# Copy/paste installation prompt for a coding agent

Paste the following into an AI coding agent **after** you have extracted the ZIP in a location the agent can access. Replace the bracketed directory path with your real extracted location.

---

Install my `ai-engineering-lifecycle` skill into the current repository from `[EXTRACTED_DIRECTORY]/ai-engineering-lifecycle/`.

Requirements:

1. Inspect the current Git working tree and project-specific `CLAUDE.md` or `AGENTS.md` instructions first; do not discard uncommitted work.
2. Preserve the entire `ai-engineering-lifecycle/` directory hierarchy. Copy it to `.claude/skills/ai-engineering-lifecycle/` for Claude Code project scope (or use an equivalent documented location for the current AI agent platform).
3. Before overwriting an existing `ai-engineering-lifecycle` installation, show differences and ask my approval. Do not modify Scaffold Kit, its separate maintainer skill or unrelated project code.
4. Validate the installed package using `python3 .claude/skills/ai-engineering-lifecycle/scripts/validate_skill.py` and `python3 -m unittest discover -s .claude/skills/ai-engineering-lifecycle/tests -v`; report actual results.
5. Do not activate any scheduler, CI workflow, agent runner, paid service, credential, production access or GitHub publication. `examples/weekly-maintenance.yml` must remain an example until I specifically approve its installation.
6. Confirm exactly where the skill is installed, whether it is detected by the current agent platform, whether `scaffold-project` is separately available, what was tested, and what is still not enabled.
7. I will create a separate maintainer skill for this lifecycle skill later. Do not create or claim a maintainer now. Keep the `references/maintainer-handoff.md` contract intact.

---

## Alternative: direct manual installation

When the extracted `ai-engineering-lifecycle/` folder is in the working directory of the target project:

```bash
mkdir -p .claude/skills
cp -R ai-engineering-lifecycle .claude/skills/
python3 .claude/skills/ai-engineering-lifecycle/scripts/validate_skill.py
python3 -m unittest discover -s .claude/skills/ai-engineering-lifecycle/tests -v
```

Use `git status` and review changes before committing. The folder must be at `.claude/skills/ai-engineering-lifecycle/SKILL.md` **for Claude Code project-scope activation**. If that destination already exists, don't use `cp -R` without comparing and approving the replacement.

The package is instructional; no automation runs just from copying it.
