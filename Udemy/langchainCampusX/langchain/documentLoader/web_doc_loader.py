from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

loader = WebBaseLoader(
    "https://huggingface.co/models?pipeline_tag=text-to-image&sort=trending"
)

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

parser = JsonOutputParser()

template = PromptTemplate(
    template="list availaible models from below {data}", input_variables=["data"]
)

chain = template | model | parser
result = chain.invoke({"data": loader.load()})
# print(loader.load())

print(result)
