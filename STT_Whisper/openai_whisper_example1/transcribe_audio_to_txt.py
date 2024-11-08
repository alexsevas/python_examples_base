# Developed by MikyPo
# More code for DA here: https://dzen.ru/mikypo
#
# ENV all2py310, extras, whisperpy310
# conda activate extras (процесс на GPU !!!)
# conda activate all2py310 (процесс на CPU)
# conda activate whisperpy310 (процесс на CPU)


# pip install git+https://github.com/openai/whisper.git --quiet
# pip install ffmpeg --quiet

import os
import whisper

# Установим путь к модели в переменную окружения
os.environ['WHISPER_CACHE_DIR'] = 'C:/Users/A43X/.cache/whisper'
language = 'fr'
#language = 'ru'
model_path = 'C:/Users/A43X/.cache/whisper/base.pt'
#model_path = 'C:/Users/A43X/.cache/whisper/medium.pt'
#model_path = 'C:/Users/A43X/.cache/whisper/large-v3.pt'

# Загружаем модель
if os.path.exists(model_path):
    model = whisper.load_model(model_path)
else:
    model = whisper.load_model('large')  # Или пусть скачает из интернета
    
options = whisper.DecodingOptions(language=language)

# Загружаем аудио файл test_ru.wav
audio = whisper.load_audio('C:\\PROJECTS\\_DATA_\\audio.mp3') # lng - FR
#audio = whisper.load_audio('test_ru.wav')

#audio = whisper.pad_or_trim(audio) #из-за это строки распознает только часть текста (одну строку пишет в файл)

# Выполняем распознавание
result = model.transcribe(audio)

# Выводим результат
print(result['text'])

# Запись результата в файл text.txt
with open ('text.txt', 'w', encoding="utf-8") as file:
    file.write(result['text'])