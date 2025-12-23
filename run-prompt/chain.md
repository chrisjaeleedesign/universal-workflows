---
description: Execute a chain of prompts (Sequential or Parallel).
---

<role>Prompt Executor (Chain)</role>

<input>
$ARGUMENTS: List of prompt files or directory path.
</input>

<process>
<step_1_queue>
<title>Build Queue</title>
1.  **Resolve**: Find all `*.md` files.
2.  **Sort**: Order by sequence number (01, 02...).
</step_1_queue>

<step_2_execute_chain>
<title>Run Chain</title>
1.  **Loop**: For each prompt in queue:
    -   Execute (call `single.md` logic or inline equivalent).
    -   Validate.
    -   Stop on failure.
    -   Archive on success.
</step_2_execute_chain>

<step_3_report>
<title>Consolidate</title>
1.  **Summary**: Report results of all steps.
</step_3_report>
</process>
