import config
from stt import Stt
from scripts.saver.elastic import Elastic

class Analysis:
    def __init__(self):
        self.stt = Stt()
        hostile_text = self.stt.binary_to_text(config.HOSTILE_LIST).lower()
        hostile_list = hostile_text.split(',')
        split_hostile_list = [w.split() for w in hostile_list]
        self.doubles_hostile_list = [w for w in split_hostile_list if len(w) > 1]
        self.singles_hostile_list = [w for w in split_hostile_list if len(w) == 1]


        lass_hostile_text = self.stt.binary_to_text(config.LASS_HOSTILE_LIST).lower()
        lass_hostile_list = lass_hostile_text.split(',')
        split_lass_hostile_list = [w.split() for w in lass_hostile_list]
        self.doubles_lass_hostile_list = [w for w in split_lass_hostile_list if len(w) > 1]
        self.singles_lass_hostile_list = [w for w in split_lass_hostile_list if len(w) == 1]

        self.elastic = Elastic()

    def hostile_calculation(self, text):
        hostile = 0
        is_hostile = False
        words = text.split(' ')
        for i in range(len(words)):
            if words[i] in self.singles_hostile_list:
                hostile += 2
                is_hostile = True
            elif words[i] in self.singles_lass_hostile_list:
                hostile += 1

            for double in self.doubles_hostile_list:
                if words[i] == double[0]:
                    if words[i] != len(words):
                        if words[i+1] == double[1]:
                            hostile += 2
                            is_hostile = True
            for double in self.doubles_lass_hostile_list:
                if words[i] == double[0]:
                    if i != len(words) and i != len(words)-1:
                        if words[i + 1] == double[1]:
                            hostile += 1

        hostility_percent = hostile / len(words)
        res = {'is_hostile': is_hostile, 'hostility_percent': hostility_percent}
        return res


    def update_stats(self,document_id, text):
        average_minute_words = 100

        res = self.hostile_calculation(text)
        hostility_percent = res['hostility_percent']
        is_hostile = res['is_hostile']
        self.elastic.update_new_field(document_id, "bds_percent", hostility_percent)

        if hostility_percent >= 4 / (average_minute_words * 2):
            is_bds = True
        else:
            is_bds = False
        self.elastic.update_new_field(document_id, "is_bds", is_bds)

        if not is_bds:
            bds_threat_level = 'none'
        elif is_hostile == True or hostility_percent >= 4 / average_minute_words:
            bds_threat_level = 'high'
        else:
            bds_threat_level = 'medium'
        self.elastic.update_new_field(document_id, "bds_threat_level", bds_threat_level)

