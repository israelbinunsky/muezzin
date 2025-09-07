from kafka import KafkaProducer
from reader import Reader
import json

def publish_metadata(topic):
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    reader = Reader()
    metadata_list = reader.get_all_files_metadata()
    for m in metadata_list:
        producer.send(topic, m)
    producer.flush()
    print("s")

publish_metadata('datas')