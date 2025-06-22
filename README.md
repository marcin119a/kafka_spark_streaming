# Kafka + Spark Structured Streaming + PySpark

A demonstration project using Apache Kafka and PySpark with Apache Spark Structured Streaming for real-time data processing.

## Technology Stack

- **Apache Kafka** – message broker for streaming data
- **Python producer** – data generator (e.g., simulated restaurant bills)
- **Apache Spark** – computation engine (standalone mode, master)
- **PySpark client** – Kafka stream consumer, writes to Parquet
- **Docker + Docker Compose** – environment orchestration

---

## Requirements

- Docker
- Docker Compose

---

## How to run the project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/kafka-spark-streaming.git
   cd kafka-spark-streaming

2. Docker Compose
```bash
docker-compose up --build
```
