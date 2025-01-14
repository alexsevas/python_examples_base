# 403
# ENV allpy311

# pip install pytube

from pytube import YouTube

# Укажите URL-адрес видео
video_url = "https://www.youtube.com/watch?v=3WUnBrqB3uQ"

# Создайте объект YouTube
yt = YouTube(video_url)

# Загрузите видео
#yt.streams.get_audio_only()
yt.streams.first().download()
