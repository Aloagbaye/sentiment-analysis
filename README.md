# 🎬 Sentiment Analysis as a Service

A full-stack MLOps project that serves a movie review sentiment model as a REST API using FastAPI, Docker, Docker Compose, and GitHub Actions CI/CD. The app predicts whether a given movie review is **positive** or **negative**.

![CI](https://github.com/Aloagbaye/sentiment-analysis/actions/workflows/ci.yml/badge.svg)

---

## 🔍 Features

- ✅ Logistic Regression sentiment model trained on IMDB data (via Hugging Face)
- ✅ REST API built with FastAPI
- ✅ PostgreSQL database for logging predictions
- ✅ Dockerized for easy deployment
- ✅ CI/CD pipeline using GitHub Actions
- ✅ Ready for Blue-Green deployment on GCP Cloud Run

---

## 🏗️ Tech Stack

- **ML**: scikit-learn, TfidfVectorizer, Logistic Regression
- **API**: FastAPI, Uvicorn
- **Data**: PostgreSQL, SQLAlchemy
- **DevOps**: Docker, Docker Compose, GitHub Actions, GCP Cloud Run

---

## 🚀 Getting Started (Local)

### 1. Clone the repo

```bash
git clone https://github.com/Aloagbaye/sentiment-analysis.git
cd sentiment-analysis
```

### 2. Train the model

```bash
python train.py
```

This saves the model to `models/model.pkl`.

### 3. Run tests

```bash
pytest app/tests/test_smoke.py
```

### 4. Start the API locally

```bash
uvicorn app.main:app --reload
```

Then visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Running with Docker Compose

### 1. Build and start services

```bash
docker compose up --build
```

This spins up:

- FastAPI container (`sentiment-api`)
- PostgreSQL container (`sentiment-db`)

### 2. Test the API

```bash
curl -X POST http://localhost:8000/predict   -H "Content-Type: application/json"   -d '{"text": "The movie was excellent!"}'
```

---

## ⚙️ GitHub Actions CI/CD

- Workflow file: `.github/workflows/ci.yml`
- Triggers on: push / PR to `main`, or manually (`workflow_dispatch`)
- Pipeline:
  - ✅ Run tests against FastAPI API
  - ✅ Build and push Docker image to Docker Hub
  - ✅ (Optional) Deploy to GCP Cloud Run using Blue-Green deployment

---

## ☁️ Deployment (GCP Cloud Run)

Coming soon!  
Blue-Green deployment strategy is configured in the CI workflow.  
Model is trained during image build and deployed as a containerized API.

---

## 🧪 API Endpoints

### `POST /predict`

```json
Request:
{
  "text": "This movie was amazing!"
}

Response:
{
  "label": "positive"
}
```

### `GET /logs`

Returns the 100 most recent predictions from the DB.

---

## 📂 Project Structure

```
.
├── app/
│   ├── main.py          ← FastAPI app
│   └── tests/           ← Smoke tests
├── models/              ← Saved model
├── train.py             ← ML training script
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/ci.yml
```

---

## 🙌 Credits

Built by [@Aloagbaye](https://github.com/Aloagbaye) as part of an MLOps capstone project.

---

## 📄 License

MIT License — see `LICENSE` file for details.