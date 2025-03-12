import streamlit as st
import pandas as pd
import datetime
import csv
import os


st.set_page_config(
    page_title="Mood Tracker 😊",
    page_icon="📊",
    layout="centered",
)


st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stSuccess {
        color: #4CAF50;
        font-weight: bold;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #4CAF50;
    }
    .stMarkdown {
        color: #2E4053;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


MOOD_FILE = "mood_log.csv"


def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    try:
        return pd.read_csv(MOOD_FILE)
    except Exception as e:
        st.error(f"Error loading mood data: {e}")
        return pd.DataFrame(columns=["Date", "Mood"])


def save_mood_data(date, mood):
    try:
        with open(MOOD_FILE, "a") as file:
            writer = csv.writer(file)
            writer.writerow([date, mood])
        st.success("Mood logged successfully! 😊")
    except Exception as e:
        st.error(f"Error saving mood data: {e}")


st.title("😊 Mood Tracker 📊")
st.markdown("Track your mood over time and visualize your emotional trends. Reflect on your feelings and improve your well-being. 💖")


data = load_mood_data()


st.subheader("📝 Log Your Mood")
col1, col2 = st.columns(2)

with col1:
    date = st.date_input("Select Date", datetime.date.today())

with col2:
    mood = st.selectbox("How are you feeling today?", ["😊 Happy", "😢 Sad", "😠 Angry", "😐 Neutral"])

if st.button("Log Mood"):
    save_mood_data(date, mood)
    st.rerun()


if not data.empty:
    st.subheader("📈 Mood Trends Over Time")
    data["Date"] = pd.to_datetime(data["Date"])

    
    mood_over_time = data.groupby(["Date", "Mood"]).size().unstack(fill_value=0)
    st.line_chart(mood_over_time)

    
    st.subheader("📊 Mood Distribution")
    mood_counts = data["Mood"].value_counts()
    st.bar_chart(mood_counts)


st.markdown("---")
st.markdown("Built with ❤️ by Sadia Batool ([GitHub](https://github.com/Pjmsadi))")