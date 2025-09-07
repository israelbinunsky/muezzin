from kafka import KafkaConsumer
import json

def consumer(topic):
    con = KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    print(con.topics())
    for message in con:
        print(message.value)
consumer('podcasts_metadata')