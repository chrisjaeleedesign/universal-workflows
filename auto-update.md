---
description: Automate deep-dive analysis and documentation updates for a directory, with self-reflection and error prevention.
allowed-tools: [run_command, view_file, notify_user, codebase_search, write_to_file, replace_file_content]
---

<role>Documentation & Maintenance Specialist</role>

<objective>
Execute a "Deep Dive & Maintenance" cycle on a target directory or component.
1. Analyze the current state (Deep Dive).
2. Perform maintenance (Gitignore, Comments).
3. Update relevant Markdown documentation (Use Code as Source of Truth).
4. Reflection on the process (Refine/Memorize).
</objective>

<parameters>
TARGET: The directory or component to analyze (e.g., "research/marketing", "src/components").
</parameters>

<context>
Project Rules: @.agent/rules/
Current Task: @.gemini/antigravity/brain/CURRENT_UUID/task.md
Best Practices: @.agent/workflows/universal-workflows/references/workflow-best-practices.md
</context>

<process>
<step_1_deep_dive_analysis>
**Goal**: Understand the *current* reality of the {TARGET}.
1.  **Explore**: List files in {TARGET} to understand structure.
2.  **Read**: content of key files (entry points, configs, existing READMEs).
3.  **Compare**: Check if existing documentation matches the code/file structure.
    - Note missing sections.
    - Note outdated information.
    - Note any "implied" knowledge that isn't written down.
</step_1_deep_dive_analysis>

<step_2_maintenance_checks>
**Goal**: Ensure code hygiene and security.
1.  **Gitignore Check**:
    -   Look at the file types in {TARGET}.
    -   Are there generated files (logs, build output) or secrets (.env) that are NOT in `.gitignore`?
    -   **Action**: If yes, update `.gitignore` immediately.
2.  **Code Commenting**:
    -   Scan complex code files (read in Step 1).
    -   Identify complex logic blocks that lack explanation.
    -   **Action**: Add brief, clarifying comments or TODOs if the logic is unclear. *Do not rewrite logic, just explain it.*
</step_2_maintenance_checks>

<step_3_update_documentation>
**Goal**: Bring context files up to date. "Code is Truth".
1.  **Target Files**: Look for:
    -   `README.md`
    -   `CONTEXT.md`
    -   Files inside `knowledge/` or `references/` directories.
2.  **Create/Update**:
    -   If no docs exist, execute judgment: does this folder need a README? If yes, create it.
    -   Update **Overview**, **Structure**, and **Usage** sections based on your Deep Dive.
    -   **Sync Knowledge**: If updating files in `knowledge/`, ensure they reflect the *actual* code behavior you observed.
    -   **CRITICAL**: Ensure file paths and dependencies mentioned in docs are accurate.
3.  **Format**: Use clear Markdown (headers, code blocks, links).
</step_3_update_documentation>

<step_4_reflect_and_memorize>
**Goal**: Prevent future amnesia and errors.
1.  **Review Execution**: Look back at the steps you just took.
2.  **Add Notes**:
    -   Add a `## Agent Notes` or `## Troubleshooting` section to the documentation.
    -   Explicitly document:
        - "Potentially confusing areas"
        - "Common pitfalls in this directory"
        - "Assumptions made during analysis"
    -   If a specific error occurred, write a rule/note on how to avoid it next time.
</step_4_reflect_and_memorize>

<step_5_finalize>
1.  **Verify**: Check that the updated Markdown renders correctly and links are valid.
2.  **Summary**: Create a `SUMMARY.md` (or output text) listing:
    -   Files analyzed.
    -   Maintenance performed (gitignore, comments).
    -   Documentation updated.
    -   Key "Learnings" added to the notes.
</step_5_finalize>
</process>

<output_format>
- Modified/New `README.md` or `CONTEXT.md` in {TARGET}.
- `SUMMARY.md` in the current artifacts directory.
</output_format>

<intelligence_rules>
- **No Hallucinations**: Only document what you verify exists in the files.
- **Source of Truth**: The CODE is the ultimate authority. If docs say X and code says Y, update docs to say Y.
- **Preserve User Intent**: Do not remove high-level "Vision" or "Goals" sections written by the user unless explicitly told to. Focus on technical accuracy and implementation details.
- **Tone**: Professional, concise, engineer-to-engineer.
</intelligence_rules>
