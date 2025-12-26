# Universal Workflows Manifest
# Source of Truth for the Antigravity Kernel (Universal Workflows OS)

- name: intake
  path: universal-workflows/intake.md
  role: System Architect (Router)
  desc: Master Router. Semantically parses natural language into execution chains.

- name: visual-planner
  path: universal-workflows/kernel/visual-planner.md
  role: System Architect (Visual Planner)
  desc: Generates visual implementation maps (Mermaid) for implicit user approval.

- name: loop
  path: universal-workflows/kernel/loop.md
  role: Reliability Manager
  desc: Enforces verification loops (Run -> Verify -> Fix) for high-reliability execution.

- name: critic
  path: universal-workflows/kernel/critic.md
  role: Quality Inspector
  desc: Audits work against strict personas and quality gates.

- name: walkthrough
  path: universal-workflows/kernel/walkthrough.md
  role: Session Reporter
  desc: Generates proof-of-work summaries and walkthrough artifacts.

- name: test
  path: universal-workflows/tools/test.md
  role: QA Lead
  desc: Intelligent testing agent for Unit, Visual, and Integration tests.

- name: create-workflow
  path: universal-workflows/tools/create-workflow.md
  role: Workflow Architect
  desc: Factory for creating or updating new agent workflows.

- name: smart-commit
  path: universal-workflows/tools/smart-commit.md
  role: Release Manager
  desc: Semantic git operations with documentation sync.

- name: auto-update
  path: universal-workflows/tools/auto-update.md
  role: System Maintainer
  desc: Self-maintenance and deep-dive analysis of directory structures.

- name: create-meta-prompt
  path: universal-workflows/tools/create-meta-prompt.md
  role: Prompt Engineer
  desc: Generates optimized meta-prompts for agent delegation.

- name: run-prompt
  path: universal-workflows/tools/run-prompt.md
  role: Prompt Executor
  desc: Executes single or chained prompt files.

- name: get-feedback
  path: universal-workflows/tools/get-feedback.md
  role: Feedback Loop
  desc: Requests AI feedback on artifacts (text/visuals).

- name: ask-db
  path: universal-workflows/tools/ask-db.md
  role: Data Analyst
  desc: Natural language query interface for the project database.

- name: chain
  path: universal-workflows/tools/chain.md
  role: Chain Orchestrator
  desc: Executes multi-step prompt chains.
- name: discussion
  path: universal-workflows/tools/discussion.md
  role: Technical Consultant
  desc: Interactive consultant mode for deep technical discussion without code changes.
