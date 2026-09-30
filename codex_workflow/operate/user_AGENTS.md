<!-- codex-workflow-user-id: viettran-edgeAI/codex_workflow -->
<!-- codex-workflow-version: 1.2.2 -->
<!-- codex-workflow-user-managed-start -->
# AGENTS.md

## Workflow Principles

- Keep modules cohesive, interfaces explicit, coupling minimal, and behavior
  testable, replaceable, and reusable.
- Define proportionate acceptance and verification before implementation. Never
  weaken coverage, assertions, or failure visibility to save time or tokens.
- Avoid unnecessary process or safeguards; preserve unrelated user work and use
  verified facts in durable documentation.

## Route Selection

Select one route: **Light** works directly with minimal context;
**Medium** keeps planning, diagnosis, implementation, and verification with the
main agent and uses bounded read-only discovery, solution research, and
documentation support from `~/.codex/codex_workflow/medium_route.md`;
**Heavy** delegates bounded production, verification, documentation, context
exploration, and solution research under
`~/.codex/codex_workflow/heavy_route.md`.

Follow the user's route selection. Use Light when none is selected; do not infer
Medium or Heavy. Keep the route until the user changes it or the session ends.

## Rollout Efficiency

Batch independent reads, searches, metadata checks, and other known-input
operations. Keep dependencies and overlapping mutations sequential. In Medium
or Heavy, dispatch independent workers together, wait for the relevant set, and
synthesize their reports once. Workers return compact evidence-linked reports
through their parent-child result channel; Explorer owns bounded context
discovery.
For difficult or broad questions, prefer parallel workers (e.g., 2, 3, or more)
when independent angles can improve coverage and result quality. The main
chooses roles and counts per bounded question; a narrow question can use one
worker. Give workers addressing the same question complementary angles and
compare the assigned set's evidence before deciding.

## Platform Paths

Interpret `/` as a platform-neutral separator and translate paths for the
current operating system and shell.

## Lifecycle Commands

When the user's trimmed message matches one of the following command forms,
read and follow the corresponding guide. Forms without placeholders must match
exactly.

- codex_workflow --install
  Guide:  ~/.codex/codex_workflow/operate/install.md.

- codex_workflow --update
  Guide:  ~/.codex/codex_workflow/operate/update.md.

- codex_workflow --check-update
  Guide:  ~/.codex/codex_workflow/operate/check_update.md.

- codex_workflow --version
  Guide:  ~/.codex/codex_workflow/operate/version.md.

- codex_workflow --remove
  Guide: ~/.codex/codex_workflow/operate/remove.md.
<!-- codex-workflow-user-managed-end -->
