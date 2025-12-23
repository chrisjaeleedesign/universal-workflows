---
name: test
description: Intelligent testing agent that infers test targets (Unit, Visual, or Agent Workflow) and executes verification.
argument-hint: "[description of what to test]"
allowed-tools: [run_command, write_to_file, read_url_content, view_file, list_dir, notify_user, task_boundary]
---

<role>QA Lead (Router)</role>

<objective>
Infer the user's testing intent and route to the specialized testing sub-workflow.
</objective>

<context>
Unit Test (Logic): @.agent/workflows/commands/universal-workflows/test/unit.md
Visual Test (Quality): @.agent/workflows/commands/universal-workflows/test/visual.md
Workflow Test (Integration): @.agent/workflows/commands/universal-workflows/test/workflow.md
Standards: @.agent/workflows/commands/universal-workflows/test/standards.md
</context>

<process>
<step_1_route>
<title>Infer Test Strategy</title>
1.  **Analyze Request**:
    -   Read `$ARGUMENTS`.
2.  **Determine Intent**:
    -   **UNIT/LOGIC**: If mentioning "code", "function", "class", "logic", "utils" -> Use `view_file` on `test/unit.md`.
    -   **VISUAL/QUALITY**: If mentioning "image", "chart", "look", "visual" -> Use `view_file` on `test/visual.md`.
    -   **WORKFLOW/AGENT**: If mentioning "command", "workflow", "agent", "/slash-command" -> Use `view_file` on `test/workflow.md`.
    -   **Default**: If unclear, ASK user.
3.  **Execute**:
    -   Call the selected sub-workflow with the arguments.
</step_1_route>
</process>
