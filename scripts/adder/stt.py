import speech_recognition as sr
import config
import pymongo
from scripts.logs import Logger
import base64
from mongo import Mongo

logger = Logger.get_logger()

class Stt:
    def __init__(self):
        self.r = sr.Recognizer()

    def binary_to_text(self, base64_data):
        decoded_bytes = base64.b64decode(base64_data)
        decoded_string = decoded_bytes.decode('utf-8', errors='ignore')
        return decoded_string

    def path_to_text(self, filepath):
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
                logger.error(e)

