# Agent Capacity and Lifecycle

Use as the main agent before creating or resuming workers in Medium, Heavy,
installation, or deployment closure. Apply the current session's tool schema
and capacity; worker role definitions do not require resident workers.
Current Codex CLI and app sessions have a platform limit of four concurrent
agents including the main (2026-10-21), leaving at most three worker turns.

## Capacity

- Convert applicable session, tool, and effective platform limits to worker
  budgets, then use the lowest. A limit stated as total agents includes the
  main; four total slots allow three workers. A limit explicitly excluding the
  main is already a worker budget.
  If no capacity is exposed, start with at most three workers and reduce that
  budget on a capacity rejection. Do not probe by launching excess workers.
- Distinguish active-turn limits from open-thread limits. An idle or completed
  worker may still occupy an open-thread slot. Count all workers charged to the
  session, including retained workers and descendants outside the current set.
  If occupancy semantics are unspecified, count retained threads until the host
  confirms their capacity is reusable. Keep workflow workers as direct children
  of the main.
- Choose total task count for coverage and ownership, then fit simultaneous
  work into available capacity. Queue overflow; a larger task set does not
  require all its workers to coexist. Platform configuration cannot override a
  stricter session limit. Do not raise limits to make a route work.
- When open threads consume slots and no release operation exists, plan room
  for all required roles before starting optional support. Roles depend on the
  task: reserve Tester only when independent verification is required, and
  Archivist for installation or substantive deployment closure. A Heavy
  deployment needing Executor, Tester, and Archivist must leave room for all
  three identities. Leave future slots unallocated until needed, reuse matching
  roles, and limit optional support to the remaining capacity.
  If required roles cannot fit and slots cannot be released, report that
  capability blocker before starting work that depends on them.

## Dispatch and Release

1. Keep a compact working queue of Task IDs, role, ownership, dependencies,
   worker identity, and state. Use retained context, not a new durable ledger.
2. Dispatch ready, independent tasks together up to available capacity. Wait
   for their reports using lifecycle events or an appropriate wait. Save each
   compact report and its evidence references before releasing the worker.
3. Reuse an idle worker only for compatible work in the same role. Send a full
   capsule with a new Task ID for a new package; a continuation keeps its Task
   ID and receives only the delta. Independent Explorer or Investigator angles
   on the same question require fresh worker contexts, full capsules, and
   distinct Task IDs, including across waves. Do not reuse a context containing
   another angle's findings as independent coverage. If a fresh context cannot
   be admitted, queue that angle or report the coverage gap for the main's
   sufficiency decision. Preserve Executor/Tester separation; do not relabel a
   worker to change its role.
4. Release workers that are no longer needed before creating replacements or
   changing role mix. If the host exposes `close_agent` or an equivalent thread
   release, close finished workers and confirm release before reusing their
   slots. Completion alone is insufficient for an open-thread limit. With an
   active-turn limit, a terminal turn releases its running slot; keep the idle
   identity only when useful and use the host's supported follow-up operation.
   Interruption is not proof of thread release; neither is runtime unloading.
5. Start the next queued tasks as capacity becomes available. A research set
   can span several waves; preserve independent searches and compare the full
   required set once before deciding. Never wait for an unstarted queued task
   as a condition for freeing the slots it needs.

For example, seven independent tasks under four total slots run in waves of
at most three, three, and one worker when slots can be released or compatible
workers reused. With one releasable worker slot, Heavy can run an Executor,
save its report and release its slot, then create an independent Tester.
If repair is needed after closing the Executor, recreate the same role
with its task capsule, current state, and failure evidence; do the same for a
closed Tester on recheck. Worker identity retention must not block progress.

## Capacity Failure and Closure

On a capacity rejection, preserve successful dispatches and reports, queue the
rejected task, and stop spawning until a turn finishes under an active-turn cap
or thread release is confirmed under an open-thread cap. Retry only after that
capacity change; do not repeat an unchanged spawn or treat slot exhaustion as a
worker's evidence-free response. If the
host offers no release operation, reuse compatible idle workers when possible.
If a required role still cannot run, report the exact capability blocker and
unfinished work without claiming completion or changing route ownership.
Medium keeps production and verification with the main; Heavy keeps them with
Executors and Testers even under reduced capacity.

Before installation documentation or substantive deployment closure, collect
relevant reports and admit one Archivist within the active budget. Under an
active-turn cap, completed turns suffice even when their threads are retained
and no close operation exists. Close finished threads only when an applicable
open-thread cap requires their release and the host supports that operation.
Create required roles only when their tasks are ready. Wait for the required
documentation and reporting handoff, preserve it, and release the Archivist if
supported.
