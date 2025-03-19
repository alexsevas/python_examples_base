import base64
import json

# Пример JSON с данными Base64
json_data = '''
{
    "image": "BASE64_ENCODED_STRING"
}
'''


# Функция для сохранения Base64 в файл JPG
def save_base64_to_jpg(base64_string, output_file):
    try:
        # Декодируем строку Base64 в бинарные данные
        image_data = base64.b64decode(base64_string)

        # Сохраняем бинарные данные в файл
        with open(output_file, 'wb') as file:
            file.write(image_data)

        print(f"Файл успешно сохранён: {output_file}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Основной код
if __name__ == "__main__":
    # Загружаем JSON
    data = json.loads(json_data)

    # Извлекаем строку Base64 из JSON
    base64_string = data.get("image")

    if base64_string:
        # Указываем путь для сохранения файла
        output_file = "output_image.jpg"

        # Сохраняем Base64 в файл JPG
        save_base64_to_jpg(base64_string, output_file)
    else:
        print("В JSON отсутствует поле 'image' или оно пустое.")
