# Universal Antigravity Workflows (Workflow OS v2.0)

This repository contains the **Workflow Operating System**, a layered architecture for high-performance agentic workflows. It is designed to replace "scripts" with robust "protocols."

## Architecture: Hub & Tools

The system follows a strict **Hub-and-Spoke** model to ensure every action is routed through a safety kernel.

```mermaid
graph TD
  Start[User Request] --> Hub["/intake (The Hub)"]
  
  subgraph Kernel [Layer 1: The Kernel (OS)]
    Plan["/plan (The Architect)"]
    Critic["/critic (The Inspector)"]
    Loop["/loop (The Manager)"]
    Report["/walkthrough (The Reporter)"]
  end
  
  subgraph Tools [Layer 2: The Tools (Capabilities)]
    Test["/test (QA)"]
    Write["/write-copy (Content)"]
    Git["/smart-commit (Ops)"]
    Flow["/create-workflow (Meta)"]
  end
  
  Hub --> Plan
  Plan --> Loop
  Loop --> Tools
  Loop --> Critic
  Tools --> Report
```

### 1. The Hub (Entry Point)
-   **[`intake.md`](intake.md)**: The Master Router. Always start here. It parses natural language (e.g., "Draft a blog") into a structured execution chain.

### 2. The Kernel (Universal Infrastructure)
These workflows provide the "Consciousness" to the agents.
-   **[`kernel/plan.md`](kernel/plan.md)**: **The Architect**. Generates a visual Mermaid flowchart of the proposed work. *Constraint*: Explicit User Approval required to proceed.
-   **[`kernel/critic.md`](kernel/critic.md)**: **The Inspector**. A "Brutally Honest Coach" that audits work against strict personas (e.g., "Security Expert", "Brand Manager").
-   **[`kernel/loop.md`](kernel/loop.md)**: **The Manager**. The Reliability Engine. It wraps execution in a retry loop:
    1.  **Execute**: Run the tool.
    2.  **Verify**: Run `tools/test.md` (Auto-Correction).
    3.  **Validate**: Ask User/Critic for approval.
-   **[`kernel/walkthrough.md`](kernel/walkthrough.md)**: **The Reporter**. Automatically generates a `walkthrough` artifact at the end of every session as "Proof of Work."

### 3. The Tools (Capabilities)
Located in `tools/`, these are the "Specialist Workers."
-   **[`tools/test.md`](tools/test.md)**: Intelligent testing (Unit, Visual, Workflow).
-   **[`tools/create-workflow.md`](tools/create-workflow.md)**: Factory for new agents.
-   **[`tools/smart-commit.md`](tools/smart-commit.md)**: Semantic git operations.
-   **[`tools/auto-update.md`](tools/auto-update.md)**: Self-maintenance.
-   **[`tools/create-meta-prompt.md`](tools/create-meta-prompt.md)**: Prompt engineering.

---

## Protocols: The Golden Path

When you use the Hub (`/intake`), the system enforces the **Golden Path** protocol. This prevents "Cowboy Coding" and ensures every task meets high standards.

### The Protocol Sequence
1.  **Phase 1: Safety (Planning)**
    -   Agent calls `/plan`.
    -   **Output**: `implementation_plan.md` with Visual Flowchart.
    -   **Gate**: User must click "Approve."
2.  **Phase 2: Reliability (Execution)**
    -   Agent calls `/loop`.
    -   **Loop Logic**:
        -   `Run Tool` -> `Run Tests` -> `Audit Result`.
        -   If any step fails, the agent **Self-Corrects** and retries.
3.  **Phase 3: Visibility (Reporting)**
    -   Agent calls `/walkthrough`.
    -   **Output**: A `walkthrough` artifact summarizing valid changes.

### Usage
To use the OS, simply invoke the Hub:

```bash
/intake "Fix the login bug on the beta branch"
```

The system will:
1.  **Plan** the fix (Show you the flowchart).
2.  **Loop** the fix (Run tests, fix bugs, audit code).
3.  **Report** the fix (Give you a walkthrough).
