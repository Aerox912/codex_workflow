# codex_workflow 1.2.3 — Session-aware agent scheduling

- Current Codex CLI and app sessions are limited by the platform to **four
  agents running in parallel, including the main agent** (2026-10-21). The
  workflow therefore runs at most three subagents simultaneously and queues
  further tasks.
- Medium and Heavy share `agent_lifecycle.md`: schedule within host capacity,
  queue overflow, retain reports, and reuse compatible workers or release
  finished threads before starting later roles. Four slots including the main
  allow three simultaneous workers; larger task sets span several waves.
- Open-thread and active-turn limits are handled separately. Capacity rejection
  preserves successful work and waits for a capacity change before retrying.
  Executor, Tester, and Archivist can run sequentially without changing their
  ownership or independent verification requirements.
- Installation and deployment closure free capacity for the required Archivist.
  Closure inheritance uses supported `all` or `none` fork values.
- Bootstrap, update, and removal preserve user-owned `[agents]` concurrency
  settings. No setting is generated to raise or bypass session limits.

Release assets: `codex_workflow-1.2.3.zip` and `SHA256SUMS`.

Validation: 64 runtime tests, 9 token-report tests, package-schema validation,
archive verification, and a temporary 1.2.2-to-1.2.3 installed-launcher upgrade
check. These checks cover instruction contracts and deterministic lifecycle
operations. A live session showed the main agent and three workers together;
after that wave reported, a Tester was admitted with earlier thread identities
retained, and a fourth Investigator identity ran in a later wave. `followup_task`
also resumed prior Investigator and Tester identities. This confirms the
scheduling handoff in this session; full CLI+App deployments remain unverified.
