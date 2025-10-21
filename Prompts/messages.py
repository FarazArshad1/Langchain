from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?"),
    # AIMessage(content="The capital of France is Paris.")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

from pprint import pprint
pprint(messages)

