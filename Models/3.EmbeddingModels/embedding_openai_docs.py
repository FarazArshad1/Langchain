from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

document = [
    'Things chnage over time',
    'So how is your work going on?'
    'Time is moving at fast pace, so hurry up!'
]

    
embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result=embedding.embed_documents(document)

print(str(result))
