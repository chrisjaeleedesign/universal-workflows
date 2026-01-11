#!/usr/bin/env python3
"""
Ask Gemini - Multimodal CLI Tool

A command-line interface for interacting with Google's Gemini models.
Supports text, images, videos, and PDFs.

Usage:
    # Text only
    python ask_gemini.py "What is 2+2?"

    # With image
    python ask_gemini.py "Describe this image" --media image.png

    # With multiple files
    python ask_gemini.py "Compare these" --media chart1.png chart2.png

    # Prompt from file
    python ask_gemini.py --file prompt.txt --media document.pdf

Uses the new google.genai SDK (not deprecated google-generativeai).
"""

import argparse
import mimetypes
import os
import sys
import time

from google import genai
from google.genai import types


def get_client() -> genai.Client:
    """Initialize and return a Gemini client."""
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)
    return genai.Client(api_key=api_key)


def upload_media(client: genai.Client, file_path: str) -> types.File:
    """
    Upload a file to Gemini and wait for processing.

    For large files (videos, long PDFs), this uploads to Google's servers
    and polls until the file is ready for use.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Uploading {file_path}...", file=sys.stderr)
    try:
        uploaded_file = client.files.upload(file=file_path)
    except Exception as e:
        print(f"Upload failed: {e}", file=sys.stderr)
        sys.exit(1)

    # Poll for processing completion (needed for videos/large files)
    print("Waiting for processing...", file=sys.stderr)
    max_wait = 120  # 2 minutes max
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


def main():
    parser = argparse.ArgumentParser(
        description="Ask Gemini (Multimodal CLI)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python ask_gemini.py "What is the capital of France?"
    python ask_gemini.py "Describe this" --media image.png
    python ask_gemini.py --file prompt.txt --media doc.pdf
    python ask_gemini.py "Compare" --media a.png b.png --model gemini-2.5-pro
        """
    )
    parser.add_argument("prompt", nargs="?", help="Text prompt to send to the model")
    parser.add_argument("--file", help="Read prompt from a text file")
    parser.add_argument("--media", nargs="+", help="Paths to media files (Images, Videos, PDFs)")
    parser.add_argument("--model", default="gemini-2.5-flash", help="Model name (default: gemini-2.5-flash)")
    parser.add_argument("--system", help="System instruction for the model")

    args = parser.parse_args()

    # 1. Prepare Prompt
    prompt_text = args.prompt
    if args.file:
        try:
            with open(args.file, 'r') as f:
                file_content = f.read().strip()
                if prompt_text:
                    prompt_text = f"{prompt_text}\n\n{file_content}"
                else:
                    prompt_text = file_content
        except Exception as e:
            print(f"Error reading prompt file: {e}", file=sys.stderr)
            sys.exit(1)

    if not prompt_text and not args.media:
        print("Error: Must provide either a prompt or media files.", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

    # 2. Setup client
    client = get_client()

    # 3. Prepare Content
    contents = []

    # Upload media if present
    if args.media:
        for media_path in args.media:
            # For small images, use Part.from_file directly
            # For large files (videos, PDFs), upload first
            file_size = os.path.getsize(media_path) if os.path.exists(media_path) else 0

            if file_size > 20 * 1024 * 1024:  # > 20MB, upload to server
                file_obj = upload_media(client, media_path)
                contents.append(file_obj)
            else:
                # Use inline Part for smaller files
                try:
                    with open(media_path, 'rb') as f:
                        media_bytes = f.read()
                    mime_type, _ = mimetypes.guess_type(media_path)
                    if not mime_type:
                        mime_type = "application/octet-stream"
                    contents.append(types.Part.from_bytes(data=media_bytes, mime_type=mime_type))
                    print(f"Loaded: {media_path}", file=sys.stderr)
                except Exception as e:
                    print(f"Error loading {media_path}: {e}", file=sys.stderr)
                    sys.exit(1)

    # Add text prompt (if any)
    if prompt_text:
        contents.append(prompt_text)

    # 4. Build config
    config = None
    if args.system:
        config = types.GenerateContentConfig(
            system_instruction=args.system,
        )

    # 5. Generate
    print(f"Generating response ({args.model})...", file=sys.stderr)
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
