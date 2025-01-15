from kafka import KafkaProducer
import json
import pandas as pd

# Load the dataset
df = pd.read_csv("/Users/rozhinazima/Desktop/projects/movielens-ratings.csv")  # Replace with your dataset path

print("First 5 rows of the dataset:")
print(df.head())  # Display the first 5 rows of the CSV

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Iterate through the dataset and push to Kafka
for index, row in df.iterrows():
    print(f"Sending to Kafka: {row.to_dict()}")  # Print the row being sent to Kafka
    producer.send('movie_ratings', value=row.to_dict())

producer.flush()  # Ensure all messages are sent
print("Finished sending all rows.")