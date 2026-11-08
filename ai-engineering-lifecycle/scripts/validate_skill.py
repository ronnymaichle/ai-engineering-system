#!/usr/bin/env python3
"""Deterministic structural validation for ai-engineering-lifecycle.

Does not execute any external code or call a model. Python 3.9+ stdlib only.
Behavioral/scenario evaluations require a separate real agent/runtime test.
"""

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    core = root / "SKILL.md"
    if not core.is_file():
        return ["Missing SKILL.md"]
    data = core.read_text(encoding="utf-8")
    parts = data.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        return ["SKILL.md must begin with --- YAML frontmatter ---"]
    metadata = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            metadata[k.strip()] = v.strip().strip('"').strip("'")
    if metadata.get("name") != "ai-engineering-lifecycle":
        errors.append("Frontmatter name must equal folder name: ai-engineering-lifecycle")
    desc = metadata.get("description", "")
    if not desc or len(desc) > 1024:
        errors.append("Frontmatter description must be present and <= 1024 chars")
    if len(data.splitlines()) > 500:
        errors.append("SKILL.md is over 500 lines; move detail into references")
    if (root / "README.md").exists():
        errors.append("Place human README beside skill folder, not inside it")
    version_path = root / "VERSION"
    if not version_path.is_file() or not re.fullmatch(r"\d+\.\d+\.\d+", version_path.read_text().strip()):
        errors.append("Missing or non-SemVer VERSION")

    required = [
        "references/decision-engine.md", "references/phase-contracts.md",
        "references/maintenance-engine.md", "references/quality-gates.md",
        "references/security-and-authority.md", "references/maintainer-handoff.md",
        "references/scaffold-kit-integration.md", "workflows/maintenance-setup.md",
        "workflows/maintenance-review.md", "examples/weekly-maintenance.yml",
        "scripts/repo_health.py", "evals/scenarios.json",
    ]
    for file in required:
        if not (root / file).is_file():
            errors.append(f"Missing required resource: {file}")

    # Verify every relative resource path mentioned in code spans of the entry point.
    for target in sorted(set(re.findall(
        r"`((?:references|workflows|scripts|assets|examples|evals)/[a-zA-Z0-9_./-]+)`", data
    ))):
        if not (root / target).exists():
            errors.append(f"Broken resource path from SKILL.md: {target}")

    for dirname in ("references", "workflows", "assets"):
        files = list((root / dirname).glob("*.md"))
        if not files:
            errors.append(f"No Markdown files in {dirname}/")
        for p in files:
            if not p.read_text(encoding="utf-8").strip():
                errors.append(f"Empty resource: {p.relative_to(root)}")

    fixture_path = root / "evals/scenarios.json"
    try:
        scenarios = json.loads(fixture_path.read_text(encoding="utf-8"))
        if not isinstance(scenarios, list) or len(scenarios) < 12:
            errors.append("Expected >=12 behavioral evaluation scenarios")
        else:
            ids = [s.get("id") for s in scenarios]
            if len(ids) != len(set(ids)):
                errors.append("Duplicate scenario IDs")
            for item in scenarios:
                if not isinstance(item.get("request"), str) or not item["request"].strip():
                    errors.append(f"Invalid request in fixture {item.get('id')}")
                phases = item.get("expected_phases")
                if not isinstance(phases, list) or 0 not in phases or any(
                    not isinstance(x, int) or not 0 <= x <= 8 for x in phases
                ):
                    errors.append(f"Invalid phase selection for fixture {item.get('id')}")
                if not item.get("must_do") or not item.get("must_not") or not item.get("decision"):
                    errors.append(f"Missing assertions/decision for fixture {item.get('id')}")
    except (OSError, ValueError) as exc:
        errors.append(f"Invalid eval fixture: {exc}")

    sample = root / "examples/weekly-maintenance.yml"
    if sample.is_file():
        src = sample.read_text(encoding="utf-8")
        if "workflow_dispatch:" not in src or "schedule:" not in src:
            errors.append("Example schedule lacks manual/scheduled triggers")
        if "permissions:\n  contents: read" not in src:
            errors.append("Example schedule must request contents: read only")
        for unsafe in ("contents: write", "id-token: write", "pull_request_target:", "git push", "auto-merge"):
            if unsafe in src:
                errors.append(f"Disallowed dangerous operation in read-only example: {unsafe}")

    return errors


def main():
    errors = validate()
    if errors:
        for problem in errors:
            print("FAIL:", problem, file=sys.stderr)
        return 1
    print("PASS: skill frontmatter, version, resources, sample workflow and 20 scenario fixtures are structurally valid.")
    print("NOTE: no live AI agent, platform compatibility or production maintenance workflow was executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
