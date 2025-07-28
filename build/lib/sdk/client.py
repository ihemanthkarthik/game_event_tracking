# Importing necessary libraries
import requests  # This library sends HTTP requests
from sdk.events import InstallEvent, PurchaseEvent  # Import the event classes you made

class GameAnalyticsClient:
    """
    GameAnalyticsClient is a helper class used by game developers
    to send game events (like installs and purchases) to a backend server.

    It provides simple methods to:
    - Send an install event when a user installs the game.
    - Send a purchase event when a user buys something in the game.

    Each method creates an event object, converts it to a dictionary,
    and sends it to the API endpoint using an HTTP POST request.

    Parameters:
        api_url (str): The base URL of the backend server (e.g., http://localhost:8000)

    Example usage:
        client = GameAnalyticsClient("http://localhost:8000")
        client.send_install_event("user123", {"os": "Android"})
        client.send_purchase_event("user123", {"item": "coins", "amount": 4.99, "currency": "USD"})
    """
    def __init__(self, api_url):
        self.api_url = api_url

    # Method to send an install event
    # Takes user_id and device_info as parameters
    # Example: client.send_install_event("user123", {"os": "Android"})
    def send_install_event(self, user_id, device_info):
        event = InstallEvent(user_id, device_info)
        return self._send_event(event)

    # Method to send a purchase event
    # Takes user_id and purchase_info as parameters
    # Example: client.send_purchase_event("user123", {"item": "coins", "amount": 4.99, "currency": "USD"})
    def send_purchase_event(self, user_id, purchase_info):
        event = PurchaseEvent(user_id, purchase_info)
        return self._send_event(event)

    # Private method to send the event to the API
    # Converts the event to a dictionary and sends it via POST request
    def _send_event(self, event):
        url = f"{self.api_url}/events"
        response = requests.post(url, json=event.to_dict())
        return response.status_code, response.json()
