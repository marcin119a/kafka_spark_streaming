FROM openjdk:17-slim

ENV SCALA_VERSION=2.13 \
    KAFKA_VERSION=3.9.0 \
    KAFKA_DIR=/opt/kafka

RUN apt-get update && apt-get install -y wget tar && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://dlcdn.apache.org/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz && \
    mkdir -p ${KAFKA_DIR} && \
    tar -xzf kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz --strip-components=1 -C ${KAFKA_DIR} && \
    rm kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz

RUN KAFKA_CLUSTER_ID=$(${KAFKA_DIR}/bin/kafka-storage.sh random-uuid) && \
    ${KAFKA_DIR}/bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c ${KAFKA_DIR}/config/kraft/server.properties

EXPOSE 9092

CMD ["sh", "-c", "/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/kraft/server.properties"]
