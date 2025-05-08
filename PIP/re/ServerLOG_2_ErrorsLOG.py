# conda activate allpy310

import re

# Указываем имя лог-файла и создаем регулярное выражение для поиска "ERROR"
log_file = 'server.log'
error_pattern = re.compile(r'ERROR')

# Открываем лог-файл для чтения и новый файл для записи ошибок
with open(log_file, 'r', encoding='utf-8') as infile, \
     open('errors.log', 'w', encoding='utf-8') as outfile:
    for line in infile:
        if error_pattern.search(line):
            outfile.write(line)

print("Парсинг завершен. Все ошибки сохранены в errors.log")
