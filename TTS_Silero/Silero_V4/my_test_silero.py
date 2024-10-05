# conda activate py310torch231gpu
# ENV py39torch231gpu, py310torch231gpu, py311torch231gpu
# а для запуска silerotts_portable нужен кратковременно инет, для загрузки yml

# V4

import os
import torch

device = torch.device('cuda')
torch.set_num_threads(4)
local_file = 'model.pt'

'''# при наличии инета попробовать прогрузить новые модели из torch.hub torch.hub
if not os.path.isfile(local_file):
    torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v4_ru.pt',
                                   local_file)  
'''
model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)

example_text = 'В недрах тундры выдры в г+етрах т+ырят в вёдра +ядра к+едров. Раз, два, три, четыри, пять - вышел зайчик погулять!'
sample_rate = 48000
speaker = 'eugene' # aidar, baya, kseniya, xenia, eugene, random

audio_paths = model.save_wav(text=example_text,
                             speaker=speaker,
                             sample_rate=sample_rate)