# pip install beautifulsoup4 requests lxml

import requests
from bs4 import BeautifulSoup
import json

# парсим страницу и сохраняем ее в index.html
'''
url = "http://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36"
}
req = requests.get(url, headers=headers)
src = req.text
#print(src)

with open("index.html", "w", encoding="utf-8") as file:
    file.write(src)
'''

# загружаем данные из index.html и работаем дальше с ним
with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")

all_categories_dict = {}
for item in all_products_hrefs:
    item_text = item.text
    item_href = "http://health-diet.ru" + item.get("href")

    all_categories_dict[item_text] = item_href
with open("all_categories_dict.json", "w", encoding="utf-8") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)