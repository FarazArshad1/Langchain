from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4o')

result = model.invoke('What is Capital of Pakistan')

print(result)