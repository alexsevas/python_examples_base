# conda activate allpy310

# Выявление скрытых крупных заявок (Iceberg Orders)
# Iceberg-заявки — это ордера, которые выглядят как маленькие, но при исполнении обновляются, показывая новую "скрытую" часть.
# Как это использовать?
# Если Iceberg в BID → крупный игрок накапливает позицию, рост вероятен
# Если Iceberg в ASK → крупный игрок разгружает позицию, может быть падение

import requests
import time

# API Bybit (глубина стакана)
ORDER_BOOK_URL = "https://api.bybit.com/v5/market/orderbook"
SYMBOL = "BTCUSDT"
DEPTH = 50  # Берём топ-50 заявок

def get_order_book():
    """Получает стакан заявок"""
    params = {"category": "spot", "symbol": SYMBOL, "limit": DEPTH}
    response = requests.get(ORDER_BOOK_URL, params=params)
    if response.status_code == 200:
        data = response.json().get("result", {})
        bids = [(float(price), float(size)) for price, size in data.get("b", [])]
        asks = [(float(price), float(size)) for price, size in data.get("a", [])]
        return bids, asks
    else:
        print(f"Ошибка API: {response.status_code}")
        return None, None

def detect_iceberg_orders():
    """Выявляет скрытые Iceberg-заявки"""
    prev_bids, prev_asks = get_order_book()
    if not prev_bids or not prev_asks:
        print("❌ Ошибка получения стакана.")
        return

    print("📡 Начинаем мониторинг Iceberg-заявок...")
    while True:
        time.sleep(2)  # Ждём обновления стакана
        bids, asks = get_order_book()
        if not bids or not asks:
            continue

        # Анализ заявок (BID - покупатели)
        for i in range(min(len(bids), len(prev_bids))):
            if bids[i][0] == prev_bids[i][0] and bids[i][1] > prev_bids[i][1] * 1.5:
                print(f"❄️ Iceberg-заявка в BID: {bids[i][0]} - новый объём {bids[i][1]} BTC (было {prev_bids[i][1]} BTC)")

        # Анализ заявок (ASK - продавцы)
        for i in range(min(len(asks), len(prev_asks))):
            if asks[i][0] == prev_asks[i][0] and asks[i][1] > prev_asks[i][1] * 1.5:
                print(f"❄️ Iceberg-заявка в ASK: {asks[i][0]} - новый объём {asks[i][1]} BTC (было {prev_asks[i][1]} BTC)")

        prev_bids, prev_asks = bids, asks  # Обновляем стакан

if __name__ == "__main__":
    detect_iceberg_orders()
