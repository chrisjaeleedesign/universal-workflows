---
name: help
description: Interactive manual for the Agent System. Lists commands or explains specific workflows.
allowed-tools: [read_resource, view_file, notify_user, task_boundary]
---

<role>System Guide</role>

<input>
$ARGUMENTS: (Optional) The name of the command to query (e.g. "intake").
</input>

<process>
<step_1_consult>
<title>Consult Registry</title>
1.  **Read**: Use `view_file` to read `.agent/workflows/workflow_registry.md`.
2.  **Analyze**:
    -   If `$ARGUMENTS` is EMPTY:
        -   **List All**:
            -   Parse all entries.
            -   **Filter**: Ignore entries where `role` contains "(Sub)" or "Hidden".
            -   **Format**: Create a Markdown Table: `| Command | Description | Example Usage |`.
            -   *Constraint*: You MUST synthesize a helpful, concrete example for each (e.g. for `/intake`, use `/intake "Build a login page"`).
    -   If `$ARGUMENTS` is SET (e.g. "intake"):
        -   **Deep Dive**:
            -   Find the entry for the requested command.
            -   Use `view_file` to read the target workflow file (`path`).
            -   **Format**: Present the `<description>`, `<input>` requirements, and `<role>`.
</step_1_consult>

<step_2_respond>
<title>Guide User</title>
1.  **Notify**: Call `notify_user` with the formatted guide.
</step_2_respond>
</process>
