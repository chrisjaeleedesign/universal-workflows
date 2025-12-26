# Auto-Update Summary
> Directory: `.agent/workflows/universal-workflows/`
> Date: 2025-12-26

## Analysis
-   **Structure**: Healthy. Matches `universal_manifest.md`.
-   **Documentation**: key files (`README.md`, `standards.md`) are present.
-   **Consistency**: `workflow-standards.md` updated to reflect "Name Required" rule.

## Execution
-   **Updates**:
    -   `README.md`: Added "Troubleshooting" section documenting the Frontmatter Rules (Name vs Argument-Hint).
-   **Verification**:
    -   Verified `intake.md` logic matches Registry implementation.

## Agent Notes
-   **Critical Learning**: The `argument-hint` field in frontmatter poisons Universal Workflows (Manifest-based), causing them to fail registration/discovery. The `name` field is required.
