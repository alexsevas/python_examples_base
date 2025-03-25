# conda activate allpy310

# pip install pydub

from pydub import AudioSegment

# Загрузка OGG-файла
audio = AudioSegment.from_file("data/voice_bass.ogg")
# Загрузка второго трека
background = AudioSegment.from_file("data/gde_more_sunday.mp3")
# Уменьшим громкость фоновой музыки (второго трека)
background = background - 20

# Наложим второй трек на первый (начало с 1 секунды)
combined = audio.overlay(background, position=1000)

# Экспорт сведенного трека
combined.export("data/combined_track.mp3", format="mp3")
