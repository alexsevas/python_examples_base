# conda activate allpy310

# Автоматическое определение консолидации цены.
# Почему это полезно:
# - Идентифицирует боковик перед сильным движением
# - Полезно для поиска точек входа в пробой
# - Можно комбинировать с объемами и RSI

# Используется публичное API Bybit

import requests
import numpy as np

# Настройки
SYMBOL = "BTCUSDT"
KLINE_URL = "https://api.bybit.com/v5/market/kline"
INTERVAL = "15"  # 15-минутные свечи
LIMIT = 50  # Количество свечей для анализа
RANGE_THRESHOLD = 0.002  # Порог для консолидации (0.2% от цены)

def get_kline_data():
    """Получает исторические свечи"""
    params = {"category": "spot", "symbol": SYMBOL, "interval": INTERVAL, "limit": LIMIT}
    response = requests.get(KLINE_URL, params=params)

    if response.status_code == 200:
        return response.json().get("result", {}).get("list", [])
    else:
        print(f"Ошибка API: {response.status_code}")
        return None

def detect_consolidation():
    """Определяет консолидацию цены"""
    candles = get_kline_data()
    if not candles:
        print("❌ Не удалось получить данные.")
        return

    closes = np.array([float(c[4]) for c in candles])
    highs = np.array([float(c[2]) for c in candles])
    lows = np.array([float(c[3]) for c in candles])

    min_price = np.min(lows[-10:])  # Минимальная цена за 10 свечей
    max_price = np.max(highs[-10:])  # Максимальная цена за 10 свечей
    price_range = (max_price - min_price) / closes[-1]

    # 🔍 Добавляем отладку:
    print(f"🔍 Анализируем последние 10 свечей...")
    print(f"🔹 Min цена: {min_price:.2f}, Max цена: {max_price:.2f}")
    print(f"🔹 Текущий диапазон: {price_range:.5f}, Порог: {RANGE_THRESHOLD}")

    if price_range < RANGE_THRESHOLD:
        print(f"📉 Консолидация: {min_price:.2f} - {max_price:.2f}, возможный пробой!")
    else:
        print("⏳ Нет консолидации. Ждем сигнала...")

if __name__ == "__main__":
    detect_consolidation()
