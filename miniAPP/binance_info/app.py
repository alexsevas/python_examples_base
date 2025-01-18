import requests
import time


def get_binance_data():
    """Получает данные о торговых парах с Binance."""
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка подключения к Binance API.")
        return []


def find_unusual_activity(data):
    """Находит пары с самым большим изменением объема торгов."""
    unusual_pairs = sorted(data, key=lambda x: float(x['quoteVolume']), reverse=True)[:10]
    return unusual_pairs


def main():
    print("Анализ  активности на Binance...")
    while True:
        data = get_binance_data()
        if data:
            unusual_pairs = find_unusual_activity(data)
            print("\nТоп-10 пар с наибольшим объемом торгов за 24 часа:")
            for pair in unusual_pairs:
                print(f"{pair['symbol']} - Объем торгов: {pair['quoteVolume']} {pair['symbol'][-3:]}")
        else:
            print("Не удалось получить данные.")

        print("\nОжидание 1 час для следующего обновления...")
        time.sleep(3600)  # Обновление каждый час


if __name__ == "__main__":
    main()
