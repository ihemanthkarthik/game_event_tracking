# Game_Event_Tracking
This project is a simplified mock system designed to track basic mobile game events like install and purchase. It demonstrates a modular and production-ready architecture using a Python SDK and a REST API backend.

## Overview
1. SDK (sdk/): Python package used by game clients to send structured install and purchase events.
2. API (api/): FastAPI-based REST server to receive and process incoming events.
3. Firehose Integration: Simulated using boto3 with Stubber to mock AWS Kinesis Firehose delivery.
4. Snowflake Design: Suggested table schema for event storage with support for multi-currency and flexible metadata.

## Project Structure

<pre>
game_event_tracking/
├── sdk/
│   ├── __init__.py
│   ├── client.py           # SDK client interface
│   └── events.py           # Event class definitions
│
├── api/
│   ├── main.py             # FastAPI app
│   ├── models.py           # Pydantic event model
│   └── firehose_client.py  # Mocked AWS Firehose client using boto3
│
├── tests/
│   ├── test_sdk.py         # Unit tests for SDK
│   └── test_api.py         # Unit tests for API
│
├── setup.py                # For SDK packaging
├── pyproject.toml          # For modern packaging tools
└── README.md               # Project overview and documentation
</pre>

## How to Use

### 1. Install Dependencies

<pre>
pip install -r requirements.txt
</pre>

### 2. Run the API Server

<pre>
uvicorn api.main:app --reload
</pre>

Go to http://127.0.0.1:8000/docs to see the interactive Swagger UI.

### 3. Use the SDK

<pre>
from sdk.client import GameAnalyticsClient

client = GameAnalyticsClient("http://localhost:8000")

# Send install event
client.send_install_event("user123", {"os": "Android", "version": "14"})

# Send purchase event
client.send_purchase_event("user123", {"item": "coins", "amount": 5.99, "currency": "USD"})
</pre>

### 4. Running Tests

Run API and SDK tests:

<pre>
pytest
</pre>

OR

<pre>
python tests/test_sdk.py
python tests/test_api.py
</pre>

### 5. Design Decisions

#### SDK
1. Easy-to-use wrapper for sending structured install/purchase events.
2. Abstracts away event formatting and API calls.

#### API
1. Built with FastAPI for validation, documentation, and speed.
2. Uses Pydantic to enforce input structure.
3. Interacts with AWS Firehose using mocked boto3 client via Stubber.

### 6. Snowflake Table Design

Please refer to [Snowflake Design](snowflake_design.md)

### 7. Assumptions

1. Events contain basic install or purchase metadata.
2. Firehose integration is mocked (not connected to real AWS).
3. Snowflake schema is designed but not implemented.
4. The system supports multi-currency and future extensibility (new event types, fields).

### 8. Future Improvements

To make the system production-ready:

1. Real AWS Firehose integration with retry logic
2. Authentication (e.g., API keys or OAuth)
3. Rate limiting and logging
4. Async event batching
5. Database-backed event persistence (e.g., Snowflake connector)