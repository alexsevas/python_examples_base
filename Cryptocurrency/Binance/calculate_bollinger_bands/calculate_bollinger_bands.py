# conda activate allpy310

import ccxt
import pandas as pd
import talib # через pip install - ошибка, ставить из бинврника

# Параметры
EXCHANGE_NAME = "binance"
PAIR = "BTC/USDT"
TIMEFRAME = "1h"
BB_PERIOD = 20  # Период Боллинджера
BB_STD_DEV = 2  # Отклонение

# Инициализация биржи
exchange = getattr(ccxt, EXCHANGE_NAME)()
exchange.load_markets()

# Получаем исторические данные
def fetch_ohlcv(symbol):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=TIMEFRAME, limit=BB_PERIOD + 5)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    return df

# Рассчет Bollinger Bands
def calculate_bollinger_bands(df):
    upper, middle, lower = talib.BBANDS(df["close"], timeperiod=BB_PERIOD, nbdevup=BB_STD_DEV, nbdevdn=BB_STD_DEV, matype=0)
    return upper.iloc[-1], middle.iloc[-1], lower.iloc[-1], df["close"].iloc[-1]

# Анализ пробоя
def bollinger_breakout():
    df = fetch_ohlcv(PAIR)
    upper, middle, lower, close = calculate_bollinger_bands(df)

    print(f"Цена: {close:.2f}, BB Upper: {upper:.2f}, BB Lower: {lower:.2f}")

    if close > upper:
        print("📈 Пробой верхней границы! Возможное продолжение роста или ложный пробой.")
    elif close < lower:
        print("📉 Пробой нижней границы! Возможный отскок вверх.")

# Запуск
if __name__ == "__main__":
    bollinger_breakout()
