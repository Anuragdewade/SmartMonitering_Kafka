from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:

    temperature = random.randint(60, 100)

    data = {
        "temperature": temperature
    }

    producer.send('sensor-data', data)

    print("Sent:", data)

    time.sleep(2)