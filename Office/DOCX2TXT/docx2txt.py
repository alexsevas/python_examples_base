# conda activate allpy310

# pip install python-docx lxml openpyxl PyPDF2

# Преобразование DOCX в TXT
# Для работы с DOCX файлами используем библиотеку python-docx.

from docx import Document

def docx_to_txt(docx_path, txt_path):
    doc = Document(docx_path)
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for para in doc.paragraphs:
            txt_file.write(para.text + '\n')

# Пример использования
docx_to_txt('D:\\AI_DATA\\PDF_DOC_DOCX_TXT\\example.docx', 'example.txt')
