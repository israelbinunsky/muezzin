import os
TOTAL_PATH = os.getenv('TOTAL_PATH','C:/Users/israel/Desktop/data')
DATA_PATH = os.getenv('DATA_PATH',f'{TOTAL_PATH}/podcasts')
TOPIC = os.getenv('TOPIC', 'podcasts_metadata')
KAFKA_SERVER = os.getenv('KAFKA_SERVER','localhost:9092')

MONGO_DB = os.getenv("MONGO_DB", 'muezzin')
MONGO_URI = os.getenv('MONGO_URI', "mongodb://localhost:27017/")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", 'podcasts')
MONGO_BINARY_COLLECTION = 'fs.chunks'

ELASTIC_SERVER = os.getenv('ELASTIC_SERVER', "http://localhost:9200")
ELASTIC_INDEX = os.getenv('ELASTIC_INDEX', "podcasts_metadata")
LOGGER_NAME = os.getenv('LOGGER_NAME', "logger")
LOGGER_INDEX = os.getenv('LOGGER_INDEX', "12345")

HOSTILE_LIST = 'R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT'
LASS_HOSTILE_LIST = 'RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=='
