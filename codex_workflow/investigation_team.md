# Investigation Team

Use this shared contract for Heavy, and for an explicitly requested Medium
evidence group, only when a serious or ambiguous issue divides into independent
read-only search lanes. Companion remains the persistent secretary;
investigators are disposable evidence gatherers. Medium retains implementation
and verification in the main agent.

## Main-Agent Grounding

Before dispatch, the main understands the task's Core Context Set:

- applicable instructions, requirements, and acceptance boundaries;
- relevant foundational or module documentation;
- the owning source path, interfaces, invariants, and public contracts; and
- the critical reproduction, trace, log excerpt, or other failure evidence.

Companion may index, organize, compare, or compress the supporting material,
but the main directly opens the decisive subset and retains authority over
task-critical decisions.

## Direct Dispatch

Use investigators for multiple plausible causes, cross-system behavior, flaky
or concurrent failure, security or performance risk, dependency/version
uncertainty, missing reproduction, or external prior art. Skip them for the
direct fast path, a known root cause, or one bounded question.

The main directly creates each useful lane with
`agent_type="investigator"`, `fork_turns="none"`, and a unique
`task_name="investigator_<deployment_id>_<lane>"`. Each main-authored brief
contains one question or hypothesis, boundaries, known facts, preferred
authoritative sources, exact starting references, forbidden scope, and evidence
format. Useful lanes include execution paths and state, reproduction and logs,
tests and races, dependency behavior, security or performance boundaries,
official documentation and source history, and clearly labeled prior art.

Launch independent lanes concurrently within the fixed capacity ceiling. The
main tracks expected task names, waits for lifecycle events, and collects each
concise terminal report directly. Waiting and collection are coordination; do
not create an LLM parent for the group. Review the complete expected set once
all lanes are terminal. Keep capacity for Companion and Closure Steward.

## Evidence and Root-Cause Gate

The main compares only material competing hypotheses, opens decisive local
sources and evidence, and records whether the cause is confirmed, probable, or
unresolved. Companion may separately solve an assigned clerical context task,
but it does not receive investigator reports as a relay or make the root-cause
decision.

Do not package a production fix until the main can state the causal chain,
affected contract, fix boundary, residual uncertainty, and acceptance test. If
the gate is not met, reactivate only a relevant investigator with a compact
evidence delta or run an explicitly diagnostic experiment; do not launch
another broad group by default.

After the gate, Medium keeps implementation and verification in the main agent;
Heavy creates executor and tester packages. If later testing contradicts the
causal model, return the decision to the main and dispatch only newly needed
focused lanes.
