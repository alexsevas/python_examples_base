#
# conda activate allpy310

import pyaudio
import wave

# Параметры аудиозаписи
FORMAT = pyaudio.paInt16
CHANNELS = 1 # количество каналов: 1- моно, 2 - стерео
RATE = 44100 # частота дискредитации
CHUNK = 1024
RECORD_SECONDS = 5  # Продолжительность записи в секундах
OUTPUT_FILENAME = "output.wav"

# Инициализация PyAudio
audio = pyaudio.PyAudio()

# Открытие потока для записи
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Начало записи...")

# Запись данных
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Запись завершена.")

# Остановка и закрытие потока
stream.stop_stream()
stream.close()
audio.terminate()

# Сохранение записанных данных в WAV файл
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Файл сохранен как {OUTPUT_FILENAME}")