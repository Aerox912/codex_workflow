# Workflow Update

Supported command forms:

    codex_workflow --update

Python 3.11 or newer is required. The lifecycle CLI applies a validated update
directly.

## Source

The script queries GitHub Releases, selects the highest
non-draft SemVer release containing both the universal ZIP and `SHA256SUMS`,
verifies the checksum, and extracts it safely. It includes prereleases and
never clones the repository. The installed launcher delegates planning and
application to the incoming CLI, which owns validation for its package schema.

## Update

Run:

```text
python3 ~/.codex/codex_workflow/workflow.py update --project <project>
```

For migration from a pre-script installation, run the incoming package's
`workflow.py` instead of an older installed launcher.

The script replaces installed routes, worker TOMLs, and workflow-owned skills
with the incoming release's fixed definitions. It preserves unrelated Codex settings and skills,
project documents, personalization, project-local instructions, source backups,
and the project's enabled/disabled state. For projects that still use an older
workflow version, it validates their
managed region against that version's source backup instead of the latest global
template. It removes obsolete workflow-owned files, creates a verified
timestamped backup, and applies user/project state as one compensating
transaction.

If a legacy project entry point contains merged local edits, the update stops.
Review and extract only the project-local instructions into a temporary file,
then rerun with:

```text
--legacy-local-instructions <reviewed-file>
```

This is a one-time migration into the dedicated local region. Never infer the
content automatically. A downgrade additionally requires `--allow-downgrade`.

Report the installed version, backup location, and any failure.
Do not describe a partial or rolled-back update as successful.
