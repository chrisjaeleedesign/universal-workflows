---
name: auto-update
description: Automate deep-dive analysis and documentation updates for a directory.
allowed-tools: [run_command, view_file, notify_user, codebase_search, write_to_file, replace_file_content, task_boundary]
---

<role>Documentation & Maintenance Specialist (Router)</role>

<objective>
Execute a "Deep Dive & Maintenance" cycle on a target directory.
</objective>

<context>
Analyze Sub-Workflow: @.agent/workflows/commands/universal-workflows/tools/auto-update/analyze.md
Execute Sub-Workflow: @.agent/workflows/commands/universal-workflows/tools/auto-update/execute.md
</context>

<input>
$ARGUMENTS: The target directory (TARGET).
</input>

<process>
<step_1_route>
<title>Orchestrate Maintenance</title>
1.  **Analyze Phase**:
    -   Call `.agent/workflows/commands/universal-workflows/tools/auto-update/analyze.md` with {TARGET}.
2.  **Execute Phase**:
    -   Call `.agent/workflows/commands/universal-workflows/tools/auto-update/execute.md` with {TARGET}.
</step_1_route>
</process>
