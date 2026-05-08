import streamlit as st
import requests
import json

st.set_page_config(
    page_title="AI-Assistant",
    page_icon="🚀",
    layout="centered"
)

st.title("AI-Assistant 🚀")

# Upload PDF
st.header("Upload PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    response = requests.post(
        "https://ai-assistant-2-qgue.onrender.com/upload",
        files={
            "file": (
                uploaded_file.name,
                uploaded_file,
                "application/pdf"
            )
        }
    )

    data = response.json()

    if "message" in data:
        st.success("PDF Uploaded Successfully ✅")
    else:
        st.error(data["error"])

# Ask Questions
st.header("Ask Questions")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask AI"):

    response = requests.get(
        "https://ai-assistant-2-qgue.onrender.com/ask",
        params={
            "question": question
        }
    )

    data = response.json()

    st.subheader("AI Answer")

    if "answer" in data:
        st.success(data["answer"])
    else:
        st.error(data["error"])

# Generate Summary
st.header("Document Summary")

if st.button("Generate Summary"):

    response = requests.get(
        "https://ai-assistant-2-qgue.onrender.com/summary"
    )

    data = response.json()

    st.subheader("Summary")

    if "summary" in data:
        st.info(data["summary"])
    else:
        st.error(data["error"])

# Interactive Quiz
st.header("Interactive Quiz")

if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None

if st.button("Generate Quiz"):

    response = requests.get(
        "https://ai-assistant-2-qgue.onrender.com/quiz"
    )

    data = response.json()

    if "quiz" in data:
        st.session_state.quiz_data = json.loads(data["quiz"])
    else:
        st.error(data["error"])

if st.session_state.quiz_data is not None:

    score = 0

    user_answers = []

    for i, quiz in enumerate(st.session_state.quiz_data):

        st.subheader(f"Q{i+1}. {quiz['question']}")

        selected = st.radio(
            "Choose your answer:",
            quiz["options"],
            index=None,
            key=f"quiz_{i}"
        )

        user_answers.append(selected)

    if st.button("Submit Quiz"):

        unanswered = []

        for i, answer in enumerate(user_answers):

            if answer is None:
                unanswered.append(i + 1)

        if unanswered:

            st.warning(
                f"Please answer all questions: {unanswered}"
            )

        else:

            for i, quiz in enumerate(st.session_state.quiz_data):

                if user_answers[i] == quiz["answer"]:
                    score += 1

            st.success(
                f"Your Score: {score}/{len(st.session_state.quiz_data)}"
            )

            if score >= 4:
                st.balloons()

            st.subheader("Correct Answers")

            for i, quiz in enumerate(st.session_state.quiz_data):

                st.write(
                    f"Q{i+1}: {quiz['answer']}"
                )