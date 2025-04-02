from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

async def get_embedding():
    embeddings = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
    result = await embeddings.aembed_query("Hello, world!")
    print(result)
    
embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result=embedding.embed_query('Islamabad is Capital of Pakistan')

print(str(result))
