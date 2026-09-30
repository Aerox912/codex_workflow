# Medium Route

Use after Medium is selected under `AGENTS.md`.

## Main Ownership

The main agent owns planning, root-cause reasoning, implementation,
production repair, verification, integration, acceptance, final claims, and user
communication. Medium does not delegate production or verification.

Optimize for fewer main-agent decision turns and lower main-agent context
consumption while preserving quality and completion. Aggregate support-worker
token use is not the optimization target.

Use only these support roles:

| Role | Ownership |
| --- | --- |
| Explorer | A disposable read-only worker mapping a bounded project-context task and returning evidence and gaps. |
| Investigator | A disposable read-only worker researching a bounded fault or solution problem. Each can propose options; the main makes every project decision. |
| Archivist | The required substantive-deployment closure worker defined by `~/.codex/codex_workflow/archivist.md`. It owns concise assigned documentation outside the main-owned deployment-state documents, read-only Git reporting, and the closing Deployment Token Report. |

## Working State

- `deployment state`: planning or executing substantive project changes or
  deliverables under a broad, possibly multi-session deployment plan.
- `leaf state`: otherwise, including standalone questions, searches, read-only
  research, and small bounded operations.

Classify by the requested outcome, not research breadth, worker count, or the
selected route. Standalone read-only research is leaf work; research supporting
an active deployment remains part of that deployment.

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

In deployment state, directly maintain `project_progress.md`,
`project_diary.md`, and `latest_session_work.md`. Before closure, record the
current goal and continuation state, concise lasting lessons, and the verified
deployment handoff in their canonical documents. Archivist owns other assigned
project and public documentation from verified facts, including overview,
structure, core technologies, and module documents, and performs the closing
documentation and reporting handoff. Require concise edits that remove stale or
redundant detail, assign module documents explicitly, and perform a direct
user-requested document edit outside deployment. During installation only, the
installer-assigned Archivist may initialize those three files when they are new
or still marked as templates.

Leaf work does not trigger automatic `agent_docs/` updates or deployment
closure. Update documents only for an explicit documentation request or verified
changes to durable project knowledge; ordinary search results alone do not
require a project progress, diary, or session-handoff entry.

Keep raw logs, temporary reasoning, and short-lived checkpoints out of durable
documents; give each fact one canonical home. Never delete a main project
document without warning. If the user has not explicitly requested or
authorized that deletion, obtain confirmation before deleting it.

## Shared Deployment-State Entry

On substantive deployment entry, before planning or execution, if session-level
intake is not complete, directly read the complete current `agent_docs/`
framework exactly once: overview, core technology, structure, progress,
diary, latest session work, and every module-specific Markdown document.
This one direct read is shared across Medium and Heavy. Never repeat it later
in the session. Use retained context or assign Explorer a bounded context delta,
module intake, or conflict check when detail or freshness matters. Missing or
unreadable required documents leave deployment entry incomplete; report the
intake blocker. For a small leaf task, read only task-relevant project documents.

## Context Routing After Intake

After the shared intake and before broader source discovery or planning, use
`agent_docs/` to create a compact working-context map:

- **Direct**: code, contracts, interfaces, and evidence the main must inspect to
  own diagnosis, implementation, verification, integration, risk, or acceptance.
- **Explorer**: bounded context discovery, supporting modules, tools,
  configuration, logs, dependencies, document deltas, and evidence retrieval.
- **Investigator**: bounded fault hypotheses, solution research, alternatives,
  feasibility, technical comparisons, or prior art using project or Internet sources.

Keep this map in working state, not durable documentation, and revise it only
when material evidence changes relevance. Directly inspect a delegated surface
when it becomes necessary for main-owned production or a material decision.
Dispatch independent Explorer or Investigator workers together when useful.

## Deployment Boundary

On substantive deployment entry, choose a unique ID
matching `[a-z0-9][a-z0-9_-]{0,63}`. Put
`<!-- codex-workflow-deployment-start: <deployment_id> -->`, with the placeholder
replaced by that ID, in the first commentary after entry. Emit it once and pass
the same ID to Archivist at closure.

