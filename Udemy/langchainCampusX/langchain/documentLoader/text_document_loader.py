from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

prompt = PromptTemplate(
    template="wite a very short summary in 3 points for {doc}", input_variable=["doc"]
)

loader = TextLoader(
    "/Volumes/rohan/RohuMain/Projects/Technical/Artificial Intelligence/Trainings/aiRohanj9327/Udemy/langchainCampusX/langchain/documentLoader/cricket.txt",
    encoding="utf-8",
)

doc = loader.load()

# print(doc)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"doc": doc[0].page_content})

print(result)
