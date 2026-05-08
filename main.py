from fastapi import FastAPI, UploadFile, File
import shutil
import fitz
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from openai import OpenAI

# Groq Client
client = OpenAI(
    api_key="YOUR_GROQ_API_KEY",
    base_url="https://api.groq.com/openai/v1"
)

# FastAPI app
app = FastAPI()

# Embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Global storage
chunks_store = []
index = None

@app.get("/")
def home():
    return {"message": "AI Research Assistant Running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    global chunks_store
    global index

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

    # Create embeddings
    embeddings = model.encode(chunks)

    embeddings = np.array(embeddings)

    # Create FAISS index
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    # Store embeddings
    index.add(embeddings)

    return {
        "message": f"{file.filename} uploaded successfully",
        "total_chunks": len(chunks),
        "faiss_vectors_stored": index.ntotal
    }

@app.get("/ask")
async def ask_question(question: str):

    global chunks_store
    global index

    # Convert question into embedding
    question_embedding = model.encode([question])

    question_embedding = np.array(question_embedding)

    # Search FAISS
    distances, indices = index.search(question_embedding, k=1)

    # Retrieve best chunk
    retrieved_chunk = chunks_store[indices[0][0]]

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

    # Combine all chunks
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