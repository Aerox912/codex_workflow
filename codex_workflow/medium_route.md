# Medium Route

Use after Medium is selected under `AGENTS.md`.

## Your Ownership

You are the main agent. Own planning, diagnosis, implementation, verification,
integration, and user communication. Keep production implementation, production
repair, root-cause decisions, and verification in your own role.

Use only these support roles:

| Role | Ownership |
| --- | --- |
| Companion | Keep one persistent read-only worker for context in the project ecosystem. Assign bounded project-context work and use its retained operational context. Keep Internet research outside this role. |
| Investigator | Create a disposable read-only worker for bounded external-information research on the Internet. Use its synthesis as evidence; retain project discovery and decisions yourself. |
| Closure Steward | Create one fresh worker at deployment closure to reconcile `agent_docs/` and produce the Deployment Token Report. Keep implementation and verification in your own role. |

## Required Documentation Read

The first time the session enters `deployment state` under either Medium or
Heavy, and before planning, modifying files, or dispatching a worker, directly
read the complete current `agent_docs/` framework exactly once:

- `project_overview.md`, `project_core_tech.md`, and `project_structure.md`;
- `project_progress.md`, `project_diary.md`, and `latest_session_work.md`;
- every module-specific Markdown document under `agent_docs/`.

Treat this as one shared session-level read across both routes. After it
completes, do not directly reopen or reread any framework document during the
rest of the session, including later deployments or route changes. Reuse the
retained context. When freshness or a later document change matters, assign
Companion a bounded delta or conflict check instead of reading the document
again yourself. If a required document is missing or unreadable during the
initial read, report the intake blocker and do not treat deployment entry as
complete.

## Initialize Companion

For each substantive Medium deployment, initialize one persistent Companion
with `agent_type="companion"`, `task_name="companion"`, and
`fork_turns="none"`, or reuse the existing target. In its first brief, provide
the goal, route, relevant constraints, a lowercase underscore-safe deployment
ID, and this exact standalone marker:

```text
codex-workflow-deployment-start: <deployment_id>
```

Use this marker as Closure Steward's reporting boundary. Reuse the same
Companion after a route change. If Companion is unavailable, continue when safe
and report the limitation.

## Assign Support Work

Decide whether Investigator is useful, what Companion should handle, and how
support work relates to your implementation. Assign a support capability only
when it fits the task.

Start each initial support package with **Task ID**, a logical identifier unique
within the deployment. Then use the capsule for that role:

| Role | Capsule parts |
| --- | --- |
| Companion | **Project Context Scope**; **Context Task + Goal**; **Main-Agent Context Guidance** |
| Investigator | **Research Context**; **Research Question + Goal**; **Main-Agent Research Guidance** |

Treat these named parts as the complete structure. Use Task ID to correlate
dispatch, reports, follow-ups, and artifacts. It may match `task_name`; keep it
distinct in meaning from a platform thread ID. Require each worker to echo Task
ID in every report. Repeat it in follow-ups and send only the delta. Treat the
Companion deployment marker and Closure Steward brief as lifecycle exceptions.
Use the package format to standardize communication while retaining the
ownership defined above.

## Fixed Boundaries

- Never create a production executor, tester, or normal doc-writer package in
  Medium. Retain that work yourself.
- Keep at most 20 active subagents in the session, including Companion,
  Investigators, and Closure Steward. Use one persistent Companion and at most
  one Closure Steward at a time.
- Give support workers bounded questions and sufficient context. Own all
  material interpretations and final claims.
- Preserve unrelated work, verify in proportion to risk, and never claim an
  unrun check passed.

Within those boundaries, choose the task-specific topology, order, concurrency,
tools, checkpoints, and response to failures. Work directly when a support role
adds no value.

## Fast Path and Closure

Use the direct fast path for questions and small or odd bounded tasks. Do not
initialize Companion or another worker, call Closure Steward, or produce a
deployment token report for that path.

Before the final response that completes, pauses, or blocks a substantive
deployment, follow `~/.codex/codex_workflow/closure_steward.md` exactly once.
Pass only the route, a unique deployment ID, and closure state. Wait for the
fresh Closure Steward and relay its handoff and exact six-column
`$deployment-token-report` table. Create a new ID, handoff, and report for each
later substantive deployment.
