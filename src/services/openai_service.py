from .config import API_KEY_OPENAI
from openai import OpenAI


client = OpenAI(api_key=API_KEY_OPENAI)

def get_response(prompt, model="gpt-4o-mini-2024-07-18"):
    input=[
        {
            "role": "system", 
            "content": "You are a trading guru. Given data on share prices over the past 3 days, write a report of no more than 150 words describing the stocks performance and recommending whether to buy, hold or sell. Use the examples provided between ### to set the style of your response."
        },
        {
            "role": "user", 
            "content": prompt
        }
    ]
    try:
        response = client.responses.create(
            model=model,
            input=input,
            temperature=1.1,
    )
        return response.output_text
    except Exception as e:
        print(f"[ERROR] Error in OpenAI API call: {e}")
        return None

