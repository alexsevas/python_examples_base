# Developed by MikyPo
# More code for DA here: https://dzen.ru/mikypo
#
# conda activate extras (в PyCharm запускает процесс на GPU !!!)
# conda activate all2py310 (в PyCharm запускает процесс на CPU)
# ENV all2py310, extras
#
# pip install git+https://github.com/openai/whisper.git --quiet
# pip install ffmpeg --quiet

import os
import whisper

# Установим путь к модели в переменную окружения
os.environ['WHISPER_CACHE_DIR'] = 'C:/AI/Whisper'
language = 'ru'
model_path = 'C:/AI/Whisper/large-v3.pt'

# Загружаем модель
if os.path.exists(model_path):
    model = whisper.load_model(model_path)
else:
    model = whisper.load_model('large')  # Или пусть скачает из интернета
    
options = whisper.DecodingOptions(language=language)

# Загружаем аудио файл
audio = whisper.load_audio('1.wav')
audio = whisper.pad_or_trim(audio)

# Выполняем распознавание
result = model.transcribe(audio)

# Выводим результат
print(result['text'])