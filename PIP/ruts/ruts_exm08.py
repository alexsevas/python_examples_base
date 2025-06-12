# conda activate allpy310
# python 3.8-3.10
# pip install ruts

'''
Библиотека позволяет создавать компоненты spaCy для следующих классов:
BasicStats
DiversityStats
MorphStats
ReadabilityStats
Русскоязычную модель spaCy можно скачать, выполнив команду:

$ python -m spacy download ru_core_news_sm
'''

import pprint
import ruts
import spacy
nlp = spacy.load('ru_core_news_sm')
nlp.add_pipe('basic', last=True)
doc = nlp("Существуют три вида лжи: ложь, наглая ложь и статистика")
pprint.pprint(doc._.basic.c_letters)

pprint.pprint(doc._.basic.get_stats())