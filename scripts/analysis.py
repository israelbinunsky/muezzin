import config
from  saver.stt import Stt

class Analysis:
    def __init__(self):
        self.stt = Stt()
        self.hostile_list = self.stt.binary_to_text(config.HOSTILE_LIST)
        self.lass_hostile_list = self.stt.binary_to_text(config.LASS_HOSTILE_LIST)

    def danger_calculation(self, text):
        text = ''
