# Standards and verified source pointers

**Source snapshot checked:** 2026-11-08. These links are references for current research, **not certifications**. Verify latest versions, legal applicability and operational prices at the moment of use.

## Skill design and platform

- Anthropic, **Skill authoring best practices**: <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices> — metadata, progressive disclosure, testing and short entry-point instructions.
- Anthropic, **Claude Code skills/hooks/rules/subagents separation**: <https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more> — avoid treating skills as runtime-enforced hooks.
- Source repository: <https://github.com/ronnymaichle/scaffold-kit> and its skill sources at `skill/scaffold-project/SKILL.md` and `skill/scaffold-kit-maintainer/SKILL.md`.

## Secure software engineering

- NIST **SSDF SP 800-218 v1.1 (final)**: <https://csrc.nist.gov/pubs/sp/800/218/final>. At snapshot time, **SP 800-218 Rev. 1 / SSDF v1.2 was still a draft**: <https://csrc.nist.gov/pubs/sp/800/218/r1/ipd>. Do not mislabel it final.
- NIST **AI Risk Management Framework**: <https://www.nist.gov/itl/ai-risk-management-framework>.
- OWASP **Top 10 for Agentic Applications 2026**: <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>.
- OWASP **2026 LLM Application Top 10**: <https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/>.
- SLSA **Supply-chain Levels for Software Artifacts v1.2**: <https://slsa.dev/spec/v1.2/> — supply-chain provenance/integrity, not a substitute for full software security.

## GitHub job and dependency behavior

- GitHub Actions **schedule and workflow_dispatch**: <https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows> — schedules run against default branch; may be delayed/dropped and public-repo schedules can be disabled after inactivity. Confirm plan/limits.
- GitHub **Dependabot security updates**: <https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-security-updates> — requires appropriate repository settings and supported ecosystems.

## Research procedure

For choices about libraries/providers/models/tools: compare official docs and current release dates, security advisories, license, dependency activity, API/limits, cost and compatibility. Where possible cite source URL and date checked in the project decision. Differentiate `verified now`, `known from project's installed version`, `approximation`, `not checked`. When no browsing/network is available, explicitly mark facts for later verification and avoid fabricated prices or availability.
