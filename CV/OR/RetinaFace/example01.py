# conda activate 3dpy39

# первый запуск:
# 24-11-12 21:41:57 - retinaface.h5 will be downloaded from the url
# https://github.com/serengil/deepface_models/releases/download/v1.0/retinaface.h5
# Downloading...
# From: https://github.com/serengil/deepface_models/releases/download/v1.0/retinaface.h5
# To: C:\Users\A43X\.deepface\weights\retinaface.h5

import json
import numpy as np

from retinaface import RetinaFace
resp = RetinaFace.detect_faces("fe.jpg")
print (resp)

# Преобразование значений NumPy в стандартные типы Python
def numpy_to_python(obj):
    if isinstance(obj, (np.integer, np.floating)):
        return int(obj) if isinstance(obj, np.integer) else float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# Сохранение словаря в JSON файл с использованием контекста with
file_path = 'example.json'
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(resp, file, default=numpy_to_python, ensure_ascii=False, indent=4)


