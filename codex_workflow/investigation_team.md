# Investigation Team

Use this shared contract for Heavy, and for an explicitly requested Medium
evidence wave, when a serious or ambiguous issue has a search space that can be
divided into independent read-only lanes. Companion remains the single
persistent secretary and office wrapper; investigators are disposable evidence
gatherers and never replace or multiply Companion. Medium keeps implementation
and verification in the main agent even when this evidence support is used.

## Main-Agent Grounding

Before dispatch, the main agent directly reads and understands the task's
**Core Context Set**:

- applicable instructions, user requirements, and acceptance boundaries;
- relevant foundational or module project documentation;
- the source path, interfaces, invariants, and public contracts that own the
  failing behavior;
- the critical reproduction, trace, log excerpt, or other failure evidence.

Companion may locate, organize, solve routine read-only questions about, and
retain this material, but its director brief is not a substitute for the main
agent's direct understanding of decisive context. Delegation may filter
operational noise; it must not transfer authority over task-critical project
decisions.

## Dispatch Gate

Create a team when multiple plausible causes, cross-system behavior, flaky or
concurrent failure, security or performance risk, dependency/version
uncertainty, missing reproduction, or external prior art makes parallel search
materially useful. Skip it for the direct fast path, a known root cause, or a
small bounded question. Do not create duplicate lanes merely to use capacity.

Create one parent with `agent_type="wave_barrier"`, a unique
`task_name="wave_barrier_<deployment_id>_investigation"`, and
`fork_turns="none"`. Its manifest defines each orthogonal lane with
`agent_type="investigator"`, a unique
`task_name="investigator_<deployment_id>_<lane>"`, and the exact main-authored
brief: question or hypothesis, boundaries, known facts, preferred authoritative
sources, useful exact references, forbidden scope, and evidence format. Useful
lanes include execution paths and state, failure reproduction and logs, tests
and races, dependency or version behavior, security or performance boundaries,
official documentation and source history, and clearly labeled technical-forum
or prior-art searches.

Select the useful lanes before dispatch and treat them as one investigation
wave. The barrier passes each brief unchanged, absorbs individual investigator
completion wakeups, waits through all descendants, and returns the complete set
of concise terminal evidence packages without summarizing them. The main waits
only on the barrier and reviews the terminal bundle once.

Use investigators when the installed agent type is available. Keep Companion's
live slot and one slot for Closure Steward within the fixed concurrency ceiling.
Investigator quantity is driven by independent search breadth, not token-cost
minimization. Keep capacity for the barrier, Companion, and Closure Steward.

## Evidence and Root-Cause Gate

The main agent owns adjudication. It reviews the complete set of concise lane
reports together, compares only material competing hypotheses, directly opens
the decisive local sources and evidence, and records whether the cause is
confirmed, probable, or unresolved. Companion may separately answer an assigned
bounded read-only context question, but it does not receive or filter worker
terminal reports.
Do not package or implement a production fix until the main agent can state the
causal chain, affected contract, fix boundary, residual uncertainty, and
acceptance test. If that gate is not met, reuse the relevant investigator thread
with one compact evidence delta or run an explicitly diagnostic experiment; do
not launch another broad wave by default.

After the gate, Medium keeps implementation and verification in the main agent;
Heavy creates executor and tester packages. If later testing contradicts the
causal model, return the decision to the main agent and dispatch only the newly
needed focused lanes before revising the fix.
