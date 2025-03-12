import streamlit as st
import random
import time


st.set_page_config(
    page_title="BTS ARMY Quiz 💜",
    page_icon="📝",
    layout="centered",
)


st.markdown(
    """
    <style>
    .stButton button {
        background-color: #FF69B4;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
    }
    .stButton button:hover {
        background-color: #FF1493;
    }
    .stRadio div {
        background-color: #F8F8FF;
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
    }
    .stSuccess {
        color: #32CD32;
        font-weight: bold;
    }
    .stError {
        color: #FF4500;
        font-weight: bold;
    }
    .stProgress > div > div > div {
        background-color: #FF69B4 !important;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #FF69B4;
    }
    .stMarkdown {
        color: #4B0082;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i.pinimg.com/originals/7a/3b/6f/7a3b6f8e9b8c1f1e8e8e8e8e8e8e8e8e.jpg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("📝 Quiz Application For BTS ARMY 💜")
st.markdown("Test your knowledge about BTS and see how much of a true ARMY you are! 💜")


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


if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
if "score" not in st.session_state:
    st.session_state.score = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "correct_answers" not in st.session_state:
    st.session_state.correct_answers = []
if "incorrect_answers" not in st.session_state:
    st.session_state.incorrect_answers = []


question = st.session_state.current_question
st.subheader(f"❓ {question['question']}")


selected_option = st.radio("Choose your answer:", question["options"], key="answer")


if st.button("Submit Answer"):
    st.session_state.total_questions += 1
    if selected_option == question["answer"]:
        st.session_state.score += 1
        st.session_state.correct_answers.append(question["question"])
        st.success("✅ Correct! Great job, ARMY! 💜")
        
        st.balloons()
    else:
        st.session_state.incorrect_answers.append(question["question"])
        st.error(f"❌ Incorrect! The correct answer is: **{question['answer']}**")

    
    progress = st.session_state.total_questions / len(questions)
    st.progress(progress)

    
    with st.spinner("Loading next question..."):
        time.sleep(2)

    
    st.session_state.current_question = random.choice(questions)
    st.rerun()


st.markdown(f"### Your Score: {st.session_state.score}/{st.session_state.total_questions}")

if st.session_state.correct_answers or st.session_state.incorrect_answers:
    st.markdown("---")
    st.subheader("📊 Score Breakdown")
    if st.session_state.correct_answers:
        st.markdown("✅ **Correct Answers:**")
        for q in st.session_state.correct_answers:
            st.markdown(f"- {q}")
    if st.session_state.incorrect_answers:
        st.markdown("❌ **Incorrect Answers:**")
        for q in st.session_state.incorrect_answers:
            st.markdown(f"- {q}")


st.markdown("---")
st.markdown("Made with 💜 by a fellow ARMY")

