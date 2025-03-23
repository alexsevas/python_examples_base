# conda activate allpy310

import ccxt
import time

# Подключение к биржам
bybit = ccxt.bybit()
binance = ccxt.binance()

SYMBOL = "BTC/USDT"

def get_prices():
    prices = {}

    try:
        bybit_ticker = bybit.fetch_ticker(SYMBOL)
        prices["Bybit"] = {
            "bid": bybit_ticker["bid"],
            "ask": bybit_ticker["ask"]
        }
    except Exception as e:
        print(f"[ERROR] Ошибка получения данных с Bybit: {e}")

    try:
        binance_ticker = binance.fetch_ticker(SYMBOL)
        prices["Binance"] = {
            "bid": binance_ticker["bid"],
            "ask": binance_ticker["ask"]
        }
    except Exception as e:
        print(f"[ERROR] Ошибка получения данных с Binance: {e}")

    return prices

def find_best_route():
    prices = get_prices()

    if not prices or len(prices) < 2:
        print("[WARN] Недостаточно данных для расчета арбитража.")
        return

    best_buy = min(prices, key=lambda x: prices[x]["ask"])
    best_sell = max(prices, key=lambda x: prices[x]["bid"])

    buy_price = prices[best_buy]["ask"]
    sell_price = prices[best_sell]["bid"]

    print("\n📊 **Текущие цены на биржах:**")
    for exchange, data in prices.items():
        print(f" - {exchange}: Bid = {data['bid']} USDT | Ask = {data['ask']} USDT")

    print("\n📌 **Рекомендация:**")
    if best_buy != best_sell:
        profit = sell_price - buy_price
        print(f"✅ **Купить на {best_buy} за {buy_price:.2f} USDT**")
        print(f"✅ **Продать на {best_sell} за {sell_price:.2f} USDT**")
        print(f"📈 **Возможная прибыль: {profit:.2f} USDT**")
    else:
        print("⚠️ Разница цен недостаточна для арбитража.")

if __name__ == "__main__":
    while True:
        print("\n[INFO] Поиск лучшей цены...")
        find_best_route()
        time.sleep(10)  # Обновление каждые 10 секунд

'''
[INFO] Поиск лучшей цены...

📊 **Текущие цены на биржах:**
 - Bybit: Bid = 84089.7 USDT | Ask = 84089.8 USDT
 - Binance: Bid = 84076.65 USDT | Ask = 84076.66 USDT

📌 **Рекомендация:**
✅ **Купить на Binance за 84076.66 USDT**
✅ **Продать на Bybit за 84089.70 USDT**
📈 **Возможная прибыль: 13.04 USDT**
'''