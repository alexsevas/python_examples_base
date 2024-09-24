import os
from bs4 import BeautifulSoup

def main():
    # Сканируем текущую папку на наличие файлов с расширением *.KML и выводим их на экран консоли
    kml_files = [f for f in os.listdir('.') if f.endswith('.KML') or f.endswith('.kml')]

    print("Найденные файлы KML:")
    for i, file in enumerate(kml_files):
        print(f"{i+1}. {file}")

    # Ожидаем ввода от пользователя порядкового номера файла
    while True:
        try:
            file_num = int(input("Введите номер файла, который вы хотите обработать: "))
            if 1 <= file_num <= len(kml_files):
                break
            else:
                print("Неверный ввод. Пожалуйста, введите число между 1 и", len(kml_files))
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")

    # Передаем выбранный файл в скрипт
    selected_file = kml_files[file_num - 1]
    print(f"Обрабатываем файл: {selected_file}")

    with open(selected_file, 'r') as f:
        s = BeautifulSoup(f, 'xml')

        filename = os.path.splitext(selected_file)[0]+".txt"

        with open(filename, 'w') as file:
            for coords in s.find_all('coordinates'):
                str = coords.string
                print(str)
                str += "\n"
                file.write(str)

if __name__ == "__main__":
    main()