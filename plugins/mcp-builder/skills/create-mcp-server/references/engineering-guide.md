# Create MCP Server — Engineering Guide

## Workflow
1. Inspect repository, API and constraints.
2. Identify human and agent use cases.
3. Build a capability map around business tasks.
4. Decide tool vs resource vs prompt.
5. Define input/output/error contracts.
6. Design authentication and authorization.
7. Classify write, destructive, privileged and sensitive operations.
8. Implement domain logic behind a thin MCP surface.
9. Add configuration, secrets handling, logging and backend adapters.
10. Add tests, examples and setup documentation.

## Minimum test matrix
Cover valid input, invalid input, missing required values, empty results, backend failure, malformed backend response and auth failure where relevant.

## Quality bar
Avoid fake TODO implementations. Make side effects explicit. Prefer structured output. Keep tool names discriminative enough for model selection.
