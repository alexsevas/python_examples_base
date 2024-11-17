# conda activate allpy310
# ENV allpy39, allpy310, all2py310

from pytube import Playlist

playlist = Playlist("https://www.youtube.com/watch?v=krBNXGa0gu8&list=PL2wnfZ7lfS0-r4PRFImooNn4MCSBGQpVp")

print(f"Загрузка плейлиста: {playlist.title}")
for video in playlist.videos:
    video.streams.first().download()
    print(f"Видео {video.title} загружено")
