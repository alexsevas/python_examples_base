# conda activate xtts

# Импортируем необходимые модули
from pydub import AudioSegment  # Для работы с аудиофайлами
import os

# Путь к исходному WAV-файлу и выходному файлу
input_file = "output_file.wav"  # Исходный файл
output_file = "outputfile_cut.wav"  # Вырезанный фрагмент будет сохранён здесь

# Загружаем WAV-файл
audio = AudioSegment.from_wav(input_file)

# Определяем временные метки для вырезания (в миллисекундах)
start_time = 15000  # Начало вырезания (5 секунд)
end_time = 45000   # Конец вырезания (10 секунд)

# Вырезаем нужный фрагмент
# Время указано в миллисекундах, поэтому 5000 = 5 секунд, 10000 = 10 секунд
extracted_audio = audio[start_time:end_time]

# Сохраняем вырезанный фрагмент в новый файл
extracted_audio.export(output_file, format="wav")

print(f"Вырезанный фрагмент сохранён как {output_file}")

# Воспроизводим файл
os.system("start outputfile_cut.wav")  # Для Windows