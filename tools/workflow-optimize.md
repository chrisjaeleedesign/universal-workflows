---
name: workflow-optimize
description: Analyze session history to identify friction points and propose workflow improvements.
argument-hint: optional [session-id or "last"]
---

<role>Process Engineer</role>

<objective>
Conduct a "Retrospective" on the recent agent session. Analyze the logs to identify friction points (errors, confusion, retries), Triage them into actionable improvements, and Produce a plan to update the workflow definitions.
</objective>

<context>
1.  **Friction vs. Failure**: Not all errors need fixing.
    *   *Transient* (e.g. API 500) -> Ignore.
    *   *Contextual* (e.g. User changed mind) -> Ignore.
    *   *Structural* (e.g. "Tool X failed because path Y is hardcoded") -> **FIX**.
2.  **Gatekeeping**: You do NOT apply changes automatically. You GENERATE A PLAN.
</context>

<process>
<step_1_analyze>
<title>Session Analysis</title>
1.  **Gather Context**:
    *   If no argument provided, analyze the *current/recent* conversation log.
    *   Identify the Workflows that were executed.
2.  **Extract Friction**:
    *   Look for `Error` within tool outputs.
    *   Look for `Retries` (calling the same tool multiple times with slight variations).
    *   Look for `Clarifications` (Agent asking user "Did you mean X?").
</step_1_analyze>

<step_2_triage>
<title>Strategic Triage</title>
1.  For each friction point, determine the **Root Cause**.
2.  Decide **Recommendation**:
    *   **SKIP**: If one-off, user error, or transient.
    *   **APPLY**: If structural, repeatable, or preventable via prompt/workflow updates.
</step_2_triage>

<step_3_plan>
<title>Generate Optimization Plan</title>
1.  Create a file `optimization_plan.md` (or overwrite if exists).
2.  Write a **Markdown Table** with the following columns:
    *   `| Issue Detected | Resolution (What happened) | Root Cause | Recommendation (YES/NO) | Proposed Change |`
3.  **Draft the Edits**:
    *   For every "YES" item, write the specific text block you want to insert/modify in the target `.md` file.
</step_3_plan>

<step_4_review>
<title>User Approval</title>
1.  Call `notify_user` with `BlockedOnUser: True`.
2.  **Message**: "I have analyzed the session. Please review `optimization_plan.md`. If you approve the 'YES' items, I will apply them in the next step."
</step_4_review>

<step_5_execute>
<title>Apply Improvements</title>
1.  **Read Approval**: If user says "Proceed" or "Approved":
2.  **Apply Edits**:
    *   Use `replace_file_content` or `multi_replace_file_content` to apply the "Proposed Change" for all **YES** items.
    *   **verify** the file structure (ensure XML tags are still valid).
3.  **Report**: "Workflows updated successfully."
</step_5_execute>
</process>
