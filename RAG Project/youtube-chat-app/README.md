# YouTube Chat App

## Overview
The YouTube Chat App is a Streamlit application that allows users to input a YouTube video URL and engage in a chat based on the video's content. The app fetches the transcript of the video, processes the text, and enables users to ask questions related to the video's content.

## Features
- Input a YouTube video URL to fetch the transcript.
- Chat interface to ask questions about the video.
- Contextual responses based on the video's content.

## Project Structure
```
youtube-chat-app
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── utils
│   │   ├── youtube_transcript.py  # Functions to fetch video transcripts
│   │   ├── text_processing.py      # Functions for processing transcript text
│   │   └── vector_store.py         # Management of embeddings and vector store
│   └── components
│       └── chat.py                # Chat interface component
├── requirements.txt               # List of dependencies
└── README.md                      # Documentation for the project
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd youtube-chat-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit app:
   ```
   streamlit run src/app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Enter a YouTube video URL in the input field and start chatting about the video's content.

## Dependencies
- Streamlit
- youtube-transcript-api
- langchain
- faiss-cpu (or faiss-gpu for GPU support)
- openai

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.