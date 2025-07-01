# conda activate allpy310

# Сбор пар для внутрибиржевого арбитража binance

import requests

def get_arbitrage_pairs():
    try:
        # Получение информации о торговых парах с публичного API Binance
        url = "https://api.binance.com/api/v3/exchangeInfo"
        response = requests.get(url)
        response.raise_for_status()
        exchange_info = response.json()
        symbols = exchange_info['symbols']

        # Фильтрация пар, доступных на спотовом рынке
        spot_pairs = [s['symbol'] for s in symbols if s['status'] == 'TRADING']

        # Создание структуры для поиска связок
        pair_dict = {}
        for pair in spot_pairs:
            if pair.endswith('USDT') or pair.startswith('USDT'):
                continue
            base, quote = pair[:-3], pair[-3:]  # Определение базового и котируемого токена
            if base not in pair_dict:
                pair_dict[base] = []
            pair_dict[base].append(quote)

        # Формирование связок (начало и конец - USDT)
        arbitrage_chains = []
        for pair in spot_pairs:
            if pair.endswith('USDT'):
                base = pair[:-4]  # Базовый токен
                if base in pair_dict:
                    for mid_token in pair_dict[base]:
                        mid_pair = f"{base}{mid_token}"
                        final_pair = f"{mid_token}USDT"
                        if mid_pair in spot_pairs and final_pair in spot_pairs:
                            arbitrage_chains.append([pair, mid_pair, final_pair])

        return arbitrage_chains
    except Exception as e:
        print(f"Ошибка: {e}")
        return []


def main():
    print (f'Result - {get_arbitrage_pairs()}')


# Запуск
if __name__ == "__main__":
    main()

'''
Результат: 
[['BTCUSDT', 'BTCEUR', 'EURUSDT'], ['ETHUSDT', 'ETHBTC', 'BTCUSDT'], ['ETHUSDT', 'ETHEUR', 'EURUSDT'] и т.д. 

Дома: "ошибка: 451 Client Error: Unavailable For Legal Reasons for url: https://api.binance.com/api/v3/exchangeInfo"
'''
