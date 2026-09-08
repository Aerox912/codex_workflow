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
Download and extract the latest `codex_workflow-<version>.zip` asset from https://github.com/viettran-edgeAI/codex_workflow/releases. Verify it against `SHA256SUMS`, then read the bundled `codex_workflow/operate/bootstrap.md` and follow it to complete the initial installation.
```
> ⭐ Recommended: use 5.6 Luna xhigh for installation. 

🔄 Restart Codex after installation

The initial bootstrap will include creating the project documentation framework `agent_docs/` using `archivist` subagent. Once that bootstrap is complete, the current project is ready to use. Whenever you need to install this workflow for a new project, simply open Codex and send: `codex_workflow --install`

> Requires Python 3.11 or newer for deterministic lifecycle operations.

**Note:** If you are currently using 1.1.3 version, you cannot upgrade directly to a newer version(cause I removed --configure feature). Run `codex_workflow --remove` to uninstall it first, then install the newer version.

## 2. Workflow usage 

### This workflow has 3 routes:
- Light route : No subagents, no workflow, minimal context.
- Heavy route : Implement the full set of workers, including `companion`, `investigator`, `default executor`, `senior executor`, `tester`, and `archivist`. The main agent orchestrates the work.
- Medium route: Deploy `Companion`, `Investigator` and `Archivist` to assistance the Main agent. The main agent handles the deployment itself. Choose this route when you want workflow-mode context support without delegating production work, like front-end design, visualization, or 3D works, but it will burn tokens faster than Heavy route.

### Built-in project memory - `agent_docs`
`agent_docs/` is the project's durable documentation framework: it records the goals, architecture, progress, decisions, and latest-session handoff. Medium and Heavy routes use it. The main agent updates progress, diary, and latest-session work for each substantive deployment; `Archivist` initializes the framework and handles other assigned documentation plus closure reporting.

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
| **Archivist** | Luna · xhigh | **Documentation and closure specialist.** Handles assigned documentation outside the three main-owned deployment-state documents, performs the read-only Git handoff, and produces the end-of-deployment token report. | 1 per substantive deployment, plus as needed |

![Heavy Route structure](heavy_route_structure.png)

> `doc-writer` and `closure_steward` have been merged into single role `archivist` since 1.1.14 version.

The coordination process is roughly as follows: The Main Agent receives the task -> read agent_docs/ to get a comprehensive understanding of the project context, structure, and timeline -> Identify critical codebase sections and read them on its own + deploys a `Companion` and `Investigator` workers when needed -> plans the work + breaks it into bounded tasks -> Each worker receives a work package containing the context scope, task and goal, and a knowledge package with the project-specific guidance needed to complete it. At substantive deployment closure, update `agent_docs/`, complete the Git handoff, and generate the integrated `$deployment-token-report`.

Illustrating the token-usage report at the end of each deployment in the Heavy route:
![End-of-session token report](token_report.png)

In this design, the **Companion** helps reduce context pressure on the Main Agent. Together with the **Investigators**, it offloads work that does not require the Main Agent's high intelligence, allowing the Main Agent to remain focused on orchestration, high-level reasoning, and critical decisions without being distracted by lower-value operational work.

Each work package contains instructions enriched with knowledge distilled from the Main Agent, benefiting from its broad understanding of the overall task and project context. Each **default_executor** can therefore focus on a compact, well-scoped package of work. **Luna** is very powerful for this type of bounded work. 

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
