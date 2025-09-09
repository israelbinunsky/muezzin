from elastic import Elastic
from mongo import Mongo
from kafka import KafkaConsumer
import json
import config
from scripts.logs import Logger
from stt import Stt

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
        stt = Stt()

        for message in con:
            print(message.value)
            logger.info(f'{message.value['filename']} pulled from topic {topic}')
            elastic.send(message.value)
            mongo.send(message.value, elastic.doc_id)
            stt.stt(message.value['filepath'])
        con.close()
    except Exception as e:
        logger.error(e)

consumer_saver_manager()


