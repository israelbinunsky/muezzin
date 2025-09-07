from kafka import KafkaProducer
import reader
import json


r = reader.Metadata()
def publish_metadata(topic='podcasts_metadata'):

    metadata_list = r.get_all_files_metadata()
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    for m in metadata_list:
        producer.send(topic, m)
    producer.flush()
    print(f"Published to kafka to topic {topic}")
publish_metadata('podcasts_metadata')

