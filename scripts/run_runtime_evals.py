#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

@dataclass
class EvalCase:
    source: str
    id: str
    prompt: str
    expected_plugins: list[str]
    expected_skills: list[str]

@dataclass
class EvalResult:
    source: str
    id: str
    prompt: str
    expected_plugins: list[str]
    expected_skills: list[str]
    actual_plugins: list[str]
    actual_skills: list[str]
    plugin_match: bool
    skill_match: bool
    passed: bool
    runner: str
    raw_output: str | None = None
    error: str | None = None

def normalize_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [x for x in value if isinstance(x, str)]
    return []

def load_cases(pattern: str) -> list[EvalCase]:
    paths = sorted(ROOT.glob(pattern))
    cases: list[EvalCase] = []

    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            continue

        for item in data:
            if not isinstance(item, dict):
                continue

            cases.append(
                EvalCase(
                    source=str(path.relative_to(ROOT)).replace("\\", "/"),
                    id=str(item.get("id", "")),
                    prompt=str(item.get("prompt", "")),
                    expected_plugins=normalize_list(item.get("expected_plugins")),
                    expected_skills=normalize_list(
                        item.get("expected_skills", item.get("expected_skill"))
                    ),
                )
            )

    return cases

def compare(expected: list[str], actual: list[str]) -> bool:
    # Routing correctness is set-based in v0.1.
    # Ordering is intentionally not enforced yet.
    return set(expected) == set(actual)

def run_fixture(case: EvalCase, fixtures: dict[str, Any]) -> tuple[list[str], list[str], str]:
    fixture = fixtures.get(case.id)
    if not isinstance(fixture, dict):
        raise KeyError(f"No fixture result found for eval id '{case.id}'.")

    plugins = normalize_list(fixture.get("actual_plugins"))
    skills = normalize_list(fixture.get("actual_skills"))
    return plugins, skills, json.dumps(fixture, ensure_ascii=False)

def parse_json_from_output(output: str) -> dict[str, Any]:
    text = output.strip()

    try:
        value = json.loads(text)
        if isinstance(value, dict):
            return value
    except json.JSONDecodeError:
        pass

    # Allow a runner to print diagnostic lines before a final JSON object.
    for line in reversed(text.splitlines()):
        line = line.strip()
        if not line:
            continue
        try:
            value = json.loads(line)
            if isinstance(value, dict):
                return value
        except json.JSONDecodeError:
            continue

    raise ValueError("Runner output does not contain a JSON object.")

def run_command(case: EvalCase, command_template: str) -> tuple[list[str], list[str], str]:
    command = command_template.replace("{prompt}", case.prompt).replace("{id}", case.id)
    completed = subprocess.run(
        command,
        cwd=ROOT,
        shell=True,
        text=True,
        capture_output=True,
    )

    raw = (completed.stdout or "") + (completed.stderr or "")

    if completed.returncode != 0:
        raise RuntimeError(
            f"Runner command failed with exit code {completed.returncode}: {raw.strip()}"
        )

    parsed = parse_json_from_output(completed.stdout or "")
    plugins = normalize_list(parsed.get("actual_plugins"))
    skills = normalize_list(parsed.get("actual_skills"))
    return plugins, skills, raw

def evaluate(
    cases: list[EvalCase],
    runner: str,
    fixtures_path: Path | None,
    command_template: str | None,
) -> list[EvalResult]:
    fixtures = {}
    if fixtures_path is not None:
        fixtures = json.loads(fixtures_path.read_text(encoding="utf-8"))

    results: list[EvalResult] = []

    for case in cases:
        try:
            if runner == "fixture":
                actual_plugins, actual_skills, raw = run_fixture(case, fixtures)
            elif runner == "command":
                if not command_template:
                    raise ValueError("--command is required for command runner.")
                actual_plugins, actual_skills, raw = run_command(case, command_template)
            else:
                raise ValueError(f"Unsupported runner: {runner}")

            plugin_match = compare(case.expected_plugins, actual_plugins)
            skill_match = compare(case.expected_skills, actual_skills)

            # Empty expected lists mean that dimension is not asserted.
            if not case.expected_plugins:
                plugin_match = True
            if not case.expected_skills:
                skill_match = True

            results.append(
                EvalResult(
                    source=case.source,
                    id=case.id,
                    prompt=case.prompt,
                    expected_plugins=case.expected_plugins,
                    expected_skills=case.expected_skills,
                    actual_plugins=actual_plugins,
                    actual_skills=actual_skills,
                    plugin_match=plugin_match,
                    skill_match=skill_match,
                    passed=plugin_match and skill_match,
                    runner=runner,
                    raw_output=raw,
                )
            )
        except Exception as exc:
            results.append(
                EvalResult(
                    source=case.source,
                    id=case.id,
                    prompt=case.prompt,
                    expected_plugins=case.expected_plugins,
                    expected_skills=case.expected_skills,
                    actual_plugins=[],
                    actual_skills=[],
                    plugin_match=False,
                    skill_match=False,
                    passed=False,
                    runner=runner,
                    error=str(exc),
                )
            )

    return results

