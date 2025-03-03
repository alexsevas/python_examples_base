# conda activate allpy310

# Отслеживание резких изменений цены токена(price alert) используя публичное API Bybit

import requests
import time

# Константы
BASE_URL = "https://api.bybit.com/v5/market/tickers"
SYMBOL = "BTCUSDT"  # Торговая пара
CATEGORY = "spot"   # Тип рынка
CHECK_INTERVAL = 10  # Интервал проверки цены (в секундах)
THRESHOLD_PERCENT = 1  # Порог изменения цены (в процентах)

def get_current_price():
    """Получить текущую цену с API Bybit"""
    params = {
        "category": CATEGORY,
        "symbol": SYMBOL
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()["result"]["list"][0]
        return float(data["lastPrice"])
    else:
        raise Exception(f"Ошибка API: {response.status_code}, {response.text}")

def main():
    print(f"Начинаем отслеживать резкие изменения цены для {SYMBOL}...")
    previous_price = get_current_price()
    print(f"Начальная цена: {previous_price}\n")

    while True:
        try:
            current_price = get_current_price()
            price_change = ((current_price - previous_price) / previous_price) * 100

            # Если изменение цены превышает порог
            if abs(price_change) >= THRESHOLD_PERCENT:
                print(f"🔔 Резкое изменение цены!")
                print(f"Старая цена: {previous_price}, Новая цена: {current_price}")
                print(f"Изменение: {price_change:.2f}%\n")
                previous_price = current_price  # Обновляем предыдущую цену

            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
