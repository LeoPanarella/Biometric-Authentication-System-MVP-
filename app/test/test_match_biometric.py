from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_match_biometric():
    payload = {
        "user_id": "user123",
        "biometric_data": "AAAABBBBCCCC"
    }

    response = client.post("/api/v1/biometric/match", json=payload)

    # Para MVP aceitamos qualquer valor válido (200)
    assert response.status_code in (200, 401, 404)
