from elasticsearch import Elasticsearch

class Elastic:
    def __init__(self):
        self.es = Elasticsearch("http://localhost:9200")

    def create_index(self, metadata):
        index = str(metadata['size_bites'] + str(int(metadata['creation_time'])))
        if self.es.indices.exists(index):
            self.es.indices.delete(index=index)
        self.es.indices.create(index=index, ignore=400)
        return index

    def send(self, metadata):
        index = self.create_index(metadata)
        res = self.es.index(index=index, document=metadata)
        print(res["result"])
        return index
