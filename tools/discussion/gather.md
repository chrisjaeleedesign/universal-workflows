---
name: discussion-gather
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

<load_resources>
Patterns: @.agent/workflows/universal-workflows/tools/create-meta-prompt/references/research-patterns.md
</load_resources>

1.  **Draft**: Generate the research brief.
2.  **Format**: 
    -   **Strictly follow the XML schema** defined in `Patterns` (e.g., `<research>`, `<findings>`, `<quality_report>`).
    -   Do not use free-form markdown for the core findings.
3.  **Persist**: 
    -   Generate filename: `.agent/memory/working/{{YYYY}}-{{MM}}-{{DD}}-{{TOPIC_SLUG}}_research.md`
    -   Save the brief there.
</step_3_synthesize>

<step_4_output>
<title>Handoff</title>
1.  **Return**: The absolute path of the generated research brief.
</step_4_output>
</process>
