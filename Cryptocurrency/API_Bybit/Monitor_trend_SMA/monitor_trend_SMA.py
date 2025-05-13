# conda activate allpy310

# Анализ тренда цены с использованием скользящей средней (SMA), используя публичное API Bybit

import requests
import time

# Константы
KLINE_URL = "https://api.bybit.com/v5/market/kline"
SYMBOL = "BTCUSDT"  # Торговая пара
CATEGORY = "spot"   # Тип рынка (spot или linear для фьючерсов)
INTERVAL = "1"  # Таймфрейм свечей (1 минута)
SMA_PERIOD = 10  # Количество свечей для расчёта SMA
REFRESH_INTERVAL = 5  # Интервал обновления (в секундах)

def get_kline_data():
    """Получить исторические свечи"""
    params = {
        "category": CATEGORY,
        "symbol": SYMBOL,
        "interval": INTERVAL,
        "limit": SMA_PERIOD  # Берём последние N свечей
    }
    response = requests.get(KLINE_URL, params=params)
    if response.status_code == 200:
        result = response.json().get("result", {}).get("list", [])
        if result:
            return [float(candle[4]) for candle in result]  # Закрытия свечей
        else:
            raise ValueError("Пустой ответ в 'result.list'.")
    else:
        raise Exception(f"Ошибка API Kline: {response.status_code}, {response.text}")

def calculate_sma(prices):
    """Рассчитать скользящую среднюю (SMA)"""
    return sum(prices) / len(prices) if prices else 0

def monitor_trend():
    """Мониторинг тренда на основе SMA"""
    try:
        print(f"Начинаем мониторинг тренда {SYMBOL}...\n")
        while True:
            # Получаем закрытия свечей
            closing_prices = get_kline_data()
            current_price = closing_prices[-1]  # Последняя цена закрытия
            sma = calculate_sma(closing_prices)

            # Определяем тренд
            trend = "⬆️ Восходящий" if current_price > sma else "⬇️ Нисходящий"

            # Выводим результаты
            print(f"Цена: {current_price:.2f}, SMA({SMA_PERIOD}): {sma:.2f}, Тренд: {trend}")

            # Интервал обновления
            time.sleep(REFRESH_INTERVAL)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    monitor_trend()
