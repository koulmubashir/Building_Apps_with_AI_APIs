import os
import openai
from dotenv import load_dotenv


load_dotenv()


def main_function():
    apiKey = ""
    baseUrl = ""
    print("This is the main function.") 
    input("Enter 1 for GrokAPI, 2 for OpenAI API: ")
    if  input == "1":
        apiKey = os.getenv("GROK_API_KEY")
        baseUrl = os.getenv("GROK_BASE_URL")
    elif input == "2":
        apiKey = os.getenv("OPENAI_API_KEY")
        baseUrl = "https://api.openai.com/v1"
    else:
        print("Invalid input. Please enter 1 or 2.")
        exit()
    client = openai.OpenAI(api_key=apiKey,base_url=baseUrl)
    response = client.chat.completions.create(
        model=os.getenv("GROK_MODEL"),
        messages=[
            {"role": "user", "content": "Hello, what is the capital of France?"}
        ]
    )
    print(response.choices[0].message.content)   







if __name__ == "__main__":
    main_function()
