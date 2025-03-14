import streamlit as st
import random
import string

# Function to generate a password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Always include letters

    if use_digits:
        characters += string.digits  # Add digits if selected

    if use_special:
        characters += string.punctuation  # Add special characters if selected

    # Generate password using random choices
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit app
st.set_page_config(page_title="Password Generator", page_icon="🔒")

# Title and description
st.title("🔒 Password Generator")
st.write("Generate strong and secure passwords with ease!")

# Sidebar for additional options
with st.sidebar:
    st.header("Settings")
    length = st.slider("Select password length", min_value=6, max_value=32, value=12)
    use_digits = st.checkbox("Include digits (0-9)", value=True)
    use_special = st.checkbox("Include special characters (!@#$%^&*)", value=True)

# Generate password button
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success("Your password has been generated successfully!")
    st.code(password, language="plaintext")  # Display password in a code block

# Additional features
st.write("### Tips for a Strong Password:")
st.write("- Use a mix of uppercase and lowercase letters.")
st.write("- Include numbers and special characters.")
st.write("- Avoid using easily guessable information like birthdays or names.")

# Footer
st.write("---")
st.write("Built with ❤️ by [Sadia Batool](https://github.com/Pjmsadi)")
st.write("For more projects, visit my [GitHub](https://github.com/Pjmsadi).")