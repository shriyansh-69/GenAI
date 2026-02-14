# 🩺 Medical Q&A Chatbot

A Streamlit-based Medical Question Answering Chatbot built using
TF-IDF + Cosine Similarity retrieval and basic NLP preprocessing.

--- 

## 🌐 Live Demo 

You Can Access The Medical Q&A Chatbot At This Below Link :- <br>
🔗 https://medicalchatbotapplication2.streamlit.app/

## Project Overview 

This Project Converts The MedQuAD dataset(XML) Into JSON,
Preprocess The Question Using NLP Techniques, And Retrieves 
The Most Relevant Answer Using TF-IDF Vectorization And Cosine Similarity.

The System Follows a Simple Retrieval-Based QA Architecture.

---

## How It Works

1. XML files are Converted into JSON Format
2. Questions are preprocessed Using:
   - Lowercasing
   - Regex 
   - Tokenization
   - Lemmatization(Wordnet)
3. TF-IDF Vectorization is Applied.
4. Cosine Similarity is Used to Find The Most Relevant  Question.
5. The Corresponding Answer Is Returned To The User.


---

## Tech Stack

- python 3:11
- streamlit 
- NLTLK 
- Scikit-learn
- Numpy
- Pandas

---






