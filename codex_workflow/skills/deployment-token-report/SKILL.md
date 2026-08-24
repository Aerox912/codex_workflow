---
name: deployment-token-report
description: Compile per-agent rollout counts and cached-input, input, and output token totals from Codex local session JSONL after a substantive Medium or Heavy deployment. Use only for the workflow's required post-deployment usage handoff, not for Light/direct-fast-path work or live cost estimation.
---

# Deployment Token Report

<!-- codex-workflow-skill: deployment-token-report -->

Use this skill only as Closure Steward after all documentation reconciliation,
compact checks, and Git inspection are complete. Treat that state as sealed:
after starting this report, do not modify the repository or run another closure
check.

The deployment's first Companion brief must have contained this exact line,
with a unique lowercase underscore-safe ID:

```text
codex-workflow-deployment-start: <deployment_id>
```

Run the bundled `scripts/report_tokens.py` with `--deployment-id` and
`--format markdown`. The script uses `CODEX_THREAD_ID` to identify this Closure
Steward rollout, resolves its parent main-agent thread, finds the exact marker
in the persistent Companion rollout, and reads only metadata and token-count
fields beneath `~/.codex/sessions/`. It excludes guardian sessions.

Return the script's six-column Markdown table verbatim to the main agent. Do
not add pricing, estimates, inferred usage, or another statistics table. If the
script fails or warns that evidence is incomplete, report that limitation
instead of repairing or inventing values.

`Input` is total input tokens and therefore includes the cached-input subset.
`Rollouts` counts model generations that have a `last_token_usage` record.
Totals stop when the script starts, intentionally excluding Closure Steward's
post-tool final response and the main agent's later final response.
