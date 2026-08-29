# AgentKit Validation

AgentKit includes a lightweight repository validator.

## Local use

```bash
python scripts/validate_agentkit.py
```

The command exits with code `1` when blocking validation errors are found.

## Current checks

### Marketplace

- `.agents/plugins/marketplace.json` is valid JSON;
- plugin names are unique;
- local plugin paths exist;
- marketplace names and paths are consistent;
- policy shape is checked.

### Plugin manifests

- manifest exists for every marketplace plugin;
- plugin name matches marketplace name;
- version uses semantic versioning;
- core metadata exists;
- skills path exists;
- optional MCP configuration exists and is valid JSON.

### Skills

- every skill has `SKILL.md`;
- frontmatter exists;
- `name` exists;
- `description` exists;
- skill name is compared with its folder name.

### Evals

- every `evals/*/cases.json` file is valid JSON;
- eval files contain arrays;
- eval IDs are present and unique per file;
- prompts are non-empty;
- quality checks have the expected structure;
- missing routing expectations produce warnings.

### Platform docs

The validator warns when key architecture files are absent.

## CI

`.github/workflows/validate-agentkit.yml` runs the same validator:

- on pull requests;
- on pushes to `main`;
- manually through `workflow_dispatch`.

## Deliberate limitations in v0.1

The validator does not yet:

- execute Codex Plugin Eval;
- prove semantic routing correctness;
- validate against an official JSON schema;
- execute plugin code;
- verify remote MCP endpoints;
- perform security scanning.

Those belong in later validation stages.
