import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Movie Sentiment Analysis",
    page_icon="🎬",
    layout='centered'
)

st.title("🎬 Movie Sentiment Analysis")
st.write("Enter a movie review and predict whether it is positive or negative.")

review = st.text_area(
    "Movie Review",
    placeholder="Example: This movie was absolutely fantastic...",
    height=180
)

if st.button("Predict Sentiment"):
    if not review.strip():
        st.warning('Please enter movie review')
    else:
        try:
            response = requests.post(
                API_URL,
                json={'review':review}
            )

            if response.status_code == 200:
                result = response.json()

                if result['sentiment'] == 'Positive':
                    st.success('Positve Review')
                else:
                    st.error('Negative Review')

            else:
                st.error('API returned an error.')

        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to the FastAPI server. "
                "Make sure the API is running."
            )