# conda activate allpy310

'''
Расчёт среднего истинного диапазона (ATR). ATR — это индикатор, который помогает измерять волатильность рынка. Он часто
используется для установки уровней стоп-лоссов или определения трендов.
Используется публичное API Bybit
'''

import requests
import pandas as pd

# Константы
BASE_URL = "https://api.bybit.com/v5/market/kline"
SYMBOL = "BTCUSDT"  # Торговая пара
CATEGORY = "spot"   # Тип рынка
INTERVAL = "60"     # Интервал свечей (60 минут)
LIMIT = 14          # Количество свечей для ATR (по умолчанию 14 периодов)

def get_historical_data():
    """Получить исторические данные (Kline)"""
    params = {
        "category": CATEGORY,
        "symbol": SYMBOL,
        "interval": INTERVAL,
        "limit": LIMIT + 1  # Нужно на 1 свечу больше для расчётов
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()["result"]["list"]
    else:
        raise Exception(f"Ошибка API: {response.status_code}, {response.text}")

def calculate_atr(klines):
    """Вычислить ATR (средний истинный диапазон)"""
    # Преобразуем данные в DataFrame
    data = [
        {"high": float(kline[2]), "low": float(kline[3]), "close": float(kline[4])}
        for kline in klines
    ]
    df = pd.DataFrame(data)

    # Вычисляем истинный диапазон (TR)
    df["previous_close"] = df["close"].shift(1)
    df["tr"] = df[["high", "previous_close"]].max(axis=1) - df[["low", "previous_close"]].min(axis=1)

    # Рассчитываем ATR как скользящее среднее истинного диапазона
    df["atr"] = df["tr"].rolling(window=LIMIT).mean()

    # Возвращаем последнее значение ATR
    return df["atr"].iloc[-1]

def main():
    try:
        print(f"Вычисляем ATR для {SYMBOL} за последние {LIMIT} периодов...\n")

        # Получаем исторические данные
        klines = get_historical_data()

        # Вычисляем ATR
        atr = calculate_atr(klines)

        # Выводим результат
        print(f"Средний истинный диапазон (ATR) за {LIMIT} периодов: {atr:.2f}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
