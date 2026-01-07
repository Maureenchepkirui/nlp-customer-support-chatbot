import json
import random

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


# Load intents
with open("intents.json") as file:
    data = json.load(file)

texts = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(intent["tag"])

# Vectorize text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, labels)


def get_response(user_input: str) -> str:
    """
    Predict intent and return a response
    """
    X_test = vectorizer.transform([user_input])
    predicted_intent = model.predict(X_test)[0]

    for intent in data["intents"]:
        if intent["tag"] == predicted_intent:
            return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."