def write_json(results: list[EvalResult], path: Path) -> None:
    payload = {
        "summary": {
            "total": len(results),
            "passed": sum(1 for x in results if x.passed),
            "failed": sum(1 for x in results if not x.passed),
        },
        "results": [asdict(x) for x in results],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def write_markdown(results: list[EvalResult], path: Path) -> None:
    passed = sum(1 for x in results if x.passed)
    failed = len(results) - passed

    lines = [
        "# AgentKit Runtime Eval Report",
        "",
        f"- Total: **{len(results)}**",
        f"- Passed: **{passed}**",
        f"- Failed: **{failed}**",
        "",
        "| Case | Plugins | Skills | Result |",
        "|---|---|---|---|",
    ]

    for result in results:
        plugins = ", ".join(result.actual_plugins) or "—"
        skills = ", ".join(result.actual_skills) or "—"
        status = "PASS" if result.passed else "FAIL"
        lines.append(f"| `{result.id}` | {plugins} | {skills} | **{status}** |")

    failures = [x for x in results if not x.passed]
    if failures:
        lines.extend(["", "## Failures", ""])
        for item in failures:
            lines.append(f"### {item.id}")
            lines.append("")
            lines.append(f"Prompt: {item.prompt}")
            lines.append("")
            lines.append(f"- Expected plugins: `{item.expected_plugins}`")
            lines.append(f"- Actual plugins: `{item.actual_plugins}`")
            lines.append(f"- Expected skills: `{item.expected_skills}`")
            lines.append(f"- Actual skills: `{item.actual_skills}`")
            if item.error:
                lines.append(f"- Error: `{item.error}`")
            lines.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def main() -> int:
    parser = argparse.ArgumentParser(description="AgentKit runtime routing eval harness")
    parser.add_argument(
        "--cases",
        default="evals/*/cases.json",
        help="Glob relative to repo root. Default: evals/*/cases.json",
    )
    parser.add_argument(
        "--runner",
        choices=["fixture", "command"],
        default="fixture",
        help="How actual routing results are obtained.",
    )
    parser.add_argument(
        "--fixtures",
        default="evals/runtime/fixtures.json",
        help="Fixture JSON for fixture runner.",
    )
    parser.add_argument(
        "--command",
        help=(
            "Shell command template for command runner. "
            "Use {prompt} and {id}; command must emit JSON with "
            "actual_plugins and actual_skills."
        ),
    )
    parser.add_argument(
        "--json-out",
        default="evals/runtime/results.json",
    )
    parser.add_argument(
        "--markdown-out",
        default="evals/runtime/results.md",
    )
    args = parser.parse_args()

    cases = load_cases(args.cases)
    if not cases:
        print("No eval cases found.", file=sys.stderr)
        return 2

    fixtures_path = ROOT / args.fixtures if args.runner == "fixture" else None

    results = evaluate(
        cases=cases,
        runner=args.runner,
        fixtures_path=fixtures_path,
        command_template=args.command,
    )

    write_json(results, ROOT / args.json_out)
    write_markdown(results, ROOT / args.markdown_out)

    total = len(results)
    passed = sum(1 for x in results if x.passed)
    failed = total - passed

    print(f"AgentKit Runtime Eval: {passed}/{total} passed, {failed} failed")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
