# conda activate extras

# pip install transformers

from transformers import pipeline
transcriber = pipeline(model="openai/whisper-large-v2")
#transcriber("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/1.flac")
result = transcriber("D:\AI\p1.wav")
print(result)