# conda activate deepfacepy39

import face_recognition
import cv2
import os
from datetime import datetime

KNOWN_DIR = "known_faces"
log_file = "face_log.txt"

known_encodings = []
known_names = []

# Загружаем известные лица
for filename in os.listdir(KNOWN_DIR):
    image = face_recognition.load_image_file(os.path.join(KNOWN_DIR, filename))
    encoding = face_recognition.face_encodings(image)[0]
    known_encodings.append(encoding)
    known_names.append(os.path.splitext(filename)[0])

# Запускаем веб-камеру
video = cv2.VideoCapture(0)

print("🧠 Распознавание началось. Нажми Q для выхода.")
while True:
    ret, frame = video.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for (top, right, bottom, left), encoding in zip(faces, encodings):
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Неизвестен"

        if True in matches:
            idx = matches.index(True)
            name = known_names[idx]
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()}: {name} замечен\n")

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("📷 Распознавание лиц", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
