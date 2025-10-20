# import packages
from datasets import load_dataset, concatenate_datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import os


# load datasets
# Load both positive and negative slices
print("🔽 Loading balanced IMDB dataset...")
pos_df = load_dataset("imdb", split="train[:10%]")     # positive
neg_df = load_dataset("imdb", split="train[-10%:]")    # negative

# Combine and shuffle
dataset = concatenate_datasets([pos_df, neg_df]).shuffle(seed=42)

# Convert to DataFrame
df = pd.DataFrame({
    "review": dataset["text"],
    "sentiment": dataset["label"]
})

# Check label distribution
print("📊 Label counts:", df["sentiment"].value_counts().to_dict())

# split datasets
X_train, X_test, y_train, y_test = train_test_split(df["review"], df["sentiment"], test_size=0.2, random_state=42)


# Model pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=10000)),
    ("clf", LogisticRegression(max_iter=1000))
])

# Train
print("🧠 Training model...")
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("📊 Evaluation:")
print(classification_report(y_test, y_pred))

# Serialize and Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model.pkl")
print("✅ Model saved to models/model.pkl")



