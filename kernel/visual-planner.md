---
name: visual-planner
description: Generates visual implementation plans (Mermaid) and requests user approval.
allowed-tools: [notify_user, write_to_file, task_boundary]
---

<role>System Architect (Planner)</role>

<input>
$ARGUMENTS: The proposed execution chain or task description.
</input>

<process>
<step_1_visualize>
<title>Generate Flowchart</title>

<load_resources>
Patterns: @.agent/workflows/universal-workflows/tools/create-meta-prompt/references/plan-patterns.md
</load_resources>

1.  **Analyze**:
    -   Review the `Patterns` to understand the required XML structure for plans.
2.  **Design**: Create a Mermaid diagram representing the flow.
    -   Nodes = Workflow Steps.
    -   Edges = Data flow / Dependencies.
    -   **Constraint**: ALWAYS quote node labels (e.g., `id["Label"]`) to avoid syntax errors with special chars.
3.  **Draft**: Write (or update) `implementation_plan.md`.
    -   **Format**: Use the XML schema defined in `Patterns` (Goal, User Review, etc) but wrap the Mermaid diagram in a standard markdown block.
    -   Include a text summary of the logic.
</step_1_visualize>

<step_2_approve>
<title>User Consent</title>
1.  **Notify**: Call `notify_user` with `BlockedOnUser=True`.
    -   Message: "I have mapped out the plan. Please review the Flowchart in `implementation_plan.md`. Shall I proceed?"
    -   PathsToReview: [`<appDataDir>/brain/<id>/implementation_plan.md`]
2.  **Listen**:
    -   If "Yes": 
        -   **Generate Schedule**: Parse the approved `implementation_plan.md`.
        -   **Populate**: Write the steps into `task.md`.
        -   Return success.
    -   If "No": Ask for feedback, update plan, repeat.
</step_2_approve>
</process>
