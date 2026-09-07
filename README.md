<h3 align="center"><big><big><strong>SIMPLE&emsp;&emsp;───&emsp;&emsp;EASY&emsp;&emsp;───&emsp;&emsp;EFFICIENT</strong></big></big></h3>
<p align="center"><small>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(to use)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(to install)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(token consumption)</small></p>
<hr>

![Workflow illustration](illustration.png)

Built for token-efficient agent orchestration, with swarm execution, persistent context support, and compact knowledge handoffs between agents. `agent_docs/` provides durable project memory for goals, architecture, decisions, progress, and session handoffs.

> ⭐ For lightweight tasks, it won’t overdo things. Light route is default.

## 1. Quick installation ⚙️
### Open Codex CLI / Codex app from your project directory

Change permision to `approve for me` or `full access`.
▶️ Send:
```text
For an agent-system-managed installation, use the agent-system installer and its pinned Aerox release. For a standalone installation, download the chosen `codex_workflow-<version>.zip` asset from https://github.com/Aerox912/codex_workflow/releases, verify `SHA256SUMS`, then follow `codex_workflow/operate/bootstrap.md`.
```
> The Aerox fork uses Astra for all six workers: default executor and companion at medium, investigator, tester and archivist at high, and senior executor at xhigh.

🔄 Restart Codex after installation

The initial bootstrap will include creating the project documentation framework `agent_docs/` using `archivist` subagent. Once that bootstrap is complete, the current project is ready to use. Whenever you need to install this workflow for a new project, simply open Codex and send: `codex_workflow --install`

> Requires Python 3.11 or newer for deterministic lifecycle operations.

## 2. Workflow usage 

### This workflow has 3 routes:
- Light route : No subagents, no workflow, minimal context.
- Heavy route : Implement the full set of workers, including `companion`, `investigator`, `default executor`, `senior executor`, `tester`, and `archivist`. The main agent orchestrates the work.
- Medium route: Implement `copmanion` and `investigator` to assist the main agent. The main agent still owns implementation.
Choose it when you want workflow-mode context support without delegating production work, like front-end design, visualization, or 3D works.

### Built-in project memory - `agent_docs`
`agent_docs/` is the project's durable documentation framework: it records the goals, architecture, progress, decisions, and latest-session handoff. Medium and Heavy routes will use this framework doc. It is created and managed automatically by `Archivist`.

### How to use
- Normally, for simple work, general Q&A, you don't need to do anything. `light route` is the default route.

--------------------------------
- When starting a new task, tell Codex :
```text
use medium/heavy route. [your task description]
```
Or continue a task that was already underway in the previous session:
```text
use medium/heavy route. Continue ongoing work.
```
> Codex stays on the selected route until you change it

---------------
> **⭐ Recommendation:** Assign very large and complex tasks to the `heavy route` to make the most of its capabilities and maximize token usage savings. Don't hesitate to choose Sol xhigh / Astra high for this route. Using much lower reasoning efforts will not actually save tokens and will severely reduce its coordination capabilities.

### Coordinating architecture

| Role | Model | Primary Responsibility | Quantity  |
|---|---|---|---:|
| **Main Agent** | Session-selected model | **Primary orchestrator.** Owns the core task context, makes high-level decisions, coordinates the workflow, and distributes the knowledge required by specialized subagents. | 1 |
| **Companion** | Luna · xhigh | **Persistent secretary and context assistant.** Reduces context pressure and operational overhead on the Main Agent by handling supporting context, organizing information, consolidating reports, and taking care of lightweight auxiliary work. | 1 |
| **Investigator** | Luna · xhigh | **Research and investigation specialist.** Searches for clues, technical evidence, documentation, prior art, and potential solutions, including information available on the Internet. Investigators can operate in parallel across independent research lanes. | As needed |
| **Default Executor** | Luna · max | **Default implementation worker.** Handles normal production tasks delegated by the Main Agent, including coding, modifications, integration work, and other routine implementation activities. Multiple Default Executors may work in parallel when tasks can be safely decomposed. | As needed |
| **Senior Executor** | Sol · medium | **High-capability implementation specialist.** Reserved for exceptionally difficult or high-impact work where stronger reasoning is justified, such as project-core changes, complex algorithms, architectural modifications, or mathematically demanding tasks. | 1 maximum |
| **Tester** | Luna · max | **Independent verification specialist.** Designs, implements, and runs tests; validates requirements and acceptance criteria; identifies regressions or defects; and provides verification evidence before work is accepted. | As needed |
| **Archivist** | Luna · high | **Documentation and session-record specialist.** Maintains and updates the project's documentation structure, records relevant workflow changes and outcomes, and produces the end-of-session token usage and statistics report. | As needed |

![Heavy Route structure](heavy_route_structure.png)

> `doc-writer` and `closure_steward` have been merged into single role `archivist` since 1.1.14 version.

The coordination process is roughly as follows: The Main Agent receives the task, deploys a `Companion` and swarm of `Investigator` when needed, plans the work, and breaks it into bounded tasks. Each worker receives a work package containing the context scope, task and goal, and a knowledge package with the project-specific guidance needed to complete it.  At the end of the session, the `Archivist` updates the `agent_docs/` project documentation framework and runs the integrated `$deployment-token-report` skill to produce the token-usage report.

Illustrating the token-usage report at the end of each deployment in the Heavy route:
![End-of-session token report](token_report.png)

In this design, the **Companion** helps reduce context pressure on the Main Agent. Together with the **Investigators**, it offloads work that does not require the Main Agent's high intelligence, allowing the Main Agent to remain focused on orchestration, high-level reasoning, and critical decisions without being distracted by lower-value operational work.

Each work package contains instructions enriched with knowledge distilled from the Main Agent, benefiting from its broad understanding of the overall task and project context. Each **default_executor** can therefore focus on a compact, well-scoped package of work using **Astra medium**.

The **Senior Executor** serves as a fallback for exceptionally difficult problems where stronger reasoning is required.

The workflow's **batching guidelines** were derived from extensive experimentation. They are designed to group related coordination and execution work more efficiently, significantly reducing the number of Main Agent rollouts and the repeated context replay associated with them.

End-of-session reporting with deploy_token_report is handled by the Archivist, preserving the Main Agent's token budget

## Light benchmark
**Batching guidelines** techniques(since 1.1.3 version) significantly reduce the main agent's rollout, which in turn reduces the main agent's cached input tokens, a major component of the operation cost, see **New workflow** below :

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
