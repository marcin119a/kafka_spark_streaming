from kafka import KafkaConsumer
import json


# Inicjalizacja KafkaConsumer
consumer = KafkaConsumer("spark-kafka-topic", bootstrap_servers="localhost:9092", value_deserializer=lambda x: json.loads(x.decode("utf-8")))

total_sum = 0
count = 0

print("Nasłuchiwanie danych z Kafki...")
for message in consumer:
  data = message.value
  total_sum += data['tip']
  count += 1
  average = total_sum / count

  print(f"Otrzymano: {data}")
  print(f"Aktualna suma: {total_sum}, Liczba elementów: {count}, Średnia: {average}")

consumer.close()
