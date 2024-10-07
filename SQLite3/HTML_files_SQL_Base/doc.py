import base64
import sqlite3
from pathlib import Path


def vacuum_base(path: str):
    """
    Очистка пустых значений из базы.
    :param path: Путь к базе данных.
    """
    conn = sqlite3.connect(path)
    conn.execute("VACUUM")
    conn.close()


def create_base(path: str):
    """
    Создаем базу данных sqlite.
    :param path: Путь к базе данных.
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS documents(
                   name TEXT,
                   tag TEXT,
                   base64 BLOB);
                """)
    conn.commit()
    cur.close()
    conn.close()


def open_base(path: str) -> list:
    """
    Открытие базы данных.
    :param path: Путь к базе данных.
    :return: Список с выборкой названий всех документов в базе.
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("SELECT name, tag FROM documents")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def update_data(path: str, name: str, tag: str, data: bytes):
    """
    Обновление записи в БД. В данном случае обновление тегов.
    :param path: Путь к базе данных.
    :param name: Название документа.
    :param tag: Теги.
    :param data: Документ в формате base64.
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    update_query = """Update documents set tag = ?, base64 = ? where name = ?"""
    column_values = (tag, data, name)
    cur.execute(update_query, column_values)
    conn.commit()
    cur.close()
    conn.close()


def delete_from_base(path: str, name: str):
    """
    Удаление документа из базы данных.
    :param path: Путь к базе данных.
    :param name: Название документа для удаления.
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    update_query = """DELETE from documents where name = ?"""
    cur.execute(update_query, (name,))
    conn.commit()
    cur.close()
    conn.close()


def save_to_base(path: str, data_list: list):
    """
    Сохраняем данные в базе.
    :param path: Путь к базе данных.
    :param data_list: Список со списками из данных: название статьи (документа), данные в формате base64.
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute('BEGIN TRANSACTION')
    for data in data_list:
        cur.executemany("INSERT INTO documents VALUES(?, ?, ?);", (data, ))
    conn.commit()
    cur.close()
    conn.close()


def encode_b64(path: str) -> tuple:
    """
    Кодирование файла в base64.
    :param path: Путь к кодируемому файлу.
    :return: Кортеж из имени кодированного документа и кодированный в base64 документ.
    """
    with open(path, "rb") as file:
        return Path(path).name.split(Path(path).suffix)[0], "no tag", base64.b64encode(file.read())


def decode_b64(path: str, data: bytes):
    """
    Декодирование файла из base64.
    :param path: Путь к базе данных.
    :param data: Строка в формате base64 для декодирования.
    """
    dec = base64.decodebytes(data)
    with open(path, 'wb') as file:
        file.write(dec)


def select_tag(path: str, tag: str) -> list:
    """
    Выборка данных из базы по определенному тегу.
    :param path: Путь к базе данных.
    :param tag: Тег, по которому нужно делать выборку.
    :return: Список из кортежей.
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    select_query = """SELECT name, tag FROM documents where tag LIKE ?"""
    cur.execute(select_query, [f'%{tag}%'])
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def save_doc_from_base(path: str, name: str) -> tuple:
    """
    Выборка из базы документа для сохранения.
    :param path: Путь к базе данных.
    :param name: Название сохраняемого документа.
    :return: Кортеж из названия документа и base64-документ.
    """
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    select_query = """SELECT * FROM documents where name = ?"""
    cur.execute(select_query, (name,))
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data
