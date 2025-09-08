from elasticsearch import Elasticsearch

import config
from scripts.logs import Logger

logger = Logger.get_logger()

class Elastic:
    def __init__(self):
        self.es = Elasticsearch(config.ELASTIC_SERVER)

    def create_index(self, metadata):
        index = str(metadata['size_bites']) + str(int(metadata['creation_time']))
        self.es.indices.create(index=index, ignore=400)
        return index

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

