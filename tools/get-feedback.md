---

allowed-tools: [run_command, read_url_content, task_boundary, notify_user]
---

<objective>
Analyze the provided resource (file) using Google's Gemini Pro Vision (or similar multimodal model) via the `ai_feedback.py` script and provide constructive feedback or answer specific questions about it.
</objective>

<context>
Script Location: @research/scripts/ai_feedback.py
Target Resource: $ARGUMENTS (first argument)
User Request: $ARGUMENTS (subsequent arguments)
</context>

<process>
<step_1_validate>
<title>Validate Inputs</title>
1.  **Check Arguments**:
    -   Ensure at least one argument (the resource path) is provided.
    -   If missing, ASK user: "Please provide the path to the file you want feedback on."
2.  **Verify File**:
    -   Check if the resource file exists at the given path.
    -   If not found, ERROR and EXIT.
</step_1_validate>

<step_2_optimize_prompt>
<title>Prompt Engineering</title>
1.  **Analyze Intent**:
    -   Review `Target Resource` type (Image/Video/Text).
    -   Review `User Request` (if any). If empty, assume "General detailed critique and improvement suggestions".
2.  **Draft Optimization**:
    -   Create a specialized system prompt for the AI model.
    -   *Structure*: [Role] + [Context] + [Task] + [Output Format].
    -   *Example*: "You are a senior UI/UX designer. Analyze this screenshot for visual hierarchy and accessibility..."
3.  **Review with User**:
    -   Use `notify_user` to present the drafted prompt.
    -   message: "I've prepared a prompt to get the best feedback. \n\n**Proposed Prompt:**\n{drafted_prompt}\n\nShall I proceed with this?"
    -   *Wait for User Approval*.
</step_2_optimize_prompt>

<step_3_execute>
<title>Request & Report</title>
1.  **Execute Tool**:
    -   Run: `python3 research/scripts/ai_feedback.py --media [resource_path] "[approved_prompt]"`
    -   *Note*: Ensure the prompt is properly quoted to handle newlines/spaces.
2.  **Report Results**:
    -   Display the output clearly to the user.
</step_3_execute>
</process>
