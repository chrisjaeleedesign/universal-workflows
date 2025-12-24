---
description: Parse natural language instructions into a sequence of executable workflow commands.
---

<role>Workflow Planner (Architect)</role>

<input>
$ARGUMENTS: Natural language description of the chain (e.g. "Create idea 'Foo' then plan it").
</input>

<context>
Available Workflows: !`find .agent/workflows/commands -name "*.md"`
</context>

<process>
<step_1_discovery>
<title>Map Capabilities</title>
1.  **Analyze**: Read the list of available workflows from context.
2.  **Map**: Create a mapping of verbs to scripts.
    -   "Idea", "Log" -> `experiments/idea.md`
    -   "Plan", "Design" -> `experiments/plan.md`
    -   "Run", "Execute" -> `experiments/run.md`
    -   "Write", "Draft" -> `content/write-copy.md`
    -   "Refine", "Edit" -> `content/refine-content.md`
</step_1_discovery>

<step_2_parse>
<title>Analyze Request</title>
1.  **Split**: Break `$ARGUMENTS` by temporal separators ("then", "after that", "and").
2.  **Structure**: For each segment, create a step object:
    -   `command`: The resolved workflow path (e.g. `experiments/idea.md`).
    -   `args`: The arguments for that command.
    -   **Bridging**: If the segment refers to previous output ("it", "that", "the ID"), use specific placeholders:
        -   `$LAST_ID`: For experiment IDs.
        -   `$LAST_FILE`: For file paths.
3.  **Output**: A list of steps (e.g., `Step 1: /idea "Foo"; Step 2: /plan "$LAST_ID"`).
</step_2_parse>

<step_3_handoff>
<title>Pass to Executor</title>
1.  **Delegate**: Call `.agent/workflows/commands/universal-workflows/tools/chain/execute.md` with the parsed list of steps.
</step_3_handoff>
</process>
