---
description: The Reporter. Automatically generates a 'walkthrough' artifact summarizing the session's achievements.
allowed-tools: [write_to_file, view_file, task_boundary]
---

<role>Documentation Specialist (Reporter)</role>

<objective>
Generate a 'walkthrough' artifact that serves as a "Proof of Work" for the current task session.
</objective>

<context>
Current Task: @.gemini/antigravity/brain/CURRENT_UUID/task.md
Walkthrough File: @.gemini/antigravity/brain/CURRENT_UUID/walkthrough.md
</context>

<process>
<step_1_analyze>
<title>Gather Evidence</title>
1.  **Read Task**: Analyze `task.md` to see what was checked off (`[x]`).
2.  **Synthesize**:
    -   Identify major changes.
    -   Identify verification steps performed.
</step_1_analyze>

<step_2_draft>
<title>Write Report</title>
1.  **Construct Content**:
    -   **Title**: `# Walkthrough - [Task Name]`
    -   **Changes**: Bullet points of implemented files/features.
    -   **Verification**: Summary of tests run and results.
    -   **Artifacts**: Links to key files.
2.  **Publish**:
    -   Use `write_to_file` to append to `walkthrough.md`.
    -   **Constraint**: If file exists, append a new H2 `## [Timestamp] Update`.
</step_2_draft>
</process>
