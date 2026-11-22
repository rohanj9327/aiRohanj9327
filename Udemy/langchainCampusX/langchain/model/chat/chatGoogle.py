from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(override=True)

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0,
    api_key=os.getenv("GOOGLE_API_KEY"),
    thinking_budget=0,
)

result = model.invoke("What is Capital of india")

print(result.content)
