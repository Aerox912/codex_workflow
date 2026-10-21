# Archivist Assignments

Before assigning a worker, apply `~/.codex/codex_workflow/agent_lifecycle.md`.
Collect relevant reports and release finished workers as needed to admit
Archivist; the role need not remain resident during other work.

Use Archivist for verified documentation work in Medium or Heavy. Give each
assignment a Task ID and the Documentation Context + Audience, Documentation
Task + Goal, and Main-Agent Documentation Guidance capsule. Identify the write
surface and provide verified facts or exact evidence references. Require the
smallest durable update that preserves current decisions, state, limitations,
and a recoverable continuation point; remove stale or redundant detail instead
of accumulating session history.
A new package has a new Task ID and full capsule; a continuation keeps the
Task ID and supplies only changed parts.

Choose the number, timing, and reuse of Archivist workers according to the task.
Give concurrent workers non-overlapping document ownership. Ordinary assignments
normally use `agent_type="archivist"` and `fork_turns="none"`.
Installation guides may assign new or still-template progress, diary, and
latest-session documents to Archivist for initialization; subsequent deployment
updates to those three documents belong to the main.

## Deployment Closure

Assign one Archivist to close each substantive deployment before the final
response, including paused or blocked work. First finish your own required
updates to `agent_docs/project_progress.md`, `agent_docs/project_diary.md`, and
`agent_docs/latest_session_work.md`. Keep those files outside Archivist's write
scope, but identify them as the canonical deployment-state sources for the
handoff. Combine other verified documentation updates with this assignment when
practical. Include the exact deployment ID, closure state (`complete`, `paused`,
or `blocked`), and read-only Git handoff.

Reuse an Archivist when its retained context plus a concise delta is sufficient.
Otherwise create one with `agent_type="archivist"`, a unique underscore-safe
task name, and `fork_turns="all"` when the inherited context fits its model.
Reference that fork as documentation context and supply only missing scope and
guidance. Otherwise use `fork_turns="none"` with the canonical deployment-state
documents and targeted verified evidence references as its context. Use only
fork values accepted by the current spawn schema.

Ensure other workers have finished changes relevant to the handoff before
Archivist seals it. Assign only one reporting owner for each deployment. Wait
for its documentation handoff and exact six-column `$deployment-token-report`
table, preserve both before releasing its slot, then relay them without
repeating its operational checks. A later
substantive deployment uses a new ID and receives its own closure and report.

Standalone questions, searches, read-only research, and small bounded leaf tasks
skip deployment closure and token reporting. Assign ordinary documentation work
only for an explicit request or verified changes to durable project knowledge.
If Archivist is unavailable or blocked, report the limitation and remaining work
accurately.
