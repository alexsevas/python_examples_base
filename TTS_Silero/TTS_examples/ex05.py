from TTS.api import TTS

# Используем многоголосую модель
tts = TTS(model_name="tts_models/en/ljspeech/glow-tts", progress_bar=False, gpu=False)

# Проверяем, является ли модель многоголосой
if tts.is_multi_speaker:
    print("Доступные голоса:")
    print(tts.speakers)  # Выводим список голосов

    # Выбираем первый доступный голос
    tts.tts_to_file(
        text="Test TTS model - Hello, people!",
        speaker=tts.speakers[0],  # Указываем конкретный голос
        file_path="output5.wav"
    )
else:
    print("Модель одноголосовая.")
    tts.tts_to_file(
        text="Test TTS model - Hello, people!",
        file_path="output5.wav"
    )