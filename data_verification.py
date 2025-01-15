from kafka import KafkaConsumer
import json

# Initialize Kafka consumer
consumer = KafkaConsumer('movie_ratings', 
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Consume and process messages
for message in consumer:
    print(f"Received: {message.value}")
