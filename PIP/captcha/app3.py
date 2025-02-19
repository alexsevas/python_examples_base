# ENV allpy310
# pip install captcha

'''
В этом коде используется ImageDraw из Pillow для рисования линий. Можно настроить количество линий (параметр lines)
и их внешний вид (цвет, толщину), а также сделать их более случайными по направлению и длине.
'''

from captcha.image import ImageCaptcha
from PIL import ImageDraw
import random
import string
import matplotlib.pyplot as plt

def generate_complex_captcha(length=8, width=300, height=100, lines=7):
    # Генерация случайной строки
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    random_string = ''.join(random.choice(letters) for i in range(length))

    # Создание изображения капчи
    image = ImageCaptcha(width=width, height=height)
    captcha_image = image.generate_image(random_string)

    # Добавление случайных линий
    draw = ImageDraw.Draw(captcha_image)
    for _ in range(lines):
        start = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([start, end], fill='green', width=2)

    # Отображение капчи
    plt.imshow(captcha_image)
    plt.axis('off')
    plt.show()

    return random_string

# Генерация и отображение сложной капчи
captcha_text = generate_complex_captcha()
print("Сгенерированный текст капчи:", captcha_text)