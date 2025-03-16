# conda activate allpy310

# pip install PyPDF2
# Данный код работает с версией библиотеки PyPDF2 <3.0.0

from PyPDF2 import PdfFileWriter, PdfFileReader

writer = PdfFileWriter()
file = "D:\\AI_DATA\\PDF_DOC_DOCX_TXT_XML\\PDF_01.pdf"
reader = PdfFileReader(file)

for page in range(reader.numPages):
    writer.addPage(reader.getPage(page))
writer.encrypt("passwordtest")

with open(f'test_encrypt_file.pdf', 'wb') as file:
    writer.write(file)

print('PDF - encrypted!')