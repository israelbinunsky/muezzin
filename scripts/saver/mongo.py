from pymongo import MongoClient
import gridfs
import config
from scripts.logs import Logger

logger = Logger.get_logger()

class Mongo:
    def __init__(self):
        self.client = MongoClient(config.MONGO_URI)
        self.db = self.client[config.MONGO_DB]
        self.fs = gridfs.GridFS(self.db)
        self.collection = config.MONGO_COLLECTION

    def send(self, metadata, index):
        filename_in_db = f'{index}.wav'
        try:
            with open(metadata['path'], 'rb') as f:
                file_id = self.fs.put(f, index=index, filename=filename_in_db, content_type='audio/wav')
                print(f"file uploaded to mongo with id: {file_id}")
                logger.info(f"file uploaded to mongo with id: {file_id}")
        except Exception as e:
            print(e)
            logger.error(e)
