# Skills4-IT AgentKit — Technical Specification

**Document:** `SPEC.md`  
**Project:** Skills4-IT AgentKit  
**Purpose:** Codex Plugin Marketplace / AI Capability Platform  
**Status:** Initial Architecture Specification  
**Target repository:** `agentkit`  
**Primary platform:** OpenAI Codex / ChatGPT Plugins  
**Secondary goal:** Portable architecture for other agent ecosystems where practical  
**Last architectural review:** 2026-08-29

---

# 1. Executive Summary

AgentKit is a GitHub-based marketplace of reusable AI capabilities.

The project must evolve into a maintainable platform containing specialized plugins for software development, Microsoft technologies, AI development, training development, MCP integrations, and organizational knowledge.

Initial planned plugins:

```text
dotnet-reviewer
mcp-builder
lab-generator
training-creator
power-platform
azure
m365-copilot
notebuddy
```

The architecture must support:

```text
Marketplace
    ↓
Plugins
    ↓
Skills
    ↓
Instructions / workflows / references
    ↓
Apps / MCP / APIs / tools
```

The first complete reference implementation MUST be:

```text
dotnet-reviewer
```

Do not attempt to fully implement every plugin before the reference implementation works end-to-end.

---

# 2. Product Vision

AgentKit should become:

> A reusable Skills4-IT AI Capability Platform that packages specialized expertise, workflows, tools, integrations and quality standards as installable AI plugins.

It should allow an AI system to perform tasks such as:

```text
Review this .NET repository.

Build an MCP server for this API.

Turn this Microsoft technology into a hands-on lab.

Create a professional training course from these requirements.

Review this Power Automate flow.

Design an Azure architecture.

Build a Microsoft 365 Copilot solution.

Search and store knowledge using NoteBuddy.
```

The platform must prioritize:

- modularity;
- reuse;
- composability;
- clear capability boundaries;
- predictable AI behavior;
- maintainability;
- testability;
- documentation;
- extensibility.

---

# 3. External Platform Facts

The implementation must respect the current OpenAI plugin architecture.

At the time of this specification:

- Codex supports plugin marketplaces imported from GitHub.
- The Codex marketplace manifest is located at:

```text
.agents/plugins/marketplace.json
```

- A plugin may contain skills.
- A plugin may reference apps.
- A plugin may contain or reference MCP configuration.
- A plugin may consist only of skills.
- Marketplace repositories may be public or private GitHub repositories.
- Workspace administrators can import a marketplace.
- Marketplace content can be synchronized from GitHub.
- Workspace policies remain separate from repository configuration.
- Importing a plugin does not automatically grant access to external systems.
- Authentication and app permissions remain controlled separately.
- Plugins declaring MCP configuration may have surface limitations such as Desktop-only behavior.

The implementation MUST NOT assume that repository configuration overrides workspace permissions.

---

# 4. Important Architecture Rule

Distinguish between:

## OpenAI-defined files

Files whose names, locations or schemas are required by the Codex/plugin platform.

Examples include:

```text
.agents/plugins/marketplace.json
.codex-plugin/plugin.json
.app.json
mcp.json
.mcp.json
```

where applicable.

## AgentKit-defined files

Internal files introduced by this repository for maintainability.

Examples:

```text
plugin-spec.md
tests/
references/
standards/
examples/
schemas/
evals/
```

AgentKit-defined conventions must NEVER be confused with official OpenAI requirements.

When modifying platform manifests:

> Verify the current official OpenAI specification before introducing undocumented schema fields.

---

# 5. Target Repository Architecture

Preferred target architecture:

