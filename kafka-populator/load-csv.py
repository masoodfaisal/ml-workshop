import pandas as pd
import os
import json
from time import sleep
from kafka import KafkaProducer, KafkaConsumer
# import sys

file_location = os.getenv('CHURN_FILE') or '../data/Customer-Churn_P2.csv'
full_product_data = pd.read_csv(file_location)

kafka_servers = os.getenv('KAFKA_SERVERS') or 'localhost:9092'
print(f"Kafka is at {kafka_servers}")

topic_name = os.getenv('KAFKA_TOPIC') or 'data'

# producer = KafkaProducer(bootstrap_servers=kafka_servers, value_serializer=lambda v: json.dumps(v).encode())
producer = KafkaProducer(bootstrap_servers=kafka_servers)

for index, row in full_product_data.iterrows():
    print(row.to_json())
    producer.send(topic_name, value = json.dumps( json.loads(row.to_json())).encode())

producer.flush()
sleep(10)

print("done submitting messages")

# consumer2 = KafkaConsumer(
#     'raw-router-data',
#     bootstrap_servers=[kafka_servers],
#     auto_offset_reset='earliest',
#     enable_auto_commit=True,
#     group_id='fm-group',
#     value_deserializer=lambda v: json.loads(v.decode('utf-8')))


# for records in consumer2:
#     print(f"**Data Consumed: {records}")

# print("done consuming messages")

# sys.exit(0)

