# переписано под PyPDF2 3.0 версию - есть изменения в методах и их названиях
# 1)печатаем в консоли текст из PDF-документа и сохраняем в text.txt
# 2)читаем текст из text.txt и преобразуем его в audio.mp3

import pyttsx3 #conda activate xtts, all2py310
'''
import PyPDF2 #conda activate allpy39, allpy310

pdfreader = PyPDF2.PdfReader(open('C:\\PROJECTS\\_DATA_\\doc.pdf', 'rb'))

for page_num in range(0, len(pdfreader.pages)):
    text = pdfreader.pages[page_num-1].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

with open("text.txt", "w", encoding="utf-8") as file:
    file.write(clean_text)
'''

# загружаем данные из index.html и работаем дальше с ними
with open("text.txt", encoding="utf-8") as file:
    clean_text = file.read()

speaker = pyttsx3.init()
speaker.save_to_file(clean_text, 'audio_doc.mp3')
speaker.runAndWait()

speaker.stop()
#'''