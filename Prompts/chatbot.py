from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input('You : ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    
    result = model.invoke(user_input)
    chat_history.append(AIMessage(content=user_input))
    # chat_history.append(result.content)
    print(f"AI : {result.content}")