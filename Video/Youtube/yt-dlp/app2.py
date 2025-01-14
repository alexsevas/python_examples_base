# GPT
# Работает с zapret
# ENV allpy311

# pip install yt-dlp

from yt_dlp import YoutubeDL
ydl_opts = {'outtmpl': 'video.mp4'}
with YoutubeDL(ydl_opts) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=3WUnBrqB3uQ"])
