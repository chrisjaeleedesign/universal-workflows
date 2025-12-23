---
description: Execute a sequence of workflow steps with smart context bridging.
---

<role>Workflow Executor (Orchestrator)</role>

<input>
$ARGUMENTS: List of steps to execute.
</input>

<context>
Tracker: @research/experiments/tracker.json
Current Task: @.gemini/antigravity/brain/CURRENT_UUID/task.md
</context>

<process>
<step_1_execute_loop>
<title>Chain Execution</title>
**Loop**: For each `step` in the input list:

1.  **Resolve Context (Pre-Flight)**:
    -   **Scan**: Check `args` for placeholders (`$LAST_ID`, `$LAST_FILE`).
    -   **Resolve `$LAST_ID`**:
        -   Read `research/experiments/tracker.json`.
        -   Find the experiment with the *latest* `start_date` or status change.
        -   Replace `$LAST_ID` with that extracted UUID.
    -   **Resolve `$LAST_FILE`**:
        -   Run `ls -t content/ | head -1` (or relevant dir).
        -   Replace `$LAST_FILE` with that filename.
    
2.  **Execute**:
    -   Construct command: `/[command] [resolved_args]`.
    -   Run it using `task_boundary` or `run_command`.
    -   **Verify**: Did it succeed? (Check for errors or basic success signals).

3.  **Halt**: If any step fails, STOP. Report the error.
</step_1_execute_loop>

<step_2_summary>
<title>Report</title>
1.  **Summarize**: List all steps executed and the final state.
</step_2_summary>
</process>
