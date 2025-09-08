from kafka import KafkaProducer
import config
import metadata
import json
from scripts.logs import Logger

logger = Logger.get_logger()
r = metadata.Metadata()
metadata_list = r.get_all_files_metadata()

def publish_metadata(topic=config.TOPIC):
    try:
        producer = KafkaProducer(bootstrap_servers=config.KAFKA_SERVER,
                                 value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        for m in metadata_list:
            producer.send(topic, m)
        producer.flush()
        print(f"Published to topic {topic}")
        logger.info(f"Published to topic {topic}")
        producer.close()
    except Exception as e:
        logger.error(e)

publish_metadata()

