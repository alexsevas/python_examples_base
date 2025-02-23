# conda activate retinafacep39

'''
Алгоритм выравнивания — Практическое руководство и демонстрация: folder/2_5321469466201055598.mp4
-----------------------
Современный конвейер распознавания лиц состоит из четырех общих этапов: обнаружение (detect), выравнивание (align),
нормализация (normalize), представление и верификация (represent and verify). Эксперименты показывают, что выравнивание
увеличивает точность распознавания лиц примерно на 1%.
В этом контексте RetinaFace может находить ланкарты лица, включая координаты глаз. Это позволяет применять выравнивание
к обнаруженным лицам с помощью функции извлечения лиц.
'''

import matplotlib.pyplot as plt
from retinaface import RetinaFace
faces = RetinaFace.extract_faces(img_path = "img3.png", align = True)
for face in faces:
    plt.imshow(face)
    plt.show()