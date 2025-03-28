import streamlit as st
import requests

def fetch_joke():
    """Fetch a random joke from the API with a fallback"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=3)
        if response.status_code == 200:
            data = response.json()
            return f"{data['setup']}<br><br><strong>{data['punchline']}</strong>"
        return "No jokes available right now!"
    except:
        return "Why did the tomato turn red?<br><br><strong>Because it saw the salad dressing!</strong>"

def main():
    """Run the Streamlit joke app"""
    # Modern, minimal styling
    st.markdown("""
        <style>
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .joke-text {
            font-size: 20px;
            line-height: 1.6;
            text-align: center;
            background-color: #f9f9f9;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .button-container {
            text-align: center;
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # App content
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.header("Joke Machine 🎉")
    st.write("Click below for a dose of humor!")

    # Button and joke display
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("Get a Joke", key="joke_btn", help="Click for a laugh!"):
        with st.spinner("Loading laughter..."):
            joke = fetch_joke()
            st.markdown(f'<div class="joke-text">{joke}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown(
        '<p style="text-align: center; color: #888; font-size: 14px; margin-top: 40px;">'
        'Crafted by <a href="https://github.com/Pjmsadi" style="color: #888;">Sadia Batool</a> '
        '| Powered by Official Joke API</p>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()