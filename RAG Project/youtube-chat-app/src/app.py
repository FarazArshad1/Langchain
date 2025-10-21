import streamlit as st
from utils.youtube_transcript import get_youtube_video_transcription, extract_video_id
from utils.text_processing import split_transcript
from utils.vector_store import (
    create_embeddings,
    create_retriever_for_vector_store,
    generate_final_prompt,
    get_llm_response
)

st.set_page_config(page_title="YouTube Video Chat", page_icon="🎥", layout="wide")

st.title("💬 YouTube Video Chat")

# Create two columns
video_col, chat_col = st.columns([0.6, 0.4])

# URL input in the video column
with video_col:
    video_url = st.text_input("Enter YouTube Video URL:", key="video_url")
    
    if video_url:
        # Display video
        video_id = extract_video_id(video_url)
        if video_id:
            st.video(f"https://youtu.be/{video_id}")
        
        # Get transcript
        with st.spinner("Processing video transcript..."):
            transcript = get_youtube_video_transcription(video_url)
            
            if transcript == "No Caption available for this video":
                st.error("This video doesn't have captions available.")
            elif transcript == "Error Occurred":
                st.error("An error occurred while processing the video.")
            else:
                # Process transcript
                chunks = split_transcript(transcript)
                vector_store = create_embeddings(chunks)
                retriever = create_retriever_for_vector_store(vector_store)
                st.success("Video processed successfully! You can now ask questions about it.")

# Chat interface in the chat column
with chat_col:
    st.subheader("Chat about the video")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if video_url and "vector_store" in locals():
        if prompt := st.chat_input("Ask something about the video..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    final_prompt = generate_final_prompt(prompt, retriever)
                    response = get_llm_response(final_prompt)
                    st.markdown(response.content)
                    st.session_state.messages.append({"role": "assistant", "content": response.content})
    else:
        st.info("Please enter a valid YouTube URL to start chatting.")