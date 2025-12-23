---
description: Create or Update an Antigravity workflow.
---

<objective>
Serve as the comprehensive entry point for workflow management. Route the user's request to either CREATE a new workflow or UPDATE an existing one.
</objective>

<context>
Standards: @.agent/workflows/commands/universal-workflows/create-workflow/standards.md
Reference (always check): https://antigravity.google/docs/rules-workflows#workflows
New Workflow Path: @.agent/workflows/commands/universal-workflows/create-workflow/new.md
Update Workflow Path: @.agent/workflows/commands/universal-workflows/create-workflow/update.md
</context>

<input>
$ARGUMENTS should contain the desired action, workflow name, and/or description.
</input>

<process>
<step_1_route>
<title>Determine Intent</title>
1.  **Analyze Input**:
    -   Does the user want to create a brand new workflow?
    -   Does the user want to modify/update an existing workflow?
2.  **Route**:
    -   IF intent is "Create": Use the `view_file` tool to read contents of `.agent/workflows/commands/universal-workflows/create-workflow/new.md` and follow its instructions.
    -   IF intent is "Update": Use the `view_file` tool to read contents of `.agent/workflows/commands/universal-workflows/create-workflow/update.md` and follow its instructions.
    -   IF unclear: ASK the user for clarification.
</step_1_route>
</process>