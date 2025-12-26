---

description: Execute a chain of prompts (Sequential or Parallel) or other workflows.
allowed-tools: [task_boundary, run_command, list_dir, view_file, notify_user]
---

<role>Workflow Orchestrator</role>

<objective>
Serve as the entry point for chaining multiple workflows together. Route to intake to parse the natural language request.
</objective>

<context>
Intake Sub-Workflow: @.agent/workflows/universal-workflows/tools/chain/chain-intake.md
Execute Sub-Workflow: @.agent/workflows/universal-workflows/tools/chain/chain-execute.md
</context>

<input>
$ARGUMENTS: Natural language chain description (e.g. "Idea Foo then Plan it").
</input>

<process>
<step_1_start>
<title>Initiate Chain</title>
1.  **Delegate**:
    -   Call `.agent/workflows/universal-workflows/intake.md` (The Master Router).
    -   Pass the user input. It will handle parsing and routing back to `chain/chain-execute.md` if needed.
</step_1_start>
</process>
