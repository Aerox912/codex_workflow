# Release Process

This repository publishes the workflow as GitHub Release assets. The release
payload is intentionally independent of the repository presentation and
development files.

## Repository and asset layout

The repository-only release machinery is:

```text
.github/workflows/release.yml
scripts/package_release.py
RELEASING.md
```

Every archive contains exactly this top-level directory and nothing beside it:

```text
codex_workflow/
├── VERSION
├── user_AGENTS.md
├── AGENTS.md
├── bootstrap.md
├── install.md
├── update.md
├── remove.md
├── enable_auto_check_update.md
├── disable_auto_check_update.md
├── enable_auto_update.md              # legacy alias
├── disable_auto_update.md             # legacy alias
├── workflow.py
├── runtime/
├── resources/                              # immutable package defaults
├── agents/
└── project_docs/
```

The package does not contain `README.md`, `illustration.png`,
`workflow_usage.md`, `RELEASING.md`, `.github/`, `scripts/`, `.git/`, or any
other repository-only file. All files below `codex_workflow/` are included so
the installed workflow remains self-contained.

Each GitHub Release publishes one universal asset for every supported operating
system:

- `codex_workflow-<version>.zip`;
- `SHA256SUMS` for the ZIP asset.

## Versioning

Use SemVer 2.0.0. Fork releases follow the upstream stable version with a
`-patch.N` prerelease suffix: `1.1.4-patch.1`, then `1.1.3-patch.2`. When the
upstream base advances, restart at patch 1, for example `1.1.4-patch.1`.
Keep the plain version in `codex_workflow/VERSION`, the
`codex-workflow-version` marker in `codex_workflow/user_AGENTS.md`, and the
companion plugin version in `plugins/codex-workflow/.codex-plugin/plugin.json`
identical. Use `scripts/set_fork_version.py` to change those surfaces together.
The release tag is the same value with a leading `v`, for example
`VERSION=1.1.4-patch.1` and tag `v1.1.4-patch.1`.

Every upstream integration selects the next unused patch number for its
upstream base from the Aerox912 fork's releases before pushing `main`:

```text
python3 scripts/set_fork_version.py --upstream-version 1.1.3 --patch 1
```

## Local build and validation

Run these commands from the repository root. The builder uses only Python's
standard library, requires Python 3.11 or newer, and works on Linux, macOS, and
Windows.

Linux/macOS:

```sh
python3 -B scripts/test_workflow_runtime.py -v
python3 scripts/package_release.py --release-tag v1.1.4-patch.1 --output-dir dist
python3 scripts/package_release.py --verify dist/codex_workflow-*.zip
```

Windows PowerShell:

```powershell
py -3 -B scripts\test_workflow_runtime.py -v
py -3 scripts/package_release.py --release-tag v1.1.4-patch.1 --output-dir dist
py -3 scripts/package_release.py --verify dist\codex_workflow-1.1.4-patch.1.zip
```

The build validates the version, marker, lifecycle runtime, and required
resources; rejects generated Python caches; creates a deterministic ZIP asset;
and writes `dist/SHA256SUMS`. Run the runtime tests before packaging and inspect
the archive listing when package contents change.

## Automatic fork publishing

A push to the Aerox912 fork's `main` branch starts
`.github/workflows/release.yml` when release-owned files change. The workflow
derives the tag from the validated package version, runs the runtime tests,
validates and builds the universal archive, verifies it, and publishes the tag
and prerelease with generated notes. If a complete release for that version
already exists, the workflow succeeds without changing it. A tag without a
complete release is a hard failure and is never moved or overwritten.

The scheduled upstream-sync task is authorized to use this path after a clean
integration and successful local validation. `workflow_dispatch` can retry the
same idempotent pipeline. Promoting a prerelease to stable or manually replacing
release assets remains a separate approval-gated operation.

If the workflow is unavailable, the equivalent manual publication command is:

```sh
gh release create v1.1.4-patch.1 \
  dist/codex_workflow-1.1.4-patch.1.zip \
  dist/SHA256SUMS \
  --title "codex_workflow v1.1.4-patch.1" \
  --generate-notes \
  --prerelease
```

The manual command is also approval-gated and must use assets built from the
same tagged commit.

## Consumer commands

- Initial installation reads the extracted release package's
  `codex_workflow/bootstrap.md`; the bundled lifecycle CLI validates and
  applies the user-level bootstrap transaction directly.
- `codex_workflow --install` reads the installed `install.md` and creates only
  project-level workflow assets from the existing bootstrap.
- At session start, the installed runtime checks GitHub Releases once when
  `auto_check_update` is enabled and reports an available update.
- `codex_workflow --enable_auto_check_update` explicitly enables that independent
  installed preference.
- `codex_workflow --disable_auto_check_update` disables it again. The former
  `--enable_auto_update` and `--disable_auto_update` prompts remain compatibility
  aliases; no command automatically installs an update.
- `codex_workflow --update` selects the latest appropriate ZIP asset, downloads
  it from its GitHub Release URL, verifies it, and follows the package's update
  procedure. It never clones the repository.
- `codex_workflow --remove` first displays a destructive dry-run summary and
  requires one explicit second confirmation before deleting workflow-owned
  files.
