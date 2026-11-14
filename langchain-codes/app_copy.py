import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load Environment Variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI API KEY not found")


model = ChatGoogleGenerativeAI(
    model = GEMINI_MODEL,
    temperature = 0.3,
    google_api_key = GEMINI_API_KEY
)

print("===========")
print("Welcome to LangChain")

question = input("Ask your question: ")

print("Generating Reponse...")

response = model.invoke(question)
print("===========")
print("AI Response")
print(response.content)