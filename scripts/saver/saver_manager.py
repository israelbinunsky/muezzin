from elastic import Elastic
from mongo import Mongo
from kafka import KafkaConsumer
import json
import config
from scripts.logs import Logger

logger = Logger.get_logger()


def consumer_saver_manager(topic=config.TOPIC):
    try:
        con = KafkaConsumer(
            topic,
            bootstrap_servers=[config.KAFKA_SERVER],
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        elastic = Elastic()
        mongo = Mongo()

        for message in con:
            data = message.value
            print(data)
            logger.info(f'{data['filename']} pulled from topic {topic}')
            elastic.send(data)
            mongo.send(data, elastic.doc_id)
        con.close()
    except Exception as e:
        logger.error(f"error {e}")

consumer_saver_manager()


