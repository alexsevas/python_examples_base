# conda activate all2py310

# #!/usr/bin/env python3
from vosk import Model, KaldiRecognizer
import os, json
import pyaudio
import torch, threading
from pygame import mixer
import time
sluh = 1

print('Ждём пока загрузятся модели!')
#----------------------------------------------------------------------------
device = torch.device('cpu')
torch.set_num_threads(4)

mixer.init()
local_file = 'v3_1_ru.pt'
if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v2_kseniya.pt',
                                   local_file)  

modeltts = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
modeltts.to(device)

# Обёртка для функций которые надо выполнять в отдельном потоке
def thread(my_func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs, daemon=True)
        my_thread.start()
    return wrapper

def create_wav(text):
    global sluh
    if text.strip()!='':
        example_batch = [text]
        sample_rate = 24000
        fnm = 'data/' + text[:200] + '.wav'
        if not os.path.exists(fnm):
            path = modeltts.save_wav(text=text, sample_rate=sample_rate, put_accent=True, put_yo=True)
            time.sleep(0.5)
            os.rename(path, fnm)
            time.sleep(0.2)
        mixer.music.load(fnm)
        mixer.music.play()
            # Пока играет файл и не сказано Стоп, делаем паузу
        while mixer.music.get_busy():
            time.sleep(0.1)
        sluh = 1
        time.sleep(1)
        print('Слушаю вас: ')
#-----------------------------------------------------------------------
# Проверяем есть ли модель
if not os.path.exists("modelvosk"):
    print ("Скачайте модель отсюда https://github.com/alphacep/vosk-api/blob/master/doc/models.md и распакуйте в папку 'modelvosk'.")
    exit (1)

# загружаем модель распознавания речи
model = Model("modelvosk")
rec = KaldiRecognizer(model, 16000)

print('Модели загружены - говори!')

# Слушаем звук с микрофона
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

@thread
def listenmic():
    global sluh
# Ожидаем голосовых команд 
    while True:
        if sluh == 1:
            data = stream.read(200, exception_on_overflow=False)
            if len(data) == 0:
                continue
            if rec.AcceptWaveform(data):
                x=json.loads(rec.Result())
                text = x["text"]
                if text.strip()!='':
                    sluh = 0
                    print('Распознано: ', text)
                    create_wav('Вы сказали ' + text)
            else:
                #print(rec.PartialResult())
                pass

listenmic()
