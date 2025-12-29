---
name: intake
description: The Master Router. Parses natural language into executable agent commands.
allowed-tools: [notify_user, list_dir, task_boundary, view_file, run_command]
---

<role>System Architect (Router)</role>

<input>
$ARGUMENTS: Natural language request (e.g., "Draft a blog regarding X then critique it").
</input>

<context>
Registry Status: !`[ -f .agent/workflows/workflow_registry.md ] && echo "active" || echo "missing"`
Registry: @.agent/workflows/workflow_registry.md
Memory Context: @.agent/memory/*.md
</context>

<process>
<step_1_analyze>
<title>Semantic Parsing & Mode Selection</title>
1.  **Check Registry**:
    -   If `Registry Status` is "missing", STOP. Return error: "⚠️ System not initialized. Run `/setup` first."
2.  **Parse & Classify**:
    -   Analyze "$ARGUMENTS" to determine Intent and Mode.
    -   **Deep Mode** (Creation/Complex): `build`, `create`, `refactor`, `implement`, `fix`.
    -   **Shallow Mode** (Admin/Simple): `archive`, `clean`, `list`, `audit`.
3.  **Session Setup**:
    -   **Generate ID**: Create a unique session ID (timestamp + topic slug).
    -   **Define Memory**: `TargetMemory = .agent/memory/working/{ID}_domain_state.md`.
4.  **Construct Chain**:
    -   **Base**: `kernel/visual-planner` (Always Plan first).
    -   **If Deep Mode**:
        -   Add: `tools/create-meta-prompt` (Arg: `TargetMemory`).
        -   Add: `kernel/loop-domain` (Arg: `TargetMemory`).
    -   **If Shallow Mode**:
        -   Add: `[Resolved Tool]` (e.g. `management/archive.md`).
        -   Add: `kernel/loop` (Standard validation loop if applicable).
    -   **Finalize**: `kernel/walkthrough` (Report).
</step_1_analyze>

<step_2_plan>
<title>Visual Planning (Safety Protocol)</title>
1.  **Delegate**: Call `.agent/workflows/universal-workflows/kernel/visual-planner.md` (Visual Planner).
    -   Pass the constructed chain.
    -   **Goal**: Generate a Mermaid flowchart in `implementation_plan.md`.
2.  **Wait**: The `plan` workflow will handle user approval.
</step_2_plan>

<step_3_execute>
<title>Golden Path Execution</title>
1.  **Route**:
    -   Delegate to `.agent/workflows/universal-workflows/tools/chain/chain-execute.md`.
    -   Pass the **Constructed Chain** from Step 1.
    -   **Deep Flow**: Plan -> Build Memory -> Domain Loop -> Report.
    -   **Shallow Flow**: Plan -> Tool -> Report.
</step_3_execute>

<step_4_finalize>
<title>Maintenance Sweep</title>
1.  **Session Assessment**:
    -   Did the session experience friction? (Errors, loops, confusion)
    -   Did the user provide corrections? (New preferences, facts)
    -   *Use these signals to recommend specific actions below.*

2.  **Maintenance Menu**:
    -   Present the following menu to the user:
        1.  **Clean Workspace** (`/clean`)
        2.  **Auto-Update Documentation** (`/auto-update`)
        3.  **Update Memory** (`/memory-update`) - *Recommended if corrections detected*
        4.  **Smart Commit** (`/smart-commit`)
        5.  **Optimize Workflow** (`/workflow-optimize`) - *Recommended if friction detected*

3.  **Execution**:
    -   Ask: "Which maintenance tasks would you like to run? (e.g., '1, 4' or 'None')"
    -   If user selects options:
        -   Construct a list of the corresponding commands (e.g., `clean`, `smart-commit`).
        -   Delegate to `.agent/workflows/universal-workflows/tools/chain/chain-execute.md` passing the list.
    -   Else: "Session complete."
</step_4_finalize>
</process>
