# AgentKit Routing Matrix

## Primary routing

| User intent | Primary plugin | Primary skill |
|---|---|---|
| Build an MCP server | MCP Builder | create-mcp-server |
| Add one MCP capability | MCP Builder | create-mcp-tool |
| Review MCP architecture | MCP Builder | review-mcp-server |
| Review MCP security | MCP Builder | secure-mcp-server |
| Test MCP behavior | MCP Builder | test-mcp-server |
| Reverse engineer API for MCP | MCP Builder | reverse-engineer-api |
| General .NET review | .NET Reviewer | review-dotnet |
| ASP.NET Core API review | .NET Reviewer | review-aspnet-api |
| EF Core review | .NET Reviewer | review-ef-core |
| .NET security review | .NET Reviewer | review-security |
| Fix prior .NET findings | .NET Reviewer | fix-findings |
| Create full training | Training Creator | design-training |
| Analyze training need | Training Creator | analyze-training-need |
| Analyze audience | Training Creator | analyze-audience |
| Define objectives | Training Creator | define-learning-objectives |
| Create assessment | Training Creator | create-assessment |
| Create instructor brief | Training Creator | create-instructor-brief |
| Review delivery readiness | Training Creator | review-training-readiness |
| Adapt full training | Training Creator | adapt-training |
| Create one hands-on lab | Lab Generator | create-lab |
| Create challenge | Lab Generator | create-challenge |
| Review lab quality | Lab Generator | review-lab |
| Test lab executability | Lab Generator | test-lab |
| Adapt one lab | Lab Generator | adapt-lab |
| Recall prior OneNote context | OneNote | recall-context |
| Capture durable knowledge | OneNote | capture-knowledge |
| Research prior notes | OneNote | research-memory |
| Build project context | OneNote | project-context |

## Cross-plugin cases

### .NET MCP server security

Use:

```text
.NET Reviewer / review-security
+
MCP Builder / secure-mcp-server
```

Separate findings by layer.

### Technical training

Use:

```text
Training Creator
+
technical plugin
+
Lab Generator
```

### Prior project context

Use:

```text
OneNote / project-context
→ target plugin
```

### Existing course, one exercise only

Use:

```text
Lab Generator
```

Do not invoke Training Creator unless the course itself must change.

## Boundary rules

### Training Creator vs Lab Generator

Training Creator owns:

- audience;
- objectives;
- sequence;
- agenda;
- assessments;
- instructor readiness.

Lab Generator owns:

- one concrete exercise;
- steps;
- checkpoints;
- challenge;
- troubleshooting.

### MCP Builder vs .NET Reviewer

MCP Builder owns:

- MCP capability design;
- tool/resource/prompt modeling;
- MCP-specific security;
- MCP protocol behavior.

.NET Reviewer owns:

- C#/.NET application quality;
- ASP.NET Core behavior;
- EF Core;
- .NET security implementation.

### OneNote vs other plugins

OneNote should not solve the task itself.

It provides relevant durable context to another capability.
