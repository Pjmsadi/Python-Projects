import streamlit as st

st.title("Simple Streamlit App")

user_input = st.text_input("Enter some text:")

if st.button("Show Text"):
    st.write(f"you entered: {user_input}")