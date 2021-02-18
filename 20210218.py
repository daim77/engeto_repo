# import requests
# from bs4 import BeautifulSoup
#
#
# r = requests.get('http://smartprague.eu')
#
# if r.status_code != 200:
#     exit()
#
# soup = BeautifulSoup(r.text, 'html.parser')
#
# print(
#     [''.join(['https://smartprague.eu', item.attrs['href']])
#      for item in soup.find_all('a')
#      if not item.attrs['href'].startswith('http')]
# )

# # ==== RSS ====
# import feedparser
#
#
# rss_url = 'https://www.kurzy.cz/zpravy/util/forext.dat?type=rss&col=wzAkcieCR'
# feeds = feedparser.parse(rss_url)
# print(feeds.keys())
#
# # print(feeds)

# ==== import html tabulky primo do csv skrz pandas ====
# import pandas as pd
#
#
# pd.read_html('http://heroes3.cz/hraci')[2].

# # ==== bitcoin ====
#
# import requests
# from bs4 import BeautifulSoup
#
#
# data = requests.get('https://kurzy.cz/bitcoin/')
# soup = BeautifulSoup(data.text, 'html.parser')
#
# print(soup.find('span', {'id': 'last_usd'}).text)

# ==== neuronove site a AI =====

