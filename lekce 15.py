# import requests
# import bs4
#
#
# getr = requests.get('http://example.com/')
# # print(getr.text)
# soup = bs4.BeautifulSoup(getr.text, "html.parser")
# print(soup.h1)

# # ===== gold price scraping from business insider =====
# import csv
# from datetime import datetime
# import requests
# import bs4
#
#
# url = 'https://markets.businessinsider.com/commodities/gold-price'
#
#
# def write_price_to_csv(price):
#     with open('/Users/martindanek/Documents/programovani/files/csv/gold.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([price, datetime.now().strftime('%d %b %Y %H %M')])
#
#
# def get_gold_price():
#     price = 'price not found'
#     request_data = requests.get(url)
#     soup = bs4.BeautifulSoup(request_data.text, "html.parser")
#
#     data = soup.find('div', class_="snapshot").script.string
#     data_list = [item.strip(',:') for item in data.split()]
#     for i, item in enumerate(data_list):
#         if item == 'price':
#             price = data_list[i + 1]
#             break
#     write_price_to_csv(price)
#
#
# if __name__ == '__main__':
#     get_gold_price()

# ===== FIO bank scrapper =====

import requests
import bs4
import csv


def compose_url(account, date_from, date_to):
    return 'https://ib.fio.cz/ib/transparent?a='\
           + str(account) + '&f='\
           + str(date_from)\
           + '&t='\
           + str(date_to)


def write_data(arg):
    with open('/Users/martindanek/Documents/programovani/files/csv/fio_kpf.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(arg)


def fio_account(account, date_from, date_to):
    url = compose_url(account, date_from, date_to)
    data = requests.get(url)

    soup = bs4.BeautifulSoup(data.text, 'html.parser')

    header = [item.text for item in soup.find('table').find_next('table').find('thead').find_all('th')]

    transaction = [item for item in soup.find('table').find_next('table').find('tbody').find_all('td')]

    clean_data = []
    sub_list = []
    clean_data.append(header)

    for index, item in enumerate(transaction):
        sub_list.append(item.text.strip('\n \t'))
        if (index + 1) % 9 == 0:
            clean_data.append(sub_list)
            sub_list = []
    write_data(clean_data)


if __name__ == '__main__':
    fio_account(2400101213, '01.01.2021', '29.01.2021')
