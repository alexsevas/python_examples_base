# pip install ultralytics

# conda activate yolo8py311

# если torch запускается на CPU:
# 1) сходить на сайт pytorch.org и сформировать ссылку для установки под нужную ОС и CUDA (выбирать последнюю)
# 2) в сформированной команде после 'pip install' добавить --upgrade
# 3) выполнить команду, юзать torch с GPU

# проверить установку torch c GPU:
#import torch
#print(torch.cuda.is_available())

# дообучение модели yolo8 small методом transfer learning
# yolo task=classify mode=train model=yolov8s-cls.pt data=flowers_prepared epochs=20 imgsz=180

# проверка обученной модели на тестовой изображении
# yolo task=classify mode=predict model=best.pt source="test_image.png"

# использование из cmd (CLI), документация и примеры:
# docs.ultralytics.com/usage/cli/
#
# yolo TASK MODE ARGS
# Where TASK is one of [detect, segment, classify]
#       MODE is one of [train, val, predict, export, track]
#       ARGS are any number of custom 'arg=value' pairs like "imgsz=320" that override defaults

# использование из python, документация и примеры:
# docs.ultralytics.com/usage/python/

from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("yolov8s-cls.pt")

results = model.predict(source="0")

im2 = cv2.imread("test_image.png")
results = model.predict(source=im2, save=True, save_txt=True)