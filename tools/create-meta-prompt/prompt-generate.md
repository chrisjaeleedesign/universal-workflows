---
name: prompt-generate
description: Generation logic for create-meta-prompt. Generates the actual prompt file.
---

<role>Prompt Engineer (Generator)</role>

<input>
$ARGUMENTS: The inferred `purpose`, `topic`, and `description`.
</input>

<process>
<step_1_generate>
<title>Generate Domain Memory</title>

<load_resources>
Template: @.agent/templates/domain_memory_template.md
Plan: @.gemini/antigravity/brain/$LAST_ID/implementation_plan.md (or implementation_plan.md in current context)
Rules: @.agent/workflows/universal-workflows/tools/create-meta-prompt/references/intelligence-rules.md
</load_resources>

<construction_logic>
**Goal**: Populate `.agent/memory/active_domain_state.md` using the Template.

1.  **Section 1: Context & Strategy (The Meta-Prompt)**
    -   **Goal**: Extract from User Input + Plan.
    -   **Context**: Summarize gathered info + "Goal" from Plan.
    -   **Architecture**: Extract from "Proposed Changes" in Plan.

2.  **Section 2: Constraints & Rules**
    -   **Base**: Keep standard constraints from Template.
    -   **Add**: Any "Requirements" found in the inputs.

3.  **Section 3: Feature Backlog (The Scoreboard)**
    -   **Source**: `implementation_plan.md`.
    -   **Parsing**:
        -   Look for `#### [MODIFY]` or `#### [NEW]` lines in the Plan.
        -   Or look for a "Steps" section.
    -   **Transformation**: Convert each item into a Table Row:
        -   `| ID (P01..) | Micro-Task (File + Action) | Verification (e.g. pytest) | 🔴 | notes |`
    -   **Constraint**: If Plan is unstructured, generate "Best Guess" rows based on file list.

4.  **Section 4: Decision Log**
    -   Keep as initialized (empty).
</construction_logic>

<file_creation>
1.  **Resolve Path**:
    -   If `$ARGUMENTS` contains a path (e.g. `.agent/memory/...`), use it.
    -   Else, default to: `.agent/memory/working/active_domain_state.md`.
2.  **Read**: `.agent/templates/domain_memory_template.md`
3.  **Replace**: Fill specific placeholders (or append to sections).
4.  **Write**: Write to the resolved path (Overwriting previous state).
</file_creation>

</step_1_generate>

<step_2_present>
<title>Present Result</title>
Present the created domain state:
`Domain Memory Initialized: .agent/memory/active_domain_state.md`
</step_2_present>
</process>
