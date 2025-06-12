# conda activate allpy310
# python 3.8-3.10
# pip install ruts

'''
Библиотека позволяет работать с несколькими заранее предобработанными наборами данных:

sov_chrest_lit - советские хрестоматии по литературе
stalin_works - полное собрание сочинений И.В. Сталина

Существует возможность работать как с чистыми текстами (без заголовочной информации), так и с записями,
а также фильтровать их по различным критериям.
'''

import pprint
from ruts.datasets import SovChLit
sc = SovChLit()
#sc.download() # загрузка набора данных
print(sc.info)

for i in sc.get_records(max_len=100, category='Весна', limit=1):
    pprint.pprint(i)
print('  ')
for i in sc.get_texts(text_type='Басня', limit=1):
    pprint.pprint(i)