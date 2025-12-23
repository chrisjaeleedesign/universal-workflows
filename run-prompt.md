---
name: run-prompt
description: Delegate one or more prompts to fresh sub-task contexts.
allowed-tools: [read_url_content, task_boundary, run_command, list_dir, view_file]
---

<role>Workflow Executor (Router)</role>

<context>
Single Sub-Workflow: @.agent/workflows/commands/universal-workflows/run-prompt/single.md
Chain Sub-Workflow: @.agent/workflows/commands/universal-workflows/run-prompt/chain.md
</context>

<input>
$ARGUMENTS: Prompt path(s) or directory.
</input>

<process>
<step_1_route>
<title>Determine Execution Mode</title>
1.  **Analyze Input**:
    -   Is it a single file? -> Route to `single.md`.
    -   Is it a directory or multiple files? -> Route to `chain.md`.
    -   Is it a partial string? -> Resolve then route.
2.  **Execute**: Call the appropriate sub-workflow.
</step_1_route>
</process>
