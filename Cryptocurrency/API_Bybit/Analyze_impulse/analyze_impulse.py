# conda activate allpy310

# Анализ импульсных движений — отслеживает сильные свечи, которые могут сигнализировать о начале тренда,
# используя публичное API Bybit

import requests

# Настройки
SYMBOL = "BTCUSDT"
KLINE_URL = "https://api.bybit.com/v5/market/kline"
INTERVAL = "15"  # 15-минутные свечи
LIMIT = 20  # Количество свечей для анализа
IMPULSE_THRESHOLD = 1.5  # Порог (x раз больше среднего тела свечи)

def get_kline_data():
    """Получает исторические свечи"""
    params = {"category": "spot", "symbol": SYMBOL, "interval": INTERVAL, "limit": LIMIT}
    response = requests.get(KLINE_URL, params=params)

    if response.status_code == 200:
        return response.json().get("result", {}).get("list", [])
    else:
        print(f"Ошибка API: {response.status_code}")
        return None

def analyze_impulse():
    """Определяет импульсные свечи"""
    candles = get_kline_data()
    if not candles:
        return

    # Вычисляем средний размер тела свечи
    body_sizes = [abs(float(c[4]) - float(c[1])) for c in candles]  # |Close - Open|
    avg_body = sum(body_sizes) / len(body_sizes)

    # Проверяем последнюю свечу
    last_open = float(candles[-1][1])
    last_close = float(candles[-1][4])
    last_body = abs(last_close - last_open)

    if last_body > avg_body * IMPULSE_THRESHOLD:
        direction = "⬆️ Вверх" if last_close > last_open else "⬇️ Вниз"
        print(f"🚀 Импульсное движение! {direction} (Тело свечи: {last_body:.2f}, Среднее: {avg_body:.2f})")
    else:
        print("📉 Нет сильного импульса.")

if __name__ == "__main__":
    analyze_impulse()
