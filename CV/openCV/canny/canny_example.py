import cv2
import numpy as np


def process_image(image_path):
    # Загружаем изображение
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        print("Ошибка: не удалось загрузить изображение.")
        return

    # Преобразуем изображение в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Применяем размытие для снижения шума
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Выполняем обнаружение краев методом Кэнни
    edges = cv2.Canny(blurred, 50, 150)

    # Показываем результат
    cv2.imshow('Original Image', image)
    cv2.imshow('Edge Detection', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Укажите путь к изображению
image_path = 'C:\\PROJECTS\\_DATA_\\images_with_bg\\deOp5GhmLzk.jpg'  # Замените на путь к вашему изображению
process_image(image_path)
