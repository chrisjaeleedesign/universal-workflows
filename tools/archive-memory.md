---
name: archive-memory
description: Moves the active Domain Memory file from working/ to archive/.
allowed-tools: [run_command, list_dir, notify_user]
---

<role>Memory Librarian</role>

<input>
$ARGUMENTS: (Optional) Specific file to archive, otherwise finds the active one.
</input>

<process>
<step_1_identify>
<title>Find Active File</title>
1.  **Scan**: List `.agent/memory/working/`.
2.  **Select**: 
    -   If `$ARGUMENTS` provided, pick that.
    -   Else, pick the most recent `.md` file.
    -   If empty, **Stop**. "No active memory to archive."
</step_1_identify>

<step_2_archive>
<title>Move to Archive</title>
1.  **Generate Name**:
    -   Source: `working/{filename}`
    -   Dest: `archive/{filename}` (Files should already have timestamps/slugs).
2.  **Execute**:
    -   `mv .agent/memory/working/{filename} .agent/memory/archive/{filename}`
3.  **Report**:
    -   "Archived memory trace: `archive/{filename}`".
</step_2_archive>
</process>
