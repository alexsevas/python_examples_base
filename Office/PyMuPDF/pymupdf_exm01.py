# conda activate allpy310

# pip install pymupdf

import pymupdf # imports the pymupdf library
doc = pymupdf.open("D:\\AI_DATA\\PDF\\PDF_01.pdf") # open a document

# iterate the document pages
for page in doc:
  text = page.get_text() # get plain text encoded as UTF-8
  print(text)
