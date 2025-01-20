# VENV rtts (system python 3.10)

from RealtimeSTT import AudioToTextRecorder

def process_text(text):
    print(text)

if __name__ == '__main__':
    print("Wait until it says 'speak now'")
    # recorder = AudioToTextRecorder()
    '''
    model (str, default="tiny"): Model size or path for transcription.
    Note: If a size is provided, the model will be downloaded from the Hugging Face Hub.
    Options: 'tiny', 'tiny.en', 'base', 'base.en', 'small', 'small.en', 'medium', 'medium.en', 'large-v1', 'large-v2'.
    '''
    # recorder = AudioToTextRecorder(model='medium')
    recorder = AudioToTextRecorder(model='large-v3')

    while True:
        recorder.text(process_text)