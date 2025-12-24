---
description: Perform deep research on a topic to gather context for discussion.
---

<role>Technical Researcher</role>

<input>
$ARGUMENTS: Topic or question to research.
</input>

<process>
<step_1_search>
<title>Broad Search</title>
1.  **Extract Keywords**: Identify key terms from "$ARGUMENTS".
2.  **Locate**:
    -   Use `grep_search` to find occurrences.
    -   Use `find` to locate file names.
3.  **Filter**: Identify the most relevant files (up to 20).
</step_1_search>

<step_2_analyze>
<title>Deep Dive</title>
**Loop**: For each file found:
1.  **Read**:
    -   If Code: Read outline (classes/functions).
    -   If Doc: Read full content.
2.  **Extract**: Note key concepts, dependencies, and definitions.
</step_2_analyze>

<step_3_synthesize>
<title>Create Brief</title>
1.  **Draft**: Create a research brief.
2.  **Structure**:
    -   **Problem**: What is being discussed?
    -   **Key Files**: List of files found + brief summary.
    -   **Concepts**: Definitions and relationships.
    -   **Missing**: What wasn't found?
3.  **Persist**: 
    -   Generate filename: `.agent/workflows/commands/universal-workflows/discussion/.discussions/discussion_[DATE]_[TOPIC_SLUG].md`
    -   Save the brief there.
</step_3_synthesize>

<step_4_output>
<title>Handoff</title>
1.  **Return**: The content of `discussion_context.md`.
</step_4_output>
</process>
