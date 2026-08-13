# 🎬 Movie Sentiment Analysis

An end-to-end **Natural Language Processing (NLP)** project that classifies movie reviews as **Positive** or **Negative** using classical machine learning techniques.

The project uses **TF-IDF** for text feature extraction and a **tuned Linear Support Vector Machine (SVM)** for sentiment classification. The trained model is integrated with a **FastAPI REST API**, **Streamlit web application**, automated testing with **Pytest**, and **Docker Compose** for containerized deployment.

---

## 📌 Project Overview

The objective of this project is to build a complete NLP machine learning pipeline starting from raw movie reviews and ending with a deployable sentiment analysis application.

The project includes:

- Data loading and exploration
- Exploratory Data Analysis (EDA)
- Text preprocessing
- TF-IDF feature extraction
- Classical machine learning models
- Model comparison
- Linear SVM hyperparameter tuning
- Model evaluation
- Error analysis
- Model serialization using Joblib
- FastAPI REST API
- Streamlit web application
- Automated testing using Pytest
- Docker containerization
- Docker Compose orchestration

---

## 🎯 Objective

The system takes a movie review as input and predicts whether the review is:

- 😊 **Positive**
- 😞 **Negative**

### Example

**Input:**

```text
This movie was absolutely fantastic and amazing.

Prediction:

Positive
📊 Dataset

The project uses a movie review sentiment dataset containing 49,582 reviews.

Dataset Shape
Rows:     49,582
Columns:  2
Dataset Columns
Column	Description
review	Movie review text
sentiment	Sentiment label
Target Distribution
Sentiment	Label	Count
Negative	0	24,698
Positive	1	24,884

The dataset is approximately balanced between positive and negative reviews.

🔄 Machine Learning Pipeline
Raw Movie Review
       │
       ▼
Data Cleaning
       │
       ▼
Text Preprocessing
       │
       ▼
Train / Test Split
       │
       ▼
TF-IDF Vectorization
       │
       ▼
Train Multiple ML Models
       │
       ▼
Model Evaluation
       │
       ▼
Linear SVM Hyperparameter Tuning
       │
       ▼
Final Linear SVM
       │
       ▼
Save Model + Vectorizer
       │
       ▼
FastAPI REST API
       │
       ▼
Streamlit Web Application
🧹 Text Preprocessing

The movie reviews are cleaned before converting them into numerical features.

The preprocessing pipeline includes:

Converting text to lowercase
Removing HTML tags
Removing special characters
Removing unnecessary whitespace
Normalizing text

The same preprocessing logic is used during prediction to maintain consistency between training and inference.

🔤 TF-IDF Feature Extraction

The project uses Term Frequency-Inverse Document Frequency (TF-IDF) to convert textual reviews into numerical feature vectors.

TF-IDF gives higher importance to words that are useful for distinguishing between positive and negative reviews while reducing the importance of very common words.

Movie Review
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorizer
      │
      ▼
Numerical Feature Vector

The trained TF-IDF vectorizer is saved using Joblib and reused during inference.

🤖 Machine Learning Models

Several classical machine learning algorithms were explored and evaluated during the project.

Models evaluated
Logistic Regression
Naive Bayes
Linear SVM

After comparison and hyperparameter tuning, Linear SVM was selected as the final classification model.

⚙️ Linear SVM

Linear Support Vector Machine (SVM) is well suited for text classification because TF-IDF produces high-dimensional sparse feature vectors.

The Linear SVM model was further improved using hyperparameter tuning.

The tuned Linear SVM was selected as the final model for deployment.

📈 Model Performance

The final model achieved the following confirmed performance:

Metric	Score
ROC-AUC	0.9683

Additional evaluation metrics were calculated during the notebook analysis:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix
ROC-AUC
🔍 Error Analysis

The project includes analysis of incorrectly classified reviews to understand model limitations.

Some reviews can be difficult to classify because of:

Sarcasm
Mixed sentiment
Complex sentences
Context-dependent expressions
Reviews containing both positive and negative opinions

Example of misclassified predictions:

Actual	Predicted
0	1
1	0
0	1
1	0

Error analysis helps identify areas where classical NLP models may struggle.

💾 Model Serialization

The final trained model and TF-IDF vectorizer are saved using Joblib.

models/
│
├── sentiment_svm.pkl
└── tfidf_vectorizer.pkl

These saved files are loaded by the FastAPI application during prediction.

🚀 Application Architecture

The project consists of a Streamlit frontend and FastAPI backend.

                         User
                           │
                           ▼
                ┌────────────────────┐
                │ Streamlit Frontend │
                │      Port 8501     │
                └─────────┬──────────┘
                          │
                          │ HTTP Request
                          ▼
                ┌────────────────────┐
                │    FastAPI API     │
                │      Port 8000     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Text Preprocessing │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │  TF-IDF Vectorizer │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │     Linear SVM     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Positive / Negative│
                └────────────────────┘
🖥️ Streamlit Application

The Streamlit application provides a simple web interface where users can enter a movie review and receive a sentiment prediction.

Positive Review

Input:

This movie was absolutely fantastic and amazing.

Output:

😊 Positive Review
Negative Review

Input:

This movie was boring, terrible and disappointing.

Output:

😞 Negative Review
⚡ FastAPI REST API

The trained machine learning model is exposed through a FastAPI REST API.

Home Endpoint
GET /
Example Response
{
    "message": "Movie Sentiment Analysis API is running"
}
Prediction Endpoint
POST /predict
Request
{
    "review": "This movie was absolutely fantastic and amazing."
}
Response
{
    "review": "This movie was absolutely fantastic and amazing.",
    "sentiment": "Positive"
}
📖 FastAPI Swagger Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

After starting the API, open:

http://localhost:8000/docs

The /predict endpoint can be tested directly from the Swagger interface.

🧪 Testing

The project uses Pytest for automated testing.

Testing covers:

FastAPI home endpoint
FastAPI prediction endpoint
Positive sentiment prediction
Negative sentiment prediction
Model prediction functionality

Run the complete test suite:

pytest
🐳 Docker

The project is containerized using Docker.

Two separate containers are used:

┌───────────────────────────────┐
│     Streamlit Container       │
│                               │
│          Port 8501            │
└───────────────┬───────────────┘
                │
                │ Docker Network
                ▼
┌───────────────────────────────┐
│       FastAPI Container       │
│                               │
│          Port 8000            │
└───────────────────────────────┘
Docker Components
Dockerfile.api
Dockerfile.streamlit
docker-compose.yml
.dockerignore
🐳 Docker Compose

Docker Compose is used to build and run the FastAPI and Streamlit containers together.

Build and Start
docker compose up --build

This command:

Builds the FastAPI image
Builds the Streamlit image
Creates the Docker network
Starts the FastAPI container
Starts the Streamlit container
Connects Streamlit to FastAPI through the Docker network
🌐 Streamlit Application

Open:

http://localhost:8501
⚡ FastAPI

Open:

http://localhost:8000
📖 FastAPI Swagger Documentation

Open:

http://localhost:8000/docs
🛑 Stop Docker Containers

To stop and remove the containers:

docker compose down
🔍 Check Docker Containers

To check the status of the containers:

docker compose ps
📜 Docker Logs
FastAPI Logs
docker compose logs api
Streamlit Logs
docker compose logs streamlit
All Logs
docker compose logs
💻 Local Installation

The project can also be run locally without Docker.

1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/sentiment-analysis.git
cd sentiment-analysis
2. Create Virtual Environment
python -m venv .venv
Windows
.venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
▶️ Run FastAPI Locally

Start the FastAPI server:

uvicorn app.main:app --reload

FastAPI will be available at:

http://localhost:8000

Swagger documentation:

http://localhost:8000/docs
▶️ Run Streamlit Locally

Open another terminal and activate the virtual environment.

Then run:

streamlit run app/streamlit_app.py

Streamlit will be available at:

http://localhost:8501
🧪 Run Tests Locally

Activate the virtual environment and run:

pytest
📁 Project Structure
sentiment-analysis/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   ├── preprocessing.py
│   └── streamlit_app.py
│
├── models/
│   ├── sentiment_svm.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebook/
│   └── sentiment_analysis.ipynb
│
├── test/
│   ├── __init__.py
│   ├── test_model.py
│   └── test_api.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile.api
├── Dockerfile.streamlit
├── docker-compose.yml
├── README.md
└── requirements.txt
🛠️ Technologies Used
Programming Language
Python
Data Science
Pandas
NumPy
Scikit-learn
Joblib
Natural Language Processing
Text Preprocessing
TF-IDF
Classical NLP
Sentiment Classification
Machine Learning
Logistic Regression
Naive Bayes
Linear SVM
Hyperparameter Tuning
Model Evaluation
Backend
FastAPI
Uvicorn
Pydantic
Frontend
Streamlit
Testing
Pytest
Containerization
Docker
Docker Compose
Development Tools
Jupyter Notebook
VS Code
Git
GitHub
📌 Key Features
✅ Binary movie sentiment classification
✅ Classical NLP pipeline
✅ Text preprocessing
✅ TF-IDF feature extraction
✅ Multiple machine learning models
✅ Model comparison
✅ Linear SVM classification
✅ Hyperparameter tuning
✅ Model evaluation
✅ ROC-AUC evaluation
✅ Error analysis
✅ Model serialization
✅ FastAPI REST API
✅ Streamlit web application
✅ Automated testing with Pytest
✅ Docker containerization
✅ Docker Compose orchestration
✅ Multi-container application
✅ Docker networking between frontend and backend
🔮 Future Improvements

The following improvements can be implemented in future versions:

Add sentiment confidence scores
Add prediction probability visualization
Experiment with word n-grams
Experiment with character n-grams
Improve text preprocessing
Compare additional classical NLP algorithms
Add model monitoring
Add structured logging
Add API health-check endpoints
Add CI/CD using GitHub Actions
Deploy the application to a cloud platform
Add authentication and API security
Add multilingual sentiment analysis
Experiment with transformer-based models such as BERT
Add model versioning
Add automated model retraining
📚 Learning Outcomes

This project provided practical experience with:

Natural Language Processing
Text preprocessing
TF-IDF
Feature engineering
Binary classification
Linear SVM
Hyperparameter tuning
Model evaluation
ROC-AUC
Error analysis
Model serialization
REST API development
Streamlit application development
API and frontend integration
Automated testing
Docker
Docker Compose
Docker networking
Multi-container applications
👨‍💻 Author
Abhinay Meshram

GitHub:

https://github.com/YOUR_USERNAME

⭐ Project Summary

This project demonstrates a complete classical NLP machine learning workflow, starting from raw movie reviews and text preprocessing and progressing through feature engineering, model training, hyperparameter tuning, evaluation, model serialization, REST API development, Streamlit integration, automated testing, and Docker-based deployment.

It demonstrates how a traditional machine learning model can be transformed into a complete, testable, containerized application.


**Important:** replace `YOUR_USERNAME` in the two GitHub locations with your actual GitHub username.