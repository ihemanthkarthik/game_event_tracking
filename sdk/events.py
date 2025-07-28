# Installing required libraries
import uuid # For generating unique event IDs
from datetime import datetime # For timestamping events

# Defining Base Event Class for both the events
class BaseEvent:
    def __init__(self, event_type, user_id, metadata):
        self.event_id = str(uuid.uuid4())  # Generate a unique event ID
        self.event_type = event_type
        self.user_id = user_id
        self.timestamp = datetime.now().isoformat()  # Current timestamp in ISO format
        self.metadata = metadata  # Additional data for the event

    # Converting the event details to a dictionary for easy serialization.
    def to_dict(self):
        return {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "user_id": self.user_id,
            "timestamp": self.timestamp,
            "metadata": self.metadata
        }

# Defining Install event class inheriting from BaseEvent
class InstallEvent(BaseEvent):
    def __init__(self, user_id, device_info):
        super().__init__("install", user_id, device_info)

# Defining Purchase event class inheriting from BaseEvent
class PurchaseEvent(BaseEvent):
    def __init__(self, user_id, purchase_info):
        super().__init__("purchase", user_id, purchase_info)