from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate

# Chat Template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history')
    ('human', '{query}'),
])

# Load Chat History
chat_history = []

with open('chat_history.txt') as f:
    chat_history.extend(f.readline())

# Create prompt
