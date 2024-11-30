# pip install qrcode[pil]
import qrcode

# Текст или ссылка для преобразования в QR-код
data = "If you wanna be ok - fuck the woman every day!"

# Создание объекта QR-кода
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

# Добавление данных в QR-код
qr.add_data(data)
qr.make(fit=True)

# Создание изображения QR-кода
img = qr.make_image(fill_color="black", back_color="white")

# Сохранение изображения в файл
img.save("xo_py_qrcode.png")
