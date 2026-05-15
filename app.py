# app.py
import os
from flask import Flask, request, render_template, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Mock OpenAI API key (replace with real key in production)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "mock_key")
client = OpenAI(api_key=OPENAI_API_KEY)

# Mock LLM response for testing
MOCK_SUMMARY = """
**TL;DR Summary:**
- [00:00] Introduction to the topic.
- [02:15] Key point 1 with details.
- [05:30] Key point 2 with examples.
- [08:45] Conclusion and takeaways.
"""

def get_transcript(video_id):
    """Fetch YouTube transcript using youtube-transcript-api."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except (TranscriptsDisabled, NoTranscriptFound):
        return None

def summarize_text(text):
    """Summarize text using OpenAI API (or mock)."""
    if OPENAI_API_KEY == "mock_key":
        return MOCK_SUMMARY
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize this YouTube transcript in 5 bullet points with timestamps."},
            {"role": "user", "content": text}
        ],
        max_tokens=200
    )
    return response.choices[0].message.content

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    youtube_url = request.form.get("youtube_url")
    video_id = youtube_url.split("v=")[-1].split("&")[0]
    
    transcript = get_transcript(video_id)
    if not transcript:
        return jsonify({"error": "No transcript available for this video."}), 400
    
    summary = summarize_text(transcript)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)