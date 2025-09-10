from scripts.saver.elastic import Elastic
from analysis import Analysis
from stt import Stt


elastic = Elastic()
analysis = Analysis()
stt = Stt()

def add_stt():
    all_docs = elastic.get_all_docs()
    for doc in all_docs:
        text = stt.path_to_text(doc['_source']['filepath'])
        elastic.add_mapping_field('transcription', 'text')
        elastic.update_new_field(doc['_id'],'transcription', text)

def add_analysis():
    all_docs = elastic.get_all_docs()
    for doc in all_docs:
        analysis.update_stats(doc['_id'], doc['transcription'])




all_docs = elastic.get_all_docs()
doc = all_docs[0]
print(doc)
text = stt.path_to_text(doc['_source']['filepath'])
elastic.add_mapping_field('transcription', 'text')
elastic.update_new_field(doc['_id'],'transcription', text)
all_docs = elastic.get_all_docs()
doc = all_docs[0]
print(doc)
# analysis.update_stats(doc['_id'], doc['transcription'])
# doc = all_docs[0]
# print(doc)