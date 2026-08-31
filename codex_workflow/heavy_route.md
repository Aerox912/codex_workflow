# Heavy Route

Use after Heavy is selected under `AGENTS.md`.

## Main Agent at the Center

The main agent is the knowledge director and central decision maker. It owns
task direction, architecture, scope, material causal decisions, package
boundaries, integration, acceptance, final claims, and user communication.
Workers surround the main as bounded capabilities; they do not form a fixed
hierarchy or pipeline.

The main decides for each task which roles are useful, how many workers to use,
what dependencies exist, what can run concurrently, when a worker should be
reused or replaced, how repair and verification should proceed, and what
evidence is sufficient. Heavy does not impose a mandatory intake, investigation
wave, execution wave, root-cause gate, tester repair loop, evidence manifest,
deployment procedure, or rollback protocol.

## Available Roles

| Role | Ownership |
| --- | --- |
| Companion | One persistent read-only worker for the project ecosystem. It retains operational context and handles bounded project-context work assigned by the main. It does not research the Internet. |
| Investigator | A disposable read-only worker for any bounded external-information question that benefits from Internet research. It returns a source-linked synthesis and does not implement or choose the project's solution. |
| Default Executor | A Luna production worker for a bounded implementation package. It owns local discovery, implementation, self-check, and ordinary repair inside its assigned surface. |
| Senior Executor | A Sol production worker for one exceptionally difficult package requiring substantial mathematical, logical, architectural, or cross-cutting reasoning. |
| Tester | An independent verification worker. Given the intended behavior, risks, boundaries, and relevant evidence, it designs and executes suitable tests; it may own assigned test assets but not production fixes. |
| Doc-writer | A worker for an assigned durable public-documentation surface based on verified facts. Automatic `agent_docs/` closure belongs to Closure Steward instead. |
| Closure Steward | One fresh end-of-deployment worker that reconciles `agent_docs/` and produces the Deployment Token Report. It does not implement or verify the task. |

Role descriptions define ownership, not eligibility recipes. The main may use a
role whenever its capability fits the task, and may omit it when it does not.

## Knowledge Distribution

Every executor receives a task capsule containing enough of the main agent's
knowledge to complete the package well. Depending on the task, that can include
the intended outcome, relevant project context, ownership and protected areas,
settled decisions and constraints, useful references, recommended reasoning or
implementation guidance, important interfaces and risks, and acceptance
expectations.

The capsule is task-specific and has no mandatory field order or universal
schema. Its purpose is knowledge transfer, not ceremony. It should resolve
choices the main has already made while leaving the executor ownership of
bounded local discovery and execution. A Senior Executor may instead receive
the unresolved decision context when solving that decision is the reason for
using it.

Other workers receive the bounded outcome, context, source boundary, ownership,
constraints, and return evidence they need. The Tester normally designs the
specific tests; the main supplies acceptance intent, risks, scope, and any
required gates rather than prescribing every test case.

Workers retain detailed operational context and return concise decision-ready
results with relevant evidence, limitations, residual risk, and any decision
needed from the main. The main evaluates that evidence and directly inspects
material that controls a high-risk decision or final claim. It need not rerun
fresh, credible worker checks without a concrete reason.

## Fixed Boundaries

- Keep at most 20 active subagents in the session. This count includes the
  persistent Companion and the later Closure Steward.
- Use one persistent Companion and at most one Senior Executor. Use at most one
  Closure Steward at a time.
- Initial task workers normally use `fork_turns="none"`; give them an explicit
  brief instead of copying the main agent's entire conversation.
- The main directly creates and coordinates every worker. Do not create an LLM
  lifecycle parent merely to launch, wait for, or collect another group.
- Run mutable assignments concurrently only when their ownership does not
  overlap. Preserve unrelated user work and keep Git mutations within explicit
  authority.
- Executors own production changes only within their capsules. Testers do not
  repair production code. Doc-writers do not infer unverified behavior.
- Never weaken validation or claim an unrun check passed.

These are platform, safety, independence, and ownership invariants. Within them,
the main freely chooses the topology and lifecycle that fit the task.

## Fast Path and Closure

Questions and small or odd bounded tasks use the direct main-agent fast path.
Do not call workers merely because Heavy is selected, and do not produce a
deployment token report for that path.

Before the final response that completes, pauses, or blocks a substantive
deployment, follow `~/.codex/codex_workflow/closure_steward.md` exactly once.
Pass only the route, unique deployment ID, and closure state. Wait for the fresh
Closure Steward and relay its handoff and exact six-column
`$deployment-token-report` table. A later substantive deployment receives a new
closure worker and report.
