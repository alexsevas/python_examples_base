# conda activate allpy310
# python 3.8-3.10
# pip install ruts

'''
Библиотека позволяет вычислять для текста следующие метрики лексического разнообразия:
Type-Token Ratio (TTR)
Root Type-Token Ratio (RTTR)
Corrected Type-Token Ratio (CTTR)
Herdan Type-Token Ratio (HTTR)
Summer Type-Token Ratio (STTR)
Mass Type-Token Ratio (MTTR)
Dugast Type-Token Ratio (DTTR)
Moving Average Type-Token Ratio (MATTR)
Mean Segmental Type-Token Ratio (MSTTR)
Measure of Textual Lexical Diversity (MTLD)
Moving Average Measure of Textual Lexical Diversity (MAMTLD)
Hypergeometric Distribution D (HD-D)
Индекс Симпсона
Гапакс-индекс
Часть реализаций метрик взята из проекта lexical_diversity (https://github.com/kristopherkyle/lexical_diversity)
'''

from ruts import DiversityStats
text = "Ног нет, а хожу, рта нет, а скажу: когда спать, когда вставать, когда работу начинать"
ds = DiversityStats(text)
print(ds.get_stats())

print(ds.print_stats())