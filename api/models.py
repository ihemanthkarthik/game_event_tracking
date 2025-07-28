# Importing necessary libraries
from pydantic import BaseModel
from typing import Dict

class EventModel(BaseModel):
    event_id: str
    timestamp: str
    event_type: str
    user_id: str
    metadata: Dict