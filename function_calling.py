import openai
import json

def get_fibonacci_number(number):
    # Function to calculate the Nth Fibonacci number
    number = int(number)
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return get_fibonacci_number(number-1) + get_fibonacci_number(number-2)
      


openai.api_key = "FILL_HERE_YOUR_API_KEY"

def run_conversation(question):
    # Step 1 Use function calling capacility to get the function and arguemnts to call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": question}],
        functions=[
            {
                "name": "get_fibonacci_number",
                "description": "Get the Nth fibonacci number",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "number": {
                            "type": "string",
                            "description": "a number representing the Fibonacci number index you want to calculate"
                        }
                    },
                    "required": ["number"],
                },
            }
        ],
        function_call="auto",
    )

    message = response["choices"][0]["message"]

    # Step 2, check if the model wants to call a function
    if message.get("function_call"):
        function_name = message["function_call"]["name"]

        # Step 3, call the function
        # Note: the JSON response from the model may not be valid JSON
        function_response = str(get_fibonacci_number(
            number=json.loads(message["function_call"]["arguments"]).get("number")
        ))

        # Step 4, send model the info on the function call and function response
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "user", "content": question},
                message,
                {
                    "role": "system",
                    "content": f'{{"function_response": "{function_response}", "function_name": "{function_name}"}}'
                }
            ],
        )
        return second_response["choices"][0]["message"]["content"]
      
if __name__ == "__main__":      
    print(run_conversation("what is the 11th fibonacci number?"))     
