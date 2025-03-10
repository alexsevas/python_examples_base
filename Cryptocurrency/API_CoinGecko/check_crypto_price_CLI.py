# pip install requests typer
# conda activate allpy310

# Использование: python check_crypto_price_CLI.py check-price bitcoin --currency rub

import requests
import typer


app = typer.Typer()
API_URL = "https://api.coingecko.com/api/v3/simple/price"


@app.command()
def get_crypto_price(crypto: str, currency: str = "usd"):
    """Получаем текущую цену криптовалюты в указанной валюте"""
    try:
        response = requests.get(
            f"{API_URL}?ids={crypto}&vs_currencies={currency}")
        data = response.json()
        price = data[crypto][currency]
        return price
    except KeyError:
        raise ValueError(f"Не удалось получить цену для криптовалюты:{crypto}")


@app.command()
def check_price(crypto: str, currency: str = "usd"):
    """Выводит текущую цену криптовалюты в указанной валюте"""
    try:
        price = get_crypto_price(crypto, currency)
        typer.echo(f"Текущая цена {crypto.upper()} в {currency.upper()}: {price:.2f}")
    except ValueError as e:
        typer.echo(f"Ошибка: {e}")


if __name__ == "__main__":
    app()
