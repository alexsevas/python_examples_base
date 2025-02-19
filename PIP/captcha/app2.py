# ENV allpy310

# pip install captcha

'''
Чтобы сгенерировать более сложную капчу с использованием библиотеки captcha, можно внести изменения в код, например,
увеличить количество символов в капче, изменить стиль шрифта или добавить шум.

- Увеличена длина строки капчи (length=8).
- Увеличены размеры изображения капчи (width=300, height=100).
- Добавлена возможность включения искажений и шума (хотя в этом коде это закомментировано и требует дополнительной
настройки в зависимости от конкретных требований).

Более сложные искажения и шумы могут потребовать более глубоких изменений в библиотеке captcha или использования других
инструментов. Библиотека captcha предоставляет базовые возможности для создания капчи, но она может быть не полностью
подходящей для создания высокоуровневых, сложно искаженных капч, используемых на коммерческих сайтах.
'''

from captcha.image import ImageCaptcha
import random
import string
import matplotlib.pyplot as plt

def generate_complex_captcha(length=8, width=300, height=100, distort=True):
    # Генерация случайной строки большей длины
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    random_string = ''.join(random.choice(letters) for i in range(length))

    # Создание более сложного изображения капчи
    image = ImageCaptcha(width=width, height=height)

    # Если требуется искажение, можно изменить стиль шрифта или добавить шум
    if distort:
        captcha_image = image.generate(random_string)
    else:
        captcha_image = image.create_captcha_image(random_string, color='black', background='white')

        # Пример добавления шума или искажений
        # image.create_noise_dots(captcha_image, color='black')
        # image.create_noise_curve(captcha_image, color='black')

    # Отображение капчи
    plt.imshow(plt.imread(captcha_image))
    plt.axis('off')
    plt.show()

    return random_string

# Генерация и отображение сложной капчи
captcha_text = generate_complex_captcha()
print("Сгенерированный текст капчи:", captcha_text)
