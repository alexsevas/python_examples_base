# conda activate OCRpy310

# Захват текста с экрана в реальном времени (OCR + скриншоты)
# Требуется установка Tesseract OCR (https://github.com/tesseract-ocr/tesseract).
# Укажите путь в коде, если не в PATH

# pip install pytesseract mss

import pytesseract
from PIL import Image
import mss
import time

# 🔹 Если нужно – явно указать путь к tesseract.exe (Windows)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

interval = 5  # Интервал между скриншотами в секундах

print("🔍 Старт OCR с экрана...")

with mss.mss() as sct:
    while True:
        screenshot = sct.shot(output="screen.png")

        # Открываем скриншот и распознаем текст
        img = Image.open("screen.png")
        text = pytesseract.image_to_string(img, lang="eng+rus")

        if text.strip():
            print("📄 Найден текст:")
            print(text.strip())
            print("-" * 40)

        time.sleep(interval)
