import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_register_biometric_success():
    payload = {
        "user_id": "user123",
        "biometric_type": "fingerprint",
        "biometric_data": "AAAABBBBCCCC"
    }

    response = client.post("/api/v1/biometric/register", json=payload)

    assert response.status_code == 200
    assert response.json()["message"] == "Biometric registered successfully"
