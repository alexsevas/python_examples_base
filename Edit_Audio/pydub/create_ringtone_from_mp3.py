# conda activate allpy310

# pip install pydub

from pydub import AudioSegment

# Загрузка MP3-файла
audio = AudioSegment.from_file("data/gde_more_sunday.mp3")

# Обрежем первые 41 секунду
trimmed_audio = audio[:41000]

# Добавим эффект плавного затухания
faded_audio = trimmed_audio.fade_in(2000).fade_out(2000)

# Сохраним результат
faded_audio.export("data/ringtone.mp3", format="mp3")
