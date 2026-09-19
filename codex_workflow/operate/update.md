# Workflow Update

Supported command forms:

    codex_workflow --update

Use Python 3.11 or newer. Apply the validated update directly with the lifecycle
CLI.

## Source

Use the script to query GitHub Releases and select the highest non-draft SemVer
release containing both the universal ZIP and `SHA256SUMS`. Include prereleases
and never clone the repository. For a different version, verify the checksum,
extract the ZIP safely, and let the installed launcher delegate planning and
application to the incoming CLI, which validates its package schema. When the
selected version matches the installed user-level version, use the installed
source to update the current project without downloading the ZIP again.

## Update

Run:

```text
python3 ~/.codex/codex_workflow/runtime/workflow.py update --project <project>
```

When the installed package still stores `VERSION` at its root, run the incoming
package's `runtime/workflow.py` instead of the installed launcher. The incoming
runtime recognizes that historical layout and migrates it transactionally.

For a newer release, let the script replace installed routes, worker TOMLs, and
workflow-owned skills with the incoming release's fixed definitions. Expect it
to set the workflow-owned `[features.multi_agent_v2]` values in
`~/.codex/config.toml` to `enabled = true`, `min_wait_timeout_ms = 120000`,
`default_wait_timeout_ms = 300000`, and `max_wait_timeout_ms = 1800000`.
Expect it to preserve unrelated Codex settings and skills, project documents,
personalization, project-local instructions, source backups, and the project's
enabled/disabled state. For a project still using an older workflow version,
expect the script to validate its managed region against that version's source
backup. Expect it to remove obsolete workflow-owned files and the retired
workflow-owned `agent_docs/` `.gitignore` rule, create a verified timestamped
backup, and apply user/project state through one compensating transaction.
Preserve an `agent_docs/` ignore rule that the user owns outside the
workflow-managed block.

When the user-level workflow already matches the selected release, expect a
project-only update. It validates the project's managed region against its
recorded historical source, updates only changed project files, and saves a
backup of those files. It leaves the installed user-level definitions and state
unchanged. If the project is already current, expect an explicit no-op with no
new backup. Run the command separately in each installed project.

If a legacy project entry point contains merged local edits, expect the update
to stop. Review and extract only the project-local instructions into a temporary
file, then rerun with:

```text
--legacy-local-instructions <reviewed-file>
```

Treat this as a one-time migration into the dedicated local region. Never infer
the content automatically. Add `--allow-downgrade` for a downgrade.

Report the installed version, the project result, backup location when one was
created, and any failure.
Do not describe a partial or rolled-back update as successful.
