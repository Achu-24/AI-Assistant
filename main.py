from fastapi import FastAPI, UploadFile, File
import shutil
import fitz
import os
from openai import OpenAI



client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# FastAPI app
app = FastAPI()

# Global storage
chunks_store = []

@app.get("/")
def home():
    return {"message": "AI-Assistant Running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    global chunks_store

    # Save uploaded PDF
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read PDF
    doc = fitz.open(file.filename)

    text = ""

    for page in doc:
        text += page.get_text()

    # Chunking
    chunk_size = 500
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    chunks_store = chunks

    return {
        "message": f"{file.filename} uploaded successfully",
        "total_chunks": len(chunks)
    }

@app.get("/ask")
async def ask_question(question: str):

    global chunks_store

    # Simple retrieval
    retrieved_chunk = " ".join(chunks_store)

    # Prompt
    prompt = f"""
Answer the question ONLY from the context below.

Context:
{retrieved_chunk}

Question:
{question}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content

        return {
            "question": question,
            "answer": answer
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/summary")
async def summarize_document():

    global chunks_store

    # Combine chunks
    document_text = " ".join(chunks_store)

    # Prompt
    prompt = f"""
Summarize the following document in simple points.

Document:
{document_text}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        summary = response.choices[0].message.content

        return {
            "summary": summary
        }

    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/quiz")
async def generate_quiz():

    global chunks_store

    # Combine chunks
    document_text = " ".join(chunks_store)

    # Prompt
    prompt = f"""
Generate 5 multiple choice questions from the document.

Return ONLY valid JSON array format.

Example format:

[
  {{
    "question": "What is Python?",
    "options": ["Language", "Database", "Browser", "OS"],
    "answer": "Language"
  }}
]

Document:
{document_text}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        quiz = response.choices[0].message.content

        return {
            "quiz": quiz
        }

    except Exception as e:
        return {
            "error": str(e)
        }