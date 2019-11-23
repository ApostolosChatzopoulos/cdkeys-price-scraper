from bs4 import BeautifulSoup
import requests
import datetime


def cost(url):
    URL = url
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find("div", {"class": "product_price"}).find("span", {"class": "price"}).text
    price = float(price[2:])  # not decimals

    return price


def sale(price, lowest_cost, gamename):
    PRICE = price
    if PRICE < lowest_cost:
        date = datetime.datetime.now()

        print('[' + str(date)[:19] + ']' +' ' +gamename + ' is on sale at ' + str(PRICE) + '$')