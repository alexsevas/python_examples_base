# conda activate allpy310

'''
Breakout Trading Bot – Бот для торговли на пробоях уровней

Смысл стратегии:
Пробой уровней сопротивления или поддержки сигнализирует о возможном сильном движении.
Пробой вверх (breakout) → цена выходит выше сопротивления → лонг (покупка).
Пробой вниз (breakdown) → цена пробивает поддержку → шорт (продажа).
Используем максимумы и минимумы за N периодов для определения ключевых уровней
'''

import ccxt
import pandas as pd

# Параметры
EXCHANGE_NAME = "binance"
PAIR = "BTC/USDT"
TIMEFRAME = "1h"
LOOKBACK_PERIOD = 20  # Количество свечей для поиска уровней

# Инициализация биржи
exchange = getattr(ccxt, EXCHANGE_NAME)()
exchange.load_markets()

# Получение данных
def fetch_ohlcv(symbol):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=TIMEFRAME, limit=LOOKBACK_PERIOD + 5)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    return df

# Определение уровней сопротивления и поддержки
def calculate_levels(df):
    resistance = df["high"].iloc[-LOOKBACK_PERIOD:].max()  # Максимум за период
    support = df["low"].iloc[-LOOKBACK_PERIOD:].min()  # Минимум за период
    return resistance, support

# Логика пробоя
def breakout_trading_bot():
    df = fetch_ohlcv(PAIR)
    resistance, support = calculate_levels(df)
    close_price = df["close"].iloc[-1]

    print(f"Цена: {close_price:.2f}, Сопротивление: {resistance:.2f}, Поддержка: {support:.2f}")

    if close_price > resistance:
        print("📈 Пробой вверх! Возможный лонг.")
    elif close_price < support:
        print("📉 Пробой вниз! Возможный шорт.")
    else:
        print("⚡️ Цена в диапазоне, ждем пробоя.")

# Запуск
if __name__ == "__main__":
    breakout_trading_bot()
