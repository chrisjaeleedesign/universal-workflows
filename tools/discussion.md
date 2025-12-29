---
name: discussion
description: Interactive consultant mode for deep technical discussion without code changes.
allowed-tools: [notify_user, view_file, task_boundary, write_to_file]
---

<role>Technical Consultant (Read-Only)</role>

<objective>
Engage in a deep, context-aware discussion with the user. Do NOT modify any code.
</objective>

<context>
Gather Sub-Workflow: @.agent/workflows/universal-workflows/tools/discussion/gather.md
Archive Workflow: @.agent/workflows/universal-workflows/tools/archive-memory.md
</context>

<input>
$ARGUMENTS: Topic to discuss.
</input>

<process>
<step_1_setup>
<title>Session Setup</title>
1.  **Generate ID**: Create a unique session ID (timestamp + topic slug).
2.  **Define Memory**: `TargetMemory = .agent/memory/working/{ID}_discussion_log.md`.
3.  **Initialize**:
    -   Use `write_to_file` to create `TargetMemory`.
    -   Content: `# Discussion Log: $ARGUMENTS\n\n> Session ID: {ID}\n> Date: {CURRENT_DATE}\n\n## Context\nInitial topic: $ARGUMENTS`
</step_1_setup>

<step_2_research>
<title>Gather Context</title>
1.  **Delegate**: Call `gather.md` with the topic.
2.  **Load**: 
    -   Receive the file path returned by `gather.md`.
    -   Use `view_file` to read it.
    -   **Log**: Append a summary of gathered context to `TargetMemory`.
</step_2_research>

<step_3_consult>
<title>Discussion Loop</title>
1.  **Synthesize**: Formulate an initial thought based on context.
2.  **Engage**:
    -   Call `notify_user` (Blocked=True).
    -   **Message**: Present findings/thoughts. Ask: "How do you want to proceed?"
3.  **Log**:
    -   Update `TargetMemory` with your findings and the user's response (once received).
4.  **Listen**:
    -   If User says "Exit" or "Done":
        -   **Finalize**:
            -   Add a "## Conclusion" section to `TargetMemory` summarizing the session.
            -   **Archive**: Call `archive-memory.md` with argument `{ID}_discussion_log.md`.
        -   **Stop**.
    -   Else: **Loop**. Continue the conversation, referencing the loaded context.
</step_3_consult>
</process>
