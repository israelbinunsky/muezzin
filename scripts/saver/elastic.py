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
        self.index = config.ELASTIC_INDEX
        self.mappings = {
             "mappings": {
    "document": {
        "properties": {
            'filepath': {"type" : "text"},
            'filename': {"type" : "text"},
            'size_kbs': {"type" : "long"},
            'size_bites': {"type" : "long"},
            'creation_datetime': {"type" : "date"},
            'creation_time': {"type" : "long"},
            'last_change_datetime': {"type" : "date"},
            'last_accessed_datetime': {"type" : "date"}
            }
        }
    }
  }

    def create_doc_id(self, metadata):
        self.doc_id = str(metadata['size_bites']) + str(int(metadata['creation_time']))

    def send(self, metadata):
        self.create_doc_id(metadata)
        try:
            self.es.indices.create(index=self.index, mappings=self.mappings, ignore=400)
            res = self.es.index(index=self.index, document=metadata, id=self.doc_id)
            logger.info(f'elastic {self.doc_id} {res["result"]}')
        except Exception as e:
            logger.error(e)


    def get_all_docs(self):
        all_documents = list()
        res = self.es.search(index=self.index, body={
            'size': 1000,
            'query': {
                'match_all': {}
            }
        })

        for doc in res['hits']['hits']:
            all_documents.append(doc)
        return all_documents

    def add_mapping_field(self, filed, filed_type):
        try:
            self.es.indices.put_mapping(
                index=self.index,
                body={
                    "properties": {
                        filed: {"type": filed_type}
                    }
                }
            )
        except Exception as e:
            logger.error(f"error {e}")

    def update_new_field(self,document_id, filed, value):
        try:
            self.es.update(
                index=self.index,
                id=document_id,
                body={"doc": {filed: value}}
            )

            logger.info(f'field {filed} updated in doc id: {document_id}')
        except Exception as e:
            logger.error(f"error {e}")

