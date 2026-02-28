# 🤖 AI Resume Screening & Candidate Ranking System

An AI-powered Resume Screening System that ranks multiple resumes against a job description using semantic similarity and skill-based weighted scoring.

## 🚀 Features

- PDF Resume Text Extraction
- NLP Preprocessing using NLTK
- Semantic Similarity using Sentence Transformers
- Skill-based Weighted Scoring
- Experience Bonus Scoring
- Automatic Shortlisting
- CSV Export
- Streamlit Web Interface

## 🧠 Scoring Logic

Final Score =  
60% Semantic Similarity  
30% Skill Match Score  
10% Experience Bonus  

## 🛠 Tech Stack

- Python
- Sentence Transformers
- Scikit-learn
- NLTK
- Streamlit
- PyTorch

## ▶ Run Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py