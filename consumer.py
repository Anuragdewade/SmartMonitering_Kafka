from kafka import KafkaConsumer
import json
import requests

consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:

    data = message.value

    print("Received:", data)

    response = requests.post(
        "http://127.0.0.1:9000/analyze",
        json=data
    )

    print("AI Response:", response.json())