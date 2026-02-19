import streamlit as st
from lang_chain_helper import get_qa_chain, create_vector_db
from scheduler import start_scheduler


if "start_scheduler" not in st.session_state:
    start_scheduler()
    st.session_state.scheduler_started = True


st.set_page_config(page_title="Customer Service Chatbot", page_icon="🤖")
st.title("Customer Service Chatbot 🤖")



question = st.text_input("Ask a question:")

if question.strip():
    chain = get_qa_chain()
    response = chain.invoke(question)

    st.subheader("Answer")
    st.write(response.content)
