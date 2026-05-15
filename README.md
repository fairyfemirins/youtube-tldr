# YouTube TL;DR

**Automatically generate TL;DR summaries for YouTube videos.**

## Problem
Users want quick summaries of long YouTube videos (tutorials, lectures, reviews) without watching the entire video. Existing tools are slow, inaccurate, or manual.

## Solution
A Flask web app that:
1. Extracts auto-generated captions from YouTube videos.
2. Summarizes the transcript using an LLM (OpenAI API or mock).
3. Returns bullet-point summaries with timestamps.

## Features
- ✅ **One-click summaries**: Paste a YouTube URL and get a TL;DR.
- ✅ **Timestamps**: Jump to key points in the video.
- ✅ **Mock mode**: Test without an OpenAI API key.
- ✅ **Error handling**: Gracefully handles missing transcripts or rate limits.

## Tech Stack
- **Backend**: Flask (Python)
- **YouTube API**: `youtube-transcript-api`
- **LLM**: OpenAI API (or mock)
- **Frontend**: HTML/CSS/JS

## Setup
1. **Clone the repo**:
   ```bash
   git clone https://github.com/femirins/youtube-tldr.git
   cd youtube-tldr
   ```

2. **Install dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   pip install -r requirements.txt
   ```

3. **Set up `.env`**:
   ```bash
   OPENAI_API_KEY=your_api_key_here  # Replace with "mock_key" for testing
   ```

4. **Run the app**:
   ```bash
   python app.py
   ```

5. **Open in browser**:
   Visit `http://127.0.0.1:5000` and paste a YouTube URL.

## Example
**Input**: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
**Output**:
```
**TL;DR Summary:**
- [00:00] Introduction to the topic.
- [02:15] Key point 1 with details.
- [05:30] Key point 2 with examples.
- [08:45] Conclusion and takeaways.
```

## Roadmap
- [ ] Add Chrome extension for one-click summaries.
- [ ] Support non-English videos.
- [ ] Add user accounts to save summaries.

## License
MIT