# conda activate allpy310

# pip install PyPDF2
# Данный код работает с версией библиотеки PyPDF2 >=3.0.0

from PyPDF2 import PdfWriter, PdfReader

writer = PdfWriter()
file_path = "D:\\AI_DATA\\PDF_DOC_DOCX_TXT_XML\\PDF_01.pdf"
reader = PdfReader(file_path)

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("passwordtest")

with open("test_encrypt_file.pdf", "wb") as file:
    writer.write(file)

print('PDF - encrypted!')
