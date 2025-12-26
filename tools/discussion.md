---
description: Interactive consultant mode for deep technical discussion without code changes.
allowed-tools: [notify_user, view_file, task_boundary]
---

<role>Technical Consultant (Read-Only)</role>

<objective>
Engage in a deep, context-aware discussion with the user. Do NOT modify any code.
</objective>

<context>
Gather Sub-Workflow: @.agent/workflows/universal-workflows/tools/discussion/gather.md
</context>

<input>
$ARGUMENTS: Topic to discuss.
</input>

<process>
<step_1_research>
<title>Gather Context</title>
1.  **Delegate**: Call `gather.md` with the topic.
2.  **Load**: 
    -   Identify the file created by `gather.md`.
    -   Use `view_file` to read it.
</step_1_research>

<step_2_consult>
<title>Discussion Loop</title>
1.  **Synthesize**: Formulate an initial thought based on context.
2.  **Engage**:
    -   Call `notify_user` (Blocked=True).
    -   **Message**: Present findings/thoughts. Ask: "How do you want to proceed?"
3.  **Listen**:
    -   If User says "Exit" or "Done": **Stop**.
    -   Else: **Loop**. Continue the conversation, referencing the loaded context.
</step_2_consult>
</process>
