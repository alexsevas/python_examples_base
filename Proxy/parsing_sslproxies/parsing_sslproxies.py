from bs4 import BeautifulSoup
import requests

def crawl_proxies():
    proxies = []
    link = "https://www.sslproxies.org/"

    # 1) данные берем с инета
    #r = requests.get(link)

    # 2) данные бем из сохраненной локально страницы
    with open('index1.html', 'r', encoding='utf-8') as file:
        r = file.read()

    # 1) парсим то, что получили сос траницы с инета
    #s = BeautifulSoup(r.text, "html.parser")

    # 2) парсим то, что в сохраненной локально странице
    s = BeautifulSoup(r, "lxml")

    for i in s.find_all("tr")[:30]:
        try:
            data = i.find_all("td")
            address = data[0].text
            port = data[1].text
            type_ = data[4].text
            proxy = address+":"+port
            proxies.append({"https":proxy})
        except:
            pass
    return proxies

proxies = crawl_proxies()
print (proxies)