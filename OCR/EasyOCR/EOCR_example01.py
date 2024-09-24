# pip install pygame
# conda activate allpy310

import easyocr

# reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('example.png')
# print(result)

reader = easyocr.Reader(['ru', 'en'])
result = reader.readtext('rov01.png', detail=0, paragraph=True)
print(result)
