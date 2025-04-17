from kafka import KafkaConsumer
import json
from datetime import datetime

# Create a Kafka consumer for the 'sensor-data' topic
consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers=['127.0.0.1:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Output file name with timestamp
file_name = f"sensor_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

# Open the file and append messages as they arrive
with open(file_name, 'a') as f:
    print(f"Listening for messages... Saving to {file_name}")
    for message in consumer:
        print("Received:", message.value)
        f.write(json.dumps(message.value) + '\n')
