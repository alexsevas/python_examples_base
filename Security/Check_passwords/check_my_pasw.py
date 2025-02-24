# conda env allpy310
# Пароли для проверки вписать в passcheck.txt.
# Для проверки паролей нужен инет.

import hashlib  # Библиотека для работы с хешами.
import requests  # Библиотека для отправки HTTP-запросов.


def request_api_data(query_char):
    """
    Отправляет запрос к API для получения данных о паролях,
    используя первые 5 символов SHA-1 хеша пароля.

    :param query_char: Первые 5 символов хеша пароля.
    :return: Ответ API, если запрос был успешным.
    :raises RuntimeError: Если статус ответа не 200.
    """
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again.')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    """
    Проверяет, сколько раз данный хеш пароля был найден в базе данных утечек.

    :param hashes: Ответ от API, содержащий хеши паролей и их количество утечек.
    :param hash_to_check: Хеш пароля, для которого нужно найти количество утечек.
    :return: Количество утечек для данного пароля.
    """
    # Генерируем пары (хеш, количество) из строк ответа
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count  # Возвращаем количество, если хеш найден
    return 0  # Возвращаем 0, если хеш не найден


def pwned_api_check(password):
    """
    Проверяет, был ли данный пароль скомпрометирован, отправляя его хеш в API.

    :param password: Пароль, который нужно проверить.
    :return: Количество утечек для данного пароля.
    """
    # Преобразуем пароль в SHA-1 хеш
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]  # Разделяем хеш на две части
    response = request_api_data(first5_char)  # Запрашиваем данные из API
    return get_password_leaks_count(response, tail)  # Проверяем количество утечек хеша


def main(args):
    """
    Основная функция, которая обрабатывает список паролей
    и выводит информацию о каждом из них.

    :param args: Список паролей для проверки.
    """
    for password in args:
        count = pwned_api_check(password)  # Проверяем каждый пароль
        if count:
            print(
                f'{password} was found {count} times..... you should probably change your password.')
        else:
            print(f'{password} was NOT found. Carry on.')
    print('Done!')  # Финальное сообщение о завершении программы


if __name__ == '__main__':
    # Читаем пароли из файла passcheck.txt
    with open('./passcheck.txt', mode='r', encoding="utf8") as file:
        pw_list = []
        for line in file:
            pw = line.strip()  # Убираем лишние пробелы и переносы
            pw_list.append(pw)  # Добавляем пароль в список
    main(pw_list)  # Запускаем основную функцию с списком паролей
