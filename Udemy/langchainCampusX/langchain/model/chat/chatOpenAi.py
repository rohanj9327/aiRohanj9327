from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

model = ChatOpenAI(model="gpt-5-mini")

result = model.invoke("Capital of india")

print(result.content)