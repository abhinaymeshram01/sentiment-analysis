from app.model import predict_sentiment

reviews = [
    "This movie was absolutely fantastic and I loved every minute of it.",
    "This was a terrible movie and I completely wasted my time.",
    "The acting was brilliant and the story was amazing.",
    "The movie was boring, slow, and disappointing."
]

for review in reviews:
    prediction = predict_sentiment(review)

    print('='*50)
    print('Review: ', review)
    print('Prediction:', prediction)