## Support Packages and Investigation

Start each initial support package with **Task ID**, a logical identifier unique
within the deployment, followed by the capsule for that role:

| Role | Capsule parts |
| --- | --- |
| Explorer | **Exploration ID**; **Exploration Context**; **Exploration Task + Goal**; **Main-Agent Exploration Guidance** |
| Investigator | **Problem ID**; **Solution Context**; **Solution Search Task + Goal**; **Main-Agent Solution Guidance** |
| Archivist | **Documentation Context + Audience**; **Documentation Task + Goal**; **Main-Agent Documentation Guidance** |

Treat these parts as the complete structure. Include only material context,
references, boundaries, intended outcomes, main-owned decisions, constraints,
and cautions. Require Task ID in every report. Follow-ups repeat it and send
only changed capsule parts.

The main retains interpretation, root-cause reasoning, and every project
decision because it holds the decisive project context. Use Explorer for
bounded context work and Investigator for solution research. Both return
evidence, unknowns, and implications; neither owns causal, architecture,
implementation, or acceptance decisions.

For difficult or broad questions, prefer parallel Explorers or Investigators
(e.g., 2, 3, or more) when independent evidence can improve coverage and result
quality. The main chooses the count needed for the task; a narrow lookup or
focused search can use a single worker.

When multiple workers address the same question, dispatch them together with
one shared Exploration ID or Problem ID, distinct Task IDs, and complementary
angles in each worker's Exploration Task + Goal or Solution Search Task + Goal.
Each worker seeks an answer to the full bounded question; its angle guides
evidence collection. Keep their searches independent. Wait for the assigned
set's reports and compare evidence, gaps, and disagreements rather than voting
before deciding. If a worker fails, retry or replace only that worker when its
missing evidence is needed; otherwise state the coverage limitation and decide
whether the available evidence is sufficient. Preserve completed reports.

## Rollout-Efficient Support

- Batch independent main-owned reads, searches, metadata checks, and tool
  operations into bounded calls.
- When several support workers inform one decision, dispatch them together,
  wait for the relevant set, and synthesize once. Start another batch only when
  existing evidence materially changes the questions.
- Do not poll support workers, request status-only updates, inspect activity
  files, or repeatedly request available evidence. Use lifecycle events,
  appropriately long waits, and `list_agents` only for genuine terminal-state
  uncertainty.
- Keep dependent or overlapping main-owned changes sequential and verification
  proportionate to risk. Never weaken validation or claim an unrun check passed.

## Fixed Boundaries

- Medium has no workflow-imposed aggregate active-subagent limit.
- Limit Medium workers to Explorer, Investigator, and Archivist.
- Give support workers bounded questions and sufficient context; retain every
  material interpretation and final claim in the main.
- Archivist owns assigned documentation outside `project_progress.md`,
  `project_diary.md`, and `latest_session_work.md`, plus closure reporting. Keep
  those three documents, implementation, production repair, root-cause
  decisions, and verification with the main.
- Preserve unrelated work and keep Git mutations within explicit authority.

## Fast Path and Closure

Use the direct fast path for standalone questions, searches, read-only research,
and small bounded leaf tasks. Work directly when no support workers are needed.
Read only task-relevant project documents and skip deployment entry, full
documentation intake, automatic `agent_docs/` updates, Archivist closure, and
token reporting. Handle explicit documentation requests within their assigned
scope. Research supporting an active deployment remains part of that deployment.

Before the final response that completes, pauses, or blocks a substantive
deployment, update `agent_docs/project_progress.md`,
`agent_docs/project_diary.md`, and `agent_docs/latest_session_work.md` yourself,
keeping them concise and canonical. Then follow
`~/.codex/codex_workflow/archivist.md` exactly once. Combine any other verified
documentation updates with its required closure assignment when practical.
Relay its handoff and exact six-column `$deployment-token-report` table. Use a
new deployment ID for each later deployment.
