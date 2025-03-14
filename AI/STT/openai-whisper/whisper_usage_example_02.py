# conda allpy310

# pip install setuptools-rust
# pip install -U openai-whisper

# CMD: whisper -h

import whisper

#model = whisper.load_model("turbo")
model = whisper.load_model("large-v3")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("C:\\PROJECTS\\_DATA_\\audio_RU_41sec.wav")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio, n_mels=128).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)
