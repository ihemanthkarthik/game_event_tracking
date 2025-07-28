# Installing necessary libraries
import boto3
import json
import logging
from botocore.stub import Stubber

# Create a boto3 Firehose client
firehose_client = boto3.client("firehose", region_name="us-east-1")

# Stubber lets us mock AWS responses
stubber = Stubber(firehose_client)

# Set up a fake successful response
stubber.add_response(
    "put_record",
    expected_params={
        "DeliveryStreamName": "mock-game-events-stream",
        "Record": {
            "Data": b'{"mock": "event"}'
        },
    },
    service_response={
        "RecordId": "12345"
    }
)

# Activate the stub
stubber.activate()

class FirehoseClient:
    def __init__(self, stream_name: str):
        self.stream_name = stream_name
        self.client = firehose_client

    def send_event(self, event: dict):
        # Convert the event to bytes
        event_data = json.dumps(event).encode("utf-8")

        # Log the event data for debugging
        logging.info(f"[MOCK SEND TO FIREHOSE] Stream: {self.stream_name}")
        response = self.client.put_record(
            DeliveryStreamName=self.stream_name,
            Record={"Data": event_data}
        )
        return {"status": "sent", "response": response}
    
    