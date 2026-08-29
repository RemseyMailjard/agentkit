# AgentKit Core — Standalone ChatGPT Skills v0.2

Supersedes `docs/agentkit-core-chatgpt-skills-v0.1.md`'s curated-subset
scope. All micro-tools are now packaged as standalone Agent Skills bundles
(https://agentskills.io/specification), not just the 8 hand-curated ones.

## Scope change from v0.1

v0.1 deliberately curated a subset of 8 micro-tools to avoid publishing
~29 overlapping "check this" / "find risks" triggers in a flat ChatGPT
skill list. The micro-tool set has since grown to 299, and the decision
was made to publish all of them individually rather than continue
curating a subset. This is a known, accepted trade-off:

- **Cost**: 299 standalone skills with narrow, sometimes overlapping
  descriptions (e.g. `risk-scanner` vs `fix-risk-assessor` vs
  `commercial-risk-detector`) increases the chance ChatGPT picks a
  neighboring skill instead of the intended one for ambiguous prompts.
- **Mitigation applied**: every `SKILL.md` description is derived from
  the micro-tool's own `Responsibility` + `Output` sections (see
  `scripts/chatgpt_skill_descriptions.json`), so at minimum each
  description is concrete and non-generic. 8 of the 299 keep their
  original hand-written v0.1 descriptions; the remaining 291 are
  mechanically generated with the same "what + when" structure.
- **Not mitigated**: cross-tool disambiguation quality has not been
  manually reviewed at this scale. Treat routing accuracy as unverified
  until real usage or `evals/agentkit-core/cases-chatgpt-skills.json`
  (still only 8 cases) is expanded to cover more of the 299.

## Pipeline (unchanged from v0.1)

```text
plugins/agentkit-core/micro-tools/<name>/MICROTOOL.md
  -> scripts/package_microtool_as_skill.py --all
  -> distribution/chatgpt-skills/<name>/SKILL.md   (generated, not committed)
  -> scripts/build_chatgpt_skill_zips.py --all
  -> dist/chatgpt-skills/<name>.zip                (generated, not committed)
  -> upload via ChatGPT Work: Create -> Upload
```

`--curated` still works and packages only the original 8; `--all` packages
every micro-tool. Both read the same `scripts/chatgpt_skill_descriptions.json`.

## Current totals

- 299 micro-tools packaged, 299 zips built, ~519KB total (well under the
  50MB per-zip / 500-file / 25MB-per-file spec limits).
- 0 name collisions.

## If routing problems surface

The fix is not to re-curate from scratch. Two lower-cost options first:

1. Sharpen the specific colliding descriptions in
   `scripts/chatgpt_skill_descriptions.json` (cheap, targeted).
2. Delete/unpublish the individual skills that cause the most confusion,
   rather than the whole set.

Only fall back to re-curating a small subset if targeted fixes don't work.
