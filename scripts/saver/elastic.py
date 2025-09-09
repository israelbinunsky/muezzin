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
        self.doc_id = None
        self.mappings = {
             "mappings": {
    "document": {
        "properties": {
            'filepath': {"type" : "text"},
            'filename': {"type" : "text"},
            'size_kbs': {"type" : "long"},
            'size_bites': {"type" : "long"},
            'creation_datetime': {"type" : "date_nanos"},
            'creation_time': {"type" : "long"},
            'last_change_datetime': {"type" : "date_nanos"},
            'last_accessed_datetime': {"type" : "date_nanos"}
            }
        }
    }
  }

    def create_doc_id(self, metadata):
        self.doc_id = str(metadata['size_bites']) + str(int(metadata['creation_time']))


    def send(self, metadata):
        self.create_doc_id(metadata)
        try:
            self.es.indices.create(index=config.ELASTIC_INDEX, mappings=self.mappings, ignore=400)
            res = self.es.index(index=config.ELASTIC_INDEX, document=metadata, id=self.doc_id)
            logger.info(f'elastic {self.doc_id} {res["result"]}')
        except Exception as e:
            logger.error(e)

