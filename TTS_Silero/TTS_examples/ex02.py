# conda activate xtts

from TTS.api import TTS

# Init TTS with the target model name
tts = TTS(model_name="tts_models/de/thorsten/tacotron2-DDC", progress_bar=False, gpu=True)
# Run TTS
tts.tts_to_file(text="Ich bin eine Testnachricht.", file_path="output2.wav")