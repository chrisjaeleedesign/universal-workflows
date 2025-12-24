# Antigravity Workflow Design Patterns & Best Practices

## Core Philosophy
Workflows are **structured cognitive maps** for agents. They transform vague intents into executed outcomes by providing:
1.  **Clear Context**: Access to necessary files and tools.
2.  **Structured Steps**: XML-defined stages that guide logic.
3.  **Role Definition**: Specific personas for specific tasks (e.g., "Experiment Manager").
4.  **Error Handling**: Pre-defined recovery paths.

## Anatomy of a Workflow

Every workflow must be a Markdown file (`.md`) with YAML frontmatter.

### 1. Frontmatter
Defines metadata and capability boundaries.
-   **Quoting**: ALWAYS quote strings that contain special characters like `[]`, `:`, or start with `*`.
    -   *Bad*: `argument-hint: [name]`
    -   *Good*: `argument-hint: "[name]"`
-   **Tools**: Verify that every tool used in the `<process>` (e.g., `notify_user` for asking questions) is listed in `allowed-tools`.

```yaml
---
name: workflow-name-kebab-case
description: Action-oriented summary of what this does.
argument-hint: "[optional input format hint]"
allowed-tools: [tool1, tool2] # Restrict tools to reduce noise
---
```

### 2. High-Level Blocks
Use XML tags to segment major sections. This helps the LLM parser maintain focus.

-   `<objective>`: What is the success state?
-   `<role>`: (Optional) Who is the agent acting as?
-   `<context>`: Where to look for info. use `!` for dynamic context.
    -   `Git status: !'git status'`
-   `<input>`: How to interpret user arguments.

### 3. The Process Block `<process>`
The core logic engine. Break down into numbered steps.

```xml
<process>
  <step_1_intake>
    <title>Step Title</title>
    1. Action 1
    2. Action 2
  </step_1_intake>

  <step_2_execute>
    ...
  </step_2_execute>
</process>
```

## Best Practices

### "Silent" Context Gathering
Do not ask the user for info you can find yourself.
-   **Bad**: "Ask user for project status."
-   **Good**: "Read `task.md`. If missing, then ask user."

### Critical Routing (Switch Statements)
Use clear `IF/ELSE` logic for decision points.
```xml
<critical_routing>
  IF input starts with "feat": Route to Feature Workflow
  ELSE IF input starts with "fix": Route to Bug Workflow
</critical_routing>
```

### Artifact Management
-   **Always** update `task.md` status.
-   **Create** `SUMMARY.md` for complex outputs.
-   **Archive** intermediate artifacts if they clutter the workspace.

## Common Anti-Patterns
1.  **"Claude-isms"**: Avoid conversational filler like "I will now do X". Just do X.
2.  **Vague Steps**: "Analyze the code" is bad. "List files in `src/`, read headers of `*.ts`" is good.
3.  **Unbounded Scope**: Workflows should have a clear "Definition of Done".

## Reusable Patterns
-   **The "Deep Dive"**: 1. List files, 2. Read key files, 3. Synthesize. (See `auto-update.md`)
-   **The "Router"**: Identify intent -> Delegate to sub-workflow/prompt. (See `experiment.md`)
-   **The "Factory"**: Gather requirements -> Generate file from template. (See `create-meta-prompt.md`)

## Workflow Architecture & Directory Structure
**Reference**: https://antigravity.google/docs/rules-workflows#workflows

### modularity
Create smaller "function-like" sub-workflows that are assembled to accomplish complex tasks.
-   **Main Workflow**: The entry point (e.g., `create-workflow.md`).
-   **Sub-directory**: Same name as the workflow (e.g., `create-workflow/`).
-   **Sub-workflows**: Specialized logical units within the sub-directory (e.g., `create-workflow/new.md`).
-   **Context**: A knowledge/reference document in the sub-directory (e.g., `create-workflow/standards.md`) for the agent to reference.

### Design Principles
1.  **Infer Intent**: The main workflow should be smart enough to route to the correct sub-workflow (e.g., Create vs Update).
2.  **Explicit Context**: Always reference the relevant standards/context file in the sub-workflows.
3.  **Verification**: Include explicit verification steps, especially for updates.
