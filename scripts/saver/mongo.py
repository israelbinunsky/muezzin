from pymongo import MongoClient
import gridfs
import config
from scripts.logs import Logger
import base64

logger = Logger.get_logger()

class Mongo:
    def __init__(self):
        try:
            self.client = MongoClient(config.MONGO_URI)
            self.db = self.client[config.MONGO_DB]
            self.fs = gridfs.GridFS(self.db)
            self.collection = config.MONGO_COLLECTION
        except Exception as e:
            logger.error(f"error {e}")

    def send(self, metadata, index):
        filename_in_db = f'{index}.wav'
        try:
            with open(metadata['filepath'], 'rb') as f:
                file_id = self.fs.put(f, index=index, filename=filename_in_db, content_type='audio/wav')
                logger.info(f"file uploaded to mongo with id: {file_id}")
        except Exception as e:
            logger.error(f"error {e}")

    def mongo_pull_field(self, field = "data"):
        binary_datas = list()
        for document in self.db.fs.chunks.find({}, {field: 1, "_id": 0}):
            binary_datas.append(document.get(field))
        return binary_datas
