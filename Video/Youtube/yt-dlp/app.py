# ENV NEW ytpy310 !!!
# python -m pip install -U "yt-dlp[default]"

# pip install yt-dlp
# conda activate allpy310
# Без VPN - ошибка, разрыв соединения,
# с VPN - ловит CAPTCHA,
# c DiscordFix - работает, но иногда не может выдернуть аудиодорожку при "bestaudio"

import yt_dlp

url = "https://www.youtube.com/shorts/i-GNaWb9TjY"

ydlp_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'noplaylist': True
}

with yt_dlp.YoutubeDL(ydlp_opts) as ydl:
    # скачиваем видео
    ydl.download([url])

