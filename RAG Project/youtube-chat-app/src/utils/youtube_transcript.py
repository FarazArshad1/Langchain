import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

def get_youtube_video_transcription(video_url):
    video_id = extract_video_id(video_url)
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=["en"])
        transcript = " ".join(chunk["text"] for chunk in transcript_list)
        return transcript
    except TranscriptsDisabled:
        return "No Caption available for this video"
    except Exception as e:
        print(e)
        return "Error Occurred"

def extract_video_id(video_url):
    if "youtu.be" in video_url:
        return video_url.split("/")[-1]
    elif "youtube.com" in video_url:
        if "watch?v=" in video_url:
            return video_url.split("watch?v=")[-1].split("&")[0]
    return None