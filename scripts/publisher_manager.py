from kafka import KafkaProducer
import config
import reader
import json


r = reader.Metadata()
metadata_list = r.get_all_files_metadata()

def publish_metadata(topic=config.TOPIC):

    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    for m in metadata_list:
        producer.send(topic, m)
    producer.flush()
    print(f"Published to topic {topic}")

publish_metadata()

