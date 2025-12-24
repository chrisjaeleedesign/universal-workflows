---
name: create-meta-prompt
description: Create optimized prompts for Agent-to-Agent communication with XML structure.
allowed-tools: [notify_user, list_dir, read_url_content, task_boundary, view_file, write_to_file]
---

<role>Prompt Engineer (Router)</role>

<objective>
Serve as the entry point for creating meta-prompts. Route the request to the `intake` sub-workflow to begin the process.
</objective>

<context>
Values: "High Quality", "Structured", "XML-based"
Reference: @.agent/workflows/commands/universal-workflows/tools/create-meta-prompt/references/intelligence-rules.md
Intake Sub-Workflow: @.agent/workflows/commands/universal-workflows/tools/create-meta-prompt/intake.md
Generate Sub-Workflow: @.agent/workflows/commands/universal-workflows/tools/create-meta-prompt/generate.md
</context>

<input>
$ARGUMENTS: User description of the task (optional).
</input>

<process>
<step_1_start>
<title>Initiate Workflow</title>
1.  **Delegate**:
    -   Use `view_file` to read the **Intake Sub-Workflow** (`.agent/workflows/commands/universal-workflows/tools/create-meta-prompt/intake.md`).
    -   Follow the instructions in that file to analyze the input and eventually call the generator.
</step_1_start>
</process>
