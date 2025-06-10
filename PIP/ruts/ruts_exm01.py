# conda activate allpy310
# python 3.8-3.10
# pip install ruts

'''
Основной функционал базируется на адаптированных для русского языка статистиках библиотеки textacy и позволяет работать
как непосредственно с текстами, так и с подготовленными Doc-объектами библиотеки spaCy.
API для знакомства с доступными функциями: https://ruts-api.herokuapp.com/docs

Библиотека позволяет создавать свои инструменты для извлечения предложений и слов из текста, которые затем можно
использовать при вычислении статистик.
'''

import re
from nltk.corpus import stopwords
from ruts import SentsExtractor, WordsExtractor
text = "Не имей 100 рублей, а имей 100 друзей"
se = SentsExtractor(tokenizer=re.compile(r', '))
se.extract(text)
print(se.extract(text))

we = WordsExtractor(use_lexemes=True, stopwords=stopwords.words('russian'), filter_nums=True, ngram_range=(1, 2))
print(we.extract(text))

print(we.get_most_common(3))