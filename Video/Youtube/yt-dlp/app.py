# pip install yt-dlp

# conda activate allpy310

import yt_dlp

url = "https://www.youtube.com/watch?v=k_k7P9Tcm3A"

ydlp_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'noplaylist': True
}

with yt_dlp.YoutubeDL(ydlp_opts) as ydl:
    # скачиваем видео
    ydl.download([url])

