import random
import time
import datetime
from kafka import KafkaProducer
import json
import threading

# Inicjalizacja Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Flaga do zatrzymania generatora
stop_event = threading.Event()

# Funkcja generująca dane
def generate_data():
    while not stop_event.is_set():  # Działa dopóki flaga stop_event nie jest ustawiona
        # Generowanie losowych danych podobnych do datasetu 'tips'
        transaction_id = random.randint(1000, 9999)
        total_bill = round(random.uniform(5, 100), 2)  # Rachunek od 5 do 100
        tip = round(total_bill * random.uniform(0.05, 0.25), 2)  # Napiwek jako % rachunku
        sex = random.choice(["Male", "Female"])
        smoker = random.choice(["Yes", "No"])
        day = random.choice(["Thur", "Fri", "Sat", "Sun"])
        time_of_day = random.choice(["Lunch", "Dinner"])
        size = random.randint(1, 6)  # Liczba osób przy stole
        timestamp = datetime.datetime.now().isoformat()  # Dodanie timestampu

        # Zbudowanie słownika z danymi
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

        # Wysłanie danych do tematu Kafka
        producer.send("spark-kafka-topic", value=data)
        print(f"Wysłano: {data}")

        # Odstęp między wysyłaniem danych
        time.sleep(1)

# Uruchom generator w wątku
generator_thread = threading.Thread(target=generate_data)
generator_thread.start()