```text
agentkit/
│
├── README.md
├── SPEC.md
├── AI-CONTEXT.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
│
├── .agents/
│   └── plugins/
│       └── marketplace.json
│
├── plugins/
│   │
│   ├── dotnet-reviewer/
│   │   ├── .codex-plugin/
│   │   │   └── plugin.json
│   │   │
│   │   ├── README.md
│   │   ├── plugin-spec.md
│   │   │
│   │   ├── skills/
│   │   │   ├── repository-review/
│   │   │   ├── architecture-review/
│   │   │   ├── code-quality-review/
│   │   │   ├── security-review/
│   │   │   ├── performance-review/
│   │   │   └── test-review/
│   │   │
│   │   ├── references/
│   │   ├── examples/
│   │   ├── evals/
│   │   └── tests/
│   │
│   ├── mcp-builder/
│   ├── lab-generator/
│   ├── training-creator/
│   ├── power-platform/
│   ├── azure/
│   ├── m365-copilot/
│   └── notebuddy/
│
├── shared/
│   ├── standards/
│   ├── templates/
│   ├── instructions/
│   ├── schemas/
│   └── evals/
│
├── examples/
│
├── tests/
│
└── tools/
```

This is the target architecture, not a requirement to create every empty directory immediately.

Only create directories when they add value.

---

# 6. Marketplace Responsibility

The Marketplace has exactly one responsibility:

> Discover and expose available AgentKit plugins.

The Marketplace should NOT contain detailed implementation logic.

Conceptually:

```text
marketplace.json
        │
        ├── dotnet-reviewer
        ├── mcp-builder
        ├── lab-generator
        ├── training-creator
        ├── power-platform
        ├── azure
        ├── m365-copilot
        └── notebuddy
```

Each Marketplace entry should point to a plugin source supported by the current Codex marketplace specification.

---

# 7. Marketplace Manifest

Required location:

```text
.agents/plugins/marketplace.json
```

The manifest must contain the plugins that are ready for distribution.

Do NOT register unfinished plugins merely because a directory exists.

Development lifecycle:

```text
planned
↓
experimental
↓
validated
↓
marketplace-ready
↓
published
```

Only:

```text
marketplace-ready
published
```

plugins should normally appear in the main Marketplace.

Experimental plugins may later use a separate development marketplace if needed.

---

# 8. Plugin Contract

Every AgentKit plugin MUST have one clear responsibility.

A plugin must define:

```text
Identity
Purpose
Target users
Activation scenarios
Inputs
Outputs
Skills
Dependencies
External tools
Quality rules
Security considerations
Examples
Tests
```

Every plugin MUST have:

```text
README.md
plugin-spec.md
```

and the platform-required plugin manifest where applicable.

---

# 9. plugin-spec.md Contract

Every plugin's `plugin-spec.md` must contain at least:

```markdown
# Plugin Name

## Purpose

## Problems solved

## Intended users

## When to use

## When not to use

## Inputs

## Outputs

## Skills

## Dependencies

## External integrations

## Security considerations

## Quality requirements

## Failure behavior

## Examples

## Tests

## Definition of Done
```

This is an AgentKit project convention.

---

# 10. Skill Design Contract

A skill represents one reusable specialist capability.

A good skill should be:

```text
focused
composable
testable
predictable
self-contained where possible
```

Bad skill:

```text
do-everything
```

Good skills:

```text
architecture-review
security-review
generate-lab
validate-lab
design-mcp-tools
review-power-automate-flow
```

---

# 11. Skill Responsibility

Each skill should answer:

```text
WHAT task does this skill perform?

WHEN should the model use it?

WHAT input does it need?

WHAT process should it follow?

WHAT output should it produce?

HOW should quality be checked?

WHEN should it stop?
```

Avoid vague instructions such as:

```text
Act as an expert and provide the best answer.
```

Prefer operational instructions.

Example:

```text
Inspect the repository structure.

Identify project boundaries.

Determine architecture style.

Identify coupling and dependency problems.

Rank findings by impact.

Provide evidence for every significant finding.

Propose concrete remediation.

Do not modify source code unless explicitly requested.
```

---

# 12. Skill Output Contracts

Where possible, skills should use predictable output structures.

Example review contract:

```text
Summary

Critical findings

High-priority findings

Medium-priority findings

Suggestions

Positive observations

Recommended next actions
```

Individual findings should preferably follow:

```text
Severity
Area
Finding
Evidence
Impact
Recommendation
```

This makes outputs easier for both humans and downstream agents to process.

---

# 13. Plugin Composition

Plugins should be composable.

Example:

