---
name: test
description: Intelligent testing agent that infers test targets (Unit vs. Visual) and executes verification.
argument-hint: "[description of what to test]"
allowed-tools: [run_command, write_to_file, read_url_content, view_file, list_dir, notify_user]
---

<objective>
Infer the user's testing intent (Code Logic vs. Output Quality), generate an appropriate test strategy (Pytest vs. AI Feedback), and execute it to provide a Pass/Fail result.
</objective>

<context>
AI Feedback Tool: @research/scripts/ai_feedback.py
Current Task: @.gemini/antigravity/brain/CURRENT_UUID/task.md
Project Structure: !'tree -L 2 -I "node_modules|venv|__pycache__"'
</context>

<process>
<step_1_scoping>
<title>Infer Test Strategy</title>
1.  **Analyze Request**:
    -   Read `$ARGUMENTS`.
    -   Scan workspace for related files (keywords in arguments).
2.  **Determine Type**:
    -   **IF** arguments mention "function", "class", "logic", "utils", "api": Set Type = **LOGIC**.
    -   **IF** arguments mention "visual", "image", "look", "quality", "ui", "feedback": Set Type = **QUALITY**.
    -   **IF** arguments mention "human", "tune", "refine", "interactive", "loop": Set Type = **HITL**.
    -   **ELSE**: 
        -   **ACTION**: Call `notify_user` to ask the user to choose:
            1.  **Logic** (Pytest)
            2.  **Quality** (AI Feedback)
            3.  **Human Tuning** (HITL)
        -   Set Type based on response.
3.  **Plan**:
    -   **LOGIC**: Plan to generate a `tests/adhoc/test_[id].py` using standard `pytest`.
    -   **QUALITY**: Delegate to `@get-feedback` workflow.
    -   **HITL**: Initiate the "Tuning Loop" (Baseline -> Critique -> Refine).
</step_1_scoping>

<step_2_generate>
<title>Generate Test Scaffolding</title>
1.  **LOGIC Route**:
    -   Create file `tests/adhoc/test_[timestamp].py`.
    -   Content: Import target module, write test cases with assertions.
2.  **QUALITY Route**:
    -   Skip generation. Proceed to `@get-feedback`.
</step_2_generate>

<step_3_execute>
<title>Run Verification</title>
1.  **LOGIC Route**:
    -   Evaluate strict boolean pass/fail if possible.
    -   If Fail: Read output, attempt to fix code OR test, re-run once.
2.  **QUALITY Route**:
    -   **SWITCH WORKFLOW**: Run `@get-feedback [path] "[optional_specific_questions]"`.
    -   Output the result from that workflow.
3.  **HITL Route (The Tuning Loop)**:
    -   **Step A (Baseline)**: Identify the current artifact (file/output). Present path to user.
    -   **Step B (Critique)**: Call `notify_user` (Blocked=True). Ask: "What specifically needs to be improved? (Tone, Logic, Style)".
    -   **Step C (Refine)**: Update the underlying code or template based on user critique.
    -   **Step D (Regenerate)**: Run the generation command again.
    -   **Step E (Verify)**: Call `notify_user` again with new output.
        -   If User says "Approved": **EXIT**.
        -   If User gives more feedback: **GOTO Step C**.
</step_3_execute>

<step_4_report>
<title>Final Report</title>
1.  **Summarize Results**:
    -   "Test Type: [Logic/Quality]"
    -   "Result: [Pass/Fail/Score]"
    -   "Details: [Brief summary]"
2.  **Cleanup**:
    -   Ask if user wants to keep the ad-hoc test file.
</step_4_report>
</process>
