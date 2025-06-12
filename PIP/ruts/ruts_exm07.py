# conda activate allpy310
# python 3.8-3.10
# pip install ruts



from collections import Counter
from nltk.corpus import stopwords
from ruts import WordsExtractor
from ruts.datasets import SovChLit
from ruts.visualizers import zipf
import pprint

'''
Библиотека позволяет визуализировать тексты с помощью следующих видов графиков:
Закон Ципфа (Zipf's law)
Литературная дактилоскопия (Literature Fingerprinting)
Дерево слов (Word Tree)
'''
sc = SovChLit()
text = '\n'.join([text for text in sc.get_texts(limit=100)])
we = WordsExtractor(use_lexemes=True, stopwords=stopwords.words('russian'), filter_nums=True)
tokens_with_count = Counter(we.extract(text))
pprint.pprint(tokens_with_count)

zipf(tokens_with_count, num_words=100, num_labels=10, log=False, show_theory=True, alpha=1.1)

