# codex_workflow 1.2.2 — Route isolation and flexible research support

- Light no longer receives the `agent_docs/` framework, intake, documentation
  ownership, or deployment handoff instructions. Those contracts live in the
  Medium and Heavy route documents. Light's subagent prohibition is removed.
- Medium and Heavy preserve the direct fast path for standalone questions,
  searches, read-only research, and small bounded tasks. These tasks skip
  deployment intake, automatic project-document updates, closure, and token
  reporting. Research supporting an active deployment remains part of it.
- The main chooses Explorer and Investigator counts for each bounded question.
  Parallel workers are recommended for difficult or broad problems when
  independent evidence improves coverage; there are no role-specific quotas.
- Senior Executor now uses `gpt-6.1-sol` with `high` reasoning.
- `codex_workflow --version` reports the locally installed workflow version
  without checking the network or requiring a project.
- Installation can initialize documentation for an empty project without
  requiring an overview first; missing context is recorded instead of invented.

Release assets: `codex_workflow-1.2.2.zip` and `SHA256SUMS`.

Validation passed: 60 runtime tests, 9 token-report tests, package-schema
validation, and release archive verification.
