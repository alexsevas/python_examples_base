# Отправка email с вложением

import smtplib
import os
from email.message import EmailMessage

# 🔹 Настройки почты (используем Gmail)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"
EMAIL_RECEIVER = "receiver_email@gmail.com"

# 🔹 Создание email
msg = EmailMessage()
msg["Subject"] = "📩 Автоматическое письмо"
msg["From"] = EMAIL_SENDER
msg["To"] = EMAIL_RECEIVER
msg.set_content("Привет! Это тестовое письмо с вложением.")

# 🔹 Добавление вложения
file_path = "file.pdf"  # Укажите файл, который хотите отправить
if os.path.exists(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()
        file_name = os.path.basename(file_path)
        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

# 🔹 Отправка email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Шифруем соединение
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
    print("✅ Письмо успешно отправлено!")
except Exception as e:
    print("❌ Ошибка отправки:", e)
