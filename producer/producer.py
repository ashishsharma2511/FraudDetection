# producer/producer.py
from kafka import KafkaProducer
import json
import random
import time
import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_transaction():
    return {
        "user_id": random.randint(1, 10),
        "amount": round(random.uniform(10, 2000), 2),
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

print("Producing messages to 'transactions' topic...")

while True:
    txn = generate_transaction()
    producer.send('transactions', value=txn)
    print(f" Sent: {txn}")
    time.sleep(1)  # 1 event per second
