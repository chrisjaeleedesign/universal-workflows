---
name: run-prompt
description: Delegate one or more prompts to fresh sub-task contexts with parallel or sequential execution
argument-hint: <prompt-number(s)-or-name> [--parallel|--sequential]
allowed-tools: [read_url_content, task_boundary, run_command, list_dir]
---

<role>Workflow Executor</role>

<context>
Git status: !`git status --short`
Recent prompts: !`ls -t ./prompts/*.md | head -5`
</context>

<objective>
Execute one or more prompts from `./prompts/` as delegated sub-tasks. Supports single prompt execution and sequential execution of dependent prompts.
</objective>

<input>
The user will specify which prompt(s) to run via $ARGUMENTS, which can be:

**Supported Inputs:**
- **Full Path**: `.prompts/2025-12-14-auth/01-research.md`
- **Folder Path**: `.prompts/2025-12-14-auth/` (runs all `*.md` in folder sequentially by number)
- **Partial**: "auth" (finds matching folders or files)
- **Empty**: Run most recent
</input>

<process>
<step_1_parse_arguments>
Parse $ARGUMENTS to extract:
- Paths/Names
</step_1_parse_arguments>

<step_2_resolve_files>
For each argument:

1. **If Folder Path** (ends in `/` or is directory):
   - Find all `*.md` files in that directory.
   - Ignore `SUMMARY.md`.
   - Sort by filename (01, 02...).
   - Add all to execution queue.

2. **If File Path** (exists on disk):
   - Add specific file to queue.

3. **If Partial String**:
   - Find files matching string in `.prompts/` (recursive).
   - If multiple matches, ask user or pick most recent.
</step_2_resolve_files>

<step_3_preflight_check>
Before executing any prompts:

1. **Dependency Scan**: Check found prompts for `@` references to other prompts.
2. **Existence Validation**:
   - If referencing a prompt execution earlier in the queue: OK (will be created).
   - If referencing a completed file (in `.prompts/*/completed/`): OK.
   - If referencing a missing file:
     - Warn user: "Prompt 002 references 'auth-research.md' which is missing."
     - Ask: "Abort or Continue?"

   - IF the input prompts are in `trash/` folder:
     - Ask: "This prompt is already marked as completed/trashed. Re-run? (y/n)"
</step_3_preflight_check>

<step_4_execute>
<title>Execution Engine</title>

<execution_modes>
<single_prompt>
Straightforward execution of one prompt.

1. Read prompt file contents
2. Execute using `task_boundary`
3. Include in task prompt:
   - The complete prompt contents
   - Output location: `.prompts/{number}-{topic}-{purpose}/{topic}-{purpose}.md`
4. Wait for completion
5. Validate output (see validation section)
6. Archive prompt to `.prompts/trash/` (move and rename)
7. Report results with next-step options
</single_prompt>

<sequential_execution>
For chained prompts where each depends on previous output.

1. Build execution queue from dependency order
2. For each prompt in queue:
   - Read prompt file
   - Execute using `task_boundary`
   - Wait for completion
   - Validate output
   - If validation fails → stop, report failure, offer recovery options
   - If success → archive prompt, continue to next
3. Report consolidated results

<progress_reporting>
Show progress during execution:
```
Executing 1/3: 001-auth-research... ✓
Executing 2/3: 002-auth-plan... ✓
Executing 3/3: 003-auth-implement... (running)
```
</progress_reporting>
</sequential_execution>

<parallel_execution>
For independent prompts with no dependencies.
(Executed sequentially in single-threaded environments but logically parallel)

1. Read all prompt files
2. Execute each prompt sequentially using `task_boundary`
3. Wait for all to complete
4. Validate all outputs
5. Archive all prompts
6. Report consolidated results (successes and failures)

<failure_handling>
Unlike sequential, "parallel" continues even if some fail:
- Collect all results
- Archive successful prompts
- Report failures with details
- Offer to retry failed prompts
</failure_handling>
</parallel_execution>

</execution_modes>

<validation>
<output_validation>
After each prompt completes, verify success:

1. **File exists**: Check output file was created
2. **Not empty**: File has content (> 100 chars)
3. **Metadata present** (for research/plan): Check for required XML tags
   - `<confidence>`
   - `<dependencies>`
   - `<open_questions>`
   - `<assumptions>`
4. **SUMMARY.md exists**: Check SUMMARY.md was created
5. **SUMMARY.md complete**: Has required sections (Key Findings, Decisions Needed, Blockers, Next Step)
6. **One-liner is substantive**: Not generic like "Research completed"

<validation_failure>
If validation fails:
- Report what's missing
- Offer options:
  - Retry the prompt
  - Continue anyway (for non-critical issues)
  - Stop and investigate
</validation_failure>
</output_validation>
</validation>

<archiving>
<archive_timing>
- **Sequential**: Archive each prompt immediately after successful completion
- **Parallel**: Archive all at end after collecting results
</archive_timing>

<archive_operation>
1. Identify source prompt path: `SOURCE_PROMPT`
2. Determine trash destination:
   ```bash
   # Create trash if missing
   mkdir -p .prompts/trash
   
   # Extract parts
   PARENT_DIR=$(basename $(dirname "$SOURCE_PROMPT"))
   FILENAME=$(basename "$SOURCE_PROMPT")
   
   # Construct new name: parent_dir--filename
   DEST=".prompts/trash/${PARENT_DIR}--${FILENAME}"
   ```
3. Move file:
   ```bash
   mv "$SOURCE_PROMPT" "$DEST"
   ```
4. Output file stays in place (not moved).
</archive_operation>
</archiving>

<result_presentation>
<single_result>
Display the actual SUMMARY.md content inline so user sees findings without opening files.
</single_result>

<chain_result>
All prompts archived. Full summaries in .prompts/*/SUMMARY.md
</chain_result>
</result_presentation>
</step_4_execute>
</process>

<critical_notes>
- Execute prompts sequentially.
- Archive prompts only after successful completion.
- If any prompt fails, stop sequential execution and report error.
- **Robust Chaining**: Output files are NEVER moved. This allows re-running a specific step in a chain without breaking subsequent references. Future steps can always find previous outputs in their original creation location.
</critical_notes>
