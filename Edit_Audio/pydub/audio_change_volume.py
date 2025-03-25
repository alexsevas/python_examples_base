# conda activate allpy310

# pip install pydub

from pydub import AudioSegment

# Загрузка MP3-файла
audio = AudioSegment.from_file("data/gde_more_sunday.mp3")

# Узнаем параметры аудио
print(f"Длина файла: {len(audio) // 1000} секунд")
print(f"Громкость: {audio.dBFS:.2f} дБ")

# Уменьшим громкость на 5 дБ
quieter_audio = audio - 5
quieter_audio.export("data/output_fix_volume.mp3", format="mp3")
