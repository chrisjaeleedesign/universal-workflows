---
description: Execute a single prompt file.
---

<role>Prompt Executor (Single)</role>

<input>
$ARGUMENTS: Path to the prompt file.
</input>

<process>
<step_1_execute>
<title>Execute Prompt</title>
1.  **Read**: Read prompt file contents.
2.  **Execute**: Use `task_boundary` to run the prompt content.
3.  **Validate**:
    -   File exists? Not empty?
    -   SUMMARY.md exists?
4.  **Archive**: Move prompt to `.prompts/trash/`.
5.  **Report**: Show SUMMARY.md inline.
</step_1_execute>
</process>
