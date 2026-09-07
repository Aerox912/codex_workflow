---
name: codex-workflow
description: Manage projects that use the Aerox912 Codex Workflow fork, including its exact codex_workflow lifecycle commands, route selection, configuration, enablement, updates, and removal. Use when the user invokes codex_workflow, asks to use Light, Medium, or Heavy route, or asks about the installed Workflow runtime.
---

# Codex Workflow

Use the installed Codex Workflow runtime as the source of truth for lifecycle behavior.

## Ownership boundary

- The plugin exposes Workflow guidance to Codex. It does not install or update the runtime.
- In an agent-system-managed setup, `~/.codex/codex_workflow` is delivered from the pinned Aerox912 fork by the agent-system installers.
- Never download, self-update, replace, or remove that runtime unless the user explicitly requests the corresponding lifecycle or agent-system operation.

## Exact lifecycle commands

When the user's trimmed message exactly matches a supported `codex_workflow` command, locate the installed runtime under `$CODEX_HOME/codex_workflow` or `~/.codex/codex_workflow`, read the command's guide completely, and follow it:

- `--install`: `operate/install.md`
- `--update`: `operate/update.md`
- `--check-update`: `operate/check_update.md`
- `--remove`: `operate/remove.md`
- `--personal`: `operate/personalization_guide.md`
- `--disable`: `operate/disable.md`
- `--enable`: `operate/enable.md`

Use the available Python 3 launcher with `runtime/workflow.py`. On an older
installation, read its root-level guide and launcher instead. Automatic-update
toggle commands are retired in the new upstream design; do not invent an
equivalent or change agent-system's update ownership.
Run project operations against the current repository root and preserve
project-local protected regions.

## Routes

- Light is the default leaf-state route and uses no Workflow workers.
- Medium and Heavy are user-selected deployment routes. Read and follow the installed route documents before entering either route.
- Do not infer Medium or Heavy from task complexity. Keep the selected route until the user changes it or the session ends.

If the runtime is absent, report that the companion plugin is installed but the separately managed runtime is missing. Point the user to the agent-system installer instead of downloading an upstream release.
