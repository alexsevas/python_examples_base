# conda activate extras2

import g4f
import requests

from g4f.client import Client
from g4f.Provider.Blackbox import Blackbox

# Initialize the GPT client with the desired provider and api key
client = Client(
    api_key="", # DELETE API KEY !!!
    provider=Blackbox
)

#image = requests.get("https://raw.githubusercontent.com/xtekky/gpt4free/refs/heads/main/docs/images/cat.jpeg", stream=True).raw
image = open("C:\\PROJECTS\\BASE\\AI\\gpt4free\\generated_images\\1742373587_image_2b00de14bd5c0288.jpg", "rb")

response = client.chat.completions.create(
    model=g4f.models.default,
    messages=[
        {
            "role": "user",
            "content": "Что изображено на фото? Ответь подробно. Отвечай только на русском языке"
        }
    ],
    image=image
    # Add any other necessary parameters
)

print(response.choices[0].message.content)

'''
**Описание изображения**

- **Субъект на изображении**: На фото изображён белый медведь.
- **Положение**: Медведь расположен прямо перед камерой, смотрит прямо на зрителя.
- **Внешний вид**:
  - Шерсть: Белый и пушистый, выглядит здоровым и крепким.
  - Лицо: Большие тёмные глаза и широкий нос.
- **Окружение**:
  - Фон: Зеленая трава, камни и несколько куртинок травы.
  - Поверхность: Кажется, что медведь находится на открытой местности, возможно, это северный пейзаж.

**Общие впечатления**:
- Изображение выглядит ярким и привлекательным. Медведь кажется дружелюбным, что может вызывать положительные эмоции у зрителя.
'''