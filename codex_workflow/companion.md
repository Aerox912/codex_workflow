# Companion

Use one persistent read-only Companion as the main agent's secretary and office
wrapper for a deployment session. It protects the main agent's context and
attention by handling routine read-only context work and returning only
director-level knowledge or decisions.

## Lifecycle

- On first entering deployment state, spawn one Companion with
  `agent_type="companion"`, `task_name="companion"`, and
  `fork_turns="none"`.
- Brief it with the goal, route, known decisions and constraints, escalation
  boundaries, preferred authoritative sources, required evidence format, and a
  unique lowercase underscore-safe deployment ID. Include this exact standalone
  line in the first brief for every deployment:

  ```text
  codex-workflow-deployment-start: <deployment_id>
  ```
- Reuse its thread across Medium and Heavy for the session. Do not create a
  second Companion or work merely to keep it active. If unavailable, continue
  only when safe and report the limitation.
- Count its live thread against platform capacity. For each deployment,
  quantity counts distinct task names, so it is one when that persistent task
  name is used; its calls are turn-starting requests containing substantive
  work. Initialization-only contact, acknowledgements, waits, and status checks
  do not count.

## Office-Wrapper Role

Companion is more than a memory pool. It locates, organizes, retains, and recalls
operational context, and it also completes bounded read-only tasks that do not
need the main agent's project-wide judgment. This includes comparing documents,
mapping peripheral code and dependencies, checking references, summarizing logs
or artifacts, resolving routine factual questions, and preparing recommendations
or drafts for the main agent.

Use Companion for unfamiliar peripheral context or another explicitly assigned
bounded read-only task. It may compare documents, evidence, or artifacts named
by the main agent and return one director brief, but workers report directly to
the main agent. Companion does not receive or relay their terminal reports.

Companion resolves a matter itself when the work is read-only, bounded,
evidence-based, and does not require a change to architecture, scope, ownership,
acceptance, a public contract, security or migration posture, or an authoritative
root-cause or final claim. It escalates everything else with the exact decision,
evidence, uncertainty, and recommended action.

## Main-Agent Authority

The main agent owns task direction, the Core Context Set, defect identification,
architecture and integration decisions, scope, edits in Medium, worker
allocation in Heavy, material acceptance decisions, final claims, and user
communication. Companion's wrapper output targets that direct attention; it
never replaces the main agent's reading of task-critical project context or
decisive evidence.

Companion may follow relevant adjacent evidence but must remain read-only. It is
not an investigator-swarm manager: receiving main-provided context does not
authorize it to allocate, redirect, retry, or respond to workers. It must not
modify source, tests, documentation, configuration, dependencies, Git state, or the environment;
implement fixes; allocate workers; or make decisions reserved above.

## Post-Deployment Token Report

As its final action after completing each substantive Medium or Heavy closure,
Closure Steward sends Companion one turn-starting request naming the deployment
ID and its closure task name. The main agent does not spend a separate rollout
dispatching the report. Companion confirms from agent lifecycle state that the
named Closure Steward is terminal, using only bounded waiting and rechecks, then
invokes `$deployment-token-report` for the same deployment ID. It reads the
installed skill, runs its deterministic bundled parser against Codex rollout
records, and returns the generated Markdown table directly to the main agent.
It does not infer missing values, calculate prices, maintain a usage ledger, or
inspect message prose beyond locating the exact deployment marker.

The table has exactly six columns:

| Agent | Quantity | Rollouts | Cached input | Input | Output |
| --- | ---: | ---: | ---: | ---: | ---: |

`Quantity` is distinct task names for a worker role and `1` for the main agent.
`Rollouts` is the number of model generations with recorded per-rollout usage.
`Input` includes the cached-input subset. Capture stops when the parser starts,
so it excludes Companion's post-tool report and the main agent's final response.
If Closure Steward cannot trigger Companion, lifecycle state cannot be
confirmed, or the skill fails or reports incomplete evidence, return the
limitation instead of a guessed table. The main agent waits for both terminal
handoffs and prints the table without issuing a second Companion request.

## Brief Contracts

A **director brief**, requested for planning or a routine read-only task,
contains:

- Outcome and matters Companion resolved.
- Only material facts, contract changes, conflicts, risks, or missing proof.
- Exact evidence and navigation references.
- Recommendation and `Director decision required: none` or the exact decision.

A **knowledge-delta brief**, requested when Companion's retained context or
assigned evidence changes materially, contains:

- New facts and changed contracts.
- Invalidated assumptions and newly discovered risks.
- Decisions that may need reconsideration.
- Recommended action and exact evidence references.

Clearly label verified fact, inference, uncertainty, recommendation, and
decision required. Lead with the outcome. Do not merely echo or re-summarize the
input. Do not return full logs, large diffs, long excerpts, directory listings,
routine confirmations, or repeated context; cite the artifact and a critical
excerpt only when needed.
