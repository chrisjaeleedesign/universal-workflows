---
name: create-workflow
description: Create or Update an Antigravity workflow via the Kernel.
allowed-tools: [task_boundary, view_file, notify_user, run_command]
---

<objective>
Serve as a Client of the Kernel. Use `/plan` to design the workflow and `/critic` to audit it.
</objective>

<context>
Values: "Hub-and-Spoke", "Agentic", "Verified"
Plan Kernel: @.agent/workflows/universal-workflows/kernel/visual-planner.md
Critic Kernel: @.agent/workflows/universal-workflows/kernel/critic.md
New Workflow Path: @.agent/workflows/universal-workflows/tools/create-workflow/workflow-new.md
Update Workflow Path: @.agent/workflows/universal-workflows/tools/create-workflow/update.md
</context>

<input>
$ARGUMENTS: Intent (e.g., "Create new workflow for X" or "Update test workflow").
</input>

<process>
<step_1_plan>
<title>Visual Design</title>
1.  **Delegate**: Call `kernel/visual-planner.md`.
    -   Pass `$ARGUMENTS`.
    -   **Goal**: Get user approval on the logic/flowchart.
</step_1_plan>

<step_2_build>
<title>Assembly</title>
1.  **Route**:
    -   If "Create": Call `tools/create-workflow/workflow-new.md`.
    -   If "Update": Call `tools/create-workflow/update.md`.
2.  **Logic**: Execute the approved plan to generate/edit the `.md` file.
</step_2_build>

<step_3_audit>
<title>Quality Gate</title>
1.  **Delegate**: Call `kernel/critic.md`.
    -   Target: The newly created/updated file.
    -   Persona: "Workflow Standards" (Checks for `allowed-tools`, frontmatter, etc.).
2.  **Refine**: If Score < 10, fix issues and repeat.
</step_3_audit>
</process>