# pip install ccxt

# conda activate allpy310

import ccxt
import pandas as pd
import time

# Инициализация Binance API
exchange = ccxt.binance()

# Параметры анализа
SYMBOLS = ["BTC/USDT", "ETH/USDT", "BNB/USDT", "SOL/USDT", "XRP/USDT"]
TIMEFRAME = "1h"  # Таймфрейм (можно поменять)
LIMIT = 50  # Количество свечей


def fetch_data(symbol, timeframe, limit):
    """ Получает исторические данные """
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df
    except Exception as e:
        print(f"[ERROR] Ошибка загрузки данных {symbol}: {e}")
        return None


def calculate_volatility(df):
    """ Вычисляет волатильность """
    df["range"] = df["high"] - df["low"]  # Размах свечи
    df["atr"] = df["range"].rolling(window=14).mean()  # ATR (средний размах)
    df["std_dev"] = df["close"].rolling(window=14).std()  # Стандартное отклонение
    return df


def main():
    print("[INFO] Анализ волатильности активов...")

    results = []

    for symbol in SYMBOLS:
        df = fetch_data(symbol, TIMEFRAME, LIMIT)
        if df is not None:
            df = calculate_volatility(df)
            latest = df.iloc[-1]
            results.append({
                "symbol": symbol,
                "last_price": latest["close"],
                "range": latest["range"],
                "atr": latest["atr"],
                "std_dev": latest["std_dev"]
            })

    # Сортировка по ATR (самые волатильные активы в топе)
    df_results = pd.DataFrame(results).sort_values(by="atr", ascending=False)
    print("\n[RESULTS] Топ волатильных активов:\n")
    print(df_results)


if __name__ == "__main__":
    main()


'''
calculate_volatility.py 
[INFO] Анализ волатильности активов...

[RESULTS] Топ волатильных активов:

     symbol  last_price     range          atr      std_dev
0  BTC/USDT  84019.3600  539.5200  1257.367857  1204.429979
1  ETH/USDT   2099.6800   26.8300    44.695000    31.158255
2  BNB/USDT    567.1300    4.1800     8.332143     6.741450
3  SOL/USDT    137.1600    2.2100     3.529286     2.877926
4  XRP/USDT      2.3673    0.0314     0.071021     0.043360
'''
