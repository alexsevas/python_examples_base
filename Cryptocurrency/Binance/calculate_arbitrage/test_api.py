
import requests

url = "https://api.binance.com/api/v3/ticker/bookTicker"
response = requests.get(url)
print(response)