# Universal Antigravity Workflows

This repository contains a collection of reusable workflows and prompt templates designed for Antigravity agents. These workflows are intended to be dropped into any project to provide instant, powerful agentic capabilities.

## Included Workflows

- **[Auto-Update](auto-update.md)**: Automates deep-dive analysis and documentation updates for directories.
- **[Create Meta-Prompt](create-meta-prompt.md)**: A meta-workflow for generating high-quality structured prompts for other agents.
- **[Create Workflow](create-workflow.md)**: A helper workflow to standardize the creation of new workflow files.
- **[Run Prompt](run-prompt.md)**: A utility to execute prompts with proper context and handling.

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
├── create-meta-prompt.md
├── create-workflow.md
├── run-prompt.md
└── references/          # Shared patterns, templates, and rules used by the workflows
```