```text
mcp-builder
    ↓
dotnet-reviewer
    ↓
lab-generator
    ↓
training-creator
```

Possible workflow:

```text
Design MCP solution
↓
Generate implementation
↓
Review implementation
↓
Generate exercises
↓
Create complete training
```

Skills should therefore avoid unnecessary assumptions about who invoked them.

---

# 14. Shared Components

Anything reused by at least two plugins should be considered for placement under:

```text
shared/
```

Examples:

```text
shared/standards/
shared/templates/
shared/instructions/
shared/evals/
```

Potential shared assets:

```text
Microsoft writing conventions
review severity model
security rules
output templates
training didactics
lab structure
repository-analysis patterns
MCP design standards
```

Do not move something into `shared` solely because it might someday be reusable.

Use the Rule of Two:

> Abstract into shared infrastructure when at least two real consumers exist.

---

# 15. Reference Plugin

The first production-quality plugin MUST be:

```text
dotnet-reviewer
```

Its purpose is to establish the AgentKit reference architecture.

All later plugins should reuse its successful conventions where appropriate.

---

# 16. dotnet-reviewer — Purpose

`dotnet-reviewer` analyzes C#/.NET projects and repositories and produces actionable technical reviews.

Primary domains:

```text
C#
.NET
ASP.NET Core
Entity Framework Core
solution architecture
testing
security
performance
maintainability
dependencies
cloud readiness
```

The initial version does NOT need external APIs.

This minimizes dependencies and makes it ideal for validating the plugin architecture.

---

# 17. dotnet-reviewer — Initial Skills

Version 1 should include:

```text
repository-review
architecture-review
code-quality-review
test-review
```

Version 2 may add:

```text
security-review
performance-review
dependency-review
cloud-readiness-review
```

Do not implement all review categories at once if that delays an end-to-end usable version.

---

# 18. repository-review Skill

Purpose:

> Perform a structured high-level review of an entire .NET repository.

Process:

```text
1. Inspect repository structure.
2. Identify solution and project files.
3. Identify application type.
4. Determine important dependencies.
5. Determine architecture boundaries.
6. Inspect representative implementation code.
7. Inspect configuration.
8. Inspect testing strategy.
9. Detect major risks.
10. Produce prioritized recommendations.
```

Output:

```text
Repository Overview
Architecture Summary
Strengths
Critical Issues
High Priority Issues
Medium Priority Issues
Quick Wins
Recommended Roadmap
```

---

# 19. architecture-review Skill

Evaluate:

```text
project boundaries
layering
dependency direction
coupling
cohesion
domain boundaries
DI architecture
application services
infrastructure concerns
configuration boundaries
API boundaries
data access architecture
```

The skill must avoid blindly prescribing architecture patterns.

For example:

> Do not recommend Clean Architecture merely because the repository does not use Clean Architecture.

Recommendations must be evidence-based.

---

# 20. code-quality-review Skill

Evaluate:

```text
readability
complexity
duplication
naming
error handling
async usage
nullability
resource management
logging
configuration handling
testability
maintainability
C# idioms
```

Every significant issue should identify concrete evidence.

---

# 21. test-review Skill

Evaluate:

```text
unit tests
integration tests
test organization
test isolation
important missing coverage
test naming
mocks
fixtures
edge cases
failure paths
API testing
data-layer testing
```

Do not optimize solely for coverage percentage.

Prioritize:

> confidence in important system behavior.

---

# 22. Severity Model

Use a shared severity model.

## Critical

Likely to cause:

```text
security compromise
data corruption
major production failure
loss of critical functionality
```

## High

Significant architecture, reliability, security or maintainability risk.

## Medium

Important improvement but unlikely to create immediate severe failure.

## Low

Minor quality improvement.

## Suggestion

Optional enhancement or stylistic recommendation.

Avoid severity inflation.

---

# 23. Evidence Requirement

Reviews MUST distinguish:

```text
observed fact
inference
recommendation
```

Example:

Bad:

```text
The architecture is badly designed.
```

Good:

```text
Observed:
Project A directly references Project Infrastructure.

Impact:
Business logic now depends on infrastructure implementation.

Recommendation:
Introduce an abstraction at the application boundary if dependency inversion
is a project requirement.
```

