---
description: Create a new Antigravity workflow.
---

<input>
$ARGUMENTS should contain the desired workflow name (kebab-case) and a brief description.
</input>

<context>
Standards: @.agent/workflows/commands/universal-workflows/tools/create-workflow/standards.md
Existing Workflows: !`ls .agent/workflows/commands/universal-workflows/tools/*.md | head -5`
Current Task: @.gemini/antigravity/brain/CURRENT_UUID/task.md
</context>

<process>
<step_1_intake>
<title>Analyze & Validate</title>
1.  **Analyze Input**:
    -   Extract `name` (first word).
    -   Extract `goal` (rest of string).
    -   If empty, ASK user: "What is the name and goal of the new workflow?"
2.  **Determine Category**:
    -   Scan `.agent/workflows/commands/` for existing subdirectories.
    -   ASK user: "Which category should this go into? (e.g., 'universal-workflows', 'content', 'experiments', or a new one)"
3.  **Validate**:
    -   Ensure name is kebab-case.
    -   Check if file `.agent/workflows/commands/{category}/{name}.md` already exists.
    -   If it exists, STOP and suggest using the `update` path or ASK to overwrite.
</step_1_intake>

<step_2_design>
<title>Architect the Workflow</title>
1.  **Read Standards**: Review `standards.md` for structure and best practices.
2.  **Select Pattern**:
    -   Research -> "Deep Dive"
    -   Action -> "Factory" or "Execution"
    -   Routing -> "Router"
3.  **Draft Content**:
    -   **Frontmatter**: Define `name`, `description`, `allowed-tools`.
    -   **Objective**: Clear definition of done.
    -   **Process**: Numbered steps with XML tags.
    -   **Context**: Dynamic context links.
</step_2_design>

<step_3_create>
<title>Generate Workflow File</title>
1.  **Construct File Path**: `.agent/workflows/commands/{category}/{name}.md`
2.  **Write Content**:
    -   Use `write_to_file`.
    -   Ensure NO conversational filler.
    -   Strictly follow the XML+Frontmatter format.
</step_3_create>

<step_4_verify>
<title>Validation & Summary</title>
1.  **Check**: Does the file exist?
2.  **Summary**: Create `SUMMARY.md` listing:
    -   New workflow path.
    -   Command to run it.
</step_4_verify>
</process>
