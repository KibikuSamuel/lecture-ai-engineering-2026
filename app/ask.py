"""Lecture 1: Script with chat history and performance metrics 
"""

import argparse
import time

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"


def ask(question: str) -> str:
    client = genai.Client(api_key=get_api_key())
    
    # Advanced Level: Measure response latency
    start_time = time.time()
    
    # Implementation Level: Use chats.create to maintain conversation history
    chat = client.chats.create(model=MODEL)
    response = chat.send_message(question)
    
    elapsed_time = time.time() - start_time
    print(f"[performance] Response time: {elapsed_time:.2f} seconds")

    if response.usage_metadata:
        print(f"[tokens] prompt: {response.usage_metadata.prompt_token_count}, output: {response.usage_metadata.candidates_token_count}")
        
    return response.text


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask questions to the LLM with chat and performance metrics")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    print(f"[model] {MODEL}")
    print(f"[質問] {args.question}\n")
    try:
        print(ask(args.question))
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()