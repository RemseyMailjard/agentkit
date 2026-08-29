# AgentKit Architecture

## Purpose

AgentKit is a marketplace of specialized AI capabilities.

The architecture is intentionally layered.

```text
User intent
   ↓
Marketplace
   ↓
Plugin selection
   ↓
Skill selection
   ↓
Optional multi-skill orchestration
   ↓
Concrete artifact / code / review / training output
```

## Domains

### BUILD

Owns implementation-oriented engineering capabilities.

Current plugin:

- MCP Builder

### QUALITY

Owns analysis, review and remediation quality workflows.

Current plugin:

- .NET Reviewer

### LEARN

Owns instructional design and hands-on learning.

Current plugins:

- Training Creator
- Lab Generator

### KNOW

Owns durable context, knowledge and memory intent.

Current plugin:

- OneNote scaffold

## Ownership rule

Each plugin should own one primary problem space.

When multiple plugins are relevant, divide work by layer.

Example:

```text
.NET MCP server security review

.NET application security
→ .NET Reviewer / review-security

MCP tool and agent security
→ MCP Builder / secure-mcp-server
```

Do not duplicate findings.

## Orchestration rule

Use multiple plugins only when the request genuinely spans multiple responsibilities.

Example:

```text
Create a one-day MCP training for .NET developers

Training Creator
→ learning design

MCP Builder
→ technical MCP correctness

Lab Generator
→ learner practice
```

## Review vs remediation

Default pattern:

```text
review
→ findings
→ explicit remediation
```

Do not silently merge these unless the user asks for both.

## Execution truthfulness

AgentKit must distinguish:

- inspected;
- inferred;
- generated;
- executed;
- validated.

Never claim execution when only static analysis occurred.

## Future shared core

AgentKit should eventually centralize:

- engineering standards;
- security principles;
- testing principles;
- documentation rules;
- eval conventions;
- definition of done.
