# conda activate allpy310

# обьединяет все PDF файлы, найденные в директории в один файл PDF

import PyPDF2
import os

# создание списка из найденных в папке с программой PDF файлов
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

#print(pdfFiles)

pdfWriter = PyPDF2.PdfWriter()

# цикл по всем PDF файлам
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    print(len(pdfReader.pages))

    # цикл по всем страницам PDF файла
    for pageNum in range(0, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum-1]
        pdfWriter.add_page(pageObj)

# Сохранение итогового PDF файла
with open('allminutes.pdf', 'wb') as pdfOutput:
    pdfWriter.write(pdfOutput)