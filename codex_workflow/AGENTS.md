<!-- codex-workflow-id: viettran-edgeAI/codex_workflow -->
<!-- codex-workflow-managed-start -->
# AGENTS.md

## Design Principles

- Keep modules cohesive, interfaces explicit, coupling minimal, and behavior
  testable, replaceable, and reusable.
- Define proportionate acceptance and verification before implementation. Never
  weaken coverage, assertions, or failure visibility to save time or tokens.
- Avoid unnecessary process or safeguards; preserve unrelated user work and use
  verified facts in durable documentation.

## Working State

-`deployment state` : planning or executing a broad, possibly multi-session deployment plan.
- `leaf state` : otherwise, including general questions and small bounded operations.

## Project Documentation

Use the durable project documents under `agent_docs/`:

- `project_overview.md`: goals, architecture, workflow, and major decisions.
- `project_core_tech.md`: concise special technology or architecture notes.
- `project_structure.md`: layout, modules, components, and ownership.
- `project_progress.md`: goal, overall progress, current position, next milestone.
- `project_diary.md`: distilled decisions, discarded approaches, mistakes, and
  reusable lessons.
- `latest_session_work.md`: detailed handoff evidence and continuation point.
- Module-specific documents, when present.

In deployment state, you own `project_diary.md` and record only lasting
decisions, discarded approaches, mistakes, and reusable lessons. Archivist owns
assigned project and public documentation from verified facts, including
overview, structure, core technologies, and closing updates to progress and
latest-session documents. Assign module documents explicitly. Perform a direct
user-requested document edit yourself outside deployment.

Keep raw logs, temporary reasoning, and short-lived checkpoints out of durable
documents; give each fact one canonical home. Never delete a main project
document without warning and a second explicit confirmation.

## Route Selection

Select one of these routes: **Light** works directly in leaf state without subagents;
**Medium** keeps planning, diagnosis, implementation, and verification with the
main agent and uses bounded support from `~/.codex/codex_workflow/medium_route.md`;
**Heavy** delegates bounded production, verification, documentation,
project-context, and Internet research under `~/.codex/codex_workflow/heavy_route.md`.

Follow the user's route selection. Use Light when none is selected; do not infer
Medium or Heavy. Keep the route until the user changes it or the session ends.
Enter deployment state for Medium or Heavy only when the work is substantive.

## Rollout Efficiency

Batch independent reads, searches, metadata checks, and other known-input
operations. Keep dependencies and overlapping mutations sequential. In Medium or
Heavy, dispatch independent workers, wait for the
relevant set, and synthesize their reports once.

Read personalization and project-local instructions from the protected regions
at the end of this file. Apply them over workflow defaults subject to higher
instruction priority.

## Required Documentation Read

On the first `deployment state` entry under either route, before planning,
modifying files, or dispatching a worker, directly read the complete current
`agent_docs/` framework exactly once: overview, core technology, structure,
progress, diary, latest session work.

This is one shared session-level read across both routes; reuse it for later
deployments and route changes. Assign Companion a bounded delta or conflict
check when documentation changes or freshness matters. Missing or unreadable
required documents leave deployment entry incomplete; report the intake blocker.

## Platform Paths

Interpret `/` as a platform-neutral separator and translate paths for the
current operating system and shell.
<!-- codex-workflow-managed-end -->

<!-- codex-workflow-project-personalization-start -->
<!-- codex-workflow-project-personalization-end -->

<!-- codex-workflow-project-local-instructions-start -->
<!-- codex-workflow-project-local-instructions-end -->
