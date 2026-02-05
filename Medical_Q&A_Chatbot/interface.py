# interface.py
# This File Is For Creating The Interface For Application To Make IT More Attractive And Interactive 

# Interface Library
import streamlit as st

# Function's From Different File's 
from entity_recognition import  extract_entities
from retriever import retrieve_answer

st.set_page_config(page_title="Medical Q&A Chatbot", layout="centered",page_icon="🩺")

st.title("🧑‍⚕️ Medical Q&A Chatbot")
st.write("Ask medical questions based on the MedQuAD Dataset.")



