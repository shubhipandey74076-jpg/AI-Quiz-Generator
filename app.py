import streamlit as st
from ai_generator import generate_quiz

st.title("🤖 AI Quiz Generator")

topic = st.text_input("Enter Quiz Topic")

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

number = st.number_input(
    "Number of Questions",
    min_value=1,
    max_value=10,
    value=5
)

if st.button("Generate Quiz"):

    if topic:
        with st.spinner("Generating quiz..."):
            quiz = generate_quiz(
                topic,
                difficulty,
                number
            )

        st.write(quiz)

    else:
        st.warning("Please enter a topic.")