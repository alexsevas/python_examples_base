# conda activate allpy310

'''
Поиск уровня с максимальным объёмом в стакане используется публичное API Bybit
'''

import requests

# Константы
BASE_URL = "https://api.bybit.com/v5/market/orderbook"
SYMBOL = "BTCUSDT"  # Торговая пара
CATEGORY = "spot"   # Тип рынка

def get_order_book():
    """Получить данные стакана (Order Book)"""
    params = {
        "category": CATEGORY,
        "symbol": SYMBOL
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()["result"]  # Данные стакана
    else:
        raise Exception(f"Ошибка API: {response.status_code}, {response.text}")

def find_max_volume_levels(order_book):
    """Найти уровни с максимальными объёмами для Bid и Ask"""
    bids = order_book["b"]  # Покупки (Bid)
    asks = order_book["a"]  # Продажи (Ask)

    # Находим цену с максимальным объёмом
    max_bid = max(bids, key=lambda x: float(x[1]))  # x[1] — объём
    max_ask = max(asks, key=lambda x: float(x[1]))  # x[1] — объём

    return max_bid, max_ask

def main():
    try:
        print(f"Анализ стакана для {SYMBOL}...\n")

        # Получаем данные стакана
        order_book = get_order_book()

        # Находим уровни с максимальными объёмами
        max_bid, max_ask = find_max_volume_levels(order_book)

        # Выводим результаты
        print("Максимальный объём на покупку (Bid):")
        print(f"Цена: {max_bid[0]}, Объём: {max_bid[1]}")
        print("\nМаксимальный объём на продажу (Ask):")
        print(f"Цена: {max_ask[0]}, Объём: {max_ask[1]}")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
