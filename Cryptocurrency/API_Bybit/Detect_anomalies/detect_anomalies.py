# conda activate allpy310

'''
Aнализ аномалий с помощью Z-Score.
- Фильтрует шум — игнорирует обычные колебания
- Выявляет сильные движения — можно использовать в стратегиях
- Просто и быстро — нет сложных вычислений
Используем публичное API Bybit
'''

import requests
import numpy as np

# Настройки
SYMBOL = "BTCUSDT"
KLINE_URL = "https://api.bybit.com/v5/market/kline"
INTERVAL = "15"  # 15-минутные свечи
LIMIT = 100  # Количество свечей

def get_kline_data():
    """Получает исторические свечи"""
    params = {"category": "spot", "symbol": SYMBOL, "interval": INTERVAL, "limit": LIMIT}
    response = requests.get(KLINE_URL, params=params)

    if response.status_code == 200:
        return response.json().get("result", {}).get("list", [])
    else:
        print(f"Ошибка API: {response.status_code}")
        return None

def detect_anomalies():
    """Анализ аномальных движений"""
    candles = get_kline_data()
    if not candles:
        return

    closes = np.array([float(c[4]) for c in candles])
    returns = np.diff(closes)  # Вычисляем разницу между свечами

    mean = np.mean(returns)
    std = np.std(returns)
    z_scores = (returns - mean) / std  # Z-оценка для каждого изменения

    threshold = 3  # Граница аномалий
    anomalies = np.where(abs(z_scores) > threshold)[0]

    for idx in anomalies:
        move = "🚀 Резкий рост" if z_scores[idx] > 0 else "⚠️ Резкое падение"
        print(f"{move}: Свеча {idx+1}, Изменение: {returns[idx]:.2f}, Z-Score: {z_scores[idx]:.2f}")

if __name__ == "__main__":
    detect_anomalies()
