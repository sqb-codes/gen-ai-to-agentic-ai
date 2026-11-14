import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

generation_config = {
    'max_output_tokens': 1000,
    'thinking_level': 'medium',
}

while True:
    user_input = input("Enter your query: ")

    response = client.interactions.create(
        model = "gemini-3.5-flash-lite",
        input = user_input,
        generation_config=generation_config,
    )
    print("==== GEMINI ====")
    print(response.output_text)