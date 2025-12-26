---
description: Wraps a command in a Validation Loop until it passes User or Critic review.
allowed-tools: [run_command, notify_user, task_boundary]
---

<role>Reliability Manager (The Loop)</role>

<input>
$ARGUMENTS: The command to loop (e.g. "/write-copy '...').
</input>

<process>
<step_1_execute>
<title>Run Cycle</title>
1.  **Execute**: Run the target command.
2.  **CaptureResult**: Look at the output/artifact.
</step_1_execute>

<step_2_verify>
<title>Automated Verification</title>
1.  **Check Context**:
    -   Did we just write code? (Yes/No)
2.  **Execute Test**:
    -   Call `.agent/workflows/universal-workflows/tools/test.md`.
    -   Arg: "Verify the changes from previous step."
3.  **Gate**:
    -   **PASS**: Proceed to `step_3_validate`.
    -   **FAIL**:
        -   Read Error.
        -   **Refine**: Attempt to fix the code.
        -   **Loop**: Restart at `step_1_execute`.
</step_2_verify>

<step_3_validate>
<title>The Gate</title>
1.  **Auto-Audit**:
    -   If no specific critic mentioned: Validate output vs `task.md` or general standards.
2.  **Check**:
    -   If `critic` involved (or auto-audit): Check Score > 8.
    -   **User Check**: Call `notify_user` (Blocked=True) asking "Is this approved?".
3.  **Decision**:
    -   **Pass**: Exit Loop.
    -   **Fail**:
        -   Gather Feedback.
        -   **Refine**: Update context/fix code.
        -   **Loop**: Go to Step 1.
</step_2_validate>
</process>
