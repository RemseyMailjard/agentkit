---
name: project-context
description: >
  Build a concise project context package from relevant OneNote knowledge so another
  AgentKit plugin can continue work with the right history, constraints and decisions.
  Scaffold only.
---

# Project Context

Use before substantial project work when historical OneNote context matters.

## Intended output

- project goal;
- current status;
- decisions already made;
- constraints;
- architecture;
- open risks;
- next actions;
- relevant references.

## Intended orchestration

Examples:

```text
OneNote / project-context
→ Training Creator
```

```text
OneNote / project-context
→ MCP Builder
```

## Boundary

This skill defines the context package only. Backend retrieval is not implemented yet.
