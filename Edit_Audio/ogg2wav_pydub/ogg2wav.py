# conda

# Импортируем необходимые модули
from pydub import AudioSegment  # Для работы с аудиофайлами
from pydub.utils import make_chunks  # Если нужно разбивать файл на чанки

# Путь к входному файлу (OGG) и выходному файлу (WAV)
input_file = "alexsevas_1min.ogg"  # Исходный файл в формате OGG
output_file = "output_file.wav"  # Результирующий файл в формате WAV

# Загружаем OGG файл
audio = AudioSegment.from_ogg(input_file)

# Устанавливаем параметры для XTTS:
# - Частота дискретизации: 22050 Гц
# - Моно звук (один канал)
# - Битовая глубина: 16 бит
converted_audio = audio.set_frame_rate(22050).set_channels(1).set_sample_width(2)

# Сохраняем преобразованный файл в формате WAV
converted_audio.export(output_file, format="wav")

print(f"Конвертация завершена. Файл сохранен как {output_file}")