---

# 24. No-Hallucination Rule

If repository evidence is insufficient:

```text
state the uncertainty
```

Do not invent:

```text
files
classes
methods
dependencies
configuration
security vulnerabilities
runtime behavior
```

A finding should be traceable to available evidence whenever possible.

---

# 25. Repository Modification Rule

Review plugins should default to:

```text
analyze first
modify second
```

Do not silently rewrite source code while performing a review.

If implementation changes are requested:

```text
review
↓
propose
↓
implement
↓
validate
```

---

# 26. mcp-builder Plugin

Purpose:

> Design, implement, review and troubleshoot Model Context Protocol integrations.

Planned skills:

```text
mcp-solution-design
mcp-tool-design
mcp-resource-design
mcp-prompt-design
mcp-server-builder
mcp-security-review
mcp-debugger
```

Supported implementation stacks may include:

```text
Python
FastMCP
TypeScript
C#
.NET
Cloudflare Workers
Azure Functions
remote HTTP MCP
```

Do not lock the plugin to one implementation language.

---

# 27. lab-generator Plugin

Purpose:

> Convert technical topics into validated hands-on labs.

Required lab structure:

```text
Title

Scenario

Level

Duration

Learning objectives

Prerequisites

Environment

Exercise 1
Exercise 2
...

Validation

Expected result

Troubleshooting

Challenge

Cleanup

What you learned
```

Potential skills:

```text
generate-lab
validate-lab
debug-lab
adjust-difficulty
generate-solution
```

---

# 28. training-creator Plugin

Purpose:

> Design complete professional technical training experiences.

Training philosophy:

```text
simple explanation first
↓
demonstration
↓
guided practice
↓
technical depth
↓
independent challenge
↓
reflection
```

Training content should prioritize realistic scenarios.

Possible skills:

```text
training-needs-analysis
course-outline
module-generator
exercise-generator
assessment-generator
trainer-guide
slide-content-generator
```

---

# 29. power-platform Plugin

Scope:

```text
Power Apps
Power Automate
Dataverse
Copilot Studio
Power Platform ALM
governance
architecture
connectors
security
```

Possible skills:

```text
power-apps-review
power-automate-review
flow-builder
dataverse-design
copilot-studio-design
power-platform-architecture
alm-review
governance-review
```

---

# 30. azure Plugin

Scope:

```text
Azure architecture
Azure Functions
App Service
Storage
SQL
identity
networking
security
monitoring
cost
deployment
troubleshooting
```

Potential skills:

```text
azure-architecture
azure-security-review
azure-cost-review
azure-deployment-review
azure-troubleshooting
azure-functions-builder
```

Avoid turning this plugin into a complete copy of Microsoft Learn.

The plugin should focus on actionable workflows.

---

# 31. m365-copilot Plugin

Scope:

```text
Microsoft 365 Copilot
Copilot Studio
agents
Microsoft Graph
enterprise knowledge
connectors
MCP
governance
adoption
```

Potential skills:

```text
agent-design
copilot-use-case-design
knowledge-source-design
copilot-governance-review
copilot-adoption-plan
copilot-studio-agent-builder
```

---

# 32. NoteBuddy Plugin

NoteBuddy should eventually demonstrate a tool-backed AgentKit plugin.

Architecture:

```text
Codex / ChatGPT
        ↓
NoteBuddy Plugin
        ↓
NoteBuddy capability layer
        ↓
MCP / App
        ↓
Microsoft Graph
        ↓
OneNote
```

Potential operations:

```text
knowledge.find
knowledge.get
knowledge.save
knowledge.upsert
knowledge.append
knowledge.findOrCreateSection
```

NoteBuddy should NOT be required for AgentKit core operation.

It is an optional integration plugin.

---

# 33. Apps vs MCP

Treat Apps and MCP as integration mechanisms rather than business logic.

Preferred separation:

```text
Skill
    ↓
Capability contract
    ↓
Integration
    ↓
External system
```

Example:

```text
knowledge-search skill
        ↓
knowledge.find
        ↓
NoteBuddy
        ↓
OneNote
```

