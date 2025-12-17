---
name: create-meta-prompt
description: Create optimized prompts for Agent-to-Agent communication with XML structure.
allowed-tools: [notify_user, list_dir, read_url_content, task_boundary]
---

<role>Prompt Engineer</role>

<objective>
Create prompts optimized for Agent-to-Agent communication in multi-stage workflows. Outputs are structured with XML and metadata for efficient parsing by subsequent prompts.

Every execution produces a `SUMMARY.md` for quick human scanning without reading full outputs.

Each prompt gets its own folder in `.prompts/` with its output artifacts, enabling clear provenance and chain detection.
</objective>

<context>
Prompts directory: !`[ -d ./.prompts ] && echo "exists" || echo "missing"`
Existing research/plans: !`find ./.prompts -name "*-research.md" -o -name "*-plan.md" 2>/dev/null | head -10`
Next prompt number: !`ls -d ./.prompts/*/ 2>/dev/null | wc -l | xargs -I {} expr {} + 1`
Project Context:
- Implementation Plan: !`[ -f .gemini/antigravity/brain/*/implementation_plan.md ] && echo "Available" || echo "Missing"`
- Task Status: !`[ -f .gemini/antigravity/brain/*/task.md ] && echo "Available" || echo "Missing"`
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

3. **Proceed to Step 2 immediately.**
</path_A_context_provided>

<path_B_no_context>
IF `$ARGUMENTS` are empty:
1. **Notify User (Single Interaction)**:
   - Header: "New Task Prompt"
   - Question: "Select purpose and describe the task."
   - Options: "Research", "Plan", "Do", "Refine"
   - Input: "Description (e.g., 'Analyze auth system')"
   
2. **Proceed to Step 2.**
</path_B_no_context>
</critical_routing>

<context_assembly>
**Silent Context Gathering** (Do not ask user):
1. **Project State**: Read `task.md` and `implementation_plan.md`.
2. **Chain History**: Scan `.prompts/` for related `*-research.md` or `*-plan.md` files matching the inferred topic.
   - *Action*: Automatically append these file paths to the `Context` section of the generated prompt.
</context_assembly>
</step_1_intake>

<step_2_generate>
<title>Generate Prompt</title>

Load purpose-specific patterns:
- Do: [references/do-patterns.md](references/do-patterns.md)
- Plan: [references/plan-patterns.md](references/plan-patterns.md)
- Research: [references/research-patterns.md](references/research-patterns.md)
- Refine: [references/refine-patterns.md](references/refine-patterns.md)

Load intelligence rules: [references/intelligence-rules.md](references/intelligence-rules.md)

<prompt_structure>
All generated prompts include:

1. **Objective**: What to accomplish, why it matters
2. **Context**: Referenced files (@), dynamic context (!)
3. **Artifact Updates** (Critical):
   - **`brain/task.md`**: Prompt MUST start by updating task.md to reflect "In Progress", and end by marking "Completed".
   - **`brain/implementation_plan.md`**: (Plan/Refine/Do) Update this file if plans change or are completed.
4. **Requirements**: Specific instructions for the task
5. **Output specification**: Where to save, what structure.
6. **Metadata requirements**: For research/plan outputs, specify XML metadata structure
7. **SUMMARY.md requirement**: All prompts must create a SUMMARY.md file
8. **Success criteria**: How to know it worked

For Research and Plan prompts, output must include:
- `<confidence>` - How confident in findings
- `<dependencies>` - What's needed to proceed
- `<open_questions>` - What remains uncertain
- `<assumptions>` - What was assumed

All prompts must create `SUMMARY.md` with:
- **One-liner** - Substantive description of outcome
- **Status** - Executed/Blocked
- **Key Findings** - Actionable takeaways
- **Brain Updates** - Changes made to task.md/implementation_plan.md
- **Next Step** - Concrete forward action
</prompt_structure>

<self_correction>
**CRITICAL**: Before saving the prompt, review it against `references/intelligence-rules.md`.

Check constraints:
1. Does it explicitly create `SUMMARY.md`?
2. Does it use the correct file paths?
3. If "Research", does it require `<confidence>` tags?
4. If "Do", does it define clear file artifacts?

If any check fails, **rewrite the prompt to fix it**.
</self_correction>

<file_creation>
1. Identify/Create Session Folder:
   - Format: `.prompts/{YYYY-MM-DD}-{topic}/`
   - Use current date.
   - If folder exists, use it. If not, create it.

2. Determine File Sequence:
   - Scan session folder for `*-{purpose}.md` files.
   - Next sequence = count + 1 (e.g., 01, 02).
   - Filename: `{sequence}-{purpose}.md` (e.g., `01-research.md`, `02-plan.md`).

3. (Skipped - using .prompts/trash/ for archives)

4. Write prompt to: `.prompts/{YYYY-MM-DD}-{topic}/{sequence}-{purpose}.md`

5. Prompt instructs output to: `.prompts/{YYYY-MM-DD}-{topic}/{topic}-{purpose}.md`
   (Note: Use kebab-case topic as prefix for outputs to avoid collisions if multiple outputs)
</file_creation>
</step_2_generate>

<step_3_present>
<title>Present Decision Tree</title>

After saving prompt(s), present inline (not notify_user):

<single_prompt_presentation>
```
Prompt created: .prompts/{YYYY-MM-DD}-{topic}/{sequence}-{purpose}.md

To execute this prompt, run:
/run-prompt .prompts/{YYYY-MM-DD}-{topic}/{sequence}-{purpose}.md
```
</single_prompt_presentation>
</step_3_present>

</process>

<reference_guides>
**Prompt patterns by purpose:**
- [references/do-patterns.md](references/do-patterns.md)
- [references/plan-patterns.md](references/plan-patterns.md)
- [references/research-patterns.md](references/research-patterns.md)
- [references/refine-patterns.md](references/refine-patterns.md)

**Shared templates:**
- [references/summary-template.md](references/summary-template.md)
- [references/metadata-guidelines.md](references/metadata-guidelines.md)

**Supporting references:**
- [references/question-bank.md](references/question-bank.md)
- [references/intelligence-rules.md](references/intelligence-rules.md)
</reference_guides>
