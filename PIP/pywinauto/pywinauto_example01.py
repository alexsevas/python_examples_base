# conda activate allpy310

# pip install pywinauto
'''
pywinauto — это библиотека для автоматизации GUI приложений в Windows. Она позволяет автоматически управлять окнами
приложений, нажимать кнопки, вводить текст, выбирать элементы и т.д.
'''

from pywinauto import Application

# Основные компоненты:
# - Application: Представляет собой приложение, с которым вы будете работать.
# - WindowSpecification: Представляет окно или элемент управления.


# Подключение к приложению:
#1. Запуск приложения через pywinauto:
app = Application(backend="win32").start("notepad.exe") # открыть Блокнот
#app = Application(backend="win32").start("mspaint.exe") # открыть Paint

#2. Подключение к уже запущенному процессу:
#app = Application(backend="win32").connect(process=17496)  # по PID
#app = Application(backend="win32").connect(path="notepad.exe")  # по имени исполняемого файла
# Backend:
#    - "win32" — для большинства классических приложений Windows.
#    - "uia" — для приложений на основе UIAutomation (WPF, UWP и т.д.).


## Основные операции с окнами:

### Получение окна:
#1. По заголовку окна:
#dlg = app.window(title="Безымянный - Блокнот")

#2. По частичному совпадению заголовка:
dlg = app.window(title_re=".*Блокнот.*")  # регулярное выражение

#3. По классу окна:
#dlg = app.window(class_name="Notepad")

### Действия с окнами:
#1. Ожидание открытия окна:
#dlg.wait("exists", timeout=10)  # ждет 10 секунд, пока окно не появится

#2. Активация окна:
#dlg.set_focus()

#3. Минимизация, максимизация и закрытие:
#dlg.minimize()
#dlg.maximize()
#dlg.close()

#4. Получение текста заголовка окна:
title = dlg.window_text()
print(title)


### Работа с элементами управления:
#1. Нажатие кнопки:
#dlg.Button.click()
#dlg.child_window(title="Справка").click()  # через child_window

#2. Ввод текста в текстовое поле:
#dlg.Edit.type_keys("Hello, World!")
#Примечание: Также можно использовать метод send_keys для более точных симуляций клавиатуры.

#3. Выбор элемента в ComboBox:
#dlg.ComboBox.select("Item 1")

#4. Установка флажка (CheckBox):
#dlg.CheckBox.check()
#dlg.CheckBox.uncheck()

#5. Получение текста из элемента:
#text = dlg.Static.texts()
#print(text)


### Действия с меню:
#1. Доступ к меню:
#dlg.menu_select("Файл->Сохранить как")

#2. Переход к пунктам меню по индексу
#dlg.menu_select("Файл[0]->Выход[5]")  # через индексы


### Работа с диалоговыми окнами:
#1. Открытие диалогового окна (например, "Открыть файл"):
#dlg.menu_select("Файл->Открыть...")

#2. Взаимодействие с диалогом открытия файла:
#dlg = app.window(title_re=".*Открытие.*")
#dlg.Edit.type_keys("D:\\errors.txt")
#dlg.Open.click()
#dlg.Button.click()


### Получение информации об элементах:
#1. Получение списка всех элементов:
dlg.print_control_identifiers()

#2. Поиск элемента по контролу:
#btn = dlg.child_window(auto_id="12345")
#btn.click()
