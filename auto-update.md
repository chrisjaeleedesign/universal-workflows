---
description: Automate deep-dive analysis and documentation updates for a directory, with self-reflection and error prevention.
---

<role>Documentation Specialist</role>

<objective>
Execute a "Deep Dive & Update" cycle on a target directory or component.
1. Analyze the current state (Deep Dive).
2. Update relevant Markdown documentation to match reality (Update).
3. Reflection on the process to identify friction and prevent future errors (Refine/Memorize).
</objective>

<parameters>
TARGET: The directory or component to analyze (e.g., "research/marketing", "src/components").
</parameters>

<context>
Project Rules: @.agent/rules/
Current Task: @.gemini/antigravity/brain/CURRENT_UUID/task.md
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

<step_2_update_documentation>
**Goal**: Bring context files up to date.
1.  **Target Files**: Look for `README.md`, `CONTEXT.md`, or specific documentation files in {TARGET}.
2.  **Create/Update**:
    - If no docs exist, create a `README.md`.
    - Update the **Overview**, **Structure**, and **Usage** sections based on your Deep Dive.
    - **CRITICAL**: Ensure file paths and dependencies mentioned in docs are accurate.
3.  **Format**: Use clear Markdown (headers, code blocks, links).
</step_2_update_documentation>

<step_3_reflect_and_memorize>
**Goal**: Prevent future amnesia and errors.
1.  **Review Execution**: Look back at the steps you just took.
2.  **Add Notes**:
    - Add a `## Agent Notes` or `## Troubleshooting` section to the documentation.
    - Explicitly document:
        - "Potentially confusing areas"
        - "Common pitfalls in this directory"
        - "Assumptions made during analysis"
    - If a specific error occurred, write a rule/note on how to avoid it next time.
</step_3_reflect_and_memorize>

<step_4_finalize>
1.  **Verify**: Check that the updated Markdown renders correctly and links are valid.
2.  **Summary**: Create a `SUMMARY.md` (or output text) listing:
    - Files analyzed.
    - Documentation updated.
    - Key "Learnings" added to the notes.
</step_4_finalize>
</process>

<output_format>
- Modified/New `README.md` or `CONTEXT.md` in {TARGET}.
- `SUMMARY.md` in the current artifacts directory.
</output_format>

<intelligence_rules>
- **No Hallucinations**: Only document what you verify exists in the files.
- **Preserve User Intent**: Do not remove high-level "Vision" or "Goals" sections written by the user unless explicitly told to. Focus on technical accuracy and implementation details.
- **Tone**: Professional, concise, engineer-to-engineer.
</intelligence_rules>
