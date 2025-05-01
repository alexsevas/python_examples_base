# Анализ цепочек пар на прибыльность сделки(внутрибиржевой арбитраж Binance)

# <Response [451]> - санкции, через браузер json выдает

import requests

def get_bid_ask_data():
    """Получение данных bid/ask для всех пар через API Binance."""
    try:
        url = "https://api.binance.com/api/v3/ticker/bookTicker"
        response = requests.get(url)
        response.raise_for_status()
        tickers = response.json()
        bid_ask_data = {t['symbol']: {'bid': float(t['bidPrice']), 'ask': float(t['askPrice'])} for t in tickers}
        return bid_ask_data
    except Exception as e:
        print(f"Ошибка получения bid/ask данных: {e}")
        return {}

def calculate_arbitrage(chain, bid_ask_data, fee=0.001):
    try:
        # Проверка наличия данных для всех пар в цепочке
        for pair in chain:
            if pair not in bid_ask_data:
                raise ValueError(f"Нет данных для пары {pair}")

        # Начальная сумма в USDT
        initial_usdt = 10

        # Первая сделка: покупка базового актива первой пары
        pair1 = chain[0]
        buy_price1 = bid_ask_data[pair1]['ask']
        amount_base = (initial_usdt / buy_price1) * (1 - fee)

        # Вторая сделка: продажа базового актива за промежуточный токен
        pair2 = chain[1]
        sell_price2 = bid_ask_data[pair2]['bid']
        amount_mid = amount_base * sell_price2 * (1 - fee)

        # Третья сделка: продажа промежуточного токена за USDT
        pair3 = chain[2]
        sell_price3 = bid_ask_data[pair3]['bid']
        final_usdt = amount_mid * sell_price3 * (1 - fee)

        return final_usdt
    except ValueError as ve:
        print(f"Предупреждение: {ve}")
        return 0
    except Exception as e:
        print(f"Ошибка расчета арбитража: {e}")
        return 0

if __name__ == "__main__":


    while True:
        chains = []
        bid_ask_data = get_bid_ask_data()
        for chain in chains:
            profit = calculate_arbitrage(chain, bid_ask_data)
            if profit > 10:
                print(f"Chain: {chain}, Final USDT: {profit}")
            else:
                pass
