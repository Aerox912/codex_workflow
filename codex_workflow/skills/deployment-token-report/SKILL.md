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

Confirm that the deployment's first Companion brief contained this exact line
with a unique lowercase underscore-safe ID:

```text
codex-workflow-deployment-start: <deployment_id>
```

Run the bundled `scripts/report_tokens.py` with `--deployment-id` and
`--format markdown`. Let it use `CODEX_THREAD_ID` to identify this Closure
Steward rollout, resolve its parent main-agent thread, find the exact marker in
user or assistant message text in the persistent Companion rollout, and read
only metadata and token-count fields beneath `~/.codex/sessions/`. Accept the
marker when surrounded by Markdown or explanatory prose. Exclude guardian
sessions.

Return the script's six-column Markdown table verbatim to the main agent. Do
not add pricing, estimates, inferred usage, or another statistics table. If the
script fails or warns that evidence is incomplete, report that limitation
instead of repairing or inventing values.

The required table template is exactly:

```text
| Agent | Quantity | Rollouts | Cached input | Input | Output |
| --- | ---: | ---: | ---: | ---: | ---: |
| <agent role> | <count> | <count> | <tokens> | <tokens> | <tokens> |
```

Do not rename, reorder, add, or remove columns. Preserve every data row emitted
by the script, including its final `main agent` row.

Interpret `Input` as total input tokens, including the cached-input subset, and
`Rollouts` as model generations with a `last_token_usage` record. Stop totals
when the script starts, excluding Closure Steward's post-tool final response
and the main agent's later final response.
