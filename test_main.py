from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health/", headers={"x-api-key": "sniper-2026"})
    assert response.status_code == 200