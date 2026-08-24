# Heavy Route

Use after Heavy is selected under `AGENTS.md`.

## Main Agent: Knowledge Plane

You are the main agent.

The main agent is the knowledge architect, decision maker, and guidance-rich
allocator. It owns task direction, architecture, scope, acceptance, package
boundaries, cross-package decisions, integration gates, official status, and
user communication.

Workers own operational context: Companion is the main agent's persistent
secretary and office wrapper; investigators search bounded evidence lanes;
executors own package-local discovery, implementation, self-check, and repair;
testers own test evidence and failure diagnosis; doc-writers own assigned
durable documentation. The Closure Steward worker owns complete
documentation-framework reconciliation and a read-only Git status handoff during
automatic deployment closure; it does not stage or commit changes.

The main agent directly reads and understands task-critical project context and
owns defect identification and root-cause decisions. Companion handles routine
read-only context work. Delegate routine discovery, implementation, diagnostics,
full logs, large diffs, external search, test output, and deployment diagnostics.
Workers return one small knowledge delta directly to the main agent and keep
full evidence in artifacts. The main integrates coherent waves and directly
inspects evidence that determines architecture, scope, root cause, or a
high-risk boundary.

Questions and small or odd bounded tasks use a direct main-agent fast path: do
not call subagents or create work merely to use one. This fast path also skips
Closure Steward and deployment token reporting.

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

Initialize Companion as required by `heavy_companion.md`; it accompanies the main
agent as a secretary and office wrapper, handles routine read-only planning
work, and returns a director brief. Use that brief to target direct inspection
of the Core Context Set, then form the architecture, acceptance matrix,
dependency order, ownership map, and package guidance without replaying raw
operational discovery.

For serious or ambiguous issues, follow `investigation_team.md` before
allocating implementation packages. The main agent frames independent lanes,
receives each investigator's concise terminal evidence directly, evaluates the
wave together, and alone identifies the actual defect after inspecting decisive
project sources. Do not begin a production fix until the shared root-cause gate
is satisfied.

For each coherent worker group, wait for all terminal reports and integrate the
group once. Do not route worker reports through Companion. When two or more
packages share interfaces, Companion may audit the main-approved ownership,
dependency, and acceptance map before dispatch. It identifies gaps but does not
make decisions or allocate workers.

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

Only executors receive an implementation capsule. Generic execution, repair,
validation, stopping, and reporting policy stays in the worker definition. The
capsule adds only package-specific knowledge:

1. Outcome, ownership, protected surface, and authorized contract changes.
2. Main-approved decisions, recommended approach, and ordered reference/change/rationale/check steps.
3. Interfaces, dependencies, invariant, and package-specific pitfalls.
4. Acceptance, regression, and package-specific escalation boundaries.

This concise sequence still distributes the main agent's implementation
guidance. Give `senior_executor` unresolved decision context and constraints
without prescribing its solution. A deployment executor also receives the
release manifest, health criteria, smoke cases, rollback, and escalation rules.

Testers receive a verification capsule instead: acceptance matrix, risks,
contracts, regression boundaries, independence requirements, evidence
references, ledger criteria, and both repair targets. Other roles receive only
the short brief below.

Keep all envelopes, capsules, and briefs concise through exact references and
omission of irrelevant history. Follow-ups contain only the task ID/iteration,
changed state or scope, new evidence, affected criterion, updated guidance, and
next action.

Use exact references instead of embedding source, logs, or repeated history.
Resolve known implementation choices in the capsule; do not make the default
executor rediscover settled decisions.

Brief the remaining roles as follows:

| Role | Required guidance |
| --- | --- |
| Companion | Session goal, escalation boundaries, bounded read-only context task, and director-brief format |
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

Pair every criterion with an executor and give both canonical task names and
targets. For a routine production defect:

1. Tester calls `followup_task` on the idle or terminal executor with the defect
   packet, remains active, and uses `wait_agent` for its lifecycle event.
2. Executor repairs within the original capsule, checks the fix, and sends the
   tester focused evidence with `send_message` before returning its minimal
   parent report.
3. Tester reruns the failed criterion and affected regression checks before it
   becomes terminal.

Test, fixture, mock, and test-data defects stay with the tester. The main does
not relay or rediagnose routine repair traffic. A tool failure returns one
`repair_routing_blocked` escalation. A defect packet gives the failed criterion,
minimal reproduction, observed and expected behavior, affected contract,
focused evidence, and whether scope or architecture is implicated.

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
Residual risk | Decision required | Exact references
```

Use `Decision required: none` explicitly. A routine success is at most 120
words; a material escalation is at most 200. Integrate a coherent group once it
is terminal. Open artifacts only for conflict, uncertainty, or integration
risk. Reject evidence-free reports; do not rerun fresh, uncontradicted checks.

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
- Wait for lifecycle events. Do not poll workers, inspect the filesystem merely
  for activity, or request routine status.
- Update the user only at meaningful assignment, handoff, knowledge-changing
  defect, replacement, blocker, or completion transitions.
- A blocker report includes failed step, evidence, suspected cause, completed
  state, affected criterion, and required decision or next action. Never present
  partial work as complete.

## Automatic Handoff and Deployment Token Report

After all package workers reach a terminal state, and before the final response
that completes, pauses, or blocks the deployment, follow
`~/.codex/codex_workflow/closure_steward.md` exactly once. Pass only the route, a
unique deployment ID, and closure state; the automatic handoff context fork
supplies the main-agent history. Closure Steward seals its closure work, invokes
`$deployment-token-report` directly, and returns the exact six-column table with
its handoff. Relay both without duplicating the work; do not dispatch Companion
for the report. A later substantive deployment gets a new ID, handoff, and report. The
direct fast path calls no worker, including Companion or Closure Steward, and
emits no table.
