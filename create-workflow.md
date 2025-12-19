---
name: create-workflow
description: Create a new Antigravity workflow following best practices.
argument-hint: "[workflow-name] [description]"
allowed-tools: [write_to_file, read_url_content, task_boundary, list_dir, notify_user]
---

<objective>
Create a new robust workflow file in `.agent/workflows/commands/` that adheres to the `workflow-best-practices.md` guidelines.
</objective>

<context>
Best Practices: @.agent/workflows/commands/references/workflow-best-practices.md
Existing Workflows: !`ls .agent/workflows/commands/*.md | head -5`
Current Task: @.gemini/antigravity/brain/CURRENT_UUID/task.md
</context>

<input>
$ARGUMENTS should contain the desired workflow name (kebab-case) and a brief description of what it should do.
Example: "deploy-production Deploy the app to the production server safely"
</input>

<process>
<step_1_intake>
<title>Analyze & Validate</title>
1.  **Analyze Input**:
    -   Extract `name` (first word).
    -   Extract `goal` (rest of string).
    -   If empty, ASK user: "What is the name and goal of the new workflow?"
2.  **Determine Category**:
    -   Scan `.agent/workflows/commands/` for existing subdirectories.
    -   ASK user: "Which category should this go into? (e.g., 'content', 'experiments', or a new one)"
3.  **Validate**:
    -   Ensure name is kebab-case.
    -   Check if file `.agent/workflows/commands/{category}/{name}.md` already exists.
    -   If it exists, ASK user: "Overwrite existing workflow {category}/{name}? (y/n)"
</step_1_intake>

<step_2_design>
<title>Architect the Workflow</title>
1.  **Read Best Practices**: Review `workflow-best-practices.md` for structure.
2.  **Select Pattern**:
    -   Is it a RESEARCH task? -> Use "Deep Dive" pattern.
    -   Is it a DO task? -> Use "Factory" or "Execution" pattern.
    -   Is it a ROUTER? -> Use "Router" pattern.
3.  **Draft Content**:
    -   **Frontmatter**: Define `name`, `description`, `allowed-tools`.
        -   *CRITICAL*: Quote `argument-hint` if it has brackets.
        -   *CRITICAL*: List ALL tools used in steps (e.g., `notify_user` if asking questions).
    -   **Objective**: Clear definition of done.
    -   **Process**: Numbered steps with XML tags.
    -   **Context**: Dynamic context links (`!`).
</step_2_design>

<step_3_create>
<title>Generate Workflow File</title>
1.  **Construct File Path**: `.agent/workflows/commands/{category}/{name}.md`
2.  **Write Content**:
    -   Use `write_to_file`.
    -   Ensure NO conversational filler in the file content.
    -   Strictly follow the XML+Frontmatter format.
3.  **Register**:
    -   (Optional) If there is a central registry file, update it. (Currently none).
</step_3_create>

<step_4_verify>
<title>Validation & Summary</title>
1.  **Check**: Does the file exist?
2.  **Summary**: Create `SUMMARY.md` listing:
    -   New workflow path.
    -   Command to run it (`/run-prompt .agent/workflows/commands/{category}/{name}.md` or `/{name}`).
    -   Key features included.
</step_4_verify>
</process>
