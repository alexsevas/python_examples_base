# ENV allpy310

# pip install translators

'''
import translators as ts

# Перевод через DeepL
result = ts.translate_html()
#result = ts.deepl("Как дела?", from_language="ru", to_language="en")
print(result)
# Вывод: How are you?
'''

import translators as ts

q_text = 'Раз, два, три - проверка тест'
q_html = '''<!DOCTYPE html><html><head><title>《季姬击鸡记》</title></head><body><p>还有另一篇文章《施氏食狮史》。</p></body></html>'''

### usage
#ts.preaccelerate()  # Optional. Caching sessions in advance, which can help improve access speed.

print(ts.translators_pool)
print(ts.translate_text(q_text))
print(ts.translate_html(q_html, translator='deepl'))

### parameters
#help(ts.translate_text)