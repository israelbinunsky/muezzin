from elasticsearch import Elasticsearch

import config
from scripts.logs import Logger

logger = Logger.get_logger()

class Elastic:
    def __init__(self):
        try:
            self.es = Elasticsearch(config.ELASTIC_SERVER)
        except Exception as e:
            logger.error(e)

    def create_index(self, metadata):
        index = str(metadata['size_bites']) + str(int(metadata['creation_time']))
        try:
            self.es.indices.create(index=index, ignore=400)
            return index
        except Exception as e:
            logger.error(e)

    def send(self, metadata):
        try:
            index = self.create_index(metadata)
            res = self.es.index(index=index, document=metadata)
            print(f'elastic id {res["result"]}')
            logger.info(f'elastic id {res["result"]}')
            return index
        except Exception as e:
            print(e)
            logger.error(e)

