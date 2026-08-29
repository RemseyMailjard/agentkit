#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []
STATS = {
    "plugins": 0,
    "skills": 0,
    "eval_files": 0,
    "eval_cases": 0,
    "golden_workflows": 0,
}

SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)

def error(message: str) -> None:
    ERRORS.append(message)

def warn(message: str) -> None:
    WARNINGS.append(message)

def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        error(f"Missing JSON file: {rel(path)}")
    except json.JSONDecodeError as exc:
        error(f"Invalid JSON: {rel(path)}:{exc.lineno}:{exc.colno} {exc.msg}")
    return None

def load_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        error(f"Missing file: {rel(path)}")
        return None

def parse_frontmatter(path: Path) -> dict[str, str]:
    text = load_text(path)
    if text is None:
        return {}

    match = FRONTMATTER.match(text)
    if not match:
        error(f"Missing YAML-style frontmatter in {rel(path)}")
        return {}

    fm = match.group(1)
    result = {}

    name_match = re.search(r"(?m)^name:\s*(.+?)\s*$", fm)
    desc_match = re.search(r"(?m)^description:\s*(?:>\s*)?(.*)$", fm)

    if not name_match:
        error(f"Missing frontmatter 'name' in {rel(path)}")
    else:
        result["name"] = name_match.group(1).strip().strip("'\"")

    if not desc_match:
        error(f"Missing frontmatter 'description' in {rel(path)}")
    else:
        result["description"] = desc_match.group(1).strip()

    return result

def validate_marketplace() -> list[dict]:
    path = ROOT / ".agents/plugins/marketplace.json"
    data = load_json(path)
    if not isinstance(data, dict):
        return []

    if data.get("name") != "skills4it":
        warn("Marketplace name is expected to be 'skills4it'.")

    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        error("Marketplace must contain a non-empty 'plugins' array.")
        return []

    seen = set()
    for i, item in enumerate(plugins):
        prefix = f"marketplace.plugins[{i}]"
        if not isinstance(item, dict):
            error(f"{prefix} must be an object.")
            continue

        name = item.get("name")
        if not isinstance(name, str) or not name:
            error(f"{prefix}.name is required.")
            continue

        if name in seen:
            error(f"Duplicate marketplace plugin name: {name}")
        seen.add(name)

        source = item.get("source")
        if not isinstance(source, dict) or source.get("source") != "local":
            error(f"{prefix}.source must use local source.")
            continue

        rel_path = source.get("path")
        if not isinstance(rel_path, str) or not rel_path.startswith("./plugins/"):
            error(f"{prefix}.source.path must start with ./plugins/")
            continue

        plugin_dir = ROOT / rel_path[2:]
        if not plugin_dir.is_dir():
            error(f"Marketplace path does not exist: {rel_path}")

        expected = f"./plugins/{name}"
        if rel_path != expected:
            warn(f"Plugin '{name}' source path is '{rel_path}', expected '{expected}'.")

        policy = item.get("policy")
        if not isinstance(policy, dict):
            error(f"{prefix}.policy is required.")
        else:
            if policy.get("installation") not in {"AVAILABLE", "REQUIRED", "BLOCKED"}:
                warn(f"{prefix}.policy.installation has unexpected value.")
            if "authentication" not in policy:
                warn(f"{prefix}.policy.authentication is not defined.")

    STATS["plugins"] = len(plugins)
    return plugins

