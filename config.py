import os
PATH = 'C:/Users/israel/Desktop/data'
TOPIC = 'podcasts_metadata'
MONGO_DB = os.getenv("MONGO_DB", )
MONGO_URI = os.getenv('MONGO_URI', "mongodb://localhost:27017/")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", 'podcasts')