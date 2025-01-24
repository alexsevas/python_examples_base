# pip install pygame
# conda activate allpy310
import time
import easyocr
import torch

print (torch.cuda.get_device_name(0))
t = time.monotonic()

# reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('example.png')
# print(result)

reader = easyocr.Reader(['ru', 'en'])
result = reader.readtext('rov01.png', detail=0, paragraph=True)
print(result)

print(f'\nВремя работы скрипта: {time.monotonic() - t} с.')
