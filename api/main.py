# Import necessary libraries
from fastapi import FastAPI
from api.models import EventModel
from api.firehose_client import FirehoseClient

app = FastAPI()

# Initialize the mock Firehose client
firehose = FirehoseClient("game-events-stream")

@app.post("/events")
def receive_event(event: EventModel):
    result = firehose.send_event(event.model_dump()) # dict() is deprecated in pydantic v2, so used model_dump() instead
    return {"message": "Event received", "firehose": result}