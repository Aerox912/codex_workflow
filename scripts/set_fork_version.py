#!/usr/bin/env python3
"""Set the Aerox912 fork version from an upstream base and patch number."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


UPSTREAM_VERSION = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
USER_VERSION = re.compile(r"<!-- codex-workflow-version: ([^ ]+) -->")


class ForkVersionError(ValueError):
    """Raised when the fork version surfaces are missing or inconsistent."""


def set_fork_version(root: Path, upstream_version: str, patch_number: int) -> dict:
    root = root.resolve()
    upstream_version = upstream_version.removeprefix("v")
    if not UPSTREAM_VERSION.fullmatch(upstream_version):
        raise ForkVersionError(
            "upstream version must be a stable X.Y.Z semantic version"
        )
    if patch_number < 1:
        raise ForkVersionError("patch number must be at least 1")

    operate = root / "codex_workflow" / "operate"
    if not (operate / "VERSION").is_file():
        operate = root / "codex_workflow"
    version_path = operate / "VERSION"
    user_agents_path = operate / "user_AGENTS.md"
    plugin_path = root / "plugins" / "codex-workflow" / ".codex-plugin" / "plugin.json"

    current_version = version_path.read_text(encoding="utf-8").strip()
    user_agents = user_agents_path.read_text(encoding="utf-8")
    user_match = USER_VERSION.search(user_agents)
    if user_match is None:
        raise ForkVersionError("codex_workflow/user_AGENTS.md version marker is missing")

    plugin_text = plugin_path.read_text(encoding="utf-8")
    plugin = json.loads(plugin_text)
    plugin_version = plugin.get("version")
    if plugin.get("name") != "codex-workflow" or not isinstance(plugin_version, str):
        raise ForkVersionError("companion plugin metadata is invalid")

    current_versions = {current_version, user_match.group(1), plugin_version}
    if len(current_versions) != 1:
        raise ForkVersionError(
            "fork version surfaces disagree: " + ", ".join(sorted(current_versions))
        )

    target_version = f"{upstream_version}-patch.{patch_number}"
    changed: list[str] = []
    if current_version != target_version:
        updated_agents, marker_count = USER_VERSION.subn(
            f"<!-- codex-workflow-version: {target_version} -->",
            user_agents,
            count=1,
        )
        if marker_count != 1:
            raise ForkVersionError("unable to update the user workflow version marker")
        old_plugin_field = f'"version": "{plugin_version}"'
        if plugin_text.count(old_plugin_field) != 1:
            raise ForkVersionError("unable to update the companion plugin version")
        updated_plugin = plugin_text.replace(
            old_plugin_field,
            f'"version": "{target_version}"',
            1,
        )

        version_path.write_text(target_version + "\n", encoding="utf-8")
        changed.append(version_path.relative_to(root).as_posix())
        user_agents_path.write_text(updated_agents, encoding="utf-8")
        changed.append(user_agents_path.relative_to(root).as_posix())
        plugin_path.write_text(
            updated_plugin,
            encoding="utf-8",
        )
        changed.append(plugin_path.relative_to(root).as_posix())

    return {
        "upstream_version": upstream_version,
        "previous_version": current_version,
        "version": target_version,
        "patch": patch_number,
        "changed": changed,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream-version", required=True)
    parser.add_argument("--patch", required=True, type=int)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the script's repository)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = set_fork_version(args.root, args.upstream_version, args.patch)
    except (ForkVersionError, OSError, json.JSONDecodeError) as error:
        print(f"fork version update failed: {error}")
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
