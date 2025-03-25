# conda activate OCRpy310

# pip install pytesseract

from PIL import Image
import pytesseract

# Укажите путь к исполняемому файлу tesseract, если необходимо
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Открываем изображение
image = Image.open('rov01.png')

# Распознаем текст
text = pytesseract.image_to_string(image, lang='eng')

print(text)