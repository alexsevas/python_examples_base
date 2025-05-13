# EDIT

# conda activate allpy310

# Поиск крупных рыночных сделок (детектор "китов"). Этот скрипт поможет выявлять аномально большие ордера, которые
# могут повлиять на цену. используя публичное API Bybit

import requests
import time

# Константы
TRADES_URL = "https://api.bybit.com/v5/market/recent-trade"
SYMBOL = "BTCUSDT"  # Торговая пара
CATEGORY = "spot"   # Тип рынка (spot или linear для фьючерсов)
VOLUME_THRESHOLD = 5  # Минимальный объём сделки для "кита" (в BTC)
REFRESH_INTERVAL = 2  # Интервал обновления (в секундах)

def get_recent_trades():
    """Получить последние сделки"""
    params = {
        "category": CATEGORY,
        "symbol": SYMBOL,
        "limit": 50  # Берём последние 50 сделок
    }
    response = requests.get(TRADES_URL, params=params)
    if response.status_code == 200:
        return response.json().get("result", {}).get("list", [])
    else:
        raise Exception(f"Ошибка API Trades: {response.status_code}, {response.text}")

def detect_whale_trades():
    """Мониторинг крупных сделок (китов)"""
    try:
        print(f"Начинаем мониторинг крупных сделок для {SYMBOL}...\n")
        while True:
            trades = get_recent_trades()

            for trade in trades:
                price = float(trade["p"])  # Цена сделки
                volume = float(trade["q"])  # Объём сделки
                side = "🟢 Покупка" if trade["S"] == "Buy" else "🔴 Продажа"

                # Фильтруем только крупные сделки
                if volume >= VOLUME_THRESHOLD:
                    print(f"{side} на {volume:.2f} BTC по цене {price:.2f}")

            time.sleep(REFRESH_INTERVAL)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    detect_whale_trades()
