# import packages
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import joblib
import os

# load model
model_path = os.path.join("models", "model.pkl")
model = joblib.load(model_path)

# DB setup
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "sentiment")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "secret")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# log predictions
class PredictionLog(Base):
    __tablename__ = "prediction_logs"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    label = Column(String(20), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create table if it doesn't exist
Base.metadata.create_all(bind=engine)


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
    db = SessionLocal()
    log_entry = PredictionLog(text=review.text, label=label)
    db.add(log_entry)
    db.commit()
    db.close()
    return {"label": label}
