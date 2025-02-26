import requests
import os

#url = "http://localhost:8020/tts_stream?text=%D0%9B%D0%BE%D0%BD%D0%B4%D0%BE%D0%BD%20-%20%D1%81%D1%82%D0%BE%D0%BB%D0%B8%D1%86%D0%B0%20%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%BE%D0%B1%D1%80%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D0%B8&speaker_wav=Kurt%20Cobain&language=ru"  # Порт может быть другим, проверьте документацию сервера
text = "Это пример текста для синтеза речи. Раз, два, три, четыри, пять - вышел зайчик побухать. Ахахаха. If you wanna be OK, fuck the woman every day!"
speaker_id = "Google"  # ID спикера (если используется предварительно обученная модель)
language = "ru"  # Язык текста (например, "en" для английского)

#url = "http://localhost:8020/tts_stream?text=красиво&speaker_wav=Valentin&language=ru"
url = "http://localhost:8020/tts_stream?text=" + text + "&speaker_wav=" + speaker_id + "&language=" + language


response = requests.get(url)

if response.status_code == 200:
    # Сохраняем полученный WAV-файл
    with open("output.wav", "wb") as f:
        f.write(response.content)
else:
    print("Ошибка:", response.text)

# Воспроизводим файл
os.system("start output.wav")  # Для Windows