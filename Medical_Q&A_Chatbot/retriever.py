# Description 
# This File Is For Retrieval of Answer From Our Dataset(medquad.json) For Medical Chatbot 

import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess

# Loading the Dataset 
with open("data\medquad.json","r",encoding="utf-8") as f:
    data = json.load(f)

# Preprocessing s All Question's
questions = [preprocess(item["question"]) for item in data]

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)
questions_vectorizer = vectorizer.fit_transform(questions)













