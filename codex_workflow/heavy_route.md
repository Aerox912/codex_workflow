# Heavy Route

Use after Heavy is selected under `AGENTS.md`.

## Main Agent: Knowledge Plane

You are the main agent.

The main agent is the knowledge architect, decision maker, and guidance-rich
allocator. It owns task direction, architecture, scope, acceptance, package
boundaries, cross-package decisions, integration gates, official status, and
user communication.

Workers own operational context: Companion is the persistent secretary;
investigators search evidence lanes; executors discover, implement, self-check,
and repair packages; testers own test evidence and failure diagnosis; and
doc-writers own assigned durable documentation. Closure Steward reconciles the
documentation framework and returns read-only Git status without committing.

The main agent directly reads and understands task-critical project context and
owns defect identification and root-cause decisions. Companion handles routine
read-only context work. Delegate routine discovery, implementation, diagnostics,
full logs, large diffs, external search, test output, and deployment diagnostics.
Workers return one small knowledge delta and keep full evidence in artifacts. A
multi-worker wave delivers unchanged deltas through one terminal `wave_barrier`
bundle. The main integrates it once and directly inspects decision evidence.

Questions and small or odd bounded tasks use a direct main-agent fast path: do
not call subagents or create work merely to use one; skip Closure Steward and
token reporting.

## Main-Agent Execution Boundary

For a substantive Heavy deployment, the main agent's own tool use is limited to
task-critical source or evidence inspection, architecture and scope decisions,
orchestration, and the smallest integration check that cannot safely be
delegated. Owning acceptance and integration gates means defining each gate,
assigning its execution, evaluating returned evidence, and deciding acceptance;
it does not mean rerunning an executor's or tester's evidenced checks.

Assign deployment state, public endpoints, uploads, browser or screenshot work,
external search, routine Git or status collation, tool or API discovery, and
operational diagnostics to the responsible worker. If a genuinely
non-delegable main-agent check remains, resolve its exact operation first and
batch all already-known independent reads and checks into one bounded tool turn.
Unless an existing escalation gate applies, a failure or ambiguous result
returns to the responsible worker with the new evidence; it does not authorize
a main-agent diagnostic loop.

For each main-owned gate, start with the owning contract, decisive source
excerpt, and decisive failure or verification artifact. Ask Companion to locate
or compress supporting material. Exceed this soft evidence budget only for
conflict, material uncertainty, or high risk.

## Investigation and Planning

At the session's first substantive deployment, directly read the complete
`agent_docs/` framework once. Initialize Companion under `heavy_companion.md`;
it loads the same framework but returns only its marker and intake status, never
a framework summary or project facts. Later reuse both retained models and
refresh only changed or decision-critical text. Inspect the remaining Core
Context Set before deciding architecture, acceptance, ownership, and guidance.

For serious or ambiguous issues, follow `investigation_team.md`. The main frames
lanes and exact briefs, receives one unmodified `wave_barrier` terminal set,
evaluates it together, and alone identifies the actual defect from decisive
sources before production work begins.

For each group of two or more workers, create one `wave_barrier` with
`fork_turns="none"` and give it the main-approved launch manifest plus exact
briefs or capsules. It launches the workers, absorbs individual completion
wakeups, waits until every member and descendant is terminal, and returns all
reports unchanged. Wait only on the barrier and integrate once; await a single
worker directly. Never route reports through Companion. For shared interfaces,
Companion may audit the approved ownership, dependency, and acceptance map.

For durable work, the main may update `agent_docs/project_progress.md` once for
plan activation. Closure Steward owns final reconciliation and
`latest_session_work.md`; no other worker edits either file.

After defining Heavy acceptance, run bundled `verification_ledger.py init
--project <root> --deployment-id <id> --criterion <criterion>=<owner_task_id>`;
repeat the criterion flag and give the ledger fields to its owners.

## Packages and Knowledge Distribution

Delegate coherent, independently completable packages large enough for one
executor to perform local discovery, implementation, self-check, and routine
repair. Run packages concurrently only when outcomes and mutable ownership are
independent. Keep one child slot available for Closure Steward.

Every initial worker uses `fork_turns="none"` and receives a minimal envelope:
task ID and outcome; scope and protected areas; exact starting references;
escalation conditions; and return format. It is routing metadata, not project knowledge.

For a multi-worker wave, send these exact items in one `wave_barrier` manifest;
it passes them unchanged, keeping the main as the guidance source.

Only executors receive an implementation capsule. Generic execution, repair,
validation, stopping, and reporting policy stays in the worker definition. The
capsule adds only package-specific knowledge:

1. Outcome, ownership, protected surface, and authorized contract changes.
2. Main-approved decisions, recommended approach, and ordered reference/change/rationale/check steps.
3. Interfaces, dependencies, invariant, and package-specific pitfalls.
4. Acceptance, regression, and package-specific escalation boundaries.
5. Expected durable-documentation delta—lasting facts, decision consequences,
   discarded approaches, reusable lessons, or `none`—for Closure Steward;
   workers do not edit `agent_docs/`.

This concise sequence still distributes the main agent's implementation
guidance. Give `senior_executor` unresolved decision context and constraints
without prescribing its solution. A deployment executor also receives the
release manifest, health criteria, smoke cases, rollback, and escalation rules.

