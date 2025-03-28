import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

while True:  # Start an infinite loop
    user_input = input("Enter your message (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':  # Check if the user wants to exit
        break  # Exit the loop

    response = model.generate_content(user_input)
    print(response.text)