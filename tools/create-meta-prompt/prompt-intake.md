---
description: Intake logic for create-meta-prompt. Analyzes user intent and gathers context.
---

<role>Prompt Engineer (Intake Specialist)</role>

<input>
$ARGUMENTS: The user's raw input description.
</input>

<context>
Prompts directory: !`[ -d ./.prompts ] && echo "exists" || echo "missing"`
Existing research/plans: !`find ./.prompts -name "*-research.md" -o -name "*-plan.md" 2>/dev/null | head -10`
</context>

<process>
<step_1_intake>
<title>Fast-Path Intake</title>

<critical_routing>
**Goal**: Infer intent and proceed to generation immediately. Minimize user friction.

<path_A_context_provided>
IF `$ARGUMENTS` are provided:
1. **Infer Purpose**:
   - `do`, `build`, `fix` -> **Do**
   - `plan`, `roadmap` -> **Plan**
   - `research`, `analyze` -> **Research**
   - `refine` -> **Refine**
   - *Default if unclear*: **Research** (Safety first)

2. **Infer Topic**:
   - Extract kebab-case subject from args (e.g. "auth-system" -> `auth-system`).
   - If no distinct topic found, use `general`.

3. **Proceed**.
</path_A_context_provided>

<path_B_no_context>
IF `$ARGUMENTS` are empty:
1. **Notify User (Single Interaction)**:
   - Header: "New Task Prompt"
   - Question: "Select purpose and describe the task."
   - Options: "Research", "Plan", "Do", "Refine"
   - Input: "Description (e.g., 'Analyze auth system')"
   
2. **Proceed**.
</path_B_no_context>
</critical_routing>

<context_assembly>
**Silent Context Gathering** (Do not ask user):
1. **Project State**: Read `task.md` and `implementation_plan.md`.
2. **Chain History**: Scan `.prompts/` for related `*-research.md` or `*-plan.md` files matching the inferred topic.
</context_assembly>

</step_1_intake>

<step_2_handoff>
<title>Route to Generator</title>
1. **Call Generator**:
   - Use `view_file` to read `.agent/workflows/universal-workflows/tools/create-meta-prompt/prompt-generate.md`.
   - Pass the inferred `purpose` and `topic` and `context_files` as arguments or context.
</step_2_handoff>
</process>
