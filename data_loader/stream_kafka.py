from confluent_kafka import Producer
import csv
import time
import json

# Kafka configuration
bootstrap_servers = 'localhost:9092'
topic = 'sales_data_topic'

# Kafka producer configuration
conf = {'bootstrap.servers': bootstrap_servers}

# Create Kafka producer instance
producer = Producer(conf)

# Function to read CSV file and produce messages to Kafka topic
def produce_sales_data():
    with open('sales_data_sample.csv', encoding = 'unicode_escape') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convert row to JSON or string format as per your requirements
            # Here, assuming row is converted to JSON string
            json_row = json.dumps(row)
            producer.produce(topic, value=json_row)
            time.sleep(0.1)  # Adjust this delay if needed to control message rate

    producer.flush()  # Ensure all messages are sent

if __name__ == '__main__':
    produce_sales_data()
