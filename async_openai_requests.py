import os
import sys
import asyncio
from typing import Any
from dotenv import load_dotenv
import openai

load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

async def dispatch_openai_requests(
    messages_list: list[list[dict[str, Any]]],
    model: str,
    temperature: float,
    max_tokens: int,
    top_p: float,
) -> list[str]:
    """Dispatches requests to OpenAI API asynchronously.

    Args:
        messages_list: List of messages to be sent to OpenAI ChatCompletion API.
        model: OpenAI model to use.
        temperature: Temperature to use for the model.
        max_tokens: Maximum number of tokens to generate.
        top_p: Top p to use for the model.
    Returns:
        List of responses from OpenAI API.
    """
    async_responses = [
        openai.Completion.create(
            engine=model,
            prompt=x,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
        )
        for x in messages_list
    ]
    return await asyncio.gather(*async_responses)

if __name__ == '__main__':
    try:
        # Example messages to send to OpenAI API
        messages_list=[
            [{"role": "user", "text": "Write a rap song about asynchronous execution."}],
            [{"role": "user", "text": "Write a classical poem about asynchronous pirates."}],
        ]
        
        # OpenAI API parameters
        model = "text-davinci-002"
        temperature = 0.3
        max_tokens = 200
        top_p = 1.0

        # Send requests to OpenAI API asynchronously
        predictions = asyncio.run(
            dispatch_openai_requests(
                messages_list=messages_list,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
            )
        )

        # Print responses from OpenAI API
        for i, x in enumerate(predictions):
            print(f"Response {i}: {x['choices'][0]['text']}\n\n")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)
