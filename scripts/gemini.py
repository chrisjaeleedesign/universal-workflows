#!/usr/bin/env python3
"""
Gemini CLI - Unified multimodal interface for Google's Gemini models.

Supports text, images, videos, PDFs with optional task modes for common use cases.
Loads GEMINI_API_KEY from scripts/.env for portability.

Usage:
    # Basic usage
    python gemini.py "What is 2+2?"
    python gemini.py "Describe this" --media image.png

    # Task modes
    python gemini.py --mode critique --media design.png
    python gemini.py --mode summarize --media document.pdf
    python gemini.py --mode explain --media diagram.png "what does this show?"

    # List available modes
    python gemini.py --list-modes

## References (for agents)

Gemini 3 Docs: https://ai.google.dev/gemini-api/docs/gemini-3
Prompting Best Practices: https://ai.google.dev/gemini-api/docs/gemini-3#prompting_best_practices

Key principles:
- Be concise and direct (Gemini 3 responds best to clear instructions)
- Avoid over-engineering (model may over-analyze verbose prompts)
- Position specific asks after context data
- Keep temperature at 1.0 for complex reasoning tasks
"""

import argparse
import mimetypes
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load .env from scripts directory (self-contained)
SCRIPT_DIR = Path(__file__).parent
load_dotenv(SCRIPT_DIR / ".env")

# Default model: Gemini 3 Flash
DEFAULT_MODEL = "gemini-3-flash-preview"

# Task modes: light hints appended to prompts (direct, per Gemini 3 best practices)
MODES = {
    "critique": {
        "hint": "Analyze what works well and what needs improvement. Provide specific, actionable suggestions. Be direct.",
        "default_prompt": "Review this and share your thoughts.",
    },
    "summarize": {
        "hint": "Extract the key points and main takeaways. Be concise. Prioritize the most important information.",
        "default_prompt": "Summarize this.",
    },
    "explain": {
        "hint": "Break this down step by step. Clarify any complex concepts. Use examples if helpful.",
        "default_prompt": "Explain this.",
    },
    "compare": {
        "hint": "Identify similarities and differences. Organize findings clearly. Highlight what matters most.",
        "default_prompt": "Compare these.",
    },
    "other": {
        "hint": None,  # No hint - full user control
        "default_prompt": None,
    },
}