def validate_plugins(plugins: list[dict]) -> tuple[dict[str, set[str]], dict[str, str]]:
    plugin_skills: dict[str, set[str]] = {}
    plugin_versions: dict[str, str] = {}

    for item in plugins:
        name = item.get("name")
        source = item.get("source", {})
        rel_path = source.get("path")
        if not isinstance(name, str) or not isinstance(rel_path, str):
            continue

        plugin_dir = ROOT / rel_path[2:]
        manifest_path = plugin_dir / ".codex-plugin/plugin.json"
        manifest = load_json(manifest_path)
        if not isinstance(manifest, dict):
            continue

        if manifest.get("name") != name:
            error(f"{rel(manifest_path)} name does not match marketplace name '{name}'.")

        version = manifest.get("version")
        if not isinstance(version, str) or not SEMVER.match(version):
            error(f"{rel(manifest_path)} has invalid or missing semver version.")
        else:
            plugin_versions[name] = version

        for field in ["description", "homepage", "repository", "license", "skills"]:
            if field not in manifest:
                error(f"{rel(manifest_path)} missing required field '{field}'.")

        # version consistency: optional plugin changelog should mention current version
        changelog = plugin_dir / "CHANGELOG.md"
        if changelog.exists() and isinstance(version, str):
            content = changelog.read_text(encoding="utf-8")
            if version not in content and f"{version.rsplit('.',1)[0]}" not in content:
                warn(f"{rel(changelog)} does not appear to mention plugin version {version}.")

        skills_rel = manifest.get("skills")
        skill_names: set[str] = set()

        if isinstance(skills_rel, str):
            skills_dir = plugin_dir / skills_rel
            if not skills_dir.exists():
                error(f"Skills path does not exist for {name}: {skills_rel}")
            else:
                skill_files = sorted(skills_dir.glob("*/SKILL.md"))
                if not skill_files:
                    error(f"No SKILL.md files found for plugin {name}.")
                for skill in skill_files:
                    fm = parse_frontmatter(skill)
                    declared = fm.get("name")
                    folder = skill.parent.name
                    if declared and declared != folder:
                        warn(f"Skill name '{declared}' does not match folder '{folder}' in {rel(skill)}")
                    skill_names.add(declared or folder)
                    STATS["skills"] += 1

        plugin_skills[name] = skill_names

        mcp_rel = manifest.get("mcpServers")
        if isinstance(mcp_rel, str):
            mcp_path = plugin_dir / mcp_rel
            if not mcp_path.exists():
                error(f"MCP configuration path does not exist for {name}: {mcp_rel}")
            else:
                load_json(mcp_path)

        ui = manifest.get("interface")
        if not isinstance(ui, dict):
            warn(f"{rel(manifest_path)} has no interface object.")
        else:
            for field in ["displayName", "shortDescription"]:
                if not ui.get(field):
                    warn(f"{rel(manifest_path)} interface.{field} is missing.")

    return plugin_skills, plugin_versions

def validate_eval_file(path: Path) -> list[dict]:
    data = load_json(path)
    if not isinstance(data, list):
        error(f"Eval file must contain an array: {rel(path)}")
        return []

    STATS["eval_files"] += 1
    STATS["eval_cases"] += len(data)

    ids = set()
    for i, case in enumerate(data):
        prefix = f"{rel(path)}[{i}]"
        if not isinstance(case, dict):
            error(f"{prefix} must be an object.")
            continue

        case_id = case.get("id")
        prompt = case.get("prompt")

        if not isinstance(case_id, str) or not case_id:
            error(f"{prefix}.id is required.")
        elif case_id in ids:
            error(f"Duplicate eval id '{case_id}' in {rel(path)}")
        else:
            ids.add(case_id)

        if not isinstance(prompt, str) or not prompt.strip():
            error(f"{prefix}.prompt is required.")

        if "expected_skill" not in case and "expected_skills" not in case and "expected_plugins" not in case:
            warn(f"{prefix} has no expected routing field.")

        checks = case.get("quality_checks")
        if checks is not None and (not isinstance(checks, list) or not all(isinstance(x, str) for x in checks)):
            error(f"{prefix}.quality_checks must be an array of strings.")

    return data

