

import requests
import hashlib
import time

URL = 'https://habr.com/ru/articles/885066/'  # замени на нужный сайт
CHECK_INTERVAL = 60  # интервал проверки в секундах

def get_hash(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return hashlib.md5(response.text.encode('utf-8')).hexdigest()
    except Exception as e:
        print("Ошибка при запросе:", e)
        return None

def monitor_site(url):
    print(f"Следим за сайтом: {url}")
    old_hash = get_hash(url)

    if old_hash is None:
        print("Не удалось получить начальное состояние.")
        return

    while True:
        time.sleep(CHECK_INTERVAL)
        new_hash = get_hash(url)

        if new_hash is None:
            continue
        if new_hash != old_hash:
            print(f"[{time.ctime()}] Сайт обновился!")
            old_hash = new_hash
        else:
            print(f"[{time.ctime()}] Без изменений.")

monitor_site(URL)
