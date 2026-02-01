# 🤖 Emotion-Aware Chatbot

An Emotion-Aware Chatbot that detects user sentiment (Positive, Negative, or Neutral) and responds appropriately using a Streamlit web interface and an LLM (Groq – LLaMA 3.1).

---

## 📌 Project Overview

This project integrates sentiment analysis into a chatbot to understand customer emotions and adapt responses accordingly.  
The chatbot classifies sentiment and generates short, professional replies to improve customer interaction and satisfaction.

---

## 🎯 Objectives

- Detect user sentiment accurately  
- Respond appropriately based on emotion  
- Improve customer satisfaction  

---

## ✨ Features

- Sentiment classification: Positive / Negative / Neutral  
- Short, professional responses (1–2 sentences)  
- Visual sentiment indicator (badge)  
- Rule-based overrides for fixed questions  
- Interactive Streamlit chat interface  
- Secure API key handling using `.env`

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- Groq LLM (LLaMA 3.1)  
- python-dotenv  

---

## 📂 Project Structure

Sentiment-Analysis-Chatbot/
│
├── app.py # Main Streamlit chatbot application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .env # API key configuration (not committed)
├── .gitignore # Git ignore rules
└── venv/ # Virtual environment
