import pytest
from app import app
import json


@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get("/ping")
    assert resp.status_code == 200


def test_root(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_prediction(client):
    test_data = {
        "Gender": "Male",
        "Married": "Unmarried",
        "ApplicantIncome": 50000,
        "Credit_History": "Cleared Debts",
        "LoanAmount": 500000
    }
    resp = client.post("/prediction", json=test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status": "Rejected"}