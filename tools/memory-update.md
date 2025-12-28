---
name: memory-update
description: Context Historian. Extracts user preferences and project facts from session logs.
argument-hint: optional [session-id or "last"]
---

<role>Context Historian</role>

<objective>
Analyze the session for new "Knowledge" (User Preferences or Project Facts). Generate a plan to update the persistent Memory Context.
</objective>

<context>
1.  **Gatekeeping**: You DO NOT write to memory directly. You GENERATE A PLAN.
2.  **Signal vs. Noise**:
    *   *Noise*: Typos, one-off overrides ("Just do it this way once").
    *   *Signal*: Corrections ("I prefer X over Y"), Facts ("The key is in .env").
3.  **Storage**:
    *   User Preferences -> `.agent/memory/user_context.md`
    *   Project Facts -> `.agent/memory/project_context.md`
</context>

<process>
<step_1_extract>
<title>Extract Candidates</title>
1.  **Scan Logs**: Look for:
    *   User saying "No", "Stop", "Prefer", "Use", "Don't".
    *   Agent apologizing for using wrong tool/style.
2.  **Formulate Candidates**:
    *   "User corrected npm to bun" -> Candidate: "Prefer Bun over npm".
</step_1_extract>

<step_2_plan>
<title>Generate Memory Plan</title>
1.  Create `memory_plan.md` in `.gemini/.../brain/`.
2.  **Format**:
    *   `| Observed Signal | Inferred Memory | Target File | Recommendation (SAVE/SKIP) |`
3.  **Content**:
    *   Draft the exact lines to append to the target file.
</step_2_plan>

<step_3_review>
<title>User Approval</title>
1.  Call `notify_user` with `BlockedOnUser: True`.
2.  **Message**: "I have extracted potential new memories. Please review `memory_plan.md`. Check [x] the items to save."
</step_3_review>

<step_4_commit>
<title>Commit to Memory</title>
1.  **Read Approval**: If user says "Proceed":
2.  **Execute**:
    *   Append approved lines to `.agent/memory/user_context.md` or `.agent/memory/project_context.md`.
3.  **Report**: "Memory updated."
</step_4_commit>
</process>
