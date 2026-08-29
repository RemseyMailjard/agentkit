# Live Codex Benchmark Policy

The AgentKit CI pipeline does not currently require:

- `OPENAI_API_KEY`
- Codex CLI installation
- unattended Codex authentication
- paid OpenAI API usage

The MCP Builder live benchmark assets remain in the repository for optional local or future use.

Current CI focuses on deterministic checks:

- AgentKit structural validator
- routing eval harness
- official `plugin-eval analyze`
- benchmark fixture validation
- golden workflow artifacts

A future release may re-enable real `codex exec` benchmarking when the desired authentication and runner strategy is finalized.
