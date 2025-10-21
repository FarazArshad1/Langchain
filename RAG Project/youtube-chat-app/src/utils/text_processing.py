def split_transcript(transcript, chunk_size=1000, chunk_overlap=200):
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.create_documents([transcript])
    
    return chunks

def clean_transcript_text(transcript):
    import re
    
    # Remove any unwanted characters or formatting
    cleaned_text = re.sub(r'\s+', ' ', transcript).strip()
    return cleaned_text

def prepare_text_for_embedding(chunks):
    # This function can be expanded to include any additional processing needed for embeddings
    return [chunk.page_content for chunk in chunks]