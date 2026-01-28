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

