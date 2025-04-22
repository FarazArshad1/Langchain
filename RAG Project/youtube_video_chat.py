import os

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate


OPEN_AI_API_KEY = os.environ.get("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2, api_key=OPEN_AI_API_KEY)

# 1a. Get the transcript of youtube video, using the youtube transcript api
def get_youtube_video_transcription(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id=video_id,
                                                            languages=["en"])
        
        
        transcript = " ".join(chunk["text"] for chunk in transcript_list)

        return transcript
        
    except TranscriptsDisabled:
        return "No Caption available for this video"
    
    except Exception as e:
        print(e)
        return "Error Occured"
      
# 1b. Chunk the transcript  
def split_transcript(transcript):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    chunks = splitter.create_documents([transcript])
    
    return chunks

# 1c. Create Embedding of Chunks and store in vector database(FAISS)
def create_embeddings(chunks):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = FAISS.from_documents(documents = chunks, embedding=embeddings)
    return vector_store

# 2. Create retriver for retriever store
def create_retriever_for_vector_store(vector_store):
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs = {"k":4})
    return retriever

# 3. Augmentation
def get_context_from_retriever(retriever, question):
    context = retriever.invoke(question)
    return context

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
        input_variables=['context','question']
    )

    
    final_prompt = prompt.invoke({"context": context_text, "question": question})
    
    return final_prompt
    
def get_llm_response(final_prompt, llm=llm):
    response = llm.invoke(input=final_prompt)
    return response
    
    
if __name__ == "__main__":
    
    transcript = get_youtube_video_transcription(video_id="oFfVt3S51T4")
    chunks = split_transcript(transcript=transcript)
    vector_store = create_embeddings(chunks=chunks)
    retriever = create_retriever_for_vector_store(vector_store=vector_store)
    final_prompt =generate_final_prompt(question="What is Future of Programming", retriever=retriever)
    response = get_llm_response(final_prompt=final_prompt)
    print(response.content)