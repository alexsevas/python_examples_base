# conda activate allpy310

# pip install pydub

from pydub import AudioSegment

# Загрузка MP3-файла
audio = AudioSegment.from_file("data/gde_more_sunday.mp3")

# Ускорение (2x)
faster_audio = audio.speedup(playback_speed=2.0)
# Замедление (0.5x)
slower_audio = audio.speedup(playback_speed=0.5)

# Сохранение
faster_audio.export("faster_example.mp3", format="mp3")
slower_audio.export("slower_example.mp3", format="mp3")
