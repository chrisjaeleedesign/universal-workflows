---
name: update-execute
description: Execute maintenance updates and documentation sync.
---

<role>Documentation & Maintenance Specialist (Executor)</role>

<input>
$ARGUMENTS: The target directory (TARGET).
</input>

<context>
Project Rules: @.agent/rules/
Standards: @.agent/workflows/universal-workflows/tools/create-workflow/workflow-standards.md
</context>

<process>
<step_1_maintenance_checks>
<title>Code Hygiene</title>
**Goal**: Ensure code hygiene and security.
1.  **Gitignore Check**:
    -   Look at the file types in {TARGET}.
    -   Are there generated files (logs, build output) or secrets (.env) that are NOT in `.gitignore`?
    -   **Action**: If yes, update `.gitignore` immediately.
2.  **Code Commenting**:
    -   Scan complex code files (read in Step 1).
    -   Identify complex logic blocks that lack explanation.
    -   **Action**: Add brief, clarifying comments or TODOs if the logic is unclear.
3.  **Frontmatter Safety (CRITICAL)**:
    -   **Context**: Universal Workflows (`universal-workflows/`) follow a Hybrid Registry pattern. Some possess `name` fields, others do not.
    -   **Rule**: **NEVER add or remove the `name` field** from valid YAML frontmatter in `universal-workflows/*`.
    -   **Rule**: **NEVER add or remove the `argument-hint` field** in `universal-workflows/*`.
    -   **Reason**: Modifying these fields causes immediate registry breakage.
</step_1_maintenance_checks>

<step_2_update_documentation>
<title>Sync Docs</title>
**Goal**: Bring context files up to date. "Code is Truth".
1.  **Target Files**: `README.md`, `CONTEXT.md`.
2.  **Create/Update**:
    -   Update **Overview**, **Structure**, and **Usage**.
    -   **CRITICAL**: Ensure file paths and dependencies are accurate.
</step_2_update_documentation>

<step_3_reflect_and_memorize>
<title>Reflection</title>
**Goal**: Prevent future amnesia.
1.  **Add Notes**: Add a `## Agent Notes` or `## Troubleshooting` section to the docs with any learnings.
</step_3_reflect_and_memorize>

<step_4_finalize>
<title>Summary</title>
1.  **Verify**: Check Markdown rendering.
2.  **Report**: Generate a `walkthrough` artifact summarizing the maintenance performed.
    -   **ArtifactType**: `walkthrough`
    -   **Content**: List files analyzed, maintenance actions taken, and documentation updates.
    -   **Note**: Do NOT write a `SUMMARY.md` file to the directory. Use the artifact system.
</step_4_finalize>
</process>
