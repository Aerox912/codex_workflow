<!-- codex-workflow-id: viettran-edgeAI/codex_workflow -->
<!-- codex-workflow-managed-start -->
# AGENTS.md

## Design Principles

- Keep modules cohesive, interfaces explicit, coupling minimal, and behavior
  testable, replaceable, and reusable.
- Define proportionate acceptance and verification before implementation. Never
  weaken coverage, assertions, or failure visibility to save time or tokens.
- Avoid unnecessary process and safeguards. Preserve unrelated user work and
  use verified facts in durable documentation.
- Medium and Heavy define available capabilities, ownership boundaries, and
  fixed safety limits. They do not prescribe a task-independent execution plan.
  The main agent designs the orchestration appropriate to the actual task.

Project personalization and project-local instructions are in protected regions
at the end of this file. They override conflicting workflow defaults, but not
higher-level instructions.

## Working State

- `deployment state`: planning or executing a broad, possibly multi-session
  deployment plan.
- `leaf state`: work outside that plan, including general questions and small,
  bounded edits or operations.

## Project Documentation

The durable project documents are under `agent_docs/`:

- `project_overview.md`: goals, architecture, workflow, and major decisions.
- `project_core_tech.md`: concise special technology or architecture notes.
- `project_structure.md`: layout, modules, components, and ownership.
- `project_progress.md`: goal, overall progress, current position, next milestone.
- `project_diary.md`: distilled decisions, discarded approaches, mistakes, and
  reusable lessons.
- `latest_session_work.md`: detailed handoff evidence and continuation point.
- Module-specific documents, when present.

`project_progress.md` and `latest_session_work.md` may be edited only in
`deployment state` or when the user explicitly requests it. The main agent owns
them during normal execution. During automatic deployment closure, the single
`closure_steward` owns reconciliation of the complete documentation framework;
no other worker participates in that closure update.

Keep raw logs, temporary reasoning, and short-lived checkpoints out of durable
documents. Give each fact one canonical home. Never delete a main project
document without warning the user and receiving a second explicit confirmation.

## Route Selection

There are three routes:

- **Light**: leaf-state work. The main agent works directly; no subagents.
- **Medium**: the main agent owns planning, diagnosis, implementation, and
  verification. Companion, Investigator, and Closure Steward provide only their
  bounded support capabilities. Read `~/.codex/codex_workflow/medium_route.md`.
- **Heavy**: the main agent can delegate bounded production, verification,
  documentation, project-context, and Internet-research work to the roles in
  `~/.codex/codex_workflow/heavy_route.md`.

The user selects the route. If unspecified, use Light; do not infer Medium or
Heavy. Keep the selected route until the user changes it or the session ends.
Medium and Heavy imply `deployment state` only for substantive work.

Questions and small or odd bounded tasks use the direct main-agent fast path
even when Medium or Heavy is selected. On that path, call no worker, including
Companion and Closure Steward, and produce no deployment token report.

## Medium and Heavy Contracts

For a substantive Medium or Heavy deployment, initialize one persistent
Companion with `agent_type="companion"`, `task_name="companion"`, and
`fork_turns="none"`, or reuse the existing target. Its first brief for each
deployment gives the goal, route, relevant constraints, a lowercase
underscore-safe deployment ID, and this exact standalone marker:

```text
codex-workflow-deployment-start: <deployment_id>
```

The marker defines the reporting boundary used by Closure Steward. A route
change reuses the same Companion. If Companion is unavailable, continue only
when safe and report the limitation.

Role ownership follows the source of the work:

- Companion is the persistent read-only project-context worker. Its source
  domain is the project ecosystem: repository material, `agent_docs/`, local
  modules and dependencies, sibling project material made available locally,
  source, tests, logs, configuration, Git history, and project artifacts. It
  does not perform Internet research.
- Investigator is a disposable read-only Internet researcher. Give it any
  bounded external-information question for which Internet research is useful.
  It adapts its search and sources to the question and returns a concise,
  source-linked synthesis. It does not implement or make the project's final
  decision.

The main agent combines project context and external information, and owns task
direction, architecture, scope, causal and acceptance decisions, integration,
final claims, and user communication. It decides dynamically whether roles are
needed, how many to use, what to ask, and how to sequence, run concurrently,
reuse, repair, or stop them within the selected route's fixed limits. Do not
introduce a mandatory investigation wave, intake ritual, evidence schema,
repair loop, deployment sequence, or other task-independent gate.

The main agent directly creates and coordinates its workers. Do not create an
LLM lifecycle parent merely to operate another group of workers. Concurrent
mutable assignments must have non-overlapping ownership. Treat worker reports
as evidence, inspect decision-critical material when necessary, and avoid
repeating fresh, credible checks without a reason.

In Heavy, every production task capsule distributes enough of the main agent's
knowledge for the executor to act well: the intended outcome, relevant project
context, ownership and protected boundaries, settled decisions and constraints,
useful references, task-specific guidance, interfaces or risks that matter, and
acceptance expectations. Adapt the capsule to the task; this list is guidance,
not a fixed form. The executor owns bounded local discovery, implementation,
self-check, and ordinary repair within the assigned surface.

Before the final response that completes, pauses, or blocks each substantive
Medium or Heavy deployment, run the automatic handoff in
`closure_steward.md` exactly once. Closure Steward reconciles `agent_docs/`,
seals its work, invokes `$deployment-token-report`, and returns its handoff plus
the six-column table. Wait for that worker and relay both results. The handoff
is not a user command, and Companion is not used for token reporting.

## Platform Paths

Workflow documents use `/` as a platform-neutral separator. Translate paths to
the current operating system and shell when running filesystem commands.
<!-- codex-workflow-managed-end -->

<!-- codex-workflow-project-personalization-start -->
<!-- codex-workflow-project-personalization-end -->

<!-- codex-workflow-project-local-instructions-start -->
<!-- codex-workflow-project-local-instructions-end -->
