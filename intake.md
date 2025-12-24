---
description: The Master Router. Parses natural language into executable agent commands.
allowed-tools: [notify_user, list_dir, task_boundary, view_file, run_command]
---

<role>System Architect (Router)</role>

<input>
$ARGUMENTS: Natural language request (e.g., "Draft a blog regarding X then critique it").
</input>

<context>
Tools: !`find .agent/workflows/commands/universal-workflows/tools -name "*.md"`
Kernel: !`find .agent/workflows/commands/universal-workflows/kernel -name "*.md"`
</context>

<process>
<step_1_analyze>
<title>Semantic Parsing</title>
1.  **Catalog**: Review the list of Available Workflows.
2.  **Parse**: Deconstruct "$ARGUMENTS" into a sequence of Intent/Action pairs.
    -   "Draft a blog" -> Intent: Content Creation -> Tool: `content/write-copy.md`
    -   "Critique it" -> Intent: Quality Gate -> Tool: `.agent/workflows/commands/universal-workflows/kernel/critic.md`
    -   "Loop until good" -> Intent: Reliability -> Tool: `.agent/workflows/commands/universal-workflows/kernel/loop.md`
3.  **Construct Chain**:
    -   Create a list of executable commands.
    -   Resolve dependencies ("it" refers to previous file).
</step_1_analyze>

<step_2_plan>
<title>Visual Planning (Safety Protocol)</title>
1.  **Delegate**: Call `.agent/workflows/commands/universal-workflows/kernel/plan.md` (Visual Planner).
    -   Pass the constructed chain.
    -   **Goal**: Generate a Mermaid flowchart in `implementation_plan.md`.
2.  **Wait**: The `plan` workflow will handle user approval.
</step_2_plan>

<step_3_execute>
<title>Golden Path Execution</title>
1.  **Construct Protocol**:
    -   **Phase 1 (Safety)**: Generate command using `.agent/workflows/commands/universal-workflows/kernel/plan.md`.
    -   **Phase 2 (Reliability)**: Generate command using `.agent/workflows/commands/universal-workflows/kernel/loop.md`.
    -   **Phase 3 (Visibility)**: Generate command using `.agent/workflows/commands/universal-workflows/kernel/walkthrough.md`.
    -   *Example*: `[kernel/plan, kernel/loop "cmd", kernel/walkthrough]`.
2.  **Route**:
    -   Delegate to `.agent/workflows/commands/universal-workflows/tools/chain/execute.md`.
    -   This ensures Plan -> Approval -> Looped Execution.
</step_3_execute>
</process>
