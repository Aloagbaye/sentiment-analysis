# import packages
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

# load model
model_path = os.path.join("models", "model.pkl")
model = joblib.load(model_path)

# format input with pydantic
# Input schema
class Review(BaseModel):
    text: str

# init FastAPI app
app = FastAPI(
    title="🎬 Movie Review Sentiment API",
    description="Predicts whether a movie review is positive or negative.",
    version="1.0"
)

# method for predict endpoint
@app.post("/predict")
def predict_sentiment(review: Review):
    prediction = model.predict([review.text])[0]
    label = "positive" if prediction == 1 else "negative"
    return {"label": label}
