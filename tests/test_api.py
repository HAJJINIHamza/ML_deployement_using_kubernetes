import numpy as np
from fastapi.testclient import TestClient

from app.dependencies.get_model import get_model
from app.main import app


# Creating a mock model
class MockModel:
    def predict(self, X):
        return np.ndarray([0 for _ in X])


# Initiating mock model
mocked_model = MockModel()
# Overriding get_model dependency
app.dependency_overrides[get_model] = lambda: mocked_model

client = TestClient(app)


# Test health, readiness and predict endpoints
def test_health():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "Health ok"}


def test_readiness():
    with TestClient(app) as client:
        response = client.get("/ready")
        assert response.status_code == 200
        assert response.json() == {"status": "Model ok"}


def test_predict():
    playload = {"s_length": 5.1, "s_width": 3.4, "p_length": 2.1, "p_width": 0.2}

    with TestClient(app) as client:
        response = client.post("/predict", json=playload)
        assert response.status_code == 200