Testers receive a verification capsule instead with acceptance, risk, contract,
regression, independence, evidence, and ledger criteria plus one repair capsule
per criterion. It names the executor type and original ownership, protected
surface, decisions, recommended approach, ordered guidance, interfaces,
invariant, pitfalls, references, and checks. Other roles receive only the short
brief below. Keep envelopes, capsules, and briefs concise through exact
references, omitting irrelevant history. Follow-ups contain only task ID/iteration,
changed state or scope, new evidence, affected criterion, updated guidance, and
next action.

Use exact references instead of embedding source, logs, or repeated history.
Resolve known implementation choices in the capsule; do not make the default
executor rediscover settled decisions.

Brief the remaining roles as follows:

| Role | Required guidance |
| --- | --- |
| Companion | Session goal, escalation boundaries, bounded read-only context task, and director-brief format |
| Wave barrier | Wave ID, exact member agent types and task names, and each main-approved brief or capsule |
| Investigator | One bounded question or hypothesis, boundaries, sources, exact references, and evidence format |
| Doc-writer | Verified facts, changed behavior, audience, terminology, limitations, public-document surface |

Use `default_executor` for production work. Use at most one `senior_executor` and reserve it
for substantial mathematical or logical reasoning or exceptionally difficult
cross-cutting work. Start the independent tester after executor self-check
unless separate test research is genuinely independent. A tester may own
several related packages when the acceptance boundary is cohesive and its
criterion-to-executor routing map is explicit. Delegate public, product,
operator, or service documentation only after verification. Closure Steward
alone edits `agent_docs/` during automatic closure.

## Repair Loop

Pair every criterion with an executor type, canonical task names, and a main-supplied repair capsule.
For a routine production defect:

1. Tester uses `spawn_agent` with `fork_turns="none"` to create a fresh repair executor child from the capsule and defect packet.
2. Tester stays active and uses `wait_agent` for the child's single terminal report.
3. Tester reruns the failed criterion and affected regressions before terminating.

Test, fixture, mock, and test-data defects stay with the tester. The main does
not relay or rediagnose routine repair traffic. Neither role uses `followup_task`
or `send_message`. Dispatch or awaited-lifecycle failure returns one
`repair_dispatch_blocked` escalation with the criterion, reproduction, observed
and expected behavior, contract, evidence, and scope or architecture impact.

Escalate to the main agent only when repair conflicts with the capsule, changes a cross-package contract,
invalidates a material decision, requires expanded ownership, introduces
security or migration risk, or the same criterion still fails after two focused
repair attempts. Escalations report the new knowledge and decision needed, not
the full repair transcript.

## Verification Ledger

The append-only ledger lives under the deployment's hidden workflow-resource
directory. Only a criterion's registered owner may record task, iteration,
status, method, result, artifact, and checked-path hashes. Records are immutable.

Run `verification_ledger.py summarize` at acceptance. A criterion is ready only
when its latest record passed and its checked paths are unchanged. Missing,
failed, or stale criteria block acceptance. For several gates, Companion may
return only gaps, conflicts, and staleness; it never receives reports or writes state.

## Layered Evidence and Reports

Workers keep full logs, diffs, responses, screenshots, diagnostics, and source
inventories in artifacts or retained context. Direct evidence cites claim,
result, method, artifact, a critical excerpt only if needed, and confidence.

Each parent report is the smallest sufficient knowledge delta:

```text
Status | Outcome | Material knowledge delta | Verification record/artifact
Durable documentation delta | Residual risk | Decision required | Exact references
```

Use `Decision required: none` explicitly. A routine success is at most 120
words; a material escalation is at most 200. The barrier preserves reports
verbatim and emits one terminal bundle. Open artifacts only for conflict,
uncertainty, or risk. Reject evidence-free reports; do not rerun fresh checks.

## Gates, Failure, and Waiting

- Executor self-check precedes independent tester verification. Require
  meaningful tests for behavior changes, bug fixes, important modules, and
  public contracts.
- Evaluate the deterministic ledger summary before accepting integration or
  deployment. Prose test counts are not authoritative state.
- If verification contradicts the causal model, return to the main-agent
  root-cause gate and dispatch only the newly needed investigation lanes.
- Prefer deterministic local fixtures. Never weaken validation, claim unrun
  checks passed, accept unrelated scope, or allow silent error suppression or
  unplanned public API/schema breaks.
- After one evidence-free response, send one focused retry. Replace the worker
  after a second; if replacement also lacks evidence, report the limitation and
  take over only the smallest critical step transparently.
- For a multi-worker wave, only `wave_barrier` waits on workers; the main waits
  once on it. Do not poll, inspect activity files, or request routine status.
- Update the user only at meaningful assignment, handoff, knowledge-changing
  defect, replacement, blocker, or completion transitions.
- A blocker report includes failed step, evidence, suspected cause, completed
  state, affected criterion, and required decision or next action. Never present
  partial work as complete.

## Automatic Handoff and Deployment Token Report

After all package workers and repair descendants reach a terminal state, use
`list_agents` to confirm no active package work and consume delivered lifecycle
results. Only then, before the final response that completes, pauses, or blocks
the deployment, follow
`~/.codex/codex_workflow/closure_steward.md` exactly once. Pass only the route, a
unique deployment ID, and closure state; the automatic handoff context fork
supplies the main-agent history. Closure Steward seals its closure work, invokes
`$deployment-token-report` directly, and returns the exact six-column table with
its handoff. Relay both without duplicating the work; do not dispatch Companion
for the report. A later substantive deployment gets a new ID, handoff, and report. The
direct fast path calls no worker, including Companion or Closure Steward, and
emits no table.
