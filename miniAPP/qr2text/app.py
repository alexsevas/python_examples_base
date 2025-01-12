# env allpy311

# pip install qr2text

import pyqrcode

qrcode = pyqrcode.create('https://ya.ru/')
print(qrcode.terminal())