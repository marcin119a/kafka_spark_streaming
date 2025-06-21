from pyspark.sql import SparkSession

PYSPARK_SCALA_VERSION = "2.12"
SPARK_VERSION = "3.3.1"
KAFKA_VERSION = "3.9.0"

kafka_brokers = "kafka:9092"
topic = "spark-kafka-topic"

packages = [
    f'org.apache.spark:spark-sql-kafka-0-10_{PYSPARK_SCALA_VERSION}:{SPARK_VERSION}',
    f'org.apache.kafka:kafka-clients:{KAFKA_VERSION}'
]

spark = SparkSession.builder \
    .appName("KafkaSparkConsumer") \
    .master("spark://spark-master:7077") \
    .config("spark.jars.packages", ",".join(packages)) \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_brokers) \
    .option("subscribe", topic) \
    .option("startingOffsets", "latest") \
    .load()

output = df.selectExpr("CAST(value AS STRING)")
query = output.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "/app/output") \
    .option("checkpointLocation", "/app/checkpoints") \
    .start()

query.awaitTermination(30)