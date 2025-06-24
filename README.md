

# 🧠 Mental Health Assistant Chatbot
A simple yet powerful AI-powered mental health assistant built with:
Flask (Python web framework)
Chroma Vector Store for semantic search
HuggingFace Sentence Embeddings
Google Gemini API (via google.generativeai)

# Features
Chat interface for user interaction
Retrieves contextually relevant data from Chroma DB
Uses Gemini to generate human-like mental health responses
Lightweight and fully local vector DB (Chroma)

# 🚀 Getting Started
1. Clone the Repository
```Bash
git clone https://github.com/your-username/mental-health-assistant.git
cd mental-health-assistant
```

2. Install Dependencies
Use a virtual environment (recommended):
```Bash
pip install -r requirements.txt
```

3. Environment Variables
Create a .env file in the project root:
```Bash
GOOGLE_API_KEY=your_google_gemini_api_key
CHROMA_DB_PATH=/absolute/path/to/chroma/db
```

4. Prepare Chroma Vector DB
Make sure the Chroma DB is pre-populated with relevant mental health documents.
If the folder is empty or not found, the app will raise an error.
No ingestion script is included in this example — you must populate the DB separately using LangChain or a custom loader.

5.Run the App
``` Bash
python app.py
Visit http://localhost:5000 in your browser.
```

The assistant is designed to be calm, supportive, and mental-health focused.
All chat history is stored in-memory (not persisted).
Ensure you comply with privacy and ethical usage guidelines when deploying.

