# conda activate 3dpy39

'''
Чтобы загрузить файл, вам нужен его идентификатор на Google Диске, который можно получить из общедоступной ссылки на файл.
Например, если ссылка на ваш файл, которой можно поделиться:

https://drive.google.com/file/d/1abcD_EfGhIjKlmNoPqr/view?usp=sharing

Идентификатор файла в данном случае — 1abcD_EfGhIjKlmNoPqr.
Вы можете скачать этот файл с помощью следующей команды:

gdown 'https://drive.google.com/uc?id=1abcD_EfGhIjKlmNoPqr'

Файл будет загружен в ваш текущий каталог.
'''

import gdown

url = "https://drive.google.com/uc?id=1l_5RK28JRL19wpT22B-DY9We3TVXnnQQ"
url2 ="https://drive.google.com/uc?id=1q1VNTtGvwvO_c7qt_bOlGOHv0LIdXVMu"

output = "test.ipynb"
gdown.download(url2, output)
