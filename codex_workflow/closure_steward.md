# Closure Steward

Use this automatic closure once after every substantive Medium or Heavy
deployment, before the post-deployment token report and main agent's final
response. It also applies
when a deployment pauses or blocks. Questions and small or odd bounded tasks on
the direct fast path do not use this handoff or produce a deployment token
report.

Spawn one fresh worker with:

- `agent_type="closure_steward"`
- `task_name="closure_steward_<deployment_id>"`, where the suffix is a unique,
  lowercase, underscore-safe deployment identifier
- `fork_turns="200"`

Pass only the active route, deployment ID, closure state (`complete`, `paused`,
or `blocked`), and the persistent Companion target returned by its original
spawn. Do not summarize the session, build a task capsule, or maintain a usage
ledger. The automatic finite fork passes recent main-agent turns so the worker
inherits the deployment context while retaining its Luna xhigh model; its TOML
contains the full procedure.

The worker alone reconciles the complete `agent_docs/` framework, performs
compact closing checks, inspects and reports relevant Git status, and returns the
final handoff report. It may inspect other documents for conflicts but never
edits outside `agent_docs/`. It never stages or commits automatically; any
commit remains a separate, explicitly authorized user action.
Do not call a second documentation worker or duplicate these steps. As its last
tool action, Closure Steward triggers the existing Companion's separate
`$deployment-token-report` handoff and then returns directly to the main agent.
Wait for both workers to become terminal, relay the closure result, and print
Companion's table. Do not send another Companion request. Create a fresh
uniquely named Closure Steward for every later substantive deployment in the
same session.

If the worker cannot be created or is blocked, report that limitation. Do not
silently transfer the handoff to Companion or another role.
