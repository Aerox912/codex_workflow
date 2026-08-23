"""Behavioral tests for the deployment verification ledger."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "codex_workflow" / "verification_ledger.py"


class VerificationLedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.project = Path(self.temporary.name) / "project"
        self.project.mkdir()
        self.source = self.project / "src"
        self.source.mkdir()
        (self.source / "app.py").write_text("value = 1\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_ledger(self, *arguments: str, success: bool = True) -> object:
        completed = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), *arguments],
            check=False,
            capture_output=True,
            text=True,
        )
        if success:
            self.assertEqual(completed.returncode, 0, completed.stderr or completed.stdout)
        else:
            self.assertNotEqual(completed.returncode, 0, completed.stdout)
        return json.loads(completed.stdout)

    def initialize(self, *criteria: str) -> object:
        arguments = [
            "init",
            "--project",
            str(self.project),
            "--deployment-id",
            "feature_a",
        ]
        for criterion in criteria:
            arguments.extend(("--criterion", f"{criterion}=tester_a"))
        return self.run_ledger(*arguments)

    def record(
        self,
        criterion: str,
        *,
        status: str = "passed",
        result: str = "1 passed",
        checked_path: str = "src",
        iteration: int = 1,
    ) -> object:
        return self.run_ledger(
            "record",
            "--project",
            str(self.project),
            "--deployment-id",
            "feature_a",
            "--task-id",
            "tester_a",
            "--iteration",
            str(iteration),
            "--criterion",
            criterion,
            "--status",
            status,
            "--method",
            "python -m unittest",
            "--result",
            result,
            "--artifact",
            "/tmp/test.log",
            "--checked-path",
            checked_path,
        )

    def summarize(self) -> dict[str, object]:
        value = self.run_ledger(
            "summarize",
            "--project",
            str(self.project),
            "--deployment-id",
            "feature_a",
        )
        self.assertIsInstance(value, dict)
        return value

    def test_fresh_passed_criteria_are_ready(self) -> None:
        self.initialize("focused", "regression")
        self.record("focused", result="4 passed")
        self.record("regression", result="60 passed")

        summary = self.summarize()

        self.assertTrue(summary["ready"])
        self.assertEqual(
            [(item["criterion"], item["status"], item["freshness"]) for item in summary["criteria"]],
            [
                ("focused", "passed", "fresh"),
                ("regression", "passed", "fresh"),
            ],
        )

    def test_only_affected_criteria_become_stale(self) -> None:
        docs = self.project / "docs"
        docs.mkdir()
        (docs / "guide.md").write_text("Current\n", encoding="utf-8")
        self.initialize("code", "docs")
        self.record("code", checked_path="src")
        self.record("docs", checked_path="docs")

        (self.source / "app.py").write_text("value = 2\n", encoding="utf-8")
        summary = self.summarize()

        by_criterion = {item["criterion"]: item for item in summary["criteria"]}
        self.assertFalse(summary["ready"])
        self.assertEqual(by_criterion["code"]["freshness"], "stale")
        self.assertEqual(by_criterion["code"]["stale_paths"], ["src"])
        self.assertEqual(by_criterion["docs"]["freshness"], "fresh")

    def test_latest_record_replaces_an_older_stale_result(self) -> None:
        self.initialize("regression")
        self.record("regression", result="58 passed")
        (self.source / "app.py").write_text("value = 2\n", encoding="utf-8")
        self.record("regression", result="60 passed", iteration=2)

        summary = self.summarize()

        self.assertTrue(summary["ready"])
        self.assertEqual(summary["criteria"][0]["result"], "60 passed")

    def test_missing_or_failed_criterion_prevents_readiness(self) -> None:
        self.initialize("focused", "regression")
        self.record("focused", status="failed", result="1 failed")

        summary = self.summarize()

        self.assertFalse(summary["ready"])
        self.assertEqual(
            [(item["criterion"], item["status"]) for item in summary["criteria"]],
            [("focused", "failed"), ("regression", "missing")],
        )

    def test_ledger_files_do_not_invalidate_project_root_fingerprint(self) -> None:
        agent_docs = self.project / "agent_docs"
        agent_docs.mkdir()
        handoff = agent_docs / "latest_session_work.md"
        handoff.write_text("Initial\n", encoding="utf-8")
        self.initialize("full_project")
        self.record("full_project", checked_path=".")

        handoff.write_text("Closure update\n", encoding="utf-8")
        summary = self.summarize()

        self.assertTrue(summary["ready"])
        self.assertEqual(summary["criteria"][0]["freshness"], "fresh")

        (self.source / "app.py").write_text("value = 3\n", encoding="utf-8")
        self.assertFalse(self.summarize()["ready"])

    def test_invalid_scope_and_unregistered_criterion_are_rejected(self) -> None:
        self.initialize("focused")
        outside = Path(self.temporary.name) / "outside.txt"
        outside.write_text("outside\n", encoding="utf-8")
        arguments = (
            "record",
            "--project",
            str(self.project),
            "--deployment-id",
            "feature_a",
            "--task-id",
            "tester_a",
            "--criterion",
            "focused",
            "--status",
            "passed",
            "--method",
            "check",
            "--result",
            "passed",
            "--checked-path",
            str(outside),
        )
        value = self.run_ledger(*arguments, success=False)
        self.assertIn("outside the project", value["error"])

        unregistered = list(arguments)
        unregistered[8] = "unknown"
        unregistered[-1] = "src"
        value = self.run_ledger(*unregistered, success=False)
        self.assertIn("not registered", value["error"])

    def test_only_registered_owner_can_record_a_criterion(self) -> None:
        self.initialize("focused")
        value = self.run_ledger(
            "record",
            "--project",
            str(self.project),
            "--deployment-id",
            "feature_a",
            "--task-id",
            "executor_a",
            "--criterion",
            "focused",
            "--status",
            "passed",
            "--method",
            "check",
            "--result",
            "passed",
            "--checked-path",
            "src",
            success=False,
        )
        self.assertIn("owned by task tester_a", value["error"])

    def test_reinitialization_cannot_change_acceptance(self) -> None:
        self.initialize("focused")
        value = self.run_ledger(
            "init",
            "--project",
            str(self.project),
            "--deployment-id",
            "feature_a",
            "--criterion",
            "regression=tester_a",
            success=False,
        )
        self.assertIn("already initialized", value["error"])

    def test_existing_legacy_resource_directory_is_supported(self) -> None:
        legacy = self.project / ".codex_workflow_hidden_resource"
        legacy.mkdir()

        self.initialize("focused")

        self.assertTrue((legacy / "deployments" / "feature_a" / "manifest.json").is_file())
        self.assertFalse((self.project / ".codex_workflow_hidden_resources").exists())


if __name__ == "__main__":
    unittest.main()
