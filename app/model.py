import joblib
from app.preprocessing import clean_text

MODEL_PATH ="models/sentiment_svm.pkl"
VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
tfidf = joblib.load(VECTORIZER_PATH)

def predict_sentiment(review):
    cleaned_review = clean_text(review)

    review_tfidf = tfidf.transform([cleaned_review])

    prediction = model.predict(review_tfidf)[0]

    if prediction == 1:
        return 'Positive'
    else:
        return 'Negative'