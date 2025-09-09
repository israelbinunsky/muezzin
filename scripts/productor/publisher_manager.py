from kafka import KafkaProducer
import config
from metadata import Metadata
import json
from scripts.logs import Logger

logger = Logger.get_logger()
metadata = Metadata()
metadata_list = metadata.get_all_files_metadata()

def publish_metadata(topic=config.TOPIC):
    try:
        producer = KafkaProducer(bootstrap_servers=config.KAFKA_SERVER,
                                 value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        for m in metadata_list:
            producer.send(topic, m)
        producer.flush()
        logger.info(f"Published to topic {topic}")
        producer.close()
    except Exception as e:
        logger.error(e)

publish_metadata()

