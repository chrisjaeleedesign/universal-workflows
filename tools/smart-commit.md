---
description: intelligently analyze changes, update documentation if needed, and generate a semantic commit message before pushing.
allowed-tools: [run_command, view_file, notify_user, codebase_search, write_to_file, replace_file_content]
---

<role>Git Operations Specialist</role>

<objective>
Execute a "Smart Commit" cycle:
1.  **Analyze**: Understand the pending changes and current git state.
2.  **Sync**: Ensure documentation (READMEs, etc.) is up-to-date with code changes.
3.  **Commit**: Generate a high-quality, conventional commit message.
4.  **Push**: Push to the correct branch (if requested).
</objective>

<parameters>
push: (Optional) Boolean. Set to 'true' to push after committing. Default: true.
</parameters>

<context>
Project Rules: @.agent/rules/
Current Task: @.gemini/antigravity/brain/CURRENT_UUID/task.md
Auto-Update Workflow: @.agent/workflows/universal-workflows/tools/auto-update.md
</context>

<process>
<step_1_analyze_state>
**Goal**: Get a clear picture of what is changing.
1.  **Check Status**: Run `git status` to see modified/staged files.
2.  **Detect Branch**: Run `git rev-parse --abbrev-ref HEAD` to identify the current active branch.
3.  **Read Diffs**: Use `git diff` (or `git diff --staged`) to understand the *content* of the changes.
    -   *Specific Check*: Look for changes in `.gitignore`, `.env.example`, `package.json`, or top-level `README.md`. These often require corresponding documentation updates.
</step_1_analyze_state>

<step_2_smart_docs_sync>
**Goal**: Prevent "Documentation Drift".
1.  **Assess Impact**: Do the changes in Step 1 affect how the code is *used* or *structured*?
    -   Did you add a new "Workflow"? -> `README.md` might need an update.
    -   Did you change a configuration file? -> Config docs might need an update.
    -   Did you add a new dependency? -> Setup guide might need an update.
2.  **Trigger Auto-Update (Conditional)**:
    -   **IF** significant documentation updates are anticipated:
        -   Inform the user: "Detected changes that may require documentation updates. Running auto-update..."
        -   **EXECUTE** the `auto-update` workflow on the relevant directory.
    -   **ELSE**: Continue to the next step.
</step_2_smart_docs_sync>

<step_3_generate_commit>
**Goal**: Create a semantic, descriptive commit message.
1.  **Synthesize**: Combine your knowledge of the diffs (Step 1) and any doc updates (Step 2).
2.  **Draft Message**: Functionally describe the change using Conventional Commits format.
    -   `feat: ...` for new features.
    -   `fix: ...` for bug fixes.
    -   `docs: ...` for documentation only.
    -   `chore: ...` for maintenance.
    -   *Rule*: Keep the first line under 50 chars. Use body for details.
3.  **Execute Commit**:
    -   **Guard**: Run `git status`. If nothing is modified or staged, **STOP**. Notify user: "No changes to commit."
    -   `git add .` (Verify this is safe/desired based on `git status` output).
    -   `git commit -m "YOUR_GENERATED_MESSAGE"`
</step_3_generate_commit>

<step_4_push_changes>
**Goal**: Upload changes to the remote repository.
1.  **Check Parameter**: Is `push` set to `false`?
    -   If yes, **STOP**. Notify user: "Changes committed locally to branch '{current_branch}'."
2.  **Execute Push**:
    -   Run `git push origin {current_branch}`.
    -   *Error Handling*: If the upstream is not set, use `git push --set-upstream origin {current_branch}`.
3.  **Finalize**:
    -   Notify user: "Successfully pushed to {current_branch}."
</step_4_push_changes>
</process>
