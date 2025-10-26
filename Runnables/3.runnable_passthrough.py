from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

passthrough = RunnablePassthrough()

result = passthrough.invoke({"name": "Faraz Arshad"})

print(result)
