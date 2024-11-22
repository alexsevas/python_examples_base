# pip install yt-dlp
# conda activate allpy310
# Без VPN - ошибка, разрыв соединения,
# с VPN - ловит CAPTCHA,
# c DiscordFix - работает, но иногда не может выдернуть аудиодорожку при "bestaudio"

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

