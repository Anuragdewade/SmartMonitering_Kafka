from kafka import KafkaConsumer
import json
import requests

print("Starting Consumer...")

consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Waiting for messages...")

for message in consumer:

    data = message.value

    print("Received:", data)

    response = requests.post(
        "http://127.0.0.1:9000/analyze",
        json=data
    )

    ai_result = response.json()

    print("AI Response:", ai_result)

    # Send to dashboard
    requests.post(
        "http://127.0.0.1:7000/update",
        json=ai_result
    )