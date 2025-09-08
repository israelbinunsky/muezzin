from pymongo import MongoClient
import gridfs
import config

class Mongo:
    def __init__(self):
        self.client = MongoClient(config.MONGO_URI)
        self.db = self.client[config.MONGO_DB]
        self.fs = gridfs.GridFS(self.db)

    def send(self, metadata, index):
        filename_in_db = f'{index}.mp3'
        with open(metadata['path'], 'rb') as f:
            file_id = self.fs.put(f, filename=filename_in_db, content_type='audio/wav')
            print(f"file uploaded with id: {file_id}")