This reduces coupling.

---

# 34. MCP Surface Constraint

Because current plugin behavior may treat plugins declaring MCP server configuration differently across product surfaces, plugin design must explicitly document:

```text
Codex support
ChatGPT Web support
ChatGPT Desktop support
authentication requirements
workspace requirements
```

Do not assume that a remote MCP URL automatically means universal web compatibility.

---

# 35. Security Architecture

Every tool-enabled plugin must document:

```text
data read
data written
external systems
authentication
authorization
sensitive actions
destructive actions
network dependencies
```

Prefer least privilege.

Initial implementation preference:

```text
read-only
```

before introducing:

```text
write
delete
send
publish
deploy
```

operations.

---

# 36. Human Approval Boundaries

Plugins must not attempt to bypass platform approval mechanisms.

Actions such as:

```text
sending messages
deleting data
deploying production systems
changing permissions
publishing externally
moving money
```

should respect host-platform confirmation and permission policies.

---

# 37. Secrets

Never commit:

```text
API keys
access tokens
passwords
client secrets
private certificates
connection strings containing credentials
```

Use:

```text
environment variables
secret managers
platform connection configuration
```

Provide:

```text
.env.example
```

only where development requires environment configuration.

Never populate it with real secrets.

---

# 38. Testing Strategy

Testing exists at multiple levels.

## Level 1 — Structure validation

Validate:

```text
required files exist
JSON parses
paths resolve
references exist
plugin names are unique
marketplace sources resolve
```

## Level 2 — Skill validation

Test whether a skill:

```text
activates appropriately
follows required process
produces required structure
avoids prohibited behavior
```

## Level 3 — Scenario evaluation

Use realistic input scenarios.

Example:

```text
small ASP.NET Core API
poor architecture sample
well-structured repository
repository with missing tests
repository with security issues
```

## Level 4 — Integration validation

Where tools exist:

```text
authentication
read operations
write operations
failure handling
permissions
rate limits
```

## Level 5 — End-to-end validation

Test actual installation and invocation through supported Codex/ChatGPT surfaces.

---

# 39. Evaluation Architecture

Each mature plugin should eventually have:

```text
evals/
```

Evals should include:

```text
positive cases
negative cases
ambiguous cases
adversarial cases
boundary cases
```

Evaluate:

```text
correctness
completeness
evidence quality
instruction following
false-positive rate
usefulness
format stability
```

---

# 40. Golden Scenarios

Each plugin should eventually have 3–10 golden scenarios.

Example for `dotnet-reviewer`:

```text
01-clean-api
02-layering-violation
03-no-tests
04-async-problems
05-large-god-service
06-good-architecture
```

An important golden scenario must be:

```text
well-designed repository
```

The reviewer must be capable of saying:

> No significant problem found.

AI quality is not measured by the number of criticisms produced.

---

# 41. Test Fixtures

Avoid depending exclusively on large external repositories.

Where useful, maintain minimal fixtures under:

```text
tests/fixtures/
```

Fixtures should demonstrate one concept clearly.

Example:

```text
tests/
└── fixtures/
    └── dotnet/
        ├── clean-api/
        ├── architecture-violation/
        └── missing-tests/
```

---

# 42. CI Validation

Introduce GitHub Actions once core structure exists.

Initial CI should validate:

```text
JSON syntax
required manifests
broken relative paths
duplicate plugin identifiers
missing required project files
Markdown links where practical
```

Later CI may include:

```text
schema validation
eval execution
unit tests
integration tests
security scanning
```

---

# 43. Marketplace Validation Script

Eventually provide a script such as:

```text
tools/validate-marketplace
```

Possible implementation:

```text
.NET
Python
Node
```

Choose the simplest stack already justified by the repository.

The validator should check:

```text
marketplace manifest exists
manifest parses
plugin source exists
plugin manifest exists
plugin name uniqueness
required documentation exists
referenced files exist
```

Do not create a complex custom framework before it is needed.

---

# 44. Versioning

Use semantic versioning where plugin versioning is supported:

```text
MAJOR.MINOR.PATCH
```

