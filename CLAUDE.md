# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

AgentKit is the Skills4-IT **Codex plugin marketplace**: a collection of modular AI
capabilities (plugins → skills) for MCP (Model Context Protocol) engineering, delivered
as markdown-defined Skills plus a marketplace manifest. There is no application code to
build, lint, or test in the traditional sense — the "product" is the set of `SKILL.md`
workflow definitions, the plugin/marketplace JSON manifests, and the eval cases that
verify routing behavior.

## Architecture

```text
Marketplace (.agents/plugins/marketplace.json)
  -> Plugin (plugins/<plugin-name>/.codex-plugin/plugin.json)
     -> Skill / Workflow (plugins/<plugin-name>/skills/<skill-name>/SKILL.md)
        -> Micro-capability
```

- `.agents/plugins/marketplace.json` registers each plugin (name, source path,
  install/auth policy, category). Adding a new plugin means adding an entry here that
  points at `./plugins/<name>`.
- `plugins/<plugin-name>/.codex-plugin/plugin.json` declares plugin metadata (name,
  version, description, keywords, `skills` dir, interface/display info, default
  prompts). This is what Codex uses to list and present the plugin.
- `plugins/<plugin-name>/skills/<skill-name>/SKILL.md` is the actual capability
  definition — a self-contained, task-focused workflow doc.
- `evals/<plugin-name>/cases.json` holds behavioral eval cases (routing, quality,
  safety, ambiguous-request handling) that verify a given prompt routes to the expected
  skill and satisfies specific `quality_checks`.
- `docs/architecture.md` is the canonical architecture doc — keep it and this file in
  sync when the layering changes.

### Plugins

**MCP Builder** (`plugins/mcp-builder/`, v0.2, flagship) — Developer Tools. Six focused
skills under `plugins/mcp-builder/skills/`: `create-mcp-server`, `create-mcp-tool`,
`review-mcp-server`, `reverse-engineer-api`, `secure-mcp-server`, `test-mcp-server`.
Skills intentionally overlap only where a real workflow crosses boundaries — routing
evals should make those boundaries observable.

**.NET Reviewer** (`plugins/dotnet-reviewer/`, v0.1) — Developer Tools. Review and
remediation workflows for .NET repositories under `plugins/dotnet-reviewer/skills/`:
`review-dotnet`, `review-aspnet-api`, `review-ef-core`, `review-security`,
`fix-findings`. Follows the same review-before-remediation split as MCP Builder —
`fix-findings` is a separate, explicit workflow from the review skills.

**Lab Generator** (`plugins/lab-generator/`, v0.1) — Education. Instructional-design
workflows for hands-on IT labs under `plugins/lab-generator/skills/`: `create-lab`,
`create-challenge`, `review-lab`, `test-lab`, `adapt-lab`.

## Design principles (apply to any new skill/plugin)

1. Capability-first, not endpoint-first — model business capabilities, don't mirror API
   endpoints 1:1.
2. Small, composable skills rather than one large monolithic workflow.
3. Review before remediation — reviewing/analyzing a server and changing it are
   separate workflows unless a task explicitly requires both.
4. Security and testing are explicit, separate workflows (`secure-mcp-server`,
   `test-mcp-server`), not implicit side effects of building.
5. Evaluations live alongside the capabilities they verify (`evals/<plugin>/cases.json`
   next to `plugins/<plugin>/`).
6. Practical outputs must work in real repositories — no fake/placeholder
   implementations presented as done.
7. Never claim execution success (tests run, commands executed) without actual
   evidence.

## Contribution rules (from AGENTS.md)

- Keep skills small and task-focused.
- Add or update eval cases in `evals/` whenever routing behavior changes.
- Do not weaken security controls or tests to make generated code appear successful.
- Do not claim commands/tests were executed unless execution evidence exists.
- Keep plugin manifests (`plugin.json`, `marketplace.json`) and repository URLs current.

### Quality bar for every skill, in any plugin

Each `SKILL.md` must define:

1. When the skill should be used.
2. When it should not be used, or which neighboring skill is preferable instead.
3. A repeatable workflow.
4. Safety or side-effect considerations.
5. A concrete output contract.
6. At least one corresponding eval case in `evals/<plugin-name>/cases.json`.
