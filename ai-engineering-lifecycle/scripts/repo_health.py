#!/usr/bin/env python3
"""Read-only repository metadata check for human/CI maintenance reviews.

Does not execute project code, fetch network resources, scan dependencies for
vulnerabilities, inspect secrets, call an AI model, deploy or change Git state.
It writes reports ONLY to explicit --output / --json paths if requested.
Python 3.9+ standard library only.
"""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys


LOCKFILES = (
    "package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lock", "bun.lockb",
    "poetry.lock", "uv.lock", "Pipfile.lock", "requirements.lock",
    "Cargo.lock", "go.sum", "Gemfile.lock", "composer.lock", "pubspec.lock",
)
MANIFESTS = (
    "package.json", "pyproject.toml", "requirements.txt", "Cargo.toml",
    "go.mod", "Gemfile", "composer.json", "pubspec.yaml", "pom.xml",
    "build.gradle", "build.gradle.kts", "mix.exs", "Makefile",
)


def git_metadata(root):
    def run(*args):
        try:
            p = subprocess.run(
                ["git", "-C", str(root), *args],
                capture_output=True, text=True, timeout=8, check=False,
            )
        except (OSError, subprocess.TimeoutExpired):
            return None
        return p.stdout.strip() if p.returncode == 0 else None

    inside = run("rev-parse", "--is-inside-work-tree") == "true"
    if not inside:
        return {"is_git_repository": False, "revision": None, "branch": None, "clean": None}
    revision = run("rev-parse", "--short=12", "HEAD")
    branch = run("branch", "--show-current")
    status = run("status", "--porcelain", "--untracked-files=no")
    return {
        "is_git_repository": True,
        "revision": revision,
        "branch": branch or "detached",
        "clean": None if status is None else status == "",
    }


def check(root):
    if not root.is_dir():
        raise NotADirectoryError("Repository path does not exist or is not a directory")

    checks = {
        "readme": (root / "README.md").is_file() or (root / "readme.md").is_file(),
        "project_instructions": any((root / x).is_file() for x in ("CLAUDE.md", "AGENTS.md")),
        "test_directory": any((root / x).is_dir() for x in ("tests", "test", "__tests__", "spec")),
        "ci_workflows": (root / ".github" / "workflows").is_dir(),
        "dependency_manifest": any((root / x).is_file() for x in MANIFESTS),
        "dependency_lockfile": any((root / x).is_file() for x in LOCKFILES),
        "operations_docs": any((root / x).is_file() for x in (
            "docs/OPERATIONS.md", "docs/RUNBOOK.md", "OPERATIONS.md", "RUNBOOK.md",
            "docs/MAINTENANCE.md", "MAINTENANCE.md",
        )),
        "security_policy": (root / "SECURITY.md").is_file(),
    }
    descriptions = {
        "readme": "Repository README present",
        "project_instructions": "Project-level agent instructions present",
        "test_directory": "Test directory present (tests NOT executed)",
        "ci_workflows": "GitHub CI workflow directory present (runs NOT checked)",
        "dependency_manifest": "Known dependency/project manifest present",
        "dependency_lockfile": "Known dependency lockfile present (integrity NOT checked)",
        "operations_docs": "Operations/maintenance documentation present",
        "security_policy": "Root SECURITY.md present",
    }
    observations = []
    for key, val in checks.items():
        observations.append({
            "domain": key,
            "observation": descriptions[key],
            "present": val,
            "status": "observed_present" if val else "not_found_in_known_locations",
        })
    warnings = []
    if not checks["readme"]:
        warnings.append("No top-level README found; inspect onboarding documentation manually.")
    if not checks["test_directory"]:
        warnings.append("No common test directory found; tests may exist elsewhere.")
    if checks["dependency_manifest"] and not checks["dependency_lockfile"]:
        warnings.append("No known root lockfile found; not all build systems require one.")
    if not checks["ci_workflows"]:
        warnings.append("No .github/workflows directory; CI may be hosted elsewhere.")
    return {
        "schema_version": "1.0",
        "kind": "repository_metadata_inventory_only",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "git": git_metadata(root),
        "observations": observations,
        "warnings": warnings,
        "not_checked": [
            "application source correctness and runtime behavior",
            "unit/integration/end-to-end tests (not executed)",
            "vulnerability advisories and dependency security",
            "CI job outcomes and branch protections",
            "runtime monitoring, errors, availability and incidents",
            "infrastructure, database consistency, backups and restore tests",
            "security posture, permissions, secrets and compliance",
            "AI agent quality, model drift, costs and external integrations",
            "scheduler activation and successful scheduled runs",
        ],
        "conclusion": "Metadata inventory only; no claim of application health or security.",
    }


def render_md(report):
    git = report["git"]
    lines = [
        "# Repository maintenance metadata report", "",
        f"- Generated UTC: `{report['generated_at_utc']}`",
        f"- Root: `{report['root']}`",
        f"- Git repo: `{git['is_git_repository']}`",
        f"- Revision: `{git['revision'] or 'unknown'}`",
        f"- Branch: `{git['branch'] or 'unknown'}`",
        f"- Tracked working tree clean: `{git['clean']}` (not a full security/release check)",
        "", "## Presence checks (not functionality tests)", "",
        "| Observation | Result |", "|---|---|",
    ]
    for item in report["observations"]:
        lines.append(f"| {item['observation']} | {item['status']} |")
    lines += ["", "## Advisory notes", ""]
    lines += [f"- {w}" for w in report["warnings"]] or ["- No structural warnings from these limited presence checks."]
    lines += ["", "## Explicitly NOT checked", ""]
    lines += [f"- {x}" for x in report["not_checked"]]
    lines += ["", f"**Conclusion:** {report['conclusion']}", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository directory to inspect")
    parser.add_argument("--output", help="Optional Markdown report destination")
    parser.add_argument("--json", dest="json_path", help="Optional JSON report destination")
    args = parser.parse_args()
    root = Path(args.root).expanduser().resolve()
    try:
        report = check(root)
        md = render_md(report)
        if args.output:
            output = Path(args.output).expanduser()
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(md, encoding="utf-8")
        if args.json_path:
            output = Path(args.json_path).expanduser()
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        if not args.output:
            sys.stdout.write(md)
    except (OSError, ValueError) as exc:
        print(f"repo_health error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
