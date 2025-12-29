---
name: loop-domain
description: Iterates through the Domain Memory Backlog, executing tasks one by one.
allowed-tools: [read_resource, write_to_file, run_command, task_boundary, notify_user]
---

<role>Domain Iterator (The Worker)</role>

<input>
$ARGUMENTS: (Optional) Path to `active_domain_state.md` (defaults to standard path).
</input>

<process>
<step_1_load_state>
<title>Read Scoreboard</title>
1.  **Resolve Path**:
    -   If `$ARGUMENTS` is provided: Use it as the memory file path.
    -   Else: Default to `.agent/memory/working/active_domain_state.md`.
2.  **Read**: Read the target file.
3.  **Parse**:
    -   Find the "Feature Backlog" table.
    -   Identify the **First** row where Status is 🔴 (Pending) or ⚠️ (Warning).
3.  **Decision**:
    -   If **No Pending Items**: 
        -   Success! All tasks complete.
        -   Proceed to `step_3_finalize`.
    -   If **Found Item**:
        -   Extract `ID`, `Micro-Task`, `Verification`.
        -   Proceed to `step_2_execute`.
</step_1_load_state>

<step_2_execute>
<title>Micro-Task Execution</title>
1.  **Announce**: `task_boundary` -> "Executing ID: [Micro-Task]".
2.  **Solve**:
    -   **Delegate**: Call `.agent/workflows/universal-workflows/tools/agent-solve.md` (Placeholder for the Coding Agent).
    -   **Pass Context**: The Micro-Task and the `active_domain_state.md` content.
    -   **Constraint**: The Solver MUST run the `Verification Command` before returning.
3.  **Update State**:
    -   **If Success**: Mark 🔴 -> ✅. Update Log.
    -   **If Fail**: Mark 🔴 -> 🔴 (or ☠️). Update Log with error.
4.  **Loop**:
    -   Return to `step_1_load_state`.
</step_2_execute>

<step_3_finalize>
<title>Synthesis</title>
1.  **Read Log**: Extract key learnings from "Decision & Learning Log".
2.  **Report**: Call `notify_user` or `kernel/walkthrough.md` to summarize the session.
</step_3_finalize>
</process>
