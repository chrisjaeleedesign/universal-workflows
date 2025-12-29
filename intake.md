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
3.  **Construct Chain**:
    -   **Base**: `kernel/visual-planner` (Always Plan first).
    -   **If Deep Mode**:
        -   Add: `tools/create-meta-prompt` (Build Domain Memory).
        -   Add: `kernel/loop-domain` (Execute Domain Loop).
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
<title>Optimization Handoff</title>
1.  **Completion Check**:
    -   Assess if the session experienced significant friction (errors, loops).
    -   Assess if the user provided corrections/preferences ("No, do X").
2.  **Suggest Optimization**:
    -   If friction detected: "⚠️ Friction detected. Run `@[/workflow-optimize]`."
    -   If corrections detected: "🧠 New Knowledge detected. Run `@[/memory-update]` to save preferences."
    -   Else: "Session complete."
</step_4_finalize>
</process>
