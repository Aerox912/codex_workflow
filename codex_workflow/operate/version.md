# Installed Workflow Version

Run the installed lifecycle CLI:

```text
python3 ~/.codex/codex_workflow/runtime/workflow.py version --json
```

On Windows, use the equivalent `py -3.11` invocation and native paths.
Report the returned `version` as the currently installed user-level workflow
version. If the command reports an error, report that error instead. This
command reads local installation metadata only; it does not check for updates.
