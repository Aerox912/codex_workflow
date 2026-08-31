# Medium Route

Use after Medium is selected under `AGENTS.md`.

## Ownership

The main agent plans, diagnoses, implements, verifies, integrates, and
communicates with the user. Medium does not delegate production implementation,
production repair, root-cause decisions, or verification to another worker.

Medium makes these support roles available:

| Role | Ownership |
| --- | --- |
| Companion | One persistent read-only worker for context in the project ecosystem. It retains useful operational context and handles bounded project-context work assigned by the main. It does not research the Internet. |
| Investigator | A disposable read-only worker for bounded external-information research on the Internet. It synthesizes sources for the main and owns neither project discovery nor project decisions. |
| Closure Steward | One fresh end-of-deployment worker that reconciles `agent_docs/` and produces the Deployment Token Report. It does not implement or verify the task. |

The main decides whether an Investigator is useful, what Companion should
handle, and how support work relates to its own implementation. These roles are
capabilities, not stages in a predefined pipeline. There is no mandatory
investigation, evidence wave, root-cause gate, intake sequence, or report schema.

## Fixed Boundaries

- Never create a production executor, tester, or normal doc-writer package in
  Medium. The main retains that work.
- Keep at most 20 active subagents in the session, including Companion,
  Investigators, and Closure Steward. Use one persistent Companion and at most
  one Closure Steward at a time.
- Give support workers bounded questions and sufficient context. The main owns
  all material interpretations and final claims.
- Preserve unrelated work, verify in proportion to risk, and never claim an
  unrun check passed.

Within those boundaries, the main chooses the task-specific topology, order,
concurrency, tools, checkpoints, and response to failures. It may work directly
without manufacturing work for an available role.

## Fast Path and Closure

Questions and small or odd bounded tasks use the direct main-agent fast path.
Do not initialize Companion or another worker, call Closure Steward, or produce
a deployment token report for that path.

Before the final response that completes, pauses, or blocks a substantive
deployment, follow `~/.codex/codex_workflow/closure_steward.md` exactly once.
Pass only the route, a unique deployment ID, and closure state. Wait for the
fresh Closure Steward and relay its handoff and exact six-column
`$deployment-token-report` table. A later substantive deployment receives a new
ID, handoff, and report.
