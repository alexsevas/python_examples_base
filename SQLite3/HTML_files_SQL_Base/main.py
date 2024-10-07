import base64
import platform
import sqlite3
import sys
import tempfile
import webbrowser
from os import system
from pathlib import Path

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from doc import open_base, delete_from_base, encode_b64, \
    save_to_base, create_base, save_doc_from_base, decode_b64, vacuum_base, update_data, select_tag
from doc_b import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.base_name = None
        self.data = None

        self.ui.saveButton.setEnabled(False)
        self.ui.deleteButton.setEnabled(False)
        self.ui.eraseButton.setEnabled(False)
        self.ui.insertButton.setEnabled(False)
        self.ui.extractButton.setEnabled(False)
        self.ui.editButton.setEnabled(False)
        self.ui.tagButton.setEnabled(False)
        self.ui.clearButton.setEnabled(False)
        self.ui.vacuumButton.setEnabled(False)
        self.ui.tagEdit.setEnabled(False)
        self.ui.searchEdit.setEnabled(False)
        self.ui.tagBox.setEnabled(False)
        self.ui.tabTag.setEnabled(False)
        self.ui.filterButton.setEnabled(False)

        self.pix = QtGui.QPixmap(str(Path.cwd() / 'pic' / 'tag.png')).scaled(41, 40)
        self.ui.tagPic.setPixmap(self.pix)
        self.pix = QtGui.QPixmap(str(Path.cwd() / 'pic' / 'document.png')).scaled(41, 40)
        self.ui.docPic.setPixmap(self.pix)

        self.ui.docTable.horizontalHeader().resizeSection(0, 740)
        self.ui.docTable.horizontalHeader().resizeSection(1, 185)
        self.ui.baseOpenName.setText('Open Base: None')

        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.openButton.clicked.connect(self.open)
        self.ui.deleteButton.clicked.connect(self.delete)
        self.ui.eraseButton.clicked.connect(self.erase_base)
        self.ui.insertButton.clicked.connect(self.insert)
        self.ui.createButton.clicked.connect(self.create_base)
        self.ui.clearButton.clicked.connect(self.clear_text)
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.editButton.clicked.connect(self.edit)
        self.ui.tagButton.clicked.connect(self.update_tag)
        self.ui.cancelButton.clicked.connect(self.cancel)
        self.ui.vacuumButton.clicked.connect(self.vacuum)
        self.ui.filterButton.clicked.connect(self.filter_tag)
        self.ui.extractButton.clicked.connect(self.extract_all)

        self.ui.searchEdit.textChanged.connect(self.search)
        self.ui.docTable.doubleClicked.connect(self.double_click_table)

    @staticmethod
    def notify(text):
        if platform.system() == "Linux":
            system(f'''notify-send "{text}"''')
        elif platform.system() == "Windows":
            from win10toast import ToastNotifier
            ToastNotifier().show_toast(f"Docu Base", text, duration=3, threaded=True)

    @staticmethod
    def exit(self):
        """
        Обработка нажатия на кнопку завершения приложения.
        Завершение работы приложения.
        """
        QtWidgets.QApplication.quit()

    def vacuum(self):
        """
        Обработка нажатия кнопки сжатия базы данных.
        """
        if self.base_name is not None:
            vacuum_base(self.base_name)
            self.notify("[!] Base compacting completed.")
        else:
            self.notify("[!] There is no open database. Nothing to condense.")

    def create_base(self):
        """
        Обработка нажатия на кнопку создания базы данных.
        Создание базы данных. Запрос места и имени базы.
        Запуск функции по созданию.
        """
        self.button_disable()
        file, check = QFileDialog.getSaveFileName(None, "Create Base",
                                                  "new_docubase.db", "Docu Base (*.db)")
        if check:
            self.base_name = file
            self.ui.baseOpenName.setText(f'Open Base: {Path(file).name}')
            create_base(file)
            self.read_base()
            self.notify(f"[!] A database has been created: {Path(file).name}")

    def double_click_table(self):
        """
        Обработка двойного щелчка по названию документа в таблице.
        Создание временного файла с документом.
        Открытие документа из базы данных в браузере по-умолчанию.
        """
        row = self.ui.docTable.currentRow()
        _, _, data = save_doc_from_base(self.base_name, self.ui.docTable.item(row, 0).text())
        dec = base64.decodebytes(data)
        with tempfile.NamedTemporaryFile('wb', delete=False, suffix='.html') as f:
            f.write(dec)
        webbrowser.open(f'file://{f.name}')

    def update_tag(self):
        """
        Обработка нажатия кнопки обновления тегов в БД.
        """
        name = self.ui.nameEdit.text()
        tag = self.ui.tagEdit.text().lower()
        update_data(self.base_name, name, tag, self.data)
        self.ui.tagEdit.setEnabled(False)
        self.ui.tagButton.setEnabled(False)
        self.ui.tagEdit.setText("")
        self.ui.nameEdit.setText("")
        self.ui.tabTag.setEnabled(False)
        self.ui.tabBase.setEnabled(True)
        self.ui.tabWidget.setCurrentIndex(0)
        self.read_base()
        self.data = None

    def cancel(self):
        """
        Обработка нажатия кнопки отмены при редактировании тегов.
        """
        self.ui.tagEdit.setText("")
        self.ui.nameEdit.setText("")
        self.data = None
        self.ui.tabTag.setEnabled(False)
        self.ui.tabBase.setEnabled(True)
        self.ui.tabWidget.setCurrentIndex(0)

    def edit(self):
        """
        Обработка нажатия кнопки редактирования тегов.
        """
        try:
            row = self.ui.docTable.currentRow()
            name, tag, data = save_doc_from_base(self.base_name, self.ui.docTable.item(row, 0).text())
            self.ui.nameEdit.setText(name)
            self.ui.tagEdit.setText(tag)
            self.ui.tagEdit.setEnabled(True)
            self.ui.tagButton.setEnabled(True)
            self.data = data
            self.ui.tabBase.setEnabled(False)
            self.ui.tabTag.setEnabled(True)
            self.ui.tabWidget.setCurrentIndex(1)
        except AttributeError:
            self.notify("No row selected for edit")
            pass

    def clear_text(self):
        """
        Обработка нажатия на кнопку очистки текста в строке поиска.
        """
        self.ui.searchEdit.setText("")

    def filter_tag(self):
        tag = self.ui.tagBox.currentText()
        if tag == "all":
            self.read_base()
        else:
            self.ui.docTable.setRowCount(0)
            for item in select_tag(self.base_name, tag):
                row_position = self.ui.docTable.rowCount()
                self.ui.docTable.insertRow(row_position)
                self.ui.docTable.setItem(row_position, 0, QtWidgets.QTableWidgetItem(item[0]))
                self.ui.docTable.setItem(row_position, 1, QtWidgets.QTableWidgetItem(item[1]))

    def read_base(self):
        """
        Чтение данных из базы. Обработка содержимого таблицы.
        Добавление активности кнопкам.
        Вспомогательная функция.
        """
        tag_set = set()
        self.ui.docTable.setRowCount(0)
        self.ui.tagBox.clear()
        for name in open_base(self.base_name):
            row_position = self.ui.docTable.rowCount()
            self.ui.docTable.insertRow(row_position)
            self.ui.docTable.setItem(row_position, 0, QtWidgets.QTableWidgetItem(name[0]))
            self.ui.docTable.setItem(row_position, 1, QtWidgets.QTableWidgetItem(name[1]))
            if len(name[1].split(",")) > 1:
                for t in name[1].split(","):
                    tag_set.add(t.strip())
                continue
            tag_set.add(name[1])
        self.ui.tagBox.addItem("all")
        for tag in sorted(tag_set):
            self.ui.tagBox.addItem(tag)
        if self.ui.docTable.rowCount() > 0:
            self.button_enable()
        else:
            self.button_disable()
            self.ui.insertButton.setEnabled(True)
        self.ui.docTable.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)

    def button_enable(self):
        """
        Вспомогательная функция.
        Делает активными указанные кнопки.
        """
        self.ui.saveButton.setEnabled(True)
        self.ui.deleteButton.setEnabled(True)
        self.ui.eraseButton.setEnabled(True)
        self.ui.insertButton.setEnabled(True)
        self.ui.extractButton.setEnabled(True)
        self.ui.editButton.setEnabled(True)
        self.ui.vacuumButton.setEnabled(True)
        self.ui.searchEdit.setEnabled(True)
        self.ui.clearButton.setEnabled(True)
        self.ui.tagBox.setEnabled(True)
        self.ui.filterButton.setEnabled(True)

    def button_disable(self):
        """
        Вспомогательная функция.
        Делает не активными указанные кнопки.
        """
        self.ui.saveButton.setEnabled(False)
        self.ui.deleteButton.setEnabled(False)
        self.ui.eraseButton.setEnabled(False)
        self.ui.insertButton.setEnabled(False)
        self.ui.extractButton.setEnabled(False)
        self.ui.editButton.setEnabled(False)
        self.ui.searchEdit.setEnabled(False)
        self.ui.clearButton.setEnabled(False)
        self.ui.tagBox.setEnabled(False)
        self.ui.filterButton.setEnabled(False)

    def open(self):
        """
        Обработка нажатия на кнопку открытия базы данных.
        """
        self.button_disable()
        file, check = QFileDialog.getOpenFileName(None, "Open Docu Base", "", "Docu Base (*.db)")
        if check:
            self.base_name = file
            self.ui.vacuumButton.setEnabled(True)
            self.ui.baseOpenName.setText(f'Open Base: {Path(file).name}')
            self.read_base()

    def save(self):
        """
        Обработка нажатия на кнопку сохранения выделенного документа из базы.
        """
        try:
            row = self.ui.docTable.currentRow()
            name, _, data = save_doc_from_base(self.base_name, self.ui.docTable.item(row, 0).text())
            file, check = QFileDialog.getSaveFileName(None, "Save From Base", f"{name}.html", "HTML (*.html)")
            if check:
                decode_b64(file, data)
        except AttributeError:
            self.notify("No row selected for save")
            pass

    def extract_all(self):
        """
        Обработка нажатия на кнопку сохранения всех документов из базы.
        """
        if self.ui.docTable.rowCount() > 0:
            directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Selecting a folder to save in", ".")
            feeds = []
            for i in range(self.ui.docTable.rowCount()):
                _, _, data = save_doc_from_base(self.base_name, self.ui.docTable.item(i, 0).text())
                file = Path(directory) / f'{self.ui.docTable.item(i, 0).text()}.html'
                feeds.append([file, data])

            for feed in feeds:
                self.ui.baseOpenName.setText(f'Extract: {Path(feed[0]).name}')
                decode_b64(feed[0], feed[1])
            self.ui.baseOpenName.setText(f'Open Base: {Path(self.base_name).name}')
            self.notify(f"[!] All data is saved in a folder: {directory}")

    @staticmethod
    def msg_box(name):
        """
        Создание диалогового окна для проверки существования записей в базе.
        :param name: Название статьи.
        :return: Код нажатой кнопки.
        """
        msg = QMessageBox()
        msg.setWindowTitle("Database warning")
        msg.setText(f'The "{name}" file exists in the database!\nAdd a file to the database?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return msg.exec_()

    def insert(self):
        """
        Обработка нажатия на кнопку добавления документов в базу данных.
        """
        conn = sqlite3.connect(self.base_name)
        cur = conn.cursor()
        sel = """SELECT name FROM documents WHERE name = ?"""
        files, check = QFileDialog.getOpenFileNames(None, "Open HTML",
                                                    "", "HTML (*.html)")
        data_list = []
        if check:
            for file in files:
                if cur.execute(sel, (Path(file).name.replace(".html", ""),)).fetchone() is not None:
                    x = self.msg_box(Path(file).name.replace(".html", ""))
                    if x == 65536:
                        continue
                    elif x == 16384:
                        self.ui.baseOpenName.setText(f'Insert: {Path(file).name}')
                        data_list.append(encode_b64(file))
                        continue
                self.ui.baseOpenName.setText(f'Insert: {Path(file).name}')
                data_list.append(encode_b64(file))
        cur.close()
        conn.close()

        if data_list:
            save_to_base(self.base_name, data_list)
            self.ui.docTable.setRowCount(0)
            self.read_base()
            self.ui.baseOpenName.setText(f'Open Base: {Path(self.base_name).name}')
            self.notify("[!] All files are added to the database")

    def search(self, s):
        """
        Поиск документов в таблице.
        :param s: Вводимый текст в строке поиска.
        """
        self.ui.docTable.setCurrentItem(None)
        if not s:
            return
        matching_items = self.ui.docTable.findItems(s, Qt.MatchContains)
        if matching_items:
            for item in matching_items:
                item.setSelected(True)

    def erase_base(self):
        """
        Обработка нажатия на кнопку удаления всех документов из базы.
        """
        for i in range(self.ui.docTable.rowCount()):
            delete_from_base(self.base_name, self.ui.docTable.item(i, 0).text())
        self.ui.tagBox.clear()
        self.read_base()
        self.ui.vacuumButton.setEnabled(True)
        self.notify("All documents have been deleted from the database")

    def delete(self):
        """
        Обработка нажатия на кнопку удаления выделенного документа из базы.
        """
        try:
            row = self.ui.docTable.currentRow()
            delete_from_base(self.base_name, self.ui.docTable.item(row, 0).text())
            self.ui.docTable.removeRow(row)
            self.read_base()
            self.ui.vacuumButton.setEnabled(True)
        except AttributeError:
            self.notify("No row selected for deletion")
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
