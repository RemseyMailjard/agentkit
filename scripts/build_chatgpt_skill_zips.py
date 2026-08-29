#!/usr/bin/env python3
"""Zip packaged Agent Skills bundles for upload to ChatGPT Work.

Reads distribution/chatgpt-skills/<name>/ (produced by
scripts/package_microtool_as_skill.py) and writes dist/chatgpt-skills/<name>.zip,
each containing exactly one top-level folder and exactly one SKILL.md, per the
Agent Skills zip rules: max 50MB zip, max 500 files, max 25MB per uncompressed
file (https://agentskills.io/specification).
"""
from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "distribution" / "chatgpt-skills"
OUTPUT_DIR = ROOT / "dist" / "chatgpt-skills"

MAX_ZIP_BYTES = 50 * 1024 * 1024
MAX_FILE_COUNT = 500
MAX_FILE_BYTES = 25 * 1024 * 1024


def validate_bundle(bundle_dir: Path) -> list[Path]:
    files = [p for p in bundle_dir.rglob("*") if p.is_file()]
    if not files:
        raise ValueError(f"{bundle_dir} contains no files")

    skill_md_count = sum(1 for p in files if p.name.lower() == "skill.md")
    if skill_md_count != 1:
        raise ValueError(
            f"{bundle_dir} must contain exactly one SKILL.md/skill.md, found {skill_md_count}"
        )

    if len(files) > MAX_FILE_COUNT:
        raise ValueError(f"{bundle_dir} has {len(files)} files, exceeds max {MAX_FILE_COUNT}")

    for f in files:
        size = f.stat().st_size
        if size > MAX_FILE_BYTES:
            raise ValueError(f"{f} is {size} bytes, exceeds max {MAX_FILE_BYTES} per file")

    return files


def build_zip(name: str, bundle_dir: Path, files: list[Path]) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = OUTPUT_DIR / f"{name}.zip"

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            # arcname keeps the single top-level "<name>/" folder required by the spec.
            arcname = Path(name) / f.relative_to(bundle_dir)
            zf.write(f, arcname)

    zip_size = zip_path.stat().st_size
    if zip_size > MAX_ZIP_BYTES:
        raise ValueError(f"{zip_path} is {zip_size} bytes, exceeds max {MAX_ZIP_BYTES}")

    return zip_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "names",
        nargs="*",
        help="skill bundle names under distribution/chatgpt-skills/ to zip; omit for --all",
    )
    parser.add_argument("--all", action="store_true", help="zip every bundle present")
    args = parser.parse_args()

    if not SOURCE_DIR.exists():
        print(
            f"ERROR: {SOURCE_DIR} does not exist; run scripts/package_microtool_as_skill.py first",
            file=sys.stderr,
        )
        return 2

    if args.all:
        names = sorted(p.name for p in SOURCE_DIR.iterdir() if p.is_dir())
    elif args.names:
        names = args.names
    else:
        parser.error("provide bundle names, or pass --all")
        return 2

    errors = 0
    for name in names:
        bundle_dir = SOURCE_DIR / name
        if not bundle_dir.is_dir():
            print(f"ERROR: no bundle at {bundle_dir}", file=sys.stderr)
            errors += 1
            continue
        try:
            files = validate_bundle(bundle_dir)
            zip_path = build_zip(name, bundle_dir, files)
            print(f"built {zip_path} ({len(files)} files, {zip_path.stat().st_size} bytes)")
        except ValueError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            errors += 1

    if errors:
        print(f"{errors} bundle(s) failed to zip", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
