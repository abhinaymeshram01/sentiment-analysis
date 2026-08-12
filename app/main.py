from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_sentiment

app = FastAPI(
    title='Movie Sentiment Analysis API',
    Description="Sentiment analysis using TF-IDF and Tuned Linear SVM",
    version="1.0.0"
)

class ReviewRequest(BaseModel):
    review: str

@app.get('/')
def home():
    return {
        'message':"Movie Sentiment Analysis API is running"
    }

@app.post('/predict')
def predict(request: ReviewRequest):

    sentiment = predict_sentiment(request.review)

    return {
        'review': request.review,
        'sentiment': sentiment
    }