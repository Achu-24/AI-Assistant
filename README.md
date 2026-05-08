# AI Research Assistant 🚀

An AI-powered Research Assistant built using FastAPI, FAISS, Sentence Transformers, and LLM APIs.

This project allows users to:

- Upload PDF documents
- Extract and process text
- Perform semantic search
- Ask questions from uploaded documents
- Generate AI-powered summaries
- Use Retrieval-Augmented Generation (RAG)

---

# Features ✨

## ✅ PDF Upload
Upload PDF documents through FastAPI endpoints.

## ✅ Text Extraction
Extracts text from PDFs using PyMuPDF (`fitz`).

## ✅ Chunking
Splits large documents into smaller chunks for efficient retrieval.

## ✅ Embeddings
Converts text chunks into vector embeddings using Sentence Transformers.

## ✅ Vector Database
Stores embeddings using FAISS for semantic similarity search.

## ✅ Question Answering
Users can ask questions related to uploaded documents.

## ✅ AI Summarization
Generates concise summaries using LLM APIs.

## ✅ Retrieval-Augmented Generation (RAG)
Combines vector retrieval + LLM generation for accurate contextual answers.

---

# Tech Stack 🛠️

## Backend
- FastAPI

## AI / ML
- Sentence Transformers
- FAISS
- LLM APIs (Groq/OpenAI Compatible)

## PDF Processing
- PyMuPDF (`fitz`)

## Language
- Python

---

# Project Architecture 🧠

```text
PDF Upload
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
FAISS Vector Storage
↓
Semantic Retrieval
↓
LLM Generation
↓
Final AI Response


# How to Run the Project ▶️

## 1. Clone the Repository

```bash
git clone <https://github.com/Achu-24/AI-Assistant.git>
cd AI-Assistant
```

---

## 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows
```bash
venv\Scripts\activate
```

#### Mac/Linux
```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install fastapi uvicorn python-multipart pymupdf sentence-transformers faiss-cpu numpy openai python-dotenv
```

---

## 4. Create `.env` File

Create a file named:

```text
.env
```

Add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

Get API Key from:
https://console.groq.com/

---

## 5. Run FastAPI Server

```bash
uvicorn main:app --reload
```

---

## 6. Open Swagger Docs

Visit:

```text
http://127.0.0.1:8000/docs
```

---

## 7. Use the APIs

### Upload PDF
Use:
```text
POST /upload
```

### Ask Questions
Use:
```text
GET /ask
```

Example:
```text
What are Hamsha's technical skills?
```

### Generate Summary
Use:
```text
GET /summary
```