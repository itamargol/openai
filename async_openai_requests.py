import os
from dotenv import load_dotenv
import openai
import asyncio
from typing import Any
load_dotenv()


# Requires Python3.10

openai.api_key = os.environ.get("OPENAI_KEY")


async def dispatch_openai_requests(
    messages_list: list[list[dict[str,Any]]],
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
        openai.ChatCompletion.acreate(
            model=model,
            messages=x,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
        )
        for x in messages_list
    ]
    return await asyncio.gather(*async_responses)


if __name__ == '__main__':

    predictions = asyncio.run(
        dispatch_openai_requests(
            messages_list=[
                [{"role": "user", "content": "Write a rap song about asynchronous execution."}],
                [{"role": "user", "content": "Write a classical poem about asynchronous pirates."}],
            ],
            model="gpt-3.5-turbo",
            temperature=0.3,
            max_tokens=200,
            top_p=1.0,
        )
    )

    for i, x in enumerate(predictions):
        print(f"Response {i}: {x['choices'][0]['message']['content']}\n\n")
