import os
import pytube
from moviepy.editor import *

# Указываем URL на youtube видео
youtube_url = "https://www.youtube.com/watch?v=E6eKvji_BoE"

# Создаем PyTube объект и получаем его аудиопоток
yt = pytube.YouTube(youtube_url)
audio_stream = yt.streams.filter(only_audio=True).first()

# Скачать аудиопоток как временный файл
temp_file = audio_stream.download()

# Конвертировать аудиопоток в mp3-файл с помощью MoviePy
audio_clip = AudioFileClip(temp_file)
mp3_file = os.path.join("Give Your own path", "Name.mp3")
audio_clip.write_audiofile(mp3_file)

# Очищаем временный файл
os.remove(temp_file)

print("Аудио извлечено и сохранено в файл", mp3_file)
