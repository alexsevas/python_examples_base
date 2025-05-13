# conda activate allpy310

# Поиск аномальной ликвидности (детектор "стенок")
# Этот скрипт анализирует глубину стакана и ищет необычно крупные лимитные ордера ("стены"), которые могут повлиять на
# движение цены,используя публичное API Bybit

import requests
import time

# Константы
ORDERBOOK_URL = "https://api.bybit.com/v5/market/orderbook"
SYMBOL = "BTCUSDT"
CATEGORY = "spot"
DEPTH_LEVELS = 20  # Количество уровней стакана для анализа
VOLUME_THRESHOLD_RATIO = 0.1  # Порог "стен" (10% от общего объёма стакана)
REFRESH_INTERVAL = 5  # Интервал обновления (в секундах)

def get_orderbook():
    """Получает стакан заявок"""
    params = {"category": CATEGORY, "symbol": SYMBOL}
    response = requests.get(ORDERBOOK_URL, params=params)
    if response.status_code == 200:
        result = response.json().get("result", {})
        return result.get("b", []), result.get("a", [])
    else:
        raise Exception(f"Ошибка API Orderbook: {response.status_code}, {response.text}")

def detect_liquidity_walls():
    """Анализ ликвидности и поиск крупных заявок"""
    try:
        print(f"Мониторинг ликвидности {SYMBOL}...\n")
        while True:
            bids, asks = get_orderbook()

            # Берём только топ-N уровней стакана
            bids = [(float(price), float(size)) for price, size in bids[:DEPTH_LEVELS]]
            asks = [(float(price), float(size)) for price, size in asks[:DEPTH_LEVELS]]

            # Считаем общий объём заявок в стакане
            total_bid_volume = sum(size for _, size in bids)
            total_ask_volume = sum(size for _, size in asks)

            # Порог для "стен" ликвидности (10% от всего объёма стакана)
            bid_threshold = total_bid_volume * VOLUME_THRESHOLD_RATIO
            ask_threshold = total_ask_volume * VOLUME_THRESHOLD_RATIO

            # Ищем "стены" – заявки, превышающие порог
            big_bids = [(price, size) for price, size in bids if size >= bid_threshold]
            big_asks = [(price, size) for price, size in asks if size >= ask_threshold]

            # Выводим результаты
            if big_bids:
                print(f"🟢 Крупные заявки на покупку:")
                for price, size in big_bids:
                    print(f"   Цена: {price:.2f}, Объём: {size:.2f}")

            if big_asks:
                print(f"🔴 Крупные заявки на продажу:")
                for price, size in big_asks:
                    print(f"   Цена: {price:.2f}, Объём: {size:.2f}")

            print("-" * 40)
            time.sleep(REFRESH_INTERVAL)

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    detect_liquidity_walls()
