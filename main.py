import os
import openai
from dotenv import load_dotenv



print( 1 +2)
print(os.getcwd())
base_url = "https://api.x.ai/v1"
model = "grok-4-fast-reasoning"


def main_function():
    print("This is the main function.") 
    api_key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI(api_key=api_key,base_url=base_url)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": "Hello, what is the capital of France?"}
        ]
    )
    print(response.choices[0].message['content'])   


if __name__ == "__main__":
    main_function()
