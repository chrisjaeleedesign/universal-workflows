---
description: Generate and execute unit tests (Pytest) for code logic.
---

<role>QA Engineer (Unit)</role>

<input>
$ARGUMENTS: File path or description of logic to test.
</input>

<context>
Standards: @.agent/workflows/commands/universal-workflows/test/standards.md
</context>

<process>
<step_1_scaffold>
<title>Generate Test</title>
1.  **Analyze**: Read target file (if provided) or find relevant code.
2.  **Generate**: Create `tests/adhoc/test_[timestamp].py`.
    -   Import target module.
    -   Write standardized `test_` functions.
    -   Include assertions for happy-path and edge cases.
</step_1_scaffold>

<step_2_execute>
<title>Run Pytest</title>
1.  **Run**: `pytest tests/adhoc/test_[timestamp].py`.
2.  **Evaluate**:
    -   **PASS**: Report success.
    -   **FAIL**: 
        -   Read failure output.
        -   Attempt to fix code OR test file.
        -   Re-run once.
</step_2_execute>

<step_3_cleanup>
<title>Finalize</title>
1.  **Ask**: "Keep test file?"
    -   If No -> Delete.
    -   If Yes -> Move to `tests/`.
</step_3_cleanup>
</process>
