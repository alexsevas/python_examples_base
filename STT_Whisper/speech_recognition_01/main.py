# conda activate extras
# pip install openai-whisper
import whisper

# Установим путь к модели в переменную окружения
#os.environ['WHISPER_CACHE_DIR'] = 'C:/PROJECTS/_Weights_/Whisper'
language = 'ru'
#model_path = 'C:\\PROJECTS\\_Weights_\\Whisper\\large-v3.pt'
audiofile = 'C:\\PROJECTS\\_DATA_\\audio.mp3'

def speech_recognition(model='tiny', audiofile='C:\\PROJECTS\\_DATA_\\audio.mp3'):
    speech_model = whisper.load_model(model)
    options = whisper.DecodingOptions(language=language)

    # Загружаем аудио файл
    #audio = whisper.load_audio(audiofile)

    # Цель метода `pad_or_trim` - обеспечить, чтобы все входные звуковые сигналы имели согласованный размер и формат,
    # что помогает Whisper производить более точные результаты. По умолчанию Whisper использует внутреннюю частоту
    # дискретизации 16 кГц, поэтому если ваш входной звуковой сигнал имеет другую частоту дискретизации, он будет
    # ресемплирован до соответствующей внутренней частоты перед обработкой.
    #audio = whisper.pad_or_trim(audio)

    # Выполняем распознавание
    result = speech_model.transcribe(audiofile)

    with open(f'transcription_{model}.txt', 'w', encoding='utf-8') as file:
        file.write(result['text'])


def main():
    models = {1: 'tiny', 2: 'base', 3: 'small', 4: 'medium', 5: 'large'}

    for k, v in models.items():
        print(f'{k}:{v}')

    model = int(input('Выберите модель передав цифру от 1 до 5: '))

    if model not in models.keys():
        raise KeyError(f'Модели {model} нет в списке!')

    print('Запущен процесс транскрибации, пожалуйста ожидайте...')
    speech_recognition(model=models[model], audiofile=audiofile)


if __name__ == '__main__':
    main()
