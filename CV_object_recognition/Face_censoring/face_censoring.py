

import cv2

# 🔹 Загрузка изображения
image_path = "data/FOOAxrwn4cU.jpg"
image = cv2.imread(image_path)

# 🔹 Инициализация каскада Хаара для распознавания лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# 🔹 Преобразуем в ч/б
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 🔹 Поиск лиц
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

print(f"👀 Найдено лиц: {len(faces)}")

# 🔹 Размытие каждого лица
for (x, y, w, h) in faces:
    face_region = image[y:y+h, x:x+w]
    blurred = cv2.GaussianBlur(face_region, (99, 99), 30)
    image[y:y+h, x:x+w] = blurred

# 🔹 Сохраняем результат
cv2.imwrite("data/blurred_faces.jpg", image)
print("✅ Сохранено: blurred_faces.jpg")
