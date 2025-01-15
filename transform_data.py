from kafka import KafkaConsumer
import json
import pandas as pd

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'movie_ratings', 
    bootstrap_servers='localhost:9092', 
    group_id='movie_ratings_group',  # Set a group ID
    consumer_timeout_ms=5000
)

# Create an empty list to store transformed data
transformed_data = []

# Start consuming messages
print("Starting to consume messages...")
for message in consumer:
    try:
        # Debugging: Print raw message (bytes)
        print(f"Raw message (bytes): {message.value}")

        # Check if the message is empty or None
        if not message.value:
            print("Received an empty or None message, skipping.")
            continue

        # Try decoding the JSON message manually
        try:
            data = json.loads(message.value.decode('utf-8'))
        except json.JSONDecodeError as e:
            print(f"Error decoding message: {e}. Skipping message: {message.value}")
            continue

        # Debugging: Print the decoded message
        print(f"Decoded message: {data}")

        # Validate numeric fields (movie_id, imdb_id, tmdb_id)
        for field in ['movie_id', 'imdb_id', 'tmdb_id']:
            if field in data:
                try:
                    data[field] = int(data[field])  # Try converting to integer
                except ValueError:
                    print(f"Warning: {field} is non-numeric. Setting {field} to None.")
                    data[field] = None  # Set to None or handle it appropriately

        # Validate rating field
        if data.get('rating') is None or data['rating'] < 1:
            data['rating'] = 1
        elif data['rating'] > 10:
            data['rating'] = 10

        # Handle missing or incorrect average_rating
        if 'average_rating' in data:
            if data['average_rating'] is None or data['average_rating'] <= 0:
                data['average_rating'] = 3.0  # Default or mean value, if missing or incorrect
        else:
            data['average_rating'] = 3.0  # If not present, add a default value

        # Add the transformed message to the list
        transformed_data.append(data)

        # Debugging: Print transformed message
        print(f"Transformed message: {data}")

    except Exception as e:
        print(f"Error processing message: {e}")

# Save transformed data to CSV if any messages were processed
if transformed_data:
    df = pd.DataFrame(transformed_data)
    df.to_csv("transformed_movie_ratings_movie_ratings_group.csv", index=False)
    print("Transformed data saved to transformed_movie_ratings_movie_ratings_group.csv.")
else:
    print("No messages were consumed.")

print("Consumer script finished.")
