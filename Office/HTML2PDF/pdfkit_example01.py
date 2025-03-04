# conda activate allpy310
# pip install pdfkit

import pdfkit

pdfkit.from_url('http://google.com', 'out.pdf')
#pdfkit.from_file('D:\Tutorials_BASE\Coding\Python_GIS\Использование ArcGIS API for Python в Jupyter Notebook _ Блог компании Техносерв _ Хабр.htm', 'out2.pdf')
#pdfkit.from_string('Hello!', 'out3.pdf')

'''
wkhtmltopdf - в качестве бэкэнда используется.
В Windows надо установить wkhtmltopdf и прописать путь к его папке в PATH
'''
