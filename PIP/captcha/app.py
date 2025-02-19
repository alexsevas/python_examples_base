# ENV allpy310

# pip install captcha

from captcha.image import ImageCaptcha
import random
import string
import matplotlib.pyplot as plt

def generate_captcha():
    # Генерация случайной строки
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    random_string = ''.join(random.choice(letters) for i in range(6))

    # Создание изображения капчи
    image = ImageCaptcha(width=280, height=90)
    captcha_image = image.generate(random_string)

    # Отображение капчи
    plt.imshow(plt.imread(captcha_image))
    plt.axis('off')
    plt.show()

    return random_string

# Генерация и отображение капчи
captcha_text = generate_captcha()
print("Сгенерированный текст капчи:", captcha_text)