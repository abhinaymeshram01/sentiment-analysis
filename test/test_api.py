from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Movie Sentiment Analysis API is running"


def test_positive_prediction():
    response = client.post(
        "/predict",
        json={
            "review": "This movie was absolutely fantastic and amazing."
        }
    )

    assert response.status_code == 200
    assert response.json()["sentiment"] == "Positive"


def test_negative_prediction():
    response = client.post(
        "/predict",
        json={
            "review": "This movie was terrible, boring and disappointing."
        }
    )

    assert response.status_code == 200
    assert response.json()["sentiment"] == "Negative"