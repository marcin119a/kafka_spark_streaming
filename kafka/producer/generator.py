import random
import time
import datetime
from kafka import KafkaProducer
import json
import threading

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

stop_event = threading.Event()

def generate_data():
    while not stop_event.is_set():
        transaction_id = random.randint(1000, 9999)
        total_bill = round(random.uniform(5, 100), 2)
        tip = round(total_bill * random.uniform(0.05, 0.25), 2)
        sex = random.choice(["Male", "Female"])
        smoker = random.choice(["Yes", "No"])
        day = random.choice(["Thur", "Fri", "Sat", "Sun"])
        time_of_day = random.choice(["Lunch", "Dinner"])
        size = random.randint(1, 6)
        timestamp = datetime.datetime.now().isoformat()

        data = {
            "transaction_id": transaction_id,
            "total_bill": total_bill,
            "tip": tip,
            "sex": sex,
            "smoker": smoker,
            "day": day,
            "time": time_of_day,
            "size": size,
            "timestamp": timestamp
        }

        producer.send("spark-kafka-topic", value=data)
        print(f"Wysłano: {data}")
        time.sleep(1)
