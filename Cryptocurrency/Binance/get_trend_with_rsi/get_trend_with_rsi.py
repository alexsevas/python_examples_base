# conda activate allpy310

# Функция с помощью которой мы можем получить суточный "тренд" любого токена

import requests
import numpy as np

def get_trend_with_rsi(symbol):
    """
    Determines the trend for the given token using SMA and RSI.

    :param symbol: Token symbol (e.g., "BTCUSDT").
    :return: A string with the trend ("uptrend", "downtrend", "sideways", "undefined").
    """
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol.upper(),
        "interval": "1h",  # Hourly data
        "limit": 24  # Last 24 hours
    }

    try:
        # Fetch data
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        # Validate data
        if not data or len(data) < 5:
            return "undefined"

        # Extract closing prices
        close_prices = np.array([float(candle[4]) for candle in data])

        # 1. Simple Moving Averages
        sma_short = np.mean(close_prices[-5:]) if len(close_prices) >= 5 else None
        sma_long = np.mean(close_prices[-20:]) if len(close_prices) >= 20 else None

        # 2. RSI (14-period)
        if len(close_prices) >= 14:
            deltas = np.diff(close_prices)
            gains = np.where(deltas > 0, deltas, 0)
            losses = np.where(deltas < 0, -deltas, 0)

            avg_gain = np.mean(gains[-14:])
            avg_loss = np.mean(losses[-14:])

            if avg_loss == 0:  # Prevent division by zero
                rsi = 100
            else:
                rs = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + rs))
        else:
            rsi = None  # Not enough data for RSI

        # Determine trend
        trend = "undefined"
        if sma_short and sma_long:
            if sma_short > sma_long:
                trend = "uptrend"
            elif sma_short < sma_long:
                trend = "downtrend"

        # Refine trend using RSI
        if rsi:
            if rsi > 70:
                return "downtrend (overbought)"
            elif rsi < 30:
                return "uptrend (oversold)"
            elif 30 <= rsi <= 70 and trend == "undefined":
                return "sideways"

        return trend
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Binance API: {e}")
        return "undefined"
    except Exception as e:
        print(f"Error: {e}")
        return "undefined"


def main():
    token_symbol = "BTCUSDT"
    print(f'Для пары {token_symbol} текущий тренд - {get_trend_with_rsi(token_symbol)}')

if __name__ == "__main__":
    main()