#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SCORE_RE = re.compile(r"^\s*-\s*Score:\s*(\d+)\s*/\s*100\s*$", re.MULTILINE)
CHECKS_RE = re.compile(
    r"^\s*-\s*Checks:\s*(\d+)\s+fail,\s*(\d+)\s+warn,\s*(\d+)\s+info\s*$",
    re.MULTILINE,
)
GRADE_RE = re.compile(r"^\s*-\s*Grade:\s*(.+?)\s*$", re.MULTILINE)
RISK_RE = re.compile(r"^\s*-\s*Risk:\s*(.+?)\s*$", re.MULTILINE)

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enforce deterministic policy over an OpenAI plugin-eval markdown report."
    )
    parser.add_argument("report", type=Path)
    parser.add_argument("--minimum-score", type=int, default=80)
    parser.add_argument("--require-zero-fails", action="store_true")
    args = parser.parse_args()

    if not args.report.exists():
        print(f"ERROR: report not found: {args.report}", file=sys.stderr)
        return 2

    text = args.report.read_text(encoding="utf-8", errors="replace")

    score_match = SCORE_RE.search(text)
    checks_match = CHECKS_RE.search(text)

    if not score_match:
        print("ERROR: could not find plugin-eval score in report.", file=sys.stderr)
        return 2

    score = int(score_match.group(1))
    fail_count = int(checks_match.group(1)) if checks_match else None
    warn_count = int(checks_match.group(2)) if checks_match else None
    info_count = int(checks_match.group(3)) if checks_match else None
    grade = GRADE_RE.search(text)
    risk = RISK_RE.search(text)

    print(f"Plugin Eval score: {score}/100")
    if grade:
        print(f"Grade: {grade.group(1)}")
    if risk:
        print(f"Risk: {risk.group(1)}")
    if checks_match:
        print(f"Checks: {fail_count} fail, {warn_count} warn, {info_count} info")

    failures: list[str] = []

    if score < args.minimum_score:
        failures.append(
            f"score {score}/100 is below required minimum {args.minimum_score}/100"
        )

    if args.require_zero_fails:
        if fail_count is None:
            failures.append("could not verify fail count")
        elif fail_count != 0:
            failures.append(f"plugin-eval reports {fail_count} hard failure(s)")

    if failures:
        for failure in failures:
            print(f"QUALITY GATE FAILED: {failure}", file=sys.stderr)
        return 1

    print("QUALITY GATE PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
