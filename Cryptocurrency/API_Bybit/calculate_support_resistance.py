# conda activate allpy310

# Уровни поддержки и сопротивления для выбранного актива используя публичное API Bybit

import requests
import pandas as pd

# Константы
BASE_URL = "https://api.bybit.com/v5/market"
SYMBOL = "BTCUSDT"  # Торговая пара
CATEGORY = "spot"   # Тип рынка: spot, linear, inverse
KLINE_LIMIT = 200   # Количество свечей для анализа
KLINE_INTERVAL = "60"  # Интервал свечей: 1, 3, 5, 15, 60, D, W, M

def get_historical_data():
    """Получить исторические данные (Kline)"""
    url = f"{BASE_URL}/kline"
    params = {
        "category": CATEGORY,
        "symbol": SYMBOL,
        "interval": KLINE_INTERVAL,
        "limit": KLINE_LIMIT
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["result"]["list"]
    else:
        raise Exception(f"Ошибка получения данных Kline: {response.status_code}, {response.text}")

def get_current_ticker_data():
    """Получить текущие данные тикера"""
    url = f"{BASE_URL}/tickers"
    params = {
        "category": CATEGORY,
        "symbol": SYMBOL
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["result"]["list"][0]
    else:
        raise Exception(f"Ошибка получения данных тикера: {response.status_code}, {response.text}")

def calculate_support_resistance(klines):
    """Вычислить уровни поддержки и сопротивления"""
    data = [
        {"time": kline[0], "high": float(kline[2]), "low": float(kline[3])}
        for kline in klines
    ]
    df = pd.DataFrame(data)
    support_level = df["low"].min()   # Минимальная цена
    resistance_level = df["high"].max()  # Максимальная цена
    return support_level, resistance_level

def main():
    try:
        # Получение исторических данных
        klines = get_historical_data()
        # Расчет уровней поддержки и сопротивления
        support, resistance = calculate_support_resistance(klines)
        print(f"Уровень поддержки: {support}")
        print(f"Уровень сопротивления: {resistance}")
        # Получение текущих данных тикера
        ticker_data = get_current_ticker_data()
        print(f"Последняя цена: {ticker_data['lastPrice']}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
