# app/tests/test_smoke.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_positive():
    response = client.post("/predict", json={"text": "This movie was amazing!"})
    assert response.status_code == 200
    assert response.json()["label"] in ["positive", "negative"]

def test_predict_negative():
    response = client.post("/predict", json={"text": "Worst movie ever."})
    assert response.status_code == 200
    assert response.json()["label"] in ["positive", "negative"]
