# Testing Standards & Requirements

## Unit Testing (Pytest)
-   **Naming**: Files must be `test_[name].py` or `tests/adhoc/test_[timestamp].py`.
-   **Framework**: Use `pytest`.
-   **Structure**: `setup -> execute -> assert`.
-   **Self-Correction**: If a test fails, the agent must attempt to fix the *code* or the *test* once before giving up.

## Visual Quality (AI Feedback)
-   **Tool**: `get-feedback.md` (Vision API).
-   **Reference**: `research/knowledge/iris_studio_brand_playbook.md`.
-   **Criteria**:
    -   Does it match the "Anti-Noise" aesthetic?
    -   Are charts clearly labeled (Semantic Titles)?
    -   Is the data-ink ratio high?

## Workflow/Agent Testing
-   **Goal**: robustly verify that an agent command works.
-   **Definition of Done**:
    -   Command runs without fatal error.
    -   Expected artifacts (files) are created.
    -   `SUMMARY.md` is generated (if applicable).
-   **Safety**: Use temporary filenames or cleanup steps to avoid polluting the workspace.
