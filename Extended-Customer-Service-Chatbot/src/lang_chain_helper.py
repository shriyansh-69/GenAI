from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import  HuggingFaceEmbeddings

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")


llm = ChatGroq(
    api_key=os.environ["GROQ_API_KEY"],
    model="llama-3.1-8b-instant",
    temperature=0.1
)


embeddings =  HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Base Directory
base_dir =  Path(__file__).resolve().parent.parent

# Dataset Path(Relative Path)
data_path = base_dir/ "dataset" / "et.csv"

# FAISS Index Path
vectordb_file_path = base_dir/"faiss_index"



def create_vector_db():
    loader = CSVLoader(
        file_path=r"C:\Users\shriyansh\OneDrive\Desktop\GenAI-main\Extended-Customer-Service-Chatbot\dataset\et.csv",
        encoding="utf-8",
        csv_args={
            "delimiter": ",",
            "quotechar": '"'
        }
    )

    documents = loader.load()
    vectordb = FAISS.from_documents(documents, embeddings)
    vectordb.save_local(vectordb_file_path)


def get_qa_chain():
    vectordb = FAISS.load_local(
    vectordb_file_path,
    embeddings,
    allow_dangerous_deserialization=True
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    prompt = PromptTemplate(
        template="""
        Answer the question ONLY using the context below.
        If the answer is not found, say "I don't know."

        CONTEXT:
        {context}

        QUESTION:
        {question}
        """,
        input_variables=["context", "question"]
    )

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    return chain


if __name__ == "__main__":
    create_vector_db()
    chain = get_qa_chain()
    print(chain.invoke("Who are you?"))