Interpretation:

```text
PATCH
minor fixes

MINOR
backward-compatible capabilities

MAJOR
breaking behavior or contract change
```

Marketplace and plugin version semantics should follow platform requirements where those requirements differ.

---

# 45. Changelog

Repository-level changes should be recorded in:

```text
CHANGELOG.md
```

Significant plugin-specific changes may additionally be documented within plugin directories.

---

# 46. Documentation Layers

Use four documentation levels.

## Repository README

For humans discovering AgentKit.

## SPEC.md

Technical source of truth for architecture.

## AI-CONTEXT.md

Context optimized for AI agents working on the project.

## Plugin README

Human explanation for one plugin.

## plugin-spec.md

Technical contract for one plugin.

Do not duplicate full content between all documentation files.

Cross-reference instead.

---

# 47. Root README Goal

The root README should explain in less than approximately five minutes:

```text
What AgentKit is
Why it exists
What plugins exist
How to install/import
How to use a plugin
How to contribute
```

---

# 48. AI Development Rules

Any AI agent modifying this repository MUST:

```text
1. Inspect existing files first.

2. Read SPEC.md.

3. Read the relevant plugin-spec.md.

4. Preserve working architecture.

5. Prefer small coherent changes.

6. Do not invent platform manifest fields.

7. Verify official platform requirements when uncertain.

8. Avoid creating unnecessary frameworks.

9. Add tests for meaningful behavior.

10. Update documentation when contracts change.

11. Never commit secrets.

12. Validate before declaring completion.
```

---

# 49. Change Discipline

Prefer:

```text
one capability
one coherent implementation
one validation path
```

over:

```text
many half-built capabilities
```

A plugin should progress vertically.

Example:

```text
manifest
↓
one skill
↓
test
↓
example
↓
actual Codex invocation
```

before adding five more skills.

---

# 50. Definition of Done — Skill

A skill is done when:

- purpose is documented;
- activation conditions are clear;
- required inputs are documented;
- workflow is explicit;
- output contract exists;
- failure behavior is defined;
- at least one realistic example exists;
- at least one positive test exists;
- at least one negative or boundary test exists;
- instructions do not depend on hidden knowledge;
- no known broken paths exist.

---

# 51. Definition of Done — Plugin

A plugin is done when:

- plugin manifest is valid;
- plugin can be discovered by its marketplace;
- README exists;
- plugin-spec exists;
- at least one useful skill works;
- required dependencies are documented;
- installation requirements are documented;
- security implications are documented;
- realistic examples exist;
- validation passes;
- end-to-end invocation has been tested on the intended surface.

---

# 52. Definition of Done — Marketplace

The AgentKit Marketplace v1 is done when:

```text
.agents/plugins/marketplace.json
```

is valid and:

- it can be imported into the intended OpenAI workspace;
- at least one plugin imports successfully;
- `dotnet-reviewer` can be selected;
- one `dotnet-reviewer` capability works end-to-end;
- a real repository can be reviewed;
- output follows the documented contract;
- plugin updates can be synchronized from GitHub;
- installation instructions are documented;
- validation runs automatically or reproducibly.

---

# 53. MVP Scope

AgentKit Marketplace MVP should contain exactly enough infrastructure to prove:

```text
GitHub repository
        ↓
Marketplace
        ↓
Plugin
        ↓
Skill
        ↓
Codex
        ↓
Useful result
```

Recommended MVP:

```text
Marketplace
└── dotnet-reviewer
    └── repository-review
```

Do not make MCP a prerequisite for the MVP.

Do not make NoteBuddy a prerequisite for the MVP.

Do not require Azure infrastructure for the MVP.

---

# 54. Phase 1 — Foundation

Deliver:

```text
SPEC.md
AI-CONTEXT.md
README.md
marketplace manifest
plugin directory conventions
dotnet-reviewer manifest
dotnet-reviewer README
dotnet-reviewer plugin-spec
```

Success condition:

> Marketplace recognizes the plugin structure.

---

# 55. Phase 2 — First Working Skill

Build:

```text
dotnet-reviewer/repository-review
```

Validate against at least:

