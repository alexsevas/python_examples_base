# conda activate allpy310
# python 3.8-3.10
# pip install ruts

'''
Библиотека позволяет извлекать из текста следующие морфологические признаки:
часть речи, одушевленность, вид,падеж, род, совместность, наклонение,число, лицо, время, переходность, залог.
Для морфологического разбора текста используется библиотека pymorphy2 (https://github.com/kmike/pymorphy2).
Описание статистик взяты из корпуса OpenCorpora (http://opencorpora.org/dict.php?act=gram).
'''

import pprint
from ruts import MorphStats
text = "Постарайтесь получить то, что любите, иначе придется полюбить то, что получили"
ms = MorphStats(text)
pprint.pprint(ms.pos)

pprint.pprint(ms.get_stats())

pprint.pprint(ms.explain_text(filter_none=True))

pprint.pprint(ms.print_stats('pos', 'tense'))