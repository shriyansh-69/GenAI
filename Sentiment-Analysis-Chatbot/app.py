#  Importing The Esstinal Library
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Loading The Environment Variable
load_dotenv()

# API Key
client = Groq(os.environ("GROQ_API_KEY"))

# System Prompt
SYSTEM_PROMPT = """
You are a customer support chatbot with sentiment analysis.

For EVERY user message,  you MUST:
1. Classify sentiment as exactly one of:
   Positive, Negative, Neutral

IMPORTANT SENTIMENT RULES:
- Any dissatifaction, dislike, criticsm or negative opinion(e.g., "boring", "bad", "not good", "hate") Must Be Classified as Negative
- Neutral is ONLY for factual questions or requests with no opinion or emotion

2. Generate a response appropraite to that sentiment.

You MUST respond in EXACTLY this format:
sentiment: <Positive|Negative|Neutral>
Response: <your reply>

Response rules:
- Negative → brief apology + help (no therapy)
- Positive → bries acknowledgment 
- Neutral → clear and professional
- Keep responses to 1–2 short sentences
- Never assume memory 
- Never use emotional or dramatic language  
"""


# Streamlit Interface

st.set_page_config(page_title="Sentiment-Analysis Chatbot",layout="centered")
st.title("🤖 Emotion-Aware Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Welcome! 😊 How can I assist you today?"}
    ]

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Creating The User Input 

user_input = st.chat_input("Type Your Message.... ")

# Show And Save User Message

if user_input:
    user_input = user_input.strip()

    with st.chat_input("user"):
        st.write(user_input)

    st.session_state.messages.append(
        {"role":"user","content":user_input}
    )

    







    

