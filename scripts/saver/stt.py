import speech_recognition as sr
from scripts.logs import Logger
logger = Logger.get_logger()

class Stt:
    def __init__(self):
        self.r = sr.Recognizer()
    def stt(self, filepath):

        with sr.AudioFile(filepath) as source:
            audio_data = self.r.record(source)
            try:
                text = self.r.recognize_google(audio_data)
                logger.info("converted to text")
                print("Transcribed Text: " + text)
            except sr.UnknownValueError as e:
                logger.error(e)
            except sr.RequestError as e:
                logger.error(e)

