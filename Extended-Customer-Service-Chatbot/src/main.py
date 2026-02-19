import streamlit as st
from lang_chain_helper import get_qa_chain, create_vector_db
from scheduler import start_scheduler

st.set_page_config(page_title="NullClass Service Chatbot", page_icon="🤖")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "start_scheduler" not in st.session_state:
    start_scheduler()
    st.session_state.scheduler_started = True


st.title("NullClass Service Chatbot 🤖")

question = st.text_input("Ask a question:")

if question.strip():
    chain = get_qa_chain()
    response = chain.invoke(question)

    st.subheader("Answer")
    st.write(response.content)
