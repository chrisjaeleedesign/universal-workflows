---
description: Verify visual assets against brand guidelines using AI Vision.
---

<role>QA Engineer (Visual)</role>

<input>
$ARGUMENTS: Path to image or visual asset.
</input>

<context>
Standards: @.agent/workflows/commands/universal-workflows/tools/test/standards.md
Feedback Workflow: @.agent/workflows/commands/universal-workflows/tools/get-feedback.md
Brand Playbook: @research/knowledge/iris_studio_brand_playbook.md
</context>

<process>
<step_1_verify>
<title>Visual Audit</title>
1.  **Delegate**:
    -   Call `view_file` on `.agent/workflows/commands/universal-workflows/tools/get-feedback.md`.
    -   Run feedback workflow on the target image.
    -   **Prompt**: "Critique this against the Iris Studio Brand Playbook. Focus on Data-Ink ratio and Semantic Titles."
</step_1_verify>

<step_2_report>
<title>Result</title>
1.  **Output**: Display the AI's critique.
</step_2_report>
</process>
