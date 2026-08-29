# .NET Reviewer v0.1

Second flagship plugin for AgentKit by Skills4-IT.

## Skills

- `review-dotnet`
- `review-aspnet-api`
- `review-ef-core`
- `review-security`
- `fix-findings`

## Core design rule

**Review is separate from remediation.**

Use specialized skills when the request is clearly scoped to ASP.NET Core, EF Core
or security. Use the general reviewer only for broad repository-level review.

## Cross-plugin routing

A .NET MCP server can legitimately involve both:

- `.NET Reviewer / review-security`
- `MCP Builder / secure-mcp-server`

The first reviews .NET application security. The second reviews MCP-specific
agent/tool security. Findings should be separated by layer and not duplicated.
