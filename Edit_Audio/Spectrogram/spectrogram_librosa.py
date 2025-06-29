# conda activate py310test

# Визуализация аудиофайла (волна и спектрограмма)
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# 🔹 Путь к аудиофайлу
audio_path = "audio.wav"  # mp3 тоже поддерживается

# 🔹 Загрузка аудио
y, sr = librosa.load(audio_path)

# 🔹 Построение графиков
plt.figure(figsize=(12, 6))

# Временная волна
plt.subplot(2, 1, 1)
librosa.display.waveshow(y, sr=sr)
plt.title("Аудиосигнал во времени")

# Спектрограмма
plt.subplot(2, 1, 2)
D = librosa.amplitude_to_db(abs(librosa.stft(y)), ref=np.max)
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar(format="%+2.0f dB")
plt.title("Спектрограмма")

plt.tight_layout()
plt.show()
