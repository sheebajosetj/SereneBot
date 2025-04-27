from flask import Flask, render_template, request
import os
import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set.")


genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # 2.0 may not be available in SDK yet

# Vector DB Setup
db_path = os.getenv("CHROMA_DB_PATH")
embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

if not os.path.exists(db_path) or not os.listdir(db_path):
    raise Exception("Chroma DB not found or empty. Please populate it before running the app.")

vector_db = Chroma(persist_directory=db_path, embedding_function=embedding_model)

# Store chat history in memory
chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    global chat_history
    if request.method == "POST":
        user_msg = request.form.get("message")
        if user_msg:
            chat_history.append({"sender": "user", "text": user_msg})

            # === Retrieve Relevant Context from Chroma Vector DB ===
            docs = vector_db.similarity_search(user_msg, k=3)
            context = "\n".join([doc.page_content for doc in docs])

            # === Build Prompt and Call Gemini ===
            prompt = f"""You are a helpful and calming mental health assistant. Use the following context to answer:

Context:
{context}

User Question:
{user_msg}
"""

            response = model.generate_content(prompt)
            reply = response.text.strip()

            chat_history.append({"sender": "bot", "text": reply})

    return render_template("index.html", messages=chat_history)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", threaded=True)
