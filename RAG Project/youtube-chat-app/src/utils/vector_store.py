from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
import os

OPEN_AI_API_KEY = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0.2)

class VectorStoreManager:
    def __init__(self):
        self.vector_store = None

    def create_embeddings(self, chunks):
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.vector_store = FAISS.from_documents(documents=chunks, embedding=embeddings)

    def retrieve_similar(self, query, k=4):
        if self.vector_store is None:
            raise ValueError("Vector store is not initialized. Please create embeddings first.")
        return self.vector_store.similarity_search(query, k=k)


def create_embeddings(chunks):
    vector_manager = VectorStoreManager()
    vector_manager.create_embeddings(chunks)
    return vector_manager.vector_store

def create_retriever_for_vector_store(vector_store):
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

def get_context_from_retriever(retriever, question):
    return retriever.invoke(question)

def generate_final_prompt(question, retriever):
    context_text = get_context_from_retriever(retriever=retriever, question=question)
    
    prompt = PromptTemplate(
        template="""
        You are a helpful assistant. 
        Answer only from the provided transcript context.
        If the context is insufficient, just say you don't know.
        
        {context}
        
        Question : {question}
        """,
        input_variables=['context', 'question']
    )
    
    return prompt.invoke({"context": context_text, "question": question})

def get_llm_response(final_prompt, llm=llm):
    return llm.invoke(input=final_prompt)