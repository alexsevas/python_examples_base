#
# conda activate allpy310

import os
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextBrowser

import sys

class KMLConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("KML Converter")
        self.setGeometry(700, 300, 500, 500)
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Из списка найденных KML-файлов в папке с программой,\nвведите номер файла для преобразования в TXT:")
        layout.addWidget(label)

        self.file_num_input = QLineEdit()
        layout.addWidget(self.file_num_input)

        button = QPushButton("Convert")
        button.clicked.connect(self.convertFile)
        layout.addWidget(button)

        self.result_browser = QTextBrowser()
        layout.addWidget(self.result_browser)

        self.result_browser.append("Найденные файлы KML:\n")
        for i, file in enumerate(kml_files):
            self.result_browser.append(f"{i + 1}. {file}")

    def convertFile(self):
        try:

            file_num = int(self.file_num_input.text())
            if 1 <= file_num <= len(kml_files):
                selected_file = kml_files[file_num - 1]
                print(f"Processing file: {selected_file}")

                with open(selected_file, 'r', encoding='utf-8') as f:
                    s = BeautifulSoup(f, 'xml')

                    filename = os.path.splitext(selected_file)[0] + ".txt"

                    with open(filename, 'w') as file:
                        for coords in s.find_all('coordinates'):
                            str = coords.string
                            print(str)
                            str += "\n"
                            file.write(str)
                        for coords in s.find_all('gx:coord'):
                            str = coords.string
                            print(str)
                            str += "\n"
                            file.write(str)

                self.result_browser.append(f"\nКонвертация {selected_file} завершена!\nРезультата сохранен в {filename}")

            else:
                self.result_browser.append("Invalid input. Please enter a number between 1 and", len(kml_files))
        except ValueError:
            self.result_browser.append("Invalid input. Please enter a number.")

if __name__ == "__main__":
    kml_files = [f for f in os.listdir('.') if f.endswith('.KML') or f.endswith('.kml')]

    app = QApplication(sys.argv)
    converter = KMLConverter()
    converter.show()
    sys.exit(app.exec_())