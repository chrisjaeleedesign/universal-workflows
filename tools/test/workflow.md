---
description: Integration testing for Agent Workflows/Commands.
---

<role>QA Engineer (Integration)</role>

<input>
$ARGUMENTS: The command string to test (e.g. "/create-content").
</input>

<context>
Standards: @.agent/workflows/universal-workflows/tools/test/test-standards.md
Project Workflows: @.agent/workflows/local-workflows/README.md
</context>

<process>
<step_1_setup>
<title>Test Environment</title>
1.  **Parse Command**: Identify the target workflow (e.g. `create-content.md`).
2.  **Prepare**:
    -   Define a "Test Scenario" (e.g. "Create a blog post about Apples").
    -   Identify expected outputs (e.g. "Should create a .md file in content/").
</step_1_setup>

<step_2_execute>
<title>Run Workflow</title>
1.  **Execute**: Run the command with the test scenario.
    -   *Example*: `/create-content "Apples (Test Run)"`
2.  **Monitor**: Wait for completion (Task Boundary updates).
</step_2_execute>

<step_3_verify>
<title>Verification</title>
1.  **Check Artifacts**:
    -   Did the expected file appear?
    -   Is it non-empty?
    -   Does `SUMMARY.md` exist (if expected)?
2.  **Report**:
    -   PASS/FAIL based on artifact existence.
</step_3_verify>

<step_4_cleanup>
<title>Cleanup</title>
1.  **Action**: Move test artifacts to `.agent/trash/` or delete them to keep the workspace clean.
</step_4_cleanup>
</process>
