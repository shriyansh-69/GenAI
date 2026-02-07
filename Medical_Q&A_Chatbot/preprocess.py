# This File Is Created For Process The Word In Dataset 

import re
import nltk
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()


def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(tokens)




