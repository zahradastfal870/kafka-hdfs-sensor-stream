from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
   bootstrap_servers=['127.0.0.1:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        'sensor_id': random.randint(1, 5),
        'temperature': round(random.uniform(20, 30), 2),
        'humidity': round(random.uniform(40, 60), 2)
    }
    producer.send('sensor-data', value=data)
    print("Sent:", data)
    time.sleep(2)
