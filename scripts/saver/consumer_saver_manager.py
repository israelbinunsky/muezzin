from elastic import Elastic
from mongo import Mongo
from kafka import KafkaConsumer
import json
import config
from scripts.logs import Logger

logger = Logger.get_logger()

elastic = Elastic()
mongo = Mongo()
def consumer_saver_manager(topic=config.TOPIC):
    try:
        con = KafkaConsumer(
            topic,
            bootstrap_servers=[config.KAFKA_SERVER],
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        for message in con:
            print(message.value)
            logger.info(f'{message.value['filename']} pulled from topic {topic}')
            idx = elastic.send(message.value)
            mongo.send(message.value, idx)
        con.close()
    except Exception as e:
        logger.error(e)

consumer_saver_manager()


