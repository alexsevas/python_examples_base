# conda activate allpy310

# pip install -U captcha pillow
from captcha.image import ImageCaptcha

# Создаем объект изображения, указываем нужный размер
image = ImageCaptcha(width=250, height=120)

# Текст капчи
text = "ADIDAS2025"

# создаем изображение на основе переданного текста
data = image.generate(text)

# сохраняем изображение
image.write(text, "captcha.png")