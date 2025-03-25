# conda activate allpy310

# pip install pydub

from pydub import AudioSegment

# Загрузка аудиофайла
audio = AudioSegment.from_file("data/gde_more_sunday.mp3")

# Обрезка аудио с 41-й по 56-ю секунду
audio_cut = audio[41000:56000]

# Изменение громкости на +3 дБ
quieter_audio = audio_cut + 3

# Экспорт измененного аудиофайла
quieter_audio.export("data/output.mp3", format="mp3")
