# GPT
# 403
# ENV allpy311

# pip install yt-dlp

from pytube import YouTube
import logging

logging.basicConfig(level=logging.DEBUG)
yt = YouTube("https://www.youtube.com/watch?v=3WUnBrqB3uQ")
yt.streams.first().download()

