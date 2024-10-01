# conda activate extras

# pip install transformers

from transformers import pipeline

import torch

device = 0 if torch.cuda.is_available() else "cpu"
file = "D:\\AI\\p1.wav"
#file = "D:\\AI\\ПОДКАСТЫ\\Podlodka #102 - Многопоточность.mp3"

#используемая модель хранится тут в кэше: C:\Users\A43X\.cache\huggingface\hub\models--openai--whisper-large-v2\
pipe = pipeline(task="automatic-speech-recognition", model="openai/whisper-large-v2", chunk_length_s=30, device=device)
text = pipe(file, batch_size=8, return_timestamps=True)["text"] #original
#text = pipe(file, batch_size=8, generate_kwargs={"task": "translate"},return_timestamps=True)["text"] #to ENG
#print(text)

with open("result.txt", "w", encoding="utf-8") as file:
    file.write(text)

del pipe
torch.cuda.empty_cache()


