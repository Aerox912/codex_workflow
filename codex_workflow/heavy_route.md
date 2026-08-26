# Heavy Route

Use after Heavy is selected under `AGENTS.md`.

## Main Agent: Knowledge Director

You are the main agent. Own task direction, architecture, scope, root-cause
adjudication, package boundaries, cross-package decisions, acceptance,
integration, official status, final claims, and user communication.

Workers own bounded operational context. Companion is the persistent read-only
secretary; investigators search evidence lanes; executors discover, implement,
self-check, and repair packages; testers produce independent verification and
failure diagnosis; doc-writers own assigned durable public documentation; and
Closure Steward reconciles `agent_docs/` and returns the final handoff.

Delegate routine discovery, implementation, diagnostics, full logs, large
diffs, external research, test output, deployment diagnostics, and clerical
aggregation. Workers keep full evidence in artifacts and return one small
knowledge delta. The main directly inspects only the evidence that controls
architecture, scope, root cause, a high-risk boundary, acceptance, or a final
claim.

Questions and small or odd bounded tasks use a direct main-agent fast path: do
not call subagents merely to use the route; skip Closure Steward and token
reporting.

## Main-Agent Execution Boundary

For a substantive Heavy deployment, limit main-agent tool use to decisive
source or evidence inspection, material decisions, orchestration, and the
smallest integration check that cannot safely be delegated. Owning a gate means
defining it, assigning execution, evaluating returned evidence, and deciding
acceptance. It does not mean rerunning an executor's or tester's evidenced
check.

Assign endpoint state, uploads, browser or screenshot work, external search,
routine Git/status collation, tool or API discovery, and operational diagnostics
to the responsible worker or Companion. If a genuinely non-delegable check
remains, resolve its exact operation and batch all already-known independent
reads and checks into one bounded tool turn. Unless a material escalation gate
applies, return failed or ambiguous operational evidence to the responsible
worker instead of starting a main-agent diagnostic loop.

For each main-owned decision, start with the owning contract, decisive source
excerpt, and decisive failure or verification artifact. Ask Companion to build
or compress the supporting bibliography. Exceed this soft evidence budget only
for conflict, material uncertainty, or high risk.

## Companion and Investigation

At the first substantive Heavy entry in the session, initialize or transition
Companion under `heavy_companion.md`. Before planning or worker dispatch, the
main reads `agent_docs/project_overview.md`, `project_core_tech.md`,
`project_structure.md`, `project_progress.md`, and `latest_session_work.md`.
Companion reads `agent_docs/project_diary.md` plus every module-specific
Markdown document under `agent_docs/`, returns the required deployment marker,
and summarizes task-related guidance with exact references and module-document
coverage. This split intake is required even when Companion started in Medium.
Reuse it on later Heavy deployments or re-entry unless a document changed or
controls a current decision.

The main does not routinely read the diary or module-specific documents. Use
Companion's brief and later clerical assignments to target exact source,
contracts, and decisive evidence; directly open a supporting document when it
is ambiguous, conflicting, or material to a decision or final claim.

Companion is available throughout the deployment, not only at intake or final
readiness. Assign bounded source/contract indexing, document-conflict checks,
external-service or tool-integration mapping, environment/configuration
matrices, runtime-asset inventories, browser/tool availability, Git/status
aggregation, owner/acceptance tracking, artifact compression, and capsule
formatting from main-owned decisions. The main reviews and approves every
capsule before dispatch and directly checks crucial evidence.

For serious or ambiguous issues, follow `investigation_team.md`. The main
directly launches the useful investigator lanes, collects their concise terminal
reports, evaluates the complete expected set once, and alone determines the
root cause after opening decisive sources. Do not begin production work until
the main can state the causal chain, affected contract, fix boundary, residual
uncertainty, and acceptance test.

## Direct Orchestration and Knowledge Distribution

The main directly launches every investigator, executor, tester, doc-writer,
and closure worker. Launching, waiting, and collecting terminal results are
coordination duties; never create an LLM parent merely to operate a wave. Launch
independent workers concurrently when their outcomes and mutable ownership do
not overlap. Wait for lifecycle events, track the expected task names, and
integrate a coherent group once all expected reports are terminal.

Every initial worker uses `fork_turns="none"` and receives a concise envelope:
task ID and outcome; scope and protected areas; exact starting references;
escalation conditions; and return format.

Only executors receive an implementation capsule. Generic execution, repair,
validation, stopping, and reporting policy stays in the worker definition. The
capsule adds package-specific knowledge:

1. Outcome, ownership, protected surface, and authorized contract changes.
2. Main-approved decisions, recommended approach, and ordered
   reference/change/rationale/check steps.
3. Interfaces, dependencies, invariant, and package-specific pitfalls.
4. Acceptance, regression, and package-specific escalation boundaries.
5. Expected durable-documentation delta—lasting facts, decision consequences,
   discarded approaches, reusable lessons, or `none`.

This capsule distributes the main agent's knowledge and implementation guidance.
Give `senior_executor` unresolved decision context and constraints without
prescribing its solution. A deployment executor also receives the release
baseline, health criteria, smoke cases, rollback authority, and escalation
conditions.

