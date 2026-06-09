import streamlit as st
import pickle
import re
from nltk.corpus import stopwords

# Load model and vectorizer
model = pickle.load(open('sentiment_model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    words = text.split()
    words = [word for word in words if word not in stop_words]

    return " ".join(words)

st.title("Amazon Review Sentiment Analysis")

review = st.text_area("Enter a Review")

if st.button("Predict"):

    cleaned_review = clean_text(review)

    review_vector = tfidf.transform([cleaned_review])

    prediction = model.predict(review_vector)[0]

    if prediction == "Positive":
        st.success("🟢 Positive Review")

    elif prediction == "Negative":
        st.error("🔴 Negative Review")

    else:
        st.info("🔵 Neutral Review")