<h3 align="center"><big><big><strong>SIMPLE&emsp;&emsp;───&emsp;&emsp;EASY&emsp;&emsp;───&emsp;&emsp;EFFICIENT</strong></big></big></h3>
<p align="center"><small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(to use)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(to install)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(token consumption)</small></p>
<hr>

![Workflow illustration](illustration.png)

Built for maximum token efficiency: Heavy-route swarm execution with the main
agent as the knowledge director, plus a persistent Companion that handles
routine read-only context work. Workers keep operational evidence in artifacts
and return small knowledge deltas. Medium keeps implementation and verification
in the main agent while retaining cross-session workflow support.

> ⭐ For lightweight tasks, it won’t overdo things. Light route is default.

## 1. Quick installation ⚙️

Requires Python 3.11 or newer for deterministic lifecycle operations.

### Open Codex CLI / Codex app from your project directory 

Change permision to `approve for me/full access`.

▶️ Send:

```text
Download and extract the latest `codex_workflow-<version>.zip` asset (not GitHub's Source code archive) from https://github.com/viettran-edgeAI/codex_workflow/releases. Verify it against `SHA256SUMS`, then read the bundled `codex_workflow/bootstrap.md` and follow it to complete the initial installation.
```
> ⭐ Recommended: use 5.6 Luna xhigh for installation. 

🔄 Restart Codex after installation

The initial bootstrap is complete only after its required `doc-writer` action
succeeds; restart Codex after both steps. Once that bootstrap is complete, the
current project is ready to use. Whenever you need to install this workflow for
a new project, simply open Codex and send: `codex_workflow --install`

## 2. Workflow usage 

### This workflow has 3 routes:
- Light route : No subagents, no workflow, minimal context.
- Heavy route : Full workflow mode. Deploy production task workers.
- Medium route: Full workflow mode, with implementation and verification kept
  in the main agent rather than delegated to production task workers.

> Full workflow mode activates the `Companion` secretary and automatic context
> and progress management. Heavy additionally uses bounded investigation teams
> and delegated production workers; Medium may use explicitly requested
> read-only evidence support, but does not delegate implementation or
> verification.

In Medium, the main agent owns implementation and verification. Choose it when
you want workflow-mode context support without delegating production work.

### How to use
- Normally, for simple work, general Q&A, you don't need to do anything. `light route` is the default route.

--------------------------------

- When starting or continuing a plan in progress, tell Codex in the prompt:

```text
use medium/heavy route. [your task description]
```
Or continue a task that was already underway in the previous session: 
```text
use medium/heavy route. Continue ongoing work.
```
Codex stays on the selected route until you change it.
---------------
> **⭐ Recommendation:** Assign very large and complex tasks to the `heavy route` to make the most of its capabilities and maximize token usage savings. Don't hesitate to choose 5.6 Sol xhigh for this route. Using lower reasoning effort will not actually save tokens and will severely reduce its coordination capabilities.

### Coordinating architecture

The Heavy route uses a main-directed coordination model: the main agent remains
the knowledge director, Companion handles routine read-only office work, and
specialized workers search, implement, verify, document, and close bounded work.

| Role or mechanism | Responsibility | Boundary |
| --- | --- | --- |
| Main agent | In Heavy, reads the five non-diary core project documents, identifies the defect, chooses the plan, and defines and evaluates acceptance gates. | Workers execute operational checks; gate ownership does not require the main agent to rerun their evidence. |
| Companion | Performs diary and Heavy module-document intake, indexing, conflict checks, integration/config/tool mapping, status aggregation, evidence-owner tracking, and decision-to-capsule formatting. | One persistent read-only secretary; the main approves decisions and directly checks decisive evidence. |
| Investigators | Explore independent bug, evidence, prior-art, and solution lanes. | The main agent defines lanes and makes the root-cause decision. |
| Role-scoped knowledge | Gives executors implementation guidance, testers verification criteria, and investigators focused search briefs. | Workers receive only the context needed for their role. |
| Executor–tester loop | `default_executor` implements; the tester verifies independently and reports production defects. | The main routes repair to the executor and reactivates the tester; leaf roles need no collaboration tools. |
| Evidence manifest | Tracks each gate's class, owner, status, method/artifact, checked scope/freshness, and limitation. | Unavailable browser/OCR evidence is distinct from product failure and does not erase unrelated passing gates. |
| Rollback policy | Compares the candidate with the actual pre-change baseline. | Rollback requires a material regression or required failure and a safer or more functional prior state. |
| Senior executor | Handles exceptionally difficult mathematical, logical, or cross-cutting work. | It is a limited reserve, not the default production agent. |
| Doc-writer | Updates verified public, product, operator, or service documentation. | Does not edit `agent_docs/` during deployment. |
| Closure Steward | Reconciles `agent_docs/` and prepares the final handoff. | Never edits outside `agent_docs/` or mutates Git. |

At the first substantive Medium deployment in a session, Companion reads
`agent_docs/project_diary.md`; Medium otherwise uses targeted documentation.
At the first substantive Heavy entry, the main reads `project_overview.md`,
`project_core_tech.md`, `project_structure.md`, `project_progress.md`, and
`latest_session_work.md`, while Companion reads and summarizes
`project_diary.md` plus every module-specific Markdown document. The split also
runs on a Medium-to-Heavy transition and is reused for later Heavy deployments
unless relevant files change. In Heavy, the main launches workers directly,
integrates their small terminal reports, routes repair, and owns the lightweight
evidence manifest. Capsules still distribute package-specific guidance. The
main retains root-cause, architecture, allocation, acceptance, rollback, and
final-claim authority.

## Light benchmark

![Light benchmark analysis](light_benchmark/analysis.png)

## 3. More details 

Send these exact commands to Codex from the relevant project directory:

| Command | Purpose |
| --- | --- |
| `codex_workflow --install` | Install workflow in the current project and initialize its documentation framework. |
| `codex_workflow --personal` | Add or update project-specific workflow preferences. |
| `codex_workflow --check-update` | Check for a newer release without installing it. |
| `codex_workflow --update` | Download, verify, and install the latest matching release. |
| `codex_workflow --disable` / `codex_workflow --enable` | Disable or re-enable the workflow for the current project. |
| `codex_workflow --remove` | Remove the installed workflow after a destructive dry-run and confirmation. |

For the complete command reference, installed-file map, scripted customization
guide, and Heavy-route design, see [workflow_break_down.md](workflow_break_down.md).
