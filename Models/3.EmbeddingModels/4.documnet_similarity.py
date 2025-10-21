from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings


load_dotenv()

def generate_embedding(text: list):
    try:
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-small", chunk_size=5, dimensions=32)
        embedding_vector = embedding_model.embed_documents(text)
        return str(embedding_vector)
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return "An error occurred while generating embeddings."


document = ["LangChain is a framework for developing applications powered by language models.",
           "LangChain helps in building applications that utilize large language models effectively.",
            "With LangChain, developers can create applications that leverage the capabilities of language models."]

if __name__ == "__main__":
    try:
        generate_embedding(document)
    except Exception as e:
        print(f"Error in main execution: {e}")



        
