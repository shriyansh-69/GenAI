# Description 
# This File Is For Retrieval of Answer From Our Dataset(medquad.json) For Medical Chatbot 

import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import preprocess


with open("data\medquad.json","r",encoding="utf-8") as f:
    data = json.load(f)



    
