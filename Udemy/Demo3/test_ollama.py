from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

llm = init_chat_model(
    model="ollama:qwen3.6",
    temperature=0,
)

print("Before invoke")

response = llm.invoke(
    [HumanMessage(content="Say hello")]
)

print("After invoke")
print(response)