# conda activate allpy310

'''
Автоанализ видео с охранной камеры — обнаружение движения с уведомлением:
Гед примененимо:
- Охрана дома / офиса / склада
- Автоматическая фиксация активности
- Мини система видеонаблюдения без интернета
- Анализ записей на потом
'''

import cv2
import time
import os

VIDEO_SOURCE = 0  # 0 = вебкамера, или URL/IP камеры, или путь к видеофайлу
SAVE_DIR = "motion_frames"
os.makedirs(SAVE_DIR, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_SOURCE)
_, prev_frame = cap.read()
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_frame = cv2.GaussianBlur(prev_frame, (21, 21), 0)

frame_id = 0

print("📹 Запущен анализ. Ctrl+C для остановки.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        diff = cv2.absdiff(prev_frame, gray)
        thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
        motion_percent = (cv2.countNonZero(thresh) / thresh.size) * 100

        if motion_percent > 1.0:
            filename = f"{SAVE_DIR}/motion_{frame_id}.jpg"
            cv2.imwrite(filename, frame)
            print(f"📸 Движение! Сохранил кадр: {filename}")

        prev_frame = gray
        frame_id += 1
        time.sleep(0.2)
except KeyboardInterrupt:
    print("🛑 Остановлено пользователем.")
finally:
    cap.release()