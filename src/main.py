from config import API_KEY_OPENAI
from openai import OpenAI

client = OpenAI(api_key=API_KEY_OPENAI)

def get_response(prompt, model="gpt-4o-mini-2024-07-18"):
    input=[
        {
            "role": "system", 
            "content": "You are an expert in  stack markets"
        },
        {
            "role": "user", 
            "content": prompt
        }
    ]
    response = client.responses.create(
        model=model,
        input=input
    )

    print(response.output_text)

get_response(prompt='what was the price of apple stock at the end of 2023?')