def get_client() -> genai.Client:
    """Initialize and return a Gemini client."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.", file=sys.stderr)
        print(f"Hint: Add it to {SCRIPT_DIR / '.env'}", file=sys.stderr)
        sys.exit(1)
    return genai.Client(api_key=api_key)


def upload_media(client: genai.Client, file_path: str) -> types.File:
    """Upload a file to Gemini and wait for processing."""
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Uploading {file_path}...", file=sys.stderr)
    try:
        uploaded_file = client.files.upload(file=file_path)
    except Exception as e:
        print(f"Upload failed: {e}", file=sys.stderr)
        sys.exit(1)

    # Poll for processing completion
    print("Waiting for processing...", file=sys.stderr)
    max_wait = 120
    waited = 0

    while uploaded_file.state.name == "PROCESSING" and waited < max_wait:
        time.sleep(2)
        waited += 2
        uploaded_file = client.files.get(name=uploaded_file.name)

    if uploaded_file.state.name == "FAILED":
        print("Error: File processing failed.", file=sys.stderr)
        sys.exit(1)

    if uploaded_file.state.name == "PROCESSING":
        print("Warning: File still processing, proceeding anyway...", file=sys.stderr)

    print(f"Ready: {uploaded_file.display_name or uploaded_file.name}", file=sys.stderr)
    return uploaded_file


def build_prompt(user_prompt: str, mode: str | None) -> str:
    """Combine user prompt with optional mode hint."""
    if not mode or mode not in MODES:
        return user_prompt
    hint = MODES[mode].get("hint")
    if not hint:  # "other" mode or no hint
        return user_prompt
    return f"{user_prompt}\n\n{hint}"


def list_modes():
    """Print available modes and exit."""
    print("Available task modes:\n")
    for name, config in MODES.items():
        hint = config.get("hint") or "(no hint - full user control)"
        default = config.get("default_prompt") or "(requires user prompt)"
        print(f"  {name}")
        print(f"    Hint: {hint}")
        print(f"    Default prompt: {default}")
        print()
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Gemini CLI - Unified multimodal interface",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python gemini.py "What is 2+2?"
    python gemini.py "Describe this" --media image.png
    python gemini.py --mode critique --media design.png
    python gemini.py --mode summarize --media document.pdf
    python gemini.py --list-modes

References:
    Gemini 3 Docs: https://ai.google.dev/gemini-api/docs/gemini-3
    Prompting: https://ai.google.dev/gemini-api/docs/gemini-3#prompting_best_practices
        """,
    )
    parser.add_argument("prompt", nargs="?", help="Text prompt to send to the model")
    parser.add_argument("--file", help="Read prompt from a text file")
    parser.add_argument(
        "--media", nargs="+", help="Paths to media files (Images, Videos, PDFs)"
    )
    parser.add_argument(
        "--model", default=DEFAULT_MODEL, help=f"Model name (default: {DEFAULT_MODEL})"
    )
    parser.add_argument("--system", help="System instruction for the model")
    parser.add_argument(
        "--mode",
        choices=list(MODES.keys()),
        help="Task mode: critique, summarize, explain, compare, other",
    )
    parser.add_argument(
        "--list-modes", action="store_true", help="Show available modes and exit"
    )

    args = parser.parse_args()

    # Handle --list-modes
    if args.list_modes:
        list_modes()

    # 1. Prepare Prompt
    prompt_text = args.prompt

    # Read from file if specified
    if args.file:
        try:
            with open(args.file, "r") as f:
                file_content = f.read().strip()
                if prompt_text:
                    prompt_text = f"{prompt_text}\n\n{file_content}"
                else:
                    prompt_text = file_content
        except Exception as e:
            print(f"Error reading prompt file: {e}", file=sys.stderr)
            sys.exit(1)

    # If mode specified but no prompt, use mode's default_prompt
    if not prompt_text and args.mode:
        default_prompt = MODES[args.mode].get("default_prompt")
        if default_prompt:
            prompt_text = default_prompt
        elif args.mode == "other":
            print("Error: 'other' mode requires a user prompt.", file=sys.stderr)
            sys.exit(1)

    # Validate we have something to work with
    if not prompt_text and not args.media:
        print("Error: Must provide either a prompt or media files.", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

    # Apply mode hint to prompt
    if prompt_text:
        prompt_text = build_prompt(prompt_text, args.mode)

    # 2. Setup client
    client = get_client()

    # 3. Prepare Content
    contents = []

    # Upload/load media if present
    if args.media:
        for media_path in args.media:
            file_size = os.path.getsize(media_path) if os.path.exists(media_path) else 0

            if file_size > 20 * 1024 * 1024:  # > 20MB
                file_obj = upload_media(client, media_path)
                contents.append(file_obj)
            else:
                try:
                    with open(media_path, "rb") as f:
                        media_bytes = f.read()
                    mime_type, _ = mimetypes.guess_type(media_path)
                    if not mime_type:
                        mime_type = "application/octet-stream"
                    contents.append(
                        types.Part.from_bytes(data=media_bytes, mime_type=mime_type)
                    )
                    print(f"Loaded: {media_path}", file=sys.stderr)
                except Exception as e:
                    print(f"Error loading {media_path}: {e}", file=sys.stderr)
                    sys.exit(1)

    # Add text prompt
    if prompt_text:
        contents.append(prompt_text)

    # 4. Build config
    config = None
    if args.system:
        config = types.GenerateContentConfig(
            system_instruction=args.system,
        )

    # 5. Generate
    mode_info = f" [{args.mode}]" if args.mode else ""
    print(f"Generating response{mode_info} ({args.model})...", file=sys.stderr)
    try:
        response = client.models.generate_content(
            model=args.model,
            contents=contents,
            config=config,
        )
        print(response.text)
    except Exception as e:
        print(f"Generation failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
