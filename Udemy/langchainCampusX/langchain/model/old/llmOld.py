import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),  # or OPENROUTER_API_KEY
    base_url="https://openrouter.ai/api/v1",
)

response = llm.invoke("What is the capital of France?")
print(response.content)
