# загрузить recasepunc.zip - 2ГБ веса для проверки пунктуации

# conda activate allpy310


from vosk import Model, KaldiRecognizer, SetLogLevel
from pydub import AudioSegment
import subprocess
import json
import os

SetLogLevel(0)

# Проверяем наличие модели
if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

# Устанавливаем Frame Rate
FRAME_RATE = 16000
CHANNELS=1

model = Model("model")
rec = KaldiRecognizer(model, FRAME_RATE)
rec.SetWords(True)

# Используя библиотеку pydub делаем предобработку аудио
mp3 = AudioSegment.from_mp3('audio.wav')
#mp3 = AudioSegment.from_mp3('C:\\PROJECTS\\_DATA_\\Vocals.wav')
mp3 = mp3.set_channels(CHANNELS)
mp3 = mp3.set_frame_rate(FRAME_RATE)

# Преобразуем вывод в json
rec.AcceptWaveform(mp3.raw_data)
result = rec.Result()
text = json.loads(result)["text"]

print(text)

# Добавляем пунктуацию
# Должен скачаться архив с весами модели (2Гб) - на текущий момент архив не загружен
#cased = subprocess.check_output('python3 recasepunc/recasepunc.py predict recasepunc/checkpoint', shell=True, text=True, input=text)

# Записываем результат в файл "data.txt"

with open('data.txt', 'w', encoding="utf-8") as f:
    json.dump(text, f, ensure_ascii=False, indent=4)
