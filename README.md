# AI-Assistant 🚀

An AI-powered Assistant built using FastAPI, FAISS, Sentence Transformers, Groq LLM APIs, and Streamlit.

This project allows users to:

- Upload PDF documents
- Extract and process text
- Perform semantic search
- Ask questions from uploaded documents
- Generate AI-powered summaries
- Generate interactive quizzes
- Evaluate quiz scores
- Use Retrieval-Augmented Generation (RAG)

---

# Features 

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

## ✅ Interactive Quiz System
Automatically generates MCQs from uploaded documents.

### Quiz Features
- Multiple-choice questions
- Interactive radio buttons
- Score calculation
- Correct answer display
- Quiz evaluation

## ✅ Retrieval-Augmented Generation (RAG)
Combines vector retrieval + LLM generation for accurate contextual answers.

---

# Tech Stack 🛠️

## Backend
- FastAPI

## Frontend
- Streamlit

## AI / ML
- Sentence Transformers
- FAISS
- Groq API (LLM)

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
```

---

# API Endpoints 📌

## `GET /`
Health check endpoint.

---

## `POST /upload`
Upload PDF documents.

### Features
- Saves uploaded PDF
- Extracts text
- Creates chunks
- Generates embeddings
- Stores vectors in FAISS

---

## `GET /ask`
Ask questions from uploaded documents.

### Example
```text
What backend technologies does Hamsha know?
```

### Response
AI-generated contextual answer from uploaded PDF.

---

## `GET /summary`
Generate summary of uploaded document.

### Response
AI-generated summarized version of document.

---

## `GET /quiz`
Generate interactive MCQs from uploaded document.

# Streamlit Frontend 

The project also includes an interactive Streamlit frontend.

## Frontend Features
- Upload PDFs
- Ask AI questions
- Generate summaries
- Interactive quiz UI
- Score calculation

---

# Installation ⚙️

## 1. Clone Repository

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
pip install fastapi uvicorn python-multipart pymupdf sentence-transformers faiss-cpu numpy openai python-dotenv streamlit requests
```

---

# API Key Setup 🔑

Add your Groq API key directly inside `main.py`.

Get API key from:
https://console.groq.com/

---

# Run Backend ▶️

```bash
uvicorn main:app --reload
```

---

# Run Frontend ▶️

Open a new terminal:

```bash
streamlit run app.py
```

---

# Open Applications 🌐

## FastAPI Docs
```text
http://127.0.0.1:8000/docs
```

## Streamlit Frontend
```text
http://localhost:8501
```

---

# Example Workflow 🧪

## Step 1 — Upload PDF
Upload a PDF document.

## Step 2 — Ask Questions
Ask contextual questions from uploaded document.

## Step 3 — Generate Summary
Generate AI summary of document.

## Step 4 — Generate Quiz
Generate MCQs automatically.

## Step 5 — Submit Quiz
Select answers and calculate score.

---

# Learning Outcomes 📚

This project helped in understanding:

- FastAPI
- Streamlit
- APIs
- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector Databases
- Semantic Search
- FAISS
- Prompt Engineering
- LLM Integration
- AI System Architecture

---
# Backend deployment link:
https://ai-assistant-project-g9vp.onrender.com

# Frontend deployment link:
