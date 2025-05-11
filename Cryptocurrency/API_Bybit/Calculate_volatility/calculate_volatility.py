# conda activate allpy310

'''
Вычисление индекса волатильности токена на основе исторических данных используется публичное API Bybit
'''

import requests
import pandas as pd
import math

# Константы
BASE_URL = "https://api.bybit.com/v5/market/kline"
SYMBOL = "BTCUSDT"  # Торговая пара
CATEGORY = "spot"   # Тип рынка
INTERVAL = "60"     # Интервал свечей (60 минут)
LIMIT = 24          # Количество свечей (24 часа = 24 свечи по 1 часу)

def get_historical_data():
    """Получить исторические данные (Kline)"""
    params = {
        "category": CATEGORY,
        "symbol": SYMBOL,
        "interval": INTERVAL,
        "limit": LIMIT
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()["result"]["list"]
    else:
        raise Exception(f"Ошибка API: {response.status_code}, {response.text}")

def calculate_volatility(klines):
    """Вычислить волатильность на основе исторических данных"""
    data = [float(kline[4]) for kline in klines]  # Закрытые цены (Close)
    df = pd.DataFrame(data, columns=["close"])

    # Вычисляем логарифмическую доходность
    df["log_return"] = df["close"].apply(math.log).diff()

    # Рассчитываем стандартное отклонение (волатильность)
    volatility = df["log_return"].std() * math.sqrt(len(df))
    return volatility

def main():
    try:
        print(f"Вычисляем волатильность для {SYMBOL} за последние {LIMIT} часов...\n")

        # Получаем исторические данные
        klines = get_historical_data()

        # Вычисляем волатильность
        volatility = calculate_volatility(klines)

        # Выводим результат
        print(f"Волатильность за {LIMIT} часов: {volatility:.2%}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
