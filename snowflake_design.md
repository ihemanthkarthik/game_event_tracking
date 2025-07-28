# Snowflake Design for Events Tracking

The following design describes a single unified table named Events_Logger that stores both install and purchase events. Each event is identified using the event_type field, and event-specific fields will remain NULL when not applicable. This design simplifies querying while maintaining flexibility.

The metadata column stores the full original JSON payload, ensuring no data is lost and enabling future-proofing for additional fields or event types.

<pre>
CREATE TABLE Events_Logger (
    event_id       STRING,           -- Unique ID for the event
    event_type     STRING,           -- 'install', 'purchase', etc.
    timestamp      TIMESTAMP_TZ,     -- When the event occurred
    user_id        STRING,           -- ID of the user
    os             STRING,           -- Device OS (e.g., Android, iOS)
    version        STRING,           -- OS version
    item           STRING,           -- Item purchased (e.g., 'coins')
    amount         FLOAT,            -- Monetary amount
    currency       STRING,           -- ISO currency code (e.g., 'USD', 'EUR')
    base_amount    FLOAT,            -- Base Monetary Amount (USD Conversion from other Currency) -- Helps in terms of analytics.
    metadata       VARIANT           -- Full original JSON payload
);
</pre>

This is a simple direct approach as all the data can be stored and queried from a single table. This approach is suggested as we have only two events to be recorded. 

However, if there are multiple events to be recorded, then a seperate table for events (Event_Master) with a primary key can be created and Event_Logger can have a foriegn key referencing the Event_Master table. This approach can be utilized as it follows normalization, improves data integrity and performance.

<pre>
CREATE TABLE Event_Master (
    event_type_id INTEGER PRIMARY KEY,
    event_type    STRING UNIQUE
);
``` </pre>

<pre> ```sql
CREATE TABLE Events_Logger (
    event_id         STRING,
    event_type_id    INTEGER REFERENCES Event_Master(event_type_id),
    timestamp        TIMESTAMP_TZ,     -- When the event occurred
    user_id          STRING,           -- ID of the user
    os               STRING,           -- Device OS (e.g., Android, iOS)
    version          STRING,           -- OS version
    item             STRING,           -- Item purchased (e.g., 'coins')
    amount           FLOAT,            -- Monetary amount
    currency         STRING,           -- ISO currency code (e.g., 'USD', 'EUR')
    base_amount      FLOAT,            -- Base Monetary Amount (USD Conversion from other Currency) -- Helps in terms of analytics.
    metadata         VARIANT           -- Full original JSON payload
);
</pre>

In terms of Currency, We use ISO currency code to track the currency ultized during payment. These are Unique and a check constraint can be utilized inorder to check if the currency is ISO Standard.

<pre>
-- Check constraint for Currency (if static list)
CHECK (currency IN ('USD', 'EUR', 'INR', 'GBP', 'AUD'))
</pre>

Note: In terms of analytics, we need currency to be in a single payment method. This can be achieved using a currency converting API to get the equivalent value of the base currency (USD) which can be utilized for analytics.