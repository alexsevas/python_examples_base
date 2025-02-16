import sqlite3

# Создаем соединение с SQLite и создаем базу данных в памяти
conn = sqlite3.connect(':memory:')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Создаем таблицу Students
cursor.execute('''
CREATE TABLE Students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    major TEXT NOT NULL
);
''')

# Функция для добавления студента
def add_student(name, major):
    cursor.execute('''
    INSERT INTO Students (name, major)
    VALUES (?, ?);
    ''', (name, major))

    # Сохраняем изменения
    conn.commit()

# Функция для вывода всех студентов
def print_students():
    cursor.execute('SELECT * FROM Students')
    print('Students:')
    for row in cursor.fetchall():
        print(row)

# Добавляем несколько студентов
add_student('Alice', 'Physics')
add_student('Bob', 'Computer Science')

# Выводим всех студентов
print_students()

# Закрываем соединение с базой данных
conn.close()

