import streamlit as st
import requests
import time
import random


st.set_page_config(
    page_title="Money Making Machine 💰",
    page_icon="💸",
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
    .stInfo {
        color: #1E90FF;
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


st.title("💰 Money Making Machine 💰")
st.markdown("Welcome to the ultimate money-making app! Generate cash, get side hustle ideas, and stay motivated to grow your wealth. 💸")


def generate_money():
    return random.randint(1, 1000)


st.subheader("💵 Instant Cash Generator")
if st.button("Generate Money 💰"):
    with st.spinner("Counting your money..."):
        time.sleep(3)
        amount = generate_money()
        st.success(f"🎉 You made **${amount}**!")


def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return "Freelancing"  
    except:
        return "Oops! Something went wrong. Try again later."


st.subheader("💡 Side Hustle Ideas")
if st.button("Generate Hustle 💼"):
    with st.spinner("Finding the perfect hustle for you..."):
        idea = fetch_side_hustle()
        st.success(f"🚀 **{idea}**")


def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return "Money is the root of all evil!" 
    except:
        return "Oops! Something went wrong. Try again later."


st.subheader("💪 Money-Making Motivation")
if st.button("Get Inspired ✨"):
    with st.spinner("Fetching a motivational quote..."):
        quote = fetch_money_quote()
        st.info(f"💬 **{quote}**")


st.markdown("---")
st.markdown("Built with ❤️ by Sadia Batool ([GitHub](https://github.com/Pjmsadi))")