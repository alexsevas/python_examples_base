# conda activate allpy310

# pip install gTTS
# online Работа - использует интернет-соединение

from gtts import gTTS
import os

# Текст для преобразования
text = "Здорова, кожаный! Проверка связи!"

# Создаем объект TTS
tts = gTTS(text=text, lang='ru')

# Сохраняем файл с речью
tts.save("output.mp3")

# Воспроизводим файл
os.system("start output.mp3")  # Для Windows
