# app.py

from dotenv import load_dotenv  # type: ignore
import os
import google.generativeai as genai  # type: ignore
import streamlit as str  # Import Streamlit

# Load environment variables
load_dotenv()

# Configure API key for Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API"))

# Function to generate response using the Gemini model
def text_to_text_chatbot(question):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(question)
    return response.text

def run_chatbot_app():
    str.title("Chatbot:")

    if "messages" not in str.session_state:
        str.session_state.messages = []

    # Display chat messages
    for message in str.session_state.messages:
        with str.chat_message(message["role"]):
            str.markdown(message["content"])

    # Input from the user
    if prompt := str.chat_input("What is your question?"):
        str.session_state.messages.append({"role": "user", "content": prompt})
        with str.chat_message("user"):
            str.markdown(prompt)

        # Get response from Google Gemini
        response_text = text_to_text_chatbot(prompt)  # Call the function to get the response

        # Append the assistant's response to the messages
        str.session_state.messages.append({"role": "assistant", "content": response_text})
        with str.chat_message("assistant"):
            str.markdown(response_text)

if __name__ == "__main__":
    run_chatbot_app()