FROM apache/spark-py

# Ustaw JAVA_HOME ręcznie (mimo że Java jest zainstalowana)
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH


WORKDIR /app
COPY . .

CMD ["python"]
