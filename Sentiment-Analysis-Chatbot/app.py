import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Loadinf The Environment Variable
load_dotenv()

# API Key
client = Groq(api_key=os.environ("GROQ_API_KEY"))

# System Prompt
SYSTEM_PROMPT = """
You are a Customer support chatbot.

Your responsibilties:
- Understand   the User's Emotional tone(positive, negative, neutral)
- Respond appropriately

Rules:
- If the user is angry or frustrated, be calm, empathetic, and apologetic
- If the user is happy , be friendly and encouraging
- If the user is neutral, be clear and professional
- Keep responses short, human, and helpful
"""

# Interface Setup

st.set_page_config(page_title="Emotion-Aware Chatbot", layout="centered")
st.title("🤖 Emotion-Aware Chatbot")

if "message" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT },
        {"role": "assistant", "content": "Welcome! 😊 How can I assist you today?"}
    ]

for msg in st.session_state.message[1:]:
    with st.chat_message(msg["Role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type You Message ... ")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.message.append(
        {"role":"user","content" : user_input}
    )

    