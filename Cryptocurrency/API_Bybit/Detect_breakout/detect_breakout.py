# conda activate allpy310

# Автоматическое обнаружение пробоя уровней поддержки и сопротивления:
# Получает исторические свечи BTCUSDT,
# Определяет ключевые уровни поддержки и сопротивления,
# Выдает сигнал, если цена пробивает уровень

import requests
import numpy as np

# Настройки
SYMBOL = "BTCUSDT"
KLINE_URL = "https://api.bybit.com/v5/market/kline"
INTERVAL = "15"  # 15-минутные свечи
LIMIT = 50  # Количество свечей для анализа
TOLERANCE = 0.002  # Допустимый разрыв (0.2%)

def get_kline_data():
    """Получает исторические свечи"""
    params = {"category": "spot", "symbol": SYMBOL, "interval": INTERVAL, "limit": LIMIT}
    response = requests.get(KLINE_URL, params=params)

    if response.status_code == 200:
        return response.json().get("result", {}).get("list", [])
    else:
        print(f"Ошибка API: {response.status_code}")
        return None

def find_support_resistance(candles):
    """Определяет уровни поддержки и сопротивления"""
    closes = np.array([float(c[4]) for c in candles])
    highs = np.array([float(c[2]) for c in candles])
    lows = np.array([float(c[3]) for c in candles])

    support = np.min(lows)
    resistance = np.max(highs)

    return support, resistance

def detect_breakout():
    """Проверяет пробой уровней"""
    candles = get_kline_data()
    if not candles:
        return

    support, resistance = find_support_resistance(candles)
    last_close = float(candles[-1][4])

    if last_close >= resistance * (1 + TOLERANCE):
        print(f"🚀 Пробой вверх! Цена {last_close:.2f} выше сопротивления {resistance:.2f}")
    elif last_close <= support * (1 - TOLERANCE):
        print(f"⚠️ Пробой вниз! Цена {last_close:.2f} ниже поддержки {support:.2f}")
    else:
        print(f"📊 Цена {last_close:.2f}, диапазон: {support:.2f} - {resistance:.2f} (без пробоя)")

if __name__ == "__main__":
    detect_breakout()
