# Importing necessary libraries
from fastapi.testclient import TestClient
from api.main import app

# Initialize the TestClient with the FastAPI app
client = TestClient(app)

# Test cases for Install event
def test_install_event():
    event_data = {
        "event_id": "test-install-event",
        "timestamp": "2025-07-28T12:00:00Z",
        "event_type": "install",
        "user_id": "Hemanth",
        "metadata": {
            "os": "Android",
            "version": "16.0"
        }
    }

    response = client.post("/events", json=event_data)
    
    assert response.status_code == 200
    assert response.json()["message"] == "Event received"
    assert "firehose" in response.json()

# Test cases for Purchase event
def test_purchase_event():
    event_data = {
        "event_id": "test_purchase-event",
        "timestamp": "2025-07-28T12:30:00Z",
        "event_type": "purchase",
        "user_id": "Hemanth",
        "metadata": {
            "item": "coins",
            "amount": 19.99,
            "currency": "EUR"
        }
    }

    response = client.post("/events", json=event_data)

    assert response.status_code == 200
    assert response.json()["message"] == "Event received"
    assert "firehose" in response.json()