```text
one small .NET repository
one intentionally problematic sample
```

Success condition:

> The AI generates a useful evidence-based repository review.

---

# 56. Phase 3 — Quality Layer

Add:

```text
tests
fixtures
evals
validation script
CI
```

Success condition:

> Breaking marketplace or plugin structure is detected automatically.

---

# 57. Phase 4 — Expand dotnet-reviewer

Add:

```text
architecture-review
code-quality-review
test-review
```

Then:

```text
security-review
performance-review
dependency-review
```

only where justified.

---

# 58. Phase 5 — Second Plugin

Recommended second plugin:

```text
mcp-builder
```

Reason:

It validates that AgentKit supports implementation-oriented capabilities rather than only reviews.

Start with:

```text
mcp-solution-design
```

before automatically generating complex MCP servers.

---

# 59. Phase 6 — Training Toolchain

Implement:

```text
lab-generator
training-creator
```

Target composition:

```text
technology/topic
↓
lab-generator
↓
validated lab
↓
training-creator
↓
training module
```

This becomes one of AgentKit's major differentiators.

---

# 60. Phase 7 — Microsoft Technology Plugins

Implement incrementally:

```text
power-platform
azure
m365-copilot
```

Avoid building giant Microsoft knowledge dumps.

Each plugin should provide operational workflows.

---

# 61. Phase 8 — Tool-backed Plugins

Introduce:

```text
NoteBuddy
```

and potentially other integrations.

This validates:

```text
skills
+
external tools
+
persistent knowledge
```

---

# 62. Future Multi-Agent Architecture

Do NOT build a complex multi-agent orchestrator during MVP.

However, maintain compatibility with future role separation:

```text
Planner
Architect
Developer
Reviewer
Security Reviewer
Tester
Documentation Agent
Training Agent
```

Plugins should therefore expose capabilities that can be independently composed.

Potential future workflow:

```text
User Goal
   ↓
Planner
   ↓
Architect
   ↓
Developer
   ↓
Reviewer
   ↓
Tester
   ↓
Documentation
```

AgentKit provides the capabilities.

An orchestration layer decides which capability to invoke.

These are separate concerns.

---

# 63. Future Capability Model

Long-term conceptual architecture:

```text
                  AgentKit

                     │
        ┌────────────┼────────────┐
        │            │            │
      Skills        Apps         MCP
        │            │            │
        └────────────┼────────────┘
                     │
                Capabilities
                     │
        ┌────────────┼────────────┐
        │            │            │
       Dev         Training     Microsoft
        │            │            │
     .NET/MCP      Labs        Azure/M365/
                              Power Platform
```

---

# 64. Non-Goals

AgentKit v1 is NOT:

```text
a full autonomous software company
a replacement for GitHub
a generic prompt repository
a new MCP protocol implementation
a full Microsoft documentation mirror
a proprietary agent runtime
a mandatory cloud service
```

Avoid scope creep into these areas.

---

# 65. Architecture Principle — Thin Plugin, Rich Capability

Plugins should primarily package and expose capabilities.

Avoid deeply coupling business logic to marketplace packaging.

Preferred:

```text
Capability
   ↓
Plugin packaging
```

rather than:

```text
Plugin-specific implementation
that cannot be reused anywhere else
```

This will make future portability easier.

---

# 66. Architecture Principle — Progressive Enhancement

Start with:

```text
instructions
```

then add:

```text
structured skills
```

then:

```text
tools
```

then:

```text
apps / MCP
```

only where they improve the capability.

A tool should not be added simply because AgentKit supports tools.

---

# 67. Architecture Principle — Evidence Before Automation

First make the AI perform the workflow correctly.

Then automate it.

Example:

```text
manual repository review skill
↓
validated output
↓
structured evaluator
↓
automated repository inspection
↓
optional tool integration
```

---

# 68. Architecture Principle — Capability Over Technology

Organize around user outcomes.

Prefer:

```text
repository-review
```

over:

```text
roslyn-parser
```

Prefer:

```text
create-hands-on-lab
```

over:

```text
markdown-generator
```

Implementation technology is secondary to capability.

