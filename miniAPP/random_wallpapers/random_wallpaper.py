# conda activate allpy310

# Автоматическая смена обоев рабочего стола

import requests
import os
import ctypes
from PIL import Image

# 🔹 URL для скачивания случайного изображения с Unsplash
#url = "https://source.unsplash.com/random/1920x1080"
url = "https://picsum.photos/2560/1600"
#url = "https://images.unsplash.com/photo-1511300636408-a63a89df3482?ixlib=rb-4.1.0&q=85&fm=jpg&crop=entropy&cs=srgb&dl=luca-micheli-ruWkmt3nU58-unsplash.jpg&w=2400"

# 🔹 Путь к файлу обоев
wallpaper_path = os.path.join(os.getcwd(), "wallpaper.jpg")

# 🔹 Скачиваем изображение
response = requests.get(url)
if response.status_code == 200:
    with open(wallpaper_path, "wb") as file:
        file.write(response.content)
    print("✅ Новые обои скачаны!")

    # 🔹 Устанавливаем обои (Windows)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
    print("🖼 Обои обновлены!")
else:
    print("❌ Ошибка загрузки изображения")


'''
Если Unsplash недоступен, попробуйте другие сервисы:

Picsum (случайные изображения):
https://picsum.photos/800/600

LoremFlickr (тематические):
https://loremflickr.com/800/600/nature'''
