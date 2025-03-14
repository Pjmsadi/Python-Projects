import streamlit as st
import random
import time

# Configure page settings
st.set_page_config(
    page_title="BTS ARMY Quiz 💜",
    page_icon="📝",
    layout="centered",
)

# Custom CSS styling for a clean and professional UI
st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background-color: #f5f0ff;
    }

    /* Title styling */
    h1 {
        color: #8e44ad !important;
        text-align: center;
        font-size: 2.5rem !important;
        margin-bottom: 1rem !important;
    }

    /* Subheader styling */
    h3 {
        color: #9b59b6 !important;
        margin-top: 1.5rem !important;
    }

    /* Button styling */
    .stButton button {
        background-color: #9b59b6 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 10px !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: background-color 0.3s ease !important;
    }

    .stButton button:hover {
        background-color: #8e44ad !important;
    }

    /* Radio button container */
    .stRadio > div {
        background: rgba(255, 255, 255, 0.9) !important;
        border-radius: 15px !important;
        padding: 1.5rem !important;
        margin: 1rem 0 !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
        border: 2px solid #9b59b6 !important;
    }

    /* Radio button labels */
    .stRadio label {
        font-size: 1.1rem !important;
        color: #4B0082 !important;
        padding: 0.75rem 1rem !important;
        margin: 0.5rem 0 !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
    }

    /* Hover effect for radio buttons */
    .stRadio label:hover {
        background: #f5f0ff !important;
        transform: translateX(5px);
    }

    /* Selected radio button */
    .stRadio label[data-baseweb="radio"]:has(input:checked) {
        background: #9b59b6 !important;
        color: white !important;
        font-weight: bold !important;
    }

    /* Progress bar styling */
    .stProgress > div > div > div {
        background-color: #9b59b6 !important;
    }

    /* Success and error messages */
    .stSuccess {
        color: #27ae60 !important;
        font-weight: bold;
    }

    .stError {
        color: #e74c3c !important;
        font-weight: bold;
    }

    /* Score display */
    .score-display {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }

    /* Footer styling */
    .footer {
        text-align: center;
        color: #666;
        margin-top: 2rem;
        padding: 1rem;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("📝 BTS ARMY Quiz 💜")
st.markdown(
    """
    <div style="text-align: center; color: #666; margin-bottom: 2rem;">
        Test your knowledge about BTS and see how much of a true ARMY you are! 💜
    </div>
    """,
    unsafe_allow_html=True,
)

# Quiz questions (all 10 questions)
questions = [
    {
        "question": "What does BTS stand for?",
        "options": ["Born To Sing", "Bangtan Sonyeondan", "Boys That Sing", "Be The Star"],
        "answer": "Bangtan Sonyeondan",
    },
    {
        "question": "Who is the leader of BTS?",
        "options": ["Jungkook", "Suga", "RM", "Jin"],
        "answer": "RM",
    },
    {
        "question": "What is the name of BTS's official fan club?",
        "options": ["ARMY", "BLINK", "ONCE", "EXO-L"],
        "answer": "ARMY",
    },
    {
        "question": "Which BTS song was their first to hit #1 on the Billboard Hot 100?",
        "options": ["Dynamite", "Boy With Luv", "Fake Love", "Blood Sweat & Tears"],
        "answer": "Dynamite",
    },
    {
        "question": "What is Jungkook's position in BTS?",
        "options": ["Main Vocalist", "Main Dancer", "Main Rapper", "Visual"],
        "answer": "Main Vocalist",
    },
    {
        "question": "Which BTS album includes the song 'Spring Day'?",
        "options": ["Love Yourself: Her", "You Never Walk Alone", "Map of the Soul: 7", "Wings"],
        "answer": "You Never Walk Alone",
    },
    {
        "question": "What is the name of BTS's reality show?",
        "options": ["Run BTS", "Bon Voyage", "In the SOOP", "All of the above"],
        "answer": "All of the above",
    },
    {
        "question": "Which member is known as the 'Worldwide Handsome'?",
        "options": ["V", "Jin", "Jimin", "J-Hope"],
        "answer": "Jin",
    },
    {
        "question": "What year did BTS debut?",
        "options": ["2012", "2013", "2014", "2015"],
        "answer": "2013",
    },
    {
        "question": "Which BTS song has the lyrics 'I’m the one I should love in this world'?",
        "options": ["Answer: Love Myself", "Magic Shop", "Epiphany", "Mikrokosmos"],
        "answer": "Epiphany",
    },
]

# Initialize session state
if "current_question" not in st.session_state:
    st.session_state.current_question = 0  # Start with the first question
if "score" not in st.session_state:
    st.session_state.score = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "correct_answers" not in st.session_state:
    st.session_state.correct_answers = []  # Store correct answers
if "incorrect_answers" not in st.session_state:
    st.session_state.incorrect_answers = []  # Store incorrect answers

# Display current question
question = questions[st.session_state.current_question]
st.subheader(f"❓ Question {st.session_state.current_question + 1}: {question['question']}")

# Display options with improved styling
selected_option = st.radio(
    "Choose your answer:",
    question["options"],
    key="answer"
)

# Submit button
if st.button("Submit Answer"):
    st.session_state.total_questions += 1
    
    # Check if answer is correct
    if selected_option == question["answer"]:
        st.session_state.score += 1
        st.session_state.correct_answers.append(
            f"✅ **Question {st.session_state.current_question + 1}:** You selected **{selected_option}** (Correct!)"
        )
        st.success("✅ Correct! Great job, ARMY! 💜")
        st.balloons()
    else:
        st.session_state.incorrect_answers.append(
            f"❌ **Question {st.session_state.current_question + 1}:** You selected **{selected_option}** (Correct answer: **{question['answer']}**)"
        )
        st.error(f"❌ Incorrect! The correct answer is: **{question['answer']}**")

    # Progress bar
    progress = (st.session_state.current_question + 1) / len(questions)
    st.progress(progress)

    # Move to the next question or finish quiz
    if st.session_state.current_question < len(questions) - 1:
        with st.spinner("Loading next question..."):
            time.sleep(2)
        st.session_state.current_question += 1  # Move to the next question
        st.rerun()
    else:
        st.session_state.quiz_complete = True

# Display score
st.markdown(
    f"""
    <div class="score-display">
        <h3>Your Score: {st.session_state.score}/{st.session_state.total_questions}</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Display score breakdown
if st.session_state.correct_answers or st.session_state.incorrect_answers:
    st.markdown("---")
    st.subheader("📊 Score Breakdown")
    if st.session_state.correct_answers:
        st.markdown("✅ **Correct Answers:**")
        for answer in st.session_state.correct_answers:
            st.markdown(f"- {answer}")
    if st.session_state.incorrect_answers:
        st.markdown("❌ **Incorrect Answers:**")
        for answer in st.session_state.incorrect_answers:
            st.markdown(f"- {answer}")

# Footer
st.markdown(
    """
    <div class="footer">
        Made with 💜 by a fellow ARMY | © Sadia Batool 💜
    </div>
    """,
    unsafe_allow_html=True,
)