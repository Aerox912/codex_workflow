#!/usr/bin/env python3
"""Append-only verification state for Heavy deployments."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path


SCHEMA_VERSION = 1
SAFE_ID = re.compile(r"^[a-z0-9_]+$")
IGNORED_ROOTS = {
    ".git",
    ".codex_workflow_hidden_resource",
    ".codex_workflow_hidden_resources",
}
ROOT_ONLY_IGNORES = {"agent_docs"}


class LedgerError(ValueError):
    """Raised when ledger input or state is invalid."""


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace(
        "+00:00", "Z"
    )


def _safe_id(value: str, label: str) -> str:
    if not SAFE_ID.fullmatch(value):
        raise LedgerError(f"{label} must contain only lowercase letters, digits, and underscores")
    return value


def _criterion_assignment(value: str) -> tuple[str, str]:
    criterion, separator, owner_task_id = value.partition("=")
    if not separator or "=" in owner_task_id:
        raise LedgerError("criterion must use criterion=owner_task_id")
    return _safe_id(criterion, "criterion"), _safe_id(owner_task_id, "owner task ID")


def _project_root(value: Path) -> Path:
    root = value.expanduser().resolve()
    if not root.is_dir():
        raise LedgerError(f"project is not a directory: {root}")
    return root


def _deployment_dir(project: Path, deployment_id: str, *, create: bool) -> Path:
    current = project / ".codex_workflow_hidden_resources"
    legacy = project / ".codex_workflow_hidden_resource"
    root = current if current.exists() or not legacy.exists() else legacy
    deployment = root / "deployments" / _safe_id(deployment_id, "deployment ID")
    for path in (root, root / "deployments", deployment):
        if path.is_symlink() or (path.exists() and not path.is_dir()):
            raise LedgerError(f"ledger path is not a regular directory: {path}")
        if create:
            path.mkdir(exist_ok=True)
    return deployment


def _atomic_json(path: Path, value: dict[str, object], *, replace: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary_name = tempfile.mkstemp(
        prefix=".verification-ledger-", suffix=".json", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(value, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        if replace:
            os.replace(temporary, path)
        else:
            try:
                os.link(temporary, path)
            except FileExistsError as error:
                raise LedgerError(f"ledger record already exists: {path}") from error
            temporary.unlink()
    finally:
        if temporary.exists():
            temporary.unlink()


def _read_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise LedgerError(f"cannot read ledger JSON {path}: {error}") from error
    if not isinstance(value, dict):
        raise LedgerError(f"ledger JSON is not an object: {path}")
    return value


def _relative_path(project: Path, raw: str) -> tuple[str, Path]:
    candidate = Path(raw)
    if not candidate.is_absolute():
        candidate = project / candidate
    candidate = Path(os.path.abspath(candidate))
    try:
        relative = candidate.relative_to(project)
    except ValueError as error:
        raise LedgerError(f"checked path is outside the project: {raw}") from error
    rendered = relative.as_posix() or "."
    return rendered, candidate


def _ignored(path: Path, project: Path, checked_root: Path) -> bool:
    try:
        relative = path.relative_to(project)
    except ValueError:
        return False
    return bool(
        relative.parts
        and (
            relative.parts[0] in IGNORED_ROOTS
            or (checked_root == project and relative.parts[0] in ROOT_ONLY_IGNORES)
        )
    )


def _hash_file(path: Path, digest: object) -> None:
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)


def _raise_walk_error(error: OSError) -> None:
    raise error


def _fingerprint(project: Path, raw: str) -> dict[str, str]:
    relative, path = _relative_path(project, raw)
    digest = hashlib.sha256()
    digest.update(b"codex-workflow-path-v1\0")
    digest.update(relative.encode("utf-8", errors="surrogateescape"))
    digest.update(b"\0")

    try:
        if path.is_symlink():
            digest.update(b"symlink\0")
            digest.update(os.readlink(path).encode("utf-8", errors="surrogateescape"))
        elif not path.exists():
            digest.update(b"missing\0")
        elif path.is_file():
            digest.update(b"file\0")
            _hash_file(path, digest)
        elif path.is_dir():
            digest.update(b"directory\0")
            for current, directory_names, file_names in os.walk(
                path, followlinks=False, onerror=_raise_walk_error
            ):
                current_path = Path(current)
                directory_names[:] = sorted(
                    name
                    for name in directory_names
                    if not _ignored(current_path / name, project, path)
                    and not (current_path / name).is_symlink()
                )
                current_relative = current_path.relative_to(path).as_posix()
                digest.update(b"dir\0")
                digest.update(current_relative.encode("utf-8", errors="surrogateescape"))
                digest.update(b"\0")
                entries = [current_path / name for name in sorted(file_names)]
                entries.extend(
                    current_path / name
                    for name in sorted(os.listdir(current_path))
                    if (current_path / name).is_symlink()
                    and name not in file_names
                )
                for entry in entries:
                    if _ignored(entry, project, path):
                        continue
                    entry_relative = entry.relative_to(path).as_posix()
                    digest.update(entry_relative.encode("utf-8", errors="surrogateescape"))
                    digest.update(b"\0")
                    if entry.is_symlink():
                        digest.update(b"symlink\0")
                        digest.update(
                            os.readlink(entry).encode("utf-8", errors="surrogateescape")
                        )
                    elif entry.is_file():
                        digest.update(b"file\0")
                        _hash_file(entry, digest)
                    else:
                        raise LedgerError(f"unsupported checked-path entry: {entry}")
        else:
            raise LedgerError(f"unsupported checked path: {path}")
    except OSError as error:
        raise LedgerError(f"cannot fingerprint checked path {path}: {error}") from error

    return {"path": relative, "sha256": digest.hexdigest()}


def _manifest_path(project: Path, deployment_id: str, *, create: bool) -> Path:
    return _deployment_dir(project, deployment_id, create=create) / "manifest.json"


def initialize(args: argparse.Namespace) -> dict[str, object]:
    project = _project_root(args.project)
    deployment_id = _safe_id(args.deployment_id, "deployment ID")
    assignments: dict[str, str] = {}
    for value in args.criterion:
        criterion, owner_task_id = _criterion_assignment(value)
        if criterion in assignments and assignments[criterion] != owner_task_id:
            raise LedgerError(f"criterion has conflicting owners: {criterion}")
        assignments[criterion] = owner_task_id
    if not assignments:
        raise LedgerError("at least one required criterion is needed")
    criteria = [
        {"criterion": criterion, "owner_task_id": assignments[criterion]}
        for criterion in sorted(assignments)
    ]
    path = _manifest_path(project, deployment_id, create=True)
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise LedgerError(f"deployment manifest is not a regular file: {path}")
    created_at = _now()
    if path.is_file():
        existing = _validated_manifest(project, deployment_id)
        if existing["required_criteria"] != criteria:
            raise LedgerError("deployment is already initialized with different criteria")
        return {
            "deployment_id": deployment_id,
            "manifest": str(path),
            "criteria": criteria,
        }
    manifest: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "deployment_id": deployment_id,
        "required_criteria": criteria,
        "created_at": created_at,
        "updated_at": _now(),
    }
    _atomic_json(path, manifest, replace=False)
    return {"deployment_id": deployment_id, "manifest": str(path), "criteria": criteria}


def record(args: argparse.Namespace) -> dict[str, object]:
    project = _project_root(args.project)
    deployment_id = _safe_id(args.deployment_id, "deployment ID")
    task_id = _safe_id(args.task_id, "task ID")
    criterion = _safe_id(args.criterion, "criterion")
    if args.iteration < 1:
        raise LedgerError("iteration must be positive")
    manifest_path = _manifest_path(project, deployment_id, create=False)
    if not manifest_path.is_file():
        raise LedgerError(f"deployment manifest is missing: {manifest_path}")
    manifest = _validated_manifest(project, deployment_id)
    required = {
        item["criterion"]: item["owner_task_id"]
        for item in manifest["required_criteria"]
    }
    if criterion not in required:
        raise LedgerError(f"criterion is not registered for deployment: {criterion}")
    if task_id != required[criterion]:
        raise LedgerError(
            f"criterion {criterion} is owned by task {required[criterion]}, not {task_id}"
        )
    if not args.checked_path:
        raise LedgerError("at least one checked path is needed")

    fingerprints = [_fingerprint(project, raw) for raw in args.checked_path]
    paths = [item["path"] for item in fingerprints]
    if len(paths) != len(set(paths)):
        raise LedgerError("checked paths must be unique")

    completed_at = _now()
    value: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "deployment_id": deployment_id,
        "task_id": task_id,
        "iteration": args.iteration,
        "criterion": criterion,
        "status": args.status,
        "method": args.method,
        "result": args.result,
        "artifact": args.artifact,
        "completed_at": completed_at,
        "checked_paths": fingerprints,
    }
    records = manifest_path.parent / "verification"
    if records.is_symlink() or (records.exists() and not records.is_dir()):
        raise LedgerError(f"verification path is not a regular directory: {records}")
    records.mkdir(exist_ok=True)
    filename = (
        f"{completed_at.replace(':', '').replace('-', '')}-{task_id}-{criterion}-"
        f"{uuid.uuid4().hex}.json"
    )
    path = records / filename
    _atomic_json(path, value, replace=False)
    return {"deployment_id": deployment_id, "criterion": criterion, "record": str(path)}


def _validated_manifest(project: Path, deployment_id: str) -> dict[str, object]:
    path = _manifest_path(project, deployment_id, create=False)
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise LedgerError(f"deployment manifest is not a regular file: {path}")
    if not path.exists():
        raise LedgerError(f"deployment manifest is missing: {path}")
    manifest = _read_json(path)
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise LedgerError(f"unsupported manifest schema: {path}")
    if manifest.get("deployment_id") != deployment_id:
        raise LedgerError(f"manifest deployment ID disagrees with its path: {path}")
    criteria = manifest.get("required_criteria")
    if not isinstance(criteria, list) or not criteria:
        raise LedgerError(f"manifest has no required criteria: {path}")
    seen: set[str] = set()
    for assignment in criteria:
        if not isinstance(assignment, dict):
            raise LedgerError(f"manifest contains an invalid criterion assignment: {path}")
        criterion = assignment.get("criterion")
        owner_task_id = assignment.get("owner_task_id")
        if not isinstance(criterion, str) or not isinstance(owner_task_id, str):
            raise LedgerError(f"manifest contains an invalid criterion assignment: {path}")
        _safe_id(criterion, "criterion")
        _safe_id(owner_task_id, "owner task ID")
        if criterion in seen:
            raise LedgerError(f"manifest contains a duplicate criterion: {path}")
        seen.add(criterion)
    return manifest


def _records(project: Path, deployment_id: str) -> list[dict[str, object]]:
    directory = _deployment_dir(project, deployment_id, create=False) / "verification"
    if not directory.exists():
        return []
    if directory.is_symlink() or not directory.is_dir():
        raise LedgerError(f"verification path is not a regular directory: {directory}")
    records: list[dict[str, object]] = []
    for path in sorted(directory.glob("*.json")):
        if path.is_symlink() or not path.is_file():
            raise LedgerError(f"verification record is not a regular file: {path}")
        value = _read_json(path)
        if value.get("schema_version") != SCHEMA_VERSION:
            raise LedgerError(f"unsupported verification schema: {path}")
        if value.get("deployment_id") != deployment_id:
            raise LedgerError(f"verification deployment ID disagrees with its path: {path}")
        for field in ("task_id", "criterion", "status", "completed_at"):
            if not isinstance(value.get(field), str):
                raise LedgerError(f"verification record lacks {field}: {path}")
        value["_path"] = str(path)
        records.append(value)
    return records


def summarize(args: argparse.Namespace) -> dict[str, object]:
    project = _project_root(args.project)
    deployment_id = _safe_id(args.deployment_id, "deployment ID")
    manifest = _validated_manifest(project, deployment_id)
    required = {
        item["criterion"]: item["owner_task_id"]
        for item in manifest["required_criteria"]
    }
    grouped: dict[str, list[dict[str, object]]] = {criterion: [] for criterion in required}
    warnings: list[str] = []
    for value in _records(project, deployment_id):
        criterion = str(value["criterion"])
        if criterion not in grouped:
            raise LedgerError(f"verification record has unregistered criterion {criterion}")
        if value["task_id"] != required[criterion]:
            raise LedgerError(
                f"criterion {criterion} has a record from non-owner task {value['task_id']}"
            )
        grouped[criterion].append(value)

    criteria: list[dict[str, object]] = []
    ready = True
    for criterion, owner_task_id in required.items():
        values = grouped[criterion]
        if not values:
            criteria.append(
                {
                    "criterion": criterion,
                    "status": "missing",
                    "freshness": "missing",
                    "result": "no verification record",
                    "task_id": None,
                    "owner_task_id": owner_task_id,
                    "artifact": None,
                    "record": None,
                }
            )
            ready = False
            continue
        latest = max(values, key=lambda item: (str(item["completed_at"]), str(item["_path"])))
        checked = latest.get("checked_paths")
        if not isinstance(checked, list) or not checked:
            raise LedgerError(f"verification record has no checked paths: {latest['_path']}")
        stale_paths: list[str] = []
        for item in checked:
            if not isinstance(item, dict) or not isinstance(item.get("path"), str):
                raise LedgerError(f"verification record has an invalid path: {latest['_path']}")
            current = _fingerprint(project, item["path"])
            if current.get("sha256") != item.get("sha256"):
                stale_paths.append(item["path"])
        freshness = "stale" if stale_paths else "fresh"
        status = str(latest["status"])
        if status != "passed" or stale_paths:
            ready = False
        criteria.append(
            {
                "criterion": criterion,
                "status": status,
                "freshness": freshness,
                "stale_paths": stale_paths,
                "result": latest.get("result"),
                "task_id": latest.get("task_id"),
                "owner_task_id": owner_task_id,
                "artifact": latest.get("artifact"),
                "record": latest.get("_path"),
                "completed_at": latest.get("completed_at"),
            }
        )

    return {
        "schema_version": SCHEMA_VERSION,
        "deployment_id": deployment_id,
        "ready": ready,
        "criteria": criteria,
        "warnings": sorted(set(warnings)),
    }


def _markdown(summary: dict[str, object]) -> str:
    lines = [
        "| Criterion | Status | Freshness | Result | Evidence |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in summary["criteria"]:
        artifact = item.get("artifact") or item.get("record") or "—"
        values = (
            item["criterion"],
            item["status"],
            item["freshness"],
            item.get("result") or "—",
            artifact,
        )
        escaped = [str(value).replace("|", "\\|").replace("\n", " ") for value in values]
        lines.append("| " + " | ".join(escaped) + " |")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    initialize_parser = commands.add_parser("init")
    initialize_parser.add_argument("--project", type=Path, required=True)
    initialize_parser.add_argument("--deployment-id", required=True)
    initialize_parser.add_argument(
        "--criterion",
        action="append",
        default=[],
        metavar="CRITERION=OWNER_TASK_ID",
    )

    record_parser = commands.add_parser("record")
    record_parser.add_argument("--project", type=Path, required=True)
    record_parser.add_argument("--deployment-id", required=True)
    record_parser.add_argument("--task-id", required=True)
    record_parser.add_argument("--iteration", type=int, default=1)
    record_parser.add_argument("--criterion", required=True)
    record_parser.add_argument(
        "--status", choices=("passed", "failed", "blocked", "skipped"), required=True
    )
    record_parser.add_argument("--method", required=True)
    record_parser.add_argument("--result", required=True)
    record_parser.add_argument("--artifact", default="")
    record_parser.add_argument("--checked-path", action="append", default=[])

    summary_parser = commands.add_parser("summarize")
    summary_parser.add_argument("--project", type=Path, required=True)
    summary_parser.add_argument("--deployment-id", required=True)
    summary_parser.add_argument("--format", choices=("json", "markdown"), default="json")

    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "init":
            value = initialize(args)
        elif args.command == "record":
            value = record(args)
        else:
            value = summarize(args)
    except (LedgerError, OSError) as error:
        print(json.dumps({"error": str(error)}, sort_keys=True))
        return 1

    if args.command == "summarize" and args.format == "markdown":
        print(_markdown(value))
    else:
        print(json.dumps(value, separators=(",", ":"), sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