---

# 69. Repository Naming Rules

Use:

```text
lowercase-kebab-case
```

for:

```text
plugin names
skill names
directories
```

Examples:

```text
dotnet-reviewer
mcp-builder
architecture-review
training-creator
```

Avoid:

```text
DotNetReviewer
dotnet_reviewer
Dotnet Reviewer
```

unless a platform-specific requirement dictates otherwise.

---

# 70. Quality Gate Before Merge

Before merging significant changes:

```text
[ ] structure valid
[ ] JSON valid
[ ] tests pass
[ ] examples still work
[ ] documentation updated
[ ] no secrets
[ ] no dead references
[ ] no unnecessary duplicated instructions
[ ] plugin scope remains coherent
[ ] backward compatibility considered
```

---

# 71. AI Implementation Priority

If an AI model is asked:

> Continue building AgentKit.

It should choose work in this priority order:

```text
1. Fix broken current functionality.

2. Complete unfinished reference-plugin functionality.

3. Add validation.

4. Improve tests.

5. Improve documentation.

6. Complete next planned vertical slice.

7. Only then introduce new plugin families.
```

---

# 72. Autonomous AI Handoff Instruction

An AI agent receiving this specification is authorized to continue implementation without repeatedly requesting architectural approval, provided that:

```text
the change follows this specification;
the change is reversible through Git;
no secrets are exposed;
no production system is destructively modified;
no undocumented platform schema is invented.
```

When uncertain:

```text
inspect repository
↓
consult current official platform documentation
↓
choose smallest safe implementation
↓
test
↓
document
```

---

# 73. Required First Autonomous Task

When beginning from an early AgentKit repository state:

```text
TASK:
Implement the smallest end-to-end AgentKit Marketplace vertical slice.
```

Target:

```text
.agents/plugins/marketplace.json
        ↓
dotnet-reviewer
        ↓
repository-review
        ↓
working Codex invocation
```

Steps:

```text
1. Inspect existing repository.

2. Preserve valid existing work.

3. Validate marketplace structure against current OpenAI documentation.

4. Complete dotnet-reviewer plugin packaging.

5. Implement repository-review.

6. Add one realistic example.

7. Add structural validation.

8. Document installation.

9. Test marketplace import.

10. Test actual repository review.

11. Record remaining issues.

12. Continue to the next vertical slice.
```

---

# 74. Product Success Criteria

AgentKit succeeds when adding a new capability becomes predictable.

Desired future development experience:

```text
Define problem
↓
Create plugin or select existing plugin
↓
Create skill
↓
Add examples
↓
Add evals
↓
Validate
↓
Publish to marketplace
↓
Use from Codex/ChatGPT
```

The user should not need to reinvent AI workflows for each project.

---

# 75. Long-Term Product Direction

AgentKit may eventually become three things simultaneously:

## Internal Skills4-IT Platform

Reusable capabilities for development, consulting and training.

## Public Developer Marketplace

Reusable high-quality plugins other professionals can install.

## Commercial Capability Platform

Premium plugins, workflows, training tooling and integrations could eventually become Skills4-IT products.

Potential categories:

```text
Development
Microsoft Cloud
AI Engineering
Training
Productivity
Knowledge
Governance
Automation
```

---

# 76. Final Architecture Statement

AgentKit must remain:

```text
simple at the core
modular at the capability level
strict at the contract level
extensible at the integration level
testable at every layer
```

The fundamental abstraction is:

> A plugin packages capabilities.  
> A skill defines a repeatable workflow.  
> An integration connects the workflow to external systems.  
> The Marketplace distributes those capabilities.

---

# 77. Immediate Next Milestone

The next milestone is:

## AgentKit Marketplace MVP

Deliver:

```text
Marketplace manifest
+
dotnet-reviewer plugin
+
repository-review skill
+
validation
+
example
+
documentation
+
successful Codex test
```

Completion criterion:

> A user can import the AgentKit Marketplace from GitHub, select `dotnet-reviewer`, point Codex at a real .NET repository, and receive a structured, evidence-based technical review.

Once this works, use it as the template for every subsequent AgentKit plugin.