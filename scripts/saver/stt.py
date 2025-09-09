import speech_recognition as sr
import config
import pymongo
from scripts.logs import Logger

logger = Logger.get_logger()

class Stt:
    def __init__(self):
        self.r = sr.Recognizer()

    def pull_binary_data(self):
        client = pymongo.MongoClient(config.MONGO_URI)
        db = client[config.MONGO_DB]
        collection = db[config.MONGO_COLLECTION]


        for document in collection.find({}, {"name": 1, "_id": 0}):
            print(document.get("name"))

        client.close()
    def stt(self, filepath):

        with sr.AudioFile(filepath) as source:
            audio_data = self.r.record(source)
            try:
                text = self.r.recognize_google(audio_data)
                logger.info("converted to text")
                print("Transcribed Text: " + text)
                return text
            except sr.UnknownValueError as e:
                logger.error(e)
            except sr.RequestError as e:
                logger.error(e)\

