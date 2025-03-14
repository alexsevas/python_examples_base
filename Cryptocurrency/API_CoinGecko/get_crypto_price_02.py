# conda activate allpy310

# Котировка криптовалют с помощью сервиса CoinGecko

'''
Меню:
1. Узнать цену криптовалюты
2. Выйти
Выберите действие (1-2): 1
Введите название криптовалюты (например, bitcoin): bitcoin
Введите валюту (например, usd, eur): usd
Текущая цена Bitcoin в USD: 81963
'''

import requests

API_URL = "https://api.coingecko.com/api/v3/simple/price"


def get_crypto_price(crypto, currency="usd"):
    """Получает текущую цену криптовалюты в указанной валюте."""
    try:
        params = {
            "ids": crypto,
            "vs_currencies": currency
        }
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            if crypto in data:
                price = data[crypto][currency]
                print(f"Текущая цена {crypto.capitalize()} в {currency.upper()}: {price}")
            else:
                print("Криптовалюта не найдена.")
        else:
            print("Не удалось получить данные. Проверьте ввод.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    print("Программа: Текущие цены криптовалют")
    while True:
        print("\nМеню:")
        print("1. Узнать цену криптовалюты")
        print("2. Выйти")
        choice = input("Выберите действие (1-2): ").strip()

        if choice == "1":
            crypto = input("Введите название криптовалюты (например, bitcoin): ").strip().lower()
            currency = input("Введите валюту (например, usd, eur): ").strip().lower()
            get_crypto_price(crypto, currency)
        elif choice == "2":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")