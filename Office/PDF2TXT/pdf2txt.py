# conda activate allpy310

# pip install python-docx lxml openpyxl PyPDF2

# Преобразование PDF в TXT
# Для работы с PDF файлами используем библиотеку PyPDF2.

import PyPDF2

def pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                txt_file.write(page.extract_text() + '\n')

# Пример использования
pdf_to_txt('D:\\AI_DATA\\PDF_DOC_DOCX_TXT_XML\\PDF_01.pdf', 'example.txt')
