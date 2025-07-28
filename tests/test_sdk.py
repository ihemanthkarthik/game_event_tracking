# Importing necessary libraries and modules
from sdk.client import GameAnalyticsClient

# Initialize the GameAnalyticsClient with the API URL
# This URL should match the one used in your FastAPI application
client = GameAnalyticsClient("http://127.0.0.1:8000")

# Testing an install event
status_code, response = client.send_install_event(
    user_id="user_1",
    device_info={"os": "Android", "version": "13"}
)
print("Install Event Response:", status_code, response)

# Testing a purchase event
status_code, response = client.send_purchase_event(
    user_id="user_1",
    purchase_info={"item": "gems", "amount": 4.99, "currency": "USD"}
)
print("Purchase Event Response:", status_code, response)