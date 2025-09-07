from elasticsearch import Elasticsearch

def elastic(metadata):
    es = Elasticsearch("http://localhost:9200")
    index = str(metadata['size_bites'] + str(int(metadata['creation_time'])))
    es.indices.create(index=index, ignore=400)
    res = es.index(index=index, document=metadata)
    print(res["result"])
