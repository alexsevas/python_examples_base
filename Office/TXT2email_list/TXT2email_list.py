# conda activate allpy310

# Извлечение из файла "LOG.txt" email-адресов и сохранения их в extracted_emails.txt

import re

# Путь к файлу логов
log_file_path = 'D:\\AI_DATA\\test_errors.txt'

# Путь к файлу, в который будут сохранены извлеченные адреса электронной почты
output_file_path = 'extracted_emails.txt'

# Регулярное выражение для поиска строк с адресами электронной почты
email_pattern = re.compile(r'RCPT TO:<([^>]+)>')

# Список для сбора найденных адресов электронной почты
extracted_emails = []

# Чтение файла логов и поиск адресов электронной почты
with open(log_file_path, 'r') as file:
    for line in file:
        match = email_pattern.search(line)
        if match:
            extracted_emails.append(match.group(1))

# Сохранение извлеченных адресов электронной почты в другой файл
with open(output_file_path, 'w') as file:
    for email in extracted_emails:
        file.write(email + '\n')
