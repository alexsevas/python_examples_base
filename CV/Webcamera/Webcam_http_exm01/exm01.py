import cv2
import requests

# URL видеопотока с веб-камеры
# Замените URL на актуальный:
# тут варианты - https://g33ktricks.blogspot.com/p/the-rtsp-real-time-streaming-protocol.html
# video_url = "http://77.222.181.11:8080/mjpg/video.mjpg"
video_url = "http://67.53.46.161:65123/mjpg/video.mjpg"

# Проверяем доступ
# Проверяем доступность URL перед началом работы
try:
    response = requests.head(video_url, timeout=5)
    if response.status_code != 200:
        raise ValueError(f"Недоступный видеопоток. Код ответа: {response.status_code}")
except Exception as e:
    print(f"Ошибка при подключении к видеопотоку: {e}")
    exit(1)

# Открываем поток с помощью OpenCV
cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("Не удалось открыть видеопоток.")
    exit(1)

# Имя окна для отображения видеопотока
window_name = "Видеопоток из Нью-Йорка"

# Основной цикл для отображения видеопотока
while True:
    ret, frame = cap.read()

    # Если кадр получен корректно
    if ret:
        # Отображаем видеокадр в окне
        cv2.imshow(window_name, frame)
    else:
        print("Ошибка при чтении кадра.")
        break

    # Завершаем работу программы при нажатии клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()
