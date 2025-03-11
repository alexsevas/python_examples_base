# activate allpy310

# Автоматическое преобразование речи в текст с помощью Vosk (локальный ASR)

import os
import queue
import sounddevice as sd
import vosk
import json

# 🔹 Укажите путь к модели Vosk
MODEL_PATH = "vosk-model-small-ru-0.22"  # Для русского языка

# 🔹 Настройки аудиозахвата
SAMPLE_RATE = 16000  # Частота дискретизации
DEVICE = None  # Использовать стандартное аудиоустройство

# 🔹 Очередь для обработки аудио
q = queue.Queue()

# 🔹 Функция обработки аудиопотока
def callback(indata, frames, time, status):
    if status:
        print(status, flush=True)
    q.put(bytes(indata))

# 🔹 Загрузка модели Vosk
if not os.path.exists(MODEL_PATH):
    print("❌ Модель не найдена! Скачайте и распакуйте её.")
    exit(1)

model = vosk.Model(MODEL_PATH)
recognizer = vosk.KaldiRecognizer(model, SAMPLE_RATE)

# 🔹 Запуск захвата аудио и распознавания
print("🎤 Говорите...")

with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=8000, device=DEVICE, dtype="int16",
                       channels=1, callback=callback):
    while True:
        data = q.get()
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "").strip()
            if text:
                print(f"📝 Распознанный текст: {text}")
