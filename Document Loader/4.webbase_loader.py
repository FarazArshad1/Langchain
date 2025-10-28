from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

url = "https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421"

model = ChatOpenAI()

prompt = PromptTemplate(
    name = "Web QA prompt",
    template = "Answer the following question \n {question} from the following text - \n {text}",
    input_variables=["question", "text"],
    validate_template=True,
)

parser = StrOutputParser()

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question' : "what is the product that we are talking about and what is its price", "text" : docs[0].page_content}))