# conda activate all2py310
# This script runs on Windows only, and you must have Word installed.
import win32com.client # install with "pip install pywin32"
import docx
wordFilename = 'C:\\PROJECTS\\alexsevas_projects\\python_examples_base\\Office\\Word2PDF_01\\2.docx'
pdfFilename = 'C:\\PROJECTS\\alexsevas_projects\\python_examples_base\\Office\\Word2PDF_01\\temp.pdf'

#doc = docx.Document()
# Code to create Word document goes here.
#doc.save(wordFilename)

wdFormatPDF = 17 # Word's numeric code for PDFs.
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()