def validate_eval_coverage(plugin_skills: dict[str, set[str]]) -> None:
    for plugin_name, skills in plugin_skills.items():
        eval_path = ROOT / "evals" / plugin_name / "cases.json"

        # scaffold plugins may intentionally not have evals yet
        manifest = ROOT / "plugins" / plugin_name / ".codex-plugin" / "plugin.json"
        manifest_data = load_json(manifest)
        desc = ""
        if isinstance(manifest_data, dict):
            desc = str(manifest_data.get("description", "")).lower()

        if not eval_path.exists():
            if "scaffold" in desc:
                warn(f"Scaffold plugin '{plugin_name}' has no eval suite yet.")
                continue
            error(f"Plugin '{plugin_name}' has no eval suite at evals/{plugin_name}/cases.json")
            continue

        cases = validate_eval_file(eval_path)
        covered: set[str] = set()

        for case in cases:
            if not isinstance(case, dict):
                continue
            one = case.get("expected_skill")
            many = case.get("expected_skills")
            if isinstance(one, str):
                covered.add(one)
            if isinstance(many, list):
                covered.update(x for x in many if isinstance(x, str))

        missing = sorted(skills - covered)
        if missing:
            error(f"Plugin '{plugin_name}' has skills without eval coverage: {', '.join(missing)}")

def validate_cross_plugin_refs(plugin_skills: dict[str, set[str]]) -> None:
    path = ROOT / "evals/cross-plugin/cases.json"
    if not path.exists():
        error("Missing cross-plugin eval suite: evals/cross-plugin/cases.json")
        return

    cases = validate_eval_file(path)
    known_plugins = set(plugin_skills.keys())
    known_skills = set().union(*plugin_skills.values()) if plugin_skills else set()

    for i, case in enumerate(cases):
        if not isinstance(case, dict):
            continue
        prefix = f"{rel(path)}[{i}]"

        plugins = case.get("expected_plugins", [])
        if isinstance(plugins, list):
            for plugin in plugins:
                if isinstance(plugin, str) and plugin not in known_plugins:
                    error(f"{prefix} references unknown plugin '{plugin}'.")

        skills = case.get("expected_skills", [])
        if isinstance(skills, list):
            for skill in skills:
                if isinstance(skill, str) and skill not in known_skills:
                    error(f"{prefix} references unknown skill '{skill}'.")

        one = case.get("expected_skill")
        if isinstance(one, str) and one not in known_skills:
            error(f"{prefix} references unknown skill '{one}'.")

def validate_golden_workflows() -> None:
    base = ROOT / "examples/golden-workflows"
    if not base.exists():
        error("Missing examples/golden-workflows directory.")
        return

    dirs = sorted(p for p in base.iterdir() if p.is_dir())
    STATS["golden_workflows"] = len(dirs)

    if not dirs:
        error("No golden workflow directories found.")
        return

    for workflow in dirs:
        readme = workflow / "README.md"
        if not readme.exists():
            error(f"Golden workflow '{workflow.name}' is missing README.md")
            continue

        content = readme.read_text(encoding="utf-8").lower()
        for phrase in ["goal", "acceptance"]:
            if phrase not in content:
                warn(f"Golden workflow '{workflow.name}' README does not mention '{phrase}'.")

def validate_docs() -> None:
    required = [
        "README.md",
        "AGENTS.md",
        "docs/architecture.md",
        "docs/routing-matrix.md",
        "docs/plugin-contract.md",
    ]
    for item in required:
        if not (ROOT / item).exists():
            error(f"Missing required platform file: {item}")

def print_summary() -> None:
    print("\nSummary")
    print("-------")
    print(f"Plugins:          {STATS['plugins']}")
    print(f"Skills:           {STATS['skills']}")
    print(f"Eval files:       {STATS['eval_files']}")
    print(f"Eval cases:       {STATS['eval_cases']}")
    print(f"Golden workflows: {STATS['golden_workflows']}")
    print(f"Warnings:         {len(WARNINGS)}")
    print(f"Errors:           {len(ERRORS)}")

def main() -> int:
    print("AgentKit Validator v0.2")
    print("=======================")

    plugins = validate_marketplace()
    plugin_skills, _ = validate_plugins(plugins)

    validate_eval_coverage(plugin_skills)
    validate_cross_plugin_refs(plugin_skills)
    validate_golden_workflows()
    validate_docs()

    if WARNINGS:
        print("\nWarnings:")
        for item in WARNINGS:
            print(f"  - {item}")

    if ERRORS:
        print("\nErrors:")
        for item in ERRORS:
            print(f"  - {item}")

    print_summary()

    if ERRORS:
        print("\nRESULT: FAIL")
        return 1

    print("\nRESULT: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
