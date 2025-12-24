---
name: test
description: Intelligent testing agent that infers test targets (Unit, Visual, or Agent Workflow) and executes verification.
argument-hint: "[description of what to test]"
allowed-tools: [run_command, task_boundary, view_file, notify_user]
---

<role>QA Lead (Router)</role>

<objective>
Infer intent, route to specialized tester, and optionally engage the Reliability Loop.
</objective>

<context>
Values: "TDD", "Verification", "Safety"
Unit Test: @.agent/workflows/commands/universal-workflows/tools/test/unit.md
Visual Test: @.agent/workflows/commands/universal-workflows/tools/test/visual.md
Workflow Test: @.agent/workflows/commands/universal-workflows/tools/test/workflow.md
Loop Kernel: @.agent/workflows/commands/universal-workflows/kernel/loop.md
</context>

<process>
<step_1_route>
<title>Infer Test Strategy</title>
1.  **Analyze**: Determine proper sub-workflow (Unit, Visual, or Workflow).
2.  **Construct Command**: Build the command string (e.g., `/test/unit arg=...`).
</step_1_route>

<step_2_execute>
<title>Execution Mode</title>
1.  **Check Mode**: 
    -   Is the user asking to "fix it" or "loop"?
2.  **Route**:
    -   **Standard**: Execute the command directly.
    -   **Loop Mode**: Delegate to `kernel/loop.md`.
        -   Pass the command.
        -   The Loop will run the test -> Check result -> Fix -> Retry.
</step_2_execute>
</process>
