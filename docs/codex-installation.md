# Installing AgentKit via Codex CLI

This repository is a Codex plugin marketplace (see [architecture.md](./architecture.md)).
For a personal ChatGPT Plus account, the reliable install route is the **Codex CLI**,
not ChatGPT Workspace settings — workspace-level marketplace import is a managed
workspace/admin feature and is generally not available on a personal Plus workspace.

## Prerequisites

The repository must contain at minimum:

```text
agentkit/
├── .agents/
│   └── plugins/
│       └── marketplace.json
└── plugins/
    └── mcp-builder/
        ├── .codex-plugin/
        │   └── plugin.json
        └── skills/
            ├── create-mcp-server/
            │   └── SKILL.md
            ├── create-mcp-tool/
            │   └── SKILL.md
            ├── review-mcp-server/
            │   └── SKILL.md
            └── reverse-engineer-api/
                └── SKILL.md
```

Codex discovers plugins through `marketplace.json`; each plugin also carries its own
`.codex-plugin/plugin.json`. This repo already satisfies this layout for all five
registered plugins (`mcp-builder`, `dotnet-reviewer`, `lab-generator`,
`training-creator`, `onenote`).

## Steps

1. **Add the GitHub repo as a marketplace.** Run this in a terminal with the Codex CLI
   available:

   ```bash
   codex plugin marketplace add RemseyMailjard/agentkit --ref main
   ```

   A GitHub `owner/repo` is an officially supported marketplace source.

2. **Verify Codex sees it:**

   ```bash
   codex plugin marketplace list
   ```

3. **List available plugins:**

   ```bash
   codex plugin list --available --json
   ```

   `mcp-builder` (and the other plugins registered in `marketplace.json`) should
   appear here.

4. **Install a plugin.** The marketplace name comes from the top-level `"name"` field
   in [`.agents/plugins/marketplace.json`](../.agents/plugins/marketplace.json), which
   is `"skills4it"`:

   ```bash
   codex plugin add mcp-builder@skills4it
   ```

   Syntax: `codex plugin add <plugin>@<marketplace>`.

5. **Confirm the install:**

   ```bash
   codex plugin list
   ```

   `mcp-builder` should now show as installed.

## Using it

Start a **new Codex thread** after installing or reinstalling a plugin, so the plugin
and any MCP tools it brings load cleanly.

Example prompt, using the plugin generically:

```text
Use the MCP Builder plugin.

Design an MCP server for a CRM with these capabilities:
- customer.search
- customer.get
- customer.create
- customer.notes.append

Use .NET 10 and ASP.NET Core.
First create the capability map and architecture.
Do not implement anything yet.
```

Or activate a specific skill directly:

```text
$create-mcp-server

Build an MCP server around this API.
```

## Codex app (GUI)

In the graphical Codex app, check **Plugins** in the sidebar. Official plugins can be
installed directly there; for a personal GitHub-based marketplace like this one, the
CLI route above is currently the more reliable path.
