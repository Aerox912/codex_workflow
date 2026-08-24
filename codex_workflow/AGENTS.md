<!-- codex-workflow-id: viettran-edgeAI/codex_workflow -->
<!-- codex-workflow-managed-start -->
# AGENTS.md

## Project Context


## Design Principles

- Keep modules cohesive, interfaces explicit, coupling minimal, and behavior
  testable, replaceable, and reusable.
- Define proportionate acceptance and verification before implementation. Keep
  related tests cohesive; never weaken coverage, assertions, or failure
  visibility to save time or tokens.
- Preserve unrelated user work and use verified facts in durable documentation.

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
- `project_diary.md`: lasting decisions, discarded approaches, and lessons. This is experience accumulated during the project development process.
- `latest_session_work.md`: detailed handoff evidence and continuation point.
- Module-specific documents, when present.

`project_progress.md` and `latest_session_work.md` may be edited only in
`deployment state` or when the user explicitly requests it. The main agent owns
them during normal execution. During automatic deployment closure, the single
`closure_steward` worker owns reconciliation of the complete documentation
framework; no other worker participates in that closure update.

Keep raw logs, temporary reasoning, and short-lived checkpoints out of durable
documents. Never delete a main project document without warning the user and
receiving a second explicit confirmation.

## Route Selection

There are three routes:

- **Light**: leaf-state work. The main agent works directly; no subagents.
- **Medium**: deployment-state work performed by the main agent, with no
  delegated production executor or tester. Companion provides workflow-mode
  secretary and context support; an optional read-only evidence wave and the
  documentation-only Closure Steward handoff never own implementation,
  verification, or root-cause decisions. Read
  `~/.codex/codex_workflow/medium_route.md`.
- **Heavy**: deployment-state work orchestrated through specialized workers.
  Read `~/.codex/codex_workflow/heavy_route.md`.

The user selects the route for the session. If unspecified, use Light; do not
infer Medium or Heavy. Light implies `leaf state`; Medium and Heavy imply
`deployment state` only for substantive work. Their direct fast path remains
`leaf state`. Keep the selected route until the user changes it or the session
ends.

## Context Loading

- In Light, inspect only material needed for the current task.
- Before initializing deployment state, classify the request. Questions and
  small or odd bounded tasks use the direct main-agent fast path even when
  Medium or Heavy is selected: call no worker, including Companion and
  `closure_steward`, and produce no deployment token report.
- For every substantive deployment, read the selected route and its Companion
  guide: `medium_companion.md` for Medium or `heavy_companion.md` for Heavy.
  Read `investigation_team.md` before a Heavy evidence wave or an explicitly
  requested Medium evidence wave.
- Initialize one persistent Companion with `agent_type="companion"`,
  `task_name="companion"`, and `fork_turns="none"`, or reuse that target. Its
  first brief for each deployment gives the goal, route, constraints,
  escalation boundaries, evidence format, lowercase underscore-safe deployment
  ID, and this exact standalone marker:

  ```text
  codex-workflow-deployment-start: <deployment_id>
  ```
- If the selected route changes, send the same Companion an explicit transition
  brief naming the new route; previous route-specific duties become inactive.
  Never create a second Companion merely because the route changed.
- If Companion is unavailable, continue only when safe and report the limitation.
- Workers return one small knowledge delta directly to the main agent. Wait
  for a coherent group to become terminal, then integrate the group once rather
  than acknowledging or analyzing routine completions individually. Use
  Companion separately for assigned read-only context work; it is not a
  worker-report relay.
- The main agent directly reads task-critical project documentation, relevant
  source paths and contracts, and decisive failure evidence. It owns defect
  identification, root-cause adjudication, architecture, scope, and final claims.
  At each gate, start with the owning contract, decisive source excerpt, and
  decisive failure or verification artifact; exceed that soft budget only when
  conflict, uncertainty, or risk requires it.
- For serious or ambiguous issues with independent search lanes, Heavy may use
  read-only investigators under `investigation_team.md`; Medium may use them
  only as explicitly requested evidence support. Investigators gather evidence;
  the main agent evaluates their concise terminal reports as one wave, opens
  decisive evidence, and adjudicates the root cause.
- In Heavy, main-agent ownership of acceptance and integration gates means
  defining the gates, assigning their execution, evaluating returned evidence,
  and deciding acceptance. It does not mean rerunning evidenced worker checks.
  Initialize the Heavy verification ledger after defining acceptance criteria;
  its deterministic summary, not prose test counts, owns freshness state.
  Delegate deployment state, endpoints, uploads, browser or screenshot work,
  external search, routine Git or status collation, tool or API discovery, and
  operational diagnostics to the responsible worker.
- If a Heavy integration check genuinely cannot be delegated, resolve the exact
  operation first and batch all already-known independent reads and checks into
  one bounded tool turn. Unless an existing escalation gate applies, return a
  failure or ambiguous result to the responsible worker instead of starting a
  main-agent diagnostic loop.
- Resolve stale or conflicting project status with targeted evidence. Load only
  relevant module documentation and avoid replaying raw logs, large diffs,
  directory listings, or complete source files into the main context.
- Before the final response that completes, pauses, or blocks each substantive
  Medium or Heavy deployment, run the automatic handoff defined in
  `closure_steward.md` exactly once. Its worker inherits recent main-agent
  context and performs the complete documentation-framework update. The
  handoff is not a user command. Closure Steward seals its closure work, invokes
  `$deployment-token-report` directly, and returns its handoff with the
  six-column table. Wait for that one worker and print both results in the final
  response; do not dispatch Companion for reporting.

## Platform Paths

Workflow documents use `/` as a platform-neutral separator. Translate paths to
the current operating system and shell when running filesystem commands.
<!-- codex-workflow-managed-end -->

<!-- codex-workflow-project-personalization-start -->
<!-- codex-workflow-project-personalization-end -->

<!-- codex-workflow-project-local-instructions-start -->
<!-- codex-workflow-project-local-instructions-end -->
