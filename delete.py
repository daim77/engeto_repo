import requests
import sys
import csv
import datetime
from bs4 import BeautifulSoup as BS


URL = 'https://ib.fio.cz/ib/transparent?a=2400101213'


def make_soup(URL, payload):
    try:
        r = requests.get(URL, params=payload)
        r.raise_for_status()
        soup = BS(r.text, "html.parser")
        return soup
    except HTTPError:
        print('Could not retrieve the page')
    except:
        print(sys.exc_info()[:1])


def extract_data(soup):
    # extracts transfers into a list of lists

    target_header = ['Datum', 'Částka', 'Typ', 'Název protiúčtu',
                     'Zpráva pro příjemce', 'KS', 'VS', 'SS', 'Poznámka']

    table_to_scrape = extract_table(soup, target_header)

    transfers = [target_header]

    for row in filter(lambda x: x != '\n', table_to_scrape.tbody.children):
        transfers.append([])
        for info in filter(lambda x: x != '\n', row.children):
            transfers[-1].append(info.attrs.get('data-value') or info.string)

    return transfers


def extract_table(soup, target_header):
    # found by the content
    for table in soup.find_all('table'):
        header = [child.string for child in table.thead.tr.children if child.string != '\n']
        if header == target_header:
            return table


def write_data(data, filename):
    with open(filename,'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print('WRITTEN {} LINES'.format(len(data)))
    print('RECEIVED {} CZK'.format(sum(map(float, extract_col(2, data[1:])))))

