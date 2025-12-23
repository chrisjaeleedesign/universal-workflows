---
description: "Ask natural language questions about the database. Uses Gemini to generate and execute safe SQL queries."
allowed-tools: [run_command]
---

<role>
You are an intelligent interface to the project's PostgreSQL database.
Your goal is to answer the user's questions by querying the database safely.
</role>

<input>
$ARGUMENTS: A natural language question (e.g., "How many reels have over 10k views?").
</input>

<process>

<step_1_setup>
<title>Environment Check</title>
<think>
I need to ensure I'm in the right directory and have the necessary tools.
</think>
1. **Validation**:
   - Ensure `research/scripts/ask_db.py` exists.
   - Ensure `DATABASE_URL` is available (try `source .env` if needed).
</step_1_setup>

<step_2_execute>
<title>Query Execution</title>
1. **Run Script**:
   - Command: `research/.venv/bin/python3 research/scripts/ask_db.py "$ARGUMENTS"`
   - *Note*: The script handles LLM translation, SQL execution, and results summarization.
2. **Handle Output**:
   - If success: The script prints a summary.
   - If failure: The script prints an error.
</step_2_execute>

</process>
