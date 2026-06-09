Amazon Review Sentiment Analysis
📌 Project Overview

This project is a Machine Learning and Natural Language Processing (NLP) application that analyzes Amazon product reviews and classifies them into:

🟢 Positive
🔵 Neutral
🔴 Negative

The model is trained on the Amazon Fine Food Reviews dataset and deployed using Streamlit for real-time sentiment prediction.

🚀 Features
Text preprocessing and cleaning
Stopword removal using NLTK
TF-IDF feature extraction
Logistic Regression classifier
Real-time sentiment prediction
Interactive Streamlit web application

📊 Dataset

Dataset: Amazon Fine Food Reviews Dataset

Over 500,000 customer reviews
Ratings from 1 to 5 stars
Reviews collected over multiple years

Sentiment Labels
Rating	Sentiment
4–5 Stars	Positive
3 Stars	Neutral
1–2 Stars	Negative

🛠️ Technologies Used
Python
Pandas
NumPy
NLTK
Scikit-learn
TF-IDF Vectorization
Logistic Regression
Matplotlib
Seaborn
WordCloud
Streamlit

📈 Machine Learning Pipeline
Data Collection
Data Cleaning
Sentiment Label Creation
Exploratory Data Analysis
TF-IDF Vectorization
Train-Test Split
Logistic Regression Training
Model Evaluation
Model Serialization using Pickle
Streamlit Deployment

📉 Model Performance
Accuracy: 84.36%

Evaluation Metrics:
Accuracy Score
Precision
Recall
F1 Score
Confusion Matrix

The model performs well on Positive and Negative reviews and reasonably well on Neutral reviews.

📂 Project Structure
Sentiment_Analysis_Amazon_Reviews/
│
├── app.py
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
└── food reviews.ipynb

▶️ Running the Application

Install dependencies:
pip install -r requirements.txt

Run Streamlit:
streamlit run app.py