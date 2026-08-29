# Skills4-IT Codex Marketplace — Contributor Instructions

This repository contains Skills4-IT Codex plugins.

## Principles

- Prefer small, composable skills over monolithic instruction files.
- Design agent capabilities around user tasks and business semantics, not raw API endpoints.
- Keep generated implementations testable and production-oriented.
- Never add secrets, tokens or customer data to the repository.
- Treat review and remediation as separate workflows unless explicitly combined.
- Add evaluation cases when adding or materially changing a skill.

## Plugin structure

Each plugin lives under `plugins/<plugin-name>/` and must contain
`.codex-plugin/plugin.json`. Skills belong under `skills/<skill-name>/SKILL.md`.

## Quality bar

A new skill should have:

- a specific routing description;
- clear workflow steps;
- explicit output expectations;
- relevant safety/reliability constraints;
- at least one evaluation case.
