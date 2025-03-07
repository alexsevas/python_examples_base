# pip install ccxt

# conda activate allpy310

import ccxt


def open_futures_order_market(api_key, api_secret, symbol, side, amount, take_profit, stop_loss, leverage):
    """
    Открывает рыночный фьючерсный ордер на Binance с тейк-профитом, стоп-лоссом и плечом.

    :param api_key: str, API ключ Binance
    :param api_secret: str, API секрет Binance
    :param symbol: str, торговая пара, например 'BTC/USDT'
    :param side: str, 'buy' для длинной позиции, 'sell' для короткой
    :param amount: float, количество базовой валюты
    :param take_profit: float, цена тейк-профита
    :param stop_loss: float, цена стоп-лосса
    :param leverage: int, размер плеча
    """
    # Подключение к Binance Futures
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret,
        'options': {'defaultType': 'future'},  # Указываем, что работаем с фьючерсами
    })

    # Установка плеча
    try:
        exchange.set_leverage(leverage, symbol)
    except Exception as e:
        print(f"Ошибка установки плеча: {e}")
        return

    # Создание рыночного ордера для входа
    try:
        order = exchange.create_order(
            symbol=symbol,
            type='market',  # Используем рыночный ордер
            side=side,
            amount=amount,
            params={'reduceOnly': False}  # Параметр для открытия позиции
        )
        print(f"Рыночный ордер на вход создан: {order}")
    except Exception as e:
        print(f"Ошибка создания рыночного ордера на вход: {e}")
        return

    # Создание ордера на тейк-профит
    try:
        tp_order = exchange.create_order(
            symbol=symbol,
            type='limit',  # Используем лимитный ордер
            side='sell' if side == 'buy' else 'buy',  # Противоположная сторона для тейк-профита
            amount=amount,
            price=take_profit,
            params={'reduceOnly': True}  # Ордер для закрытия позиции
        )
        print(f"Тейк-профит ордер создан: {tp_order}")
    except Exception as e:
        print(f"Ошибка создания тейк-профит ордера: {e}")
        return

    # Создание ордера на стоп-лосс
    try:
        sl_order = exchange.create_order(
            symbol=symbol,
            type='stop_market',  # Используем рыночный стоп-ордер
            side='sell' if side == 'buy' else 'buy',  # Противоположная сторона для стоп-лосса
            amount=amount,
            params={
                'stopPrice': stop_loss,  # Цена активации
                'reduceOnly': True  # Ордер для закрытия позиции
            }
        )
        print(f"Стоп-лосс ордер создан: {sl_order}")
    except Exception as e:
        print(f"Ошибка создания стоп-лосс ордера: {e}")
        return
