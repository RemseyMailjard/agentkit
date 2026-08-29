# AgentKit Core — Standalone ChatGPT Skills v0.1

Some agentkit-core micro-tools are useful on their own, outside the composed
Skills that normally invoke them. This packages a curated subset as
standalone Agent Skills bundles (https://agentskills.io/specification) for
upload to ChatGPT Work, independent of the agentkit-core plugin's routing
surface.

## Why curated, not all micro-tools

Micro-tools are deliberately internal and composable (see
`docs/agentkit-core-microtools-v0.1.md`): narrow responsibility, no side
effects, not marketplace entry points. Publishing all ~29 as standalone
ChatGPT skills would reintroduce the trigger-ambiguity problem that design
avoided — overlapping "check this" / "find risks" phrasing across two dozen
skills in a plain ChatGPT conversation. Instead, only micro-tools with clear
standalone value (useful without the surrounding Skill's orchestration) are
published, one at a time, as demand is confirmed.

## v0.1 curated set

- `clarity-checker`
- `risk-scanner`
- `evidence-checker`
- `tone-fit-checker`
- `root-cause-analyzer`
- `option-comparator`
- `requirement-quality-checker`
- `edge-case-finder`

## Source of truth

The original `plugins/agentkit-core/micro-tools/<name>/MICROTOOL.md` remains
the source of truth for behavior. The generated skill only adds Agent Skills
frontmatter (`name`, `description`, `metadata.origin_path`) around the same
instructions — it does not fork the logic.

## Pipeline

```text
plugins/agentkit-core/micro-tools/<name>/MICROTOOL.md
  -> scripts/package_microtool_as_skill.py --curated
  -> distribution/chatgpt-skills/<name>/SKILL.md   (generated, not committed)
  -> scripts/build_chatgpt_skill_zips.py --all
  -> dist/chatgpt-skills/<name>.zip                (generated, not committed)
  -> upload via ChatGPT Work: Create -> Upload
```

Descriptions are hand-curated in `scripts/chatgpt_skill_descriptions.json`
because Agent Skills routing quality depends on an explicit "what + when"
sentence that a generic template cannot produce reliably. Adding a new
curated tool means adding its description there first — packaging fails
loudly otherwise.

## Adding a new curated tool

1. Add an entry to `scripts/chatgpt_skill_descriptions.json` (what it does +
   when to use it, 1-1024 chars).
2. Add the tool name to this doc's curated set.
3. Add a routing eval case to `evals/agentkit-core/cases-chatgpt-skills.json`.
4. Run `python scripts/package_microtool_as_skill.py --curated` and
   `python scripts/build_chatgpt_skill_zips.py --all`.

## Known gap

Upload to ChatGPT Work is currently manual (UI: Create -> Upload -> zip).
No CI step or `POST /v1/skills` automation exists yet.
