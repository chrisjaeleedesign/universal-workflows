# Universal Antigravity Workflows

This repository contains a collection of reusable workflows and prompt templates designed for Antigravity agents. These workflows are intended to be dropped into any project to provide instant, powerful agentic capabilities.

## Included Workflows

- **[Auto-Update](auto-update.md)**: Automates deep-dive analysis and documentation updates for directories.
    - Uses `auto-update/` sub-workflows.
- **[Create Meta-Prompt](create-meta-prompt.md)**: A meta-workflow for generating high-quality structured prompts for other agents.
    - Uses `create-meta-prompt/` sub-workflows.
- **[Create Workflow](create-workflow.md)**: A helper workflow to standardize the creation of new workflow files.
    - Uses `create-workflow/` sub-workflows.
- **[Get Feedback](get-feedback.md)**: Request AI feedback (Vision/Text) on any file.
- **[Run Prompt](run-prompt.md)**: A utility to execute prompts with proper context and handling.
    - Support for `single` and `chain` execution modes.
- **[Smart Commit](smart-commit.md)**: Intelligently analyze changes, auto-update docs, and generate semantic commits.
- **[Test](test.md)**: Intelligent testing agent (Logic, Quality, Workflow) with auto-scaffolding.
    - Uses `test/` sub-workflows.

## Usage

To use these workflows in a new project, simply clone this repository into your `.agent/workflows` directory:

```bash
mkdir -p .agent/workflows
git clone https://github.com/chrisjaeleedesign/universal-workflows.git .agent/workflows/universal-workflows
```

Once cloned, the workflows will be available to your Antigravity agent (e.g., via slash commands like `/create-meta-prompt`).

## Structure

```
.
├── auto-update.md
├── auto-update/
├── create-meta-prompt.md
├── create-meta-prompt/
├── create-workflow.md
├── create-workflow/
├── get-feedback.md
├── run-prompt.md
├── run-prompt/
├── smart-commit.md
├── test.md
├── test/
└── references/          # Shared patterns (Note: Prompt patterns moved to create-meta-prompt/references)
```
