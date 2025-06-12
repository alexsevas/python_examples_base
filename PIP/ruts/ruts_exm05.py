# conda activate allpy310
# python 3.8-3.10
# pip install ruts

'''
Библиотека позволяет извлекать из текста следующие морфологические признаки:
часть речи, одушевленность, вид,падеж, род, совместность, наклонение,число, лицо, время, переходность, залог.
Для морфологического разбора текста используется библиотека pymorphy2 (https://github.com/kmike/pymorphy2).
Описание статистик взяты из корпуса OpenCorpora (http://opencorpora.org/dict.php?act=gram).
'''

from ruts import MorphStats
text = "Постарайтесь получить то, что любите, иначе придется полюбить то, что получили"
ms = MorphStats(text)
print(ms.pos)

print(ms.get_stats())

print(ms.explain_text(filter_none=True))

print(ms.print_stats('pos', 'tense'))