# Description 
# This File Is For Retrieval of Answer From Our Dataset(medquad.json) For Medical Chatbot 

import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess

# Loading the Dataset 
with open("data/medquad.json","r",encoding="utf-8") as f:
    data = json.load(f)

# Preprocessing s All Question's
questions = [preprocess(item["question"]) for item in data]

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2)
)

questions_vectorizer = vectorizer.fit_transform(questions)


def retrieve_answer(query: str) -> str:
    """
    Retrieve the most Revelant Answer From Our Dataset
    using TF-IDF and cosine similarity.
    """

    # Preprocess User Query To Cut The Word To It's Base Form
    query_processed = preprocess(query)

    # Vectorize Query 
    query_vector = vectorizer.transform([query_processed])

    # Similarity  Measurement To Know The Similar The Vectories Are 
    similarties = cosine_similarity(query_vector, questions_vectorizer)[0]

    # Get Best Matching Answer 
    best_answer = similarties.argmax()

    return data[best_answer]["answer"]

    