Testers receive a verification capsule with the acceptance manifest slice,
risks, contracts, regression boundaries, independence requirements, evidence
references, responsible executor target, and the main-approved repair capsule.
Use exact references instead of embedding source, logs, or repeated history.
Resolve settled choices before dispatch.

Brief remaining roles as follows:

| Role | Required guidance |
| --- | --- |
| Companion | Goal, boundaries, bounded clerical outcome, authoritative sources, and brief format |
| Investigator | One bounded question or hypothesis, boundaries, known facts, sources, and evidence format |
| Doc-writer | Verified facts, changed behavior, audience, terminology, limitations, and public-document surface |

Use `default_executor` for ordinary production work. Use at most one
`senior_executor`, reserved for substantial mathematical or logical reasoning
or exceptionally difficult cross-cutting work. Start independent verification
after executor self-check unless separate test research is genuinely
independent. Closure Steward alone edits `agent_docs/` during automatic closure.

## Main-Routed Repair

Tester and executor roles are leaf workers and have no assumed collaboration
tools. The main owns repair dispatch and lifecycle coordination without
rediagnosing a routine defect.

1. A tester fixes only assigned test, fixture, mock, or test-data defects. For a
   production defect it returns `Status: repair_needed` with the failed
   criterion, minimal reproduction, observed/expected behavior, affected
   contract, focused artifact, scope impact, and evidence-manifest update.
2. If the defect stays inside the approved capsule, the main forwards that
   packet unchanged with `followup_task` to the responsible executor. Spawn a
   fresh executor from the original repair capsule only when reuse is
   unavailable or unsafe. The main then waits for its terminal evidence.
3. The main reactivates the tester with only the repair delta and affected
   regression boundary. The tester reruns the criterion and returns a final
   verification report.

Escalate for capsule conflict, cross-package contract change, an invalidated
material decision, expanded ownership, security or migration risk, environment
blocker, or the same criterion failing after two focused repair attempts. Keep
routine defect packets and repair evidence out of a main-agent diagnostic loop.

## Lightweight Evidence Manifest

After defining acceptance, keep one compact manifest in deployment working
state; do not create a shared state file or immutable record store:

```text
Criterion | Class | Owner | Status | Method/artifact | Checked scope/freshness | Limitation
```

`Class` is `required`, `conditional`, or `advisory`. `Status` is `pass`, `fail`,
`unavailable`, or `not_run`. Workers return only their assigned manifest rows
with exact artifact references. The main evaluates freshness against later
changes and owns the integrated manifest. Companion may track owner coverage,
missing rows, or contradictions from main-provided metadata, but never decides
acceptance.

Keep independent concerns in separate criteria. A browser-tool error, failed
screenshot capture, or blank/low-confidence OCR result is `unavailable`; it is
not product failure and does not invalidate passed backend or service gates. It
blocks only when that exact observation is a required acceptance condition and
no reliable alternative exists. An advisory visual defect remains visible as
residual risk instead of silently collapsing unrelated passing evidence.

## Deployment and Rollback

Record the pre-change public baseline and candidate state. The main owns the
rollback decision except for narrow, preauthorized safety triggers in a
deployment capsule. A worker must otherwise pause and report the evidence; it
must not mechanically restore the prior state.

Rollback when the candidate causes a confirmed material regression, security or
data-integrity risk, or required-contract failure and the rollback state is
actually safer or more functional. Do not roll back solely because a screenshot
could not be captured, OCR was blank, an advisory visual defect remains, or a
conditional observation is unavailable. When the prior baseline is worse—such
as an outage—and the candidate restores core service, preserve the best
recoverable state while the remaining non-blocking defect is repaired, unless a
safety boundary or explicit user requirement says otherwise.

## Reports, Gates, and Closure

Workers keep full logs, diffs, responses, screenshots, diagnostics, and source
inventories in artifacts or retained context. Direct evidence states claim,
result, method, artifact, checked scope, a critical excerpt only if needed, and
confidence.

Each terminal report is the smallest sufficient knowledge delta:

```text
Status | Outcome | Material knowledge delta | Evidence-manifest rows/artifacts
Durable documentation delta | Residual risk | Decision required | Exact references
```

Use `Decision required: none` explicitly. A routine success is at most 120
words; a material escalation is at most 200. Reject evidence-free reports; do
not rerun fresh, uncontradicted checks.

- Require meaningful tests for behavior changes, bug fixes, important modules,
  and public contracts. Never weaken validation or claim an unrun check passed.
- If verification contradicts the causal model, return to the main-owned
  root-cause gate and launch only newly needed focused investigation.
- After one evidence-free response, send one focused retry. Replace the worker
  after a second; take over only the smallest critical step transparently.
- Do not poll workers or inspect activity files. Use lifecycle events and
  `list_agents` only to resolve terminal-state uncertainty before closure.
- Never present partial work as complete. A blocker includes the failed step,
  evidence, suspected cause, completed state, affected criterion, and required
  decision or next action.

After all package and repair work is terminal, follow
`~/.codex/codex_workflow/closure_steward.md` exactly once before the final
response. Pass only the route, unique deployment ID, and closure state. Closure
Steward seals its work, invokes `$deployment-token-report`, and returns the
handoff plus exact six-column table. Relay both without duplicating its work or
dispatching Companion for reporting. A later substantive deployment receives a
new closure worker and report.
