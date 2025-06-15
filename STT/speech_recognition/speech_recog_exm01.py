# conda activate allpy310

import speech_recognition as sr

# Инициализация распознавателя
recognizer = sr.Recognizer()

# Запись аудио с микрофона
with sr.Microphone() as source:
    print("Скажите что-нибудь...")
    audio = recognizer.listen(source)

# Распознавание речи с использованием Google Web Speech API
try:
    print("Google Web Speech API понял: " + recognizer.recognize_google(audio, language="ru-RU"))
except sr.UnknownValueError:
    print("Google Web Speech API не смог распознать речь")
except sr.RequestError as e:
    print("Ошибка запроса к Google Web Speech API; {0}".format(e))
