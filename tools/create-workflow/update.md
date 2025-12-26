---
description: Update an existing Antigravity workflow.
---

<input>
$ARGUMENTS should contain the workflow name or path to update, and a description of the desired changes.
</input>

<context>
Standards: @.agent/workflows/universal-workflows/tools/create-workflow/workflow-standards.md
Current Task: @.gemini/antigravity/brain/CURRENT_UUID/task.md
</context>

<process>
<step_1_intake>
<title>Analyze Request</title>
1.  **Identify Workflow**:
    -   Find the target workflow file based on input.
    -   If ambiguous, ASK user to clarify.
2.  **Read Workflow**: Read the content of the existing workflow.
3.  **Read Standards**: Review `workflow-standards.md` to ensure updates align with best practices.
</step_1_intake>

<step_2_plan>
<title>Plan Updates</title>
1.  **Gap Analysis**: Compare current workflow with requested changes and standards.
2.  **Draft Changes**: Determine specifically which sections (Frontmatter, Context, Process) need modification.
</step_2_plan>

<step_3_execute>
<title>Apply Updates</title>
1.  **Modify File**: Use `replace_file_content` or `multi_replace_file_content` to apply changes.
2.  **Refactor**: If needed, improve structure to match current standards (e.g. add XML tags if missing).
</step_3_execute>

<step_4_verify>
<title>Double Check</title>
1.  **Verify Content**: Read the file again after edits.
2.  **Self-Correction**: Does the file EXACTLY match the user's intent?
    -   Did I break the YAML frontmatter?
    -   Did I leave any placeholders?
3.  **Confirm**: If issues found, fix them immediately.
4.  **Summary**: Report the changes made to the user.
</step_4_verify>
</process>
