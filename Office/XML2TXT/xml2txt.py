# conda activate allpy310

# pip install python-docx lxml openpyxl PyPDF2

# Преобразование XML в TXT
# Для работы с XML файлами используем библиотеку lxml.


from lxml import etree

def xml_to_txt(xml_path, txt_path):
    tree = etree.parse(xml_path)
    root = tree.getroot()
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for elem in root.iter():
            txt_file.write(etree.tostring(elem, pretty_print=True).decode('utf-8') + '\n')

# Пример использования
xml_to_txt('D:\\AI_DATA\\PDF_DOC_DOCX_TXT_XML\\ASD_rez_pr_grunt_0.xml', 'example.txt')
