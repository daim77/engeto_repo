import requests
import os
import csv
from datetime import datetime as dt
from bs4 import BeautifulSoup as BS

DATE_FORMAT = '%d.%m.%Y %H:%M'
URL = "https://markets.businessinsider.com/commodities/gold-price"


def request_gold_price():
    r = requests.get(URL)

    soup = BS(r.text, "html.parser")
    price = soup.find('div', {'class': 'price'}).string

    print('The current price is {}'.format(price))

    chars = []
    for char in price:
        if char != ',':
            chars.append(char)

    price = ''.join(chars)

    return price


def write_data(price):
   with open('/Users/martindanek/Documents/programovani/files/csv/gold_price.csv', 'a') as f:
       writer = csv.writer(f)
       writer.writerow([float(price), dt.now().strftime(DATE_FORMAT)])


write_data(request_gold_price())
