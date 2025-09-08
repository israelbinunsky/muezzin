from elastic import Elastic
from mongo import Mongo
from kafka import KafkaConsumer
import json
import config


elastic = Elastic()
mongo = Mongo()
def consumer_manager(topic=config.TOPIC):
    con = KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    for message in con:
        idx = elastic.send(message)
        mongo.send(message, idx)
        print(message.value)
consumer_manager()


