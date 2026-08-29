# .NET Reviewer Architecture

## Purpose

Provide evidence-based .NET repository review and focused remediation.

## Skill boundaries

```text
review-dotnet
├── broad repository quality
│
├── review-aspnet-api
│   └── HTTP + ASP.NET Core behavior
│
├── review-ef-core
│   └── EF Core / data-access behavior
│
├── review-security
│   └── .NET application security
│
└── fix-findings
    └── scoped remediation after review
```

## Cross-plugin case

For a .NET-based MCP server:

```text
.NET application security
→ dotnet-reviewer/review-security

MCP agent/tool security
→ mcp-builder/secure-mcp-server
```

Use both only when both layers are materially relevant.
