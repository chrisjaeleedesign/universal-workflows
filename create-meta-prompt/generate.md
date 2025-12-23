---
description: Generation logic for create-meta-prompt. Generates the actual prompt file.
---

<role>Prompt Engineer (Generator)</role>

<input>
$ARGUMENTS: The inferred `purpose`, `topic`, and `description`.
</input>

<process>
<step_1_generate>
<title>Generate Prompt</title>

<load_patterns>
Load purpose-specific patterns (RELATIVELY LINKED):
- Do: [references/do-patterns.md](references/do-patterns.md)
- Plan: [references/plan-patterns.md](references/plan-patterns.md)
- Research: [references/research-patterns.md](references/research-patterns.md)
- Refine: [references/refine-patterns.md](references/refine-patterns.md)

Load intelligence rules: [references/intelligence-rules.md](references/intelligence-rules.md)
</load_patterns>

<prompt_structure>
All generated prompts include:
1. **Objective**: What to accomplish
2. **Context**: Referenced files (@), dynamic context (!)
3. **Artifact Updates** (Critical): `brain/task.md` and `brain/implementation_plan.md`
4. **Requirements**: Specific instructions
5. **Output specification**: XML metadata, SUMMARY.md
6. **Success criteria**

For Research and Plan prompts, output must include:
- `<confidence>`, `<dependencies>`, `<open_questions>`, `<assumptions>`

All prompts must create `SUMMARY.md`.
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
1. Identify/Create Session Folder: `.prompts/{YYYY-MM-DD}-{topic}/`
2. Determine File Sequence: Check existing `*-{purpose}.md` files, increment counter (e.g., `01`, `02`).
3. Write prompt to: `.prompts/{YYYY-MM-DD}-{topic}/{sequence}-{purpose}.md`
</file_creation>
</step_1_generate>

<step_2_present>
<title>Present Result</title>
Present the created prompt path and the run command:
` /run-prompt .prompts/{YYYY-MM-DD}-{topic}/{sequence}-{purpose}.md `
</step_2_present>
</process>
