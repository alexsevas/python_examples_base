# conda activate retinafacep39
#pip install deepface

'''
Сравнение двух лиц
-------------------
Модуль распознавания лиц в проекте InsightFace использует ArcFace, а модуль обнаружения лиц — RetinaFace.
Комбинация ArcFace и RetinaFace интегрирована в библиотеку DeepFace для Python.
Рассмотрите возможность использования DeepFace, если вам нужен готовый конвейер для распознавания лиц.

Важно отметить, что модель ArcFace демонстрирует точность 99.40% на наборе данных LFW (Labeled Faces in the Wild),
в то время как уровень уверенности человека составляет всего 97.53%
'''

from deepface import DeepFace
obj = DeepFace.verify("img1.png", "img3.png", model_name = 'ArcFace', detector_backend = 'retinaface')
print(obj["verified"])
print(obj)