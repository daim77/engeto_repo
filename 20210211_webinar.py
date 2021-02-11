# # ===== pocitani barev =====
#
# list_barev = ["cervena", "cervena", "modra", "bila", 'cerna', 'zluta', 'modra']
#
# print({item: list_barev.count(item) for item in set(list_barev)})

# for item in map(lambda color: {color: list_barev.count(color)},
#                 set(list_barev)):
#     print(item)
#
#
# counter = map(lambda color: {color: list_barev.count(color)},
#               set(list_barev))
# print(list(counter))

# import csv
#
#
# list_barev = ["cervena", "cervena", "modra", "bila", 'cerna', 'zluta', 'modra']
# with open('example.csv', 'w') as file:
#     file_writer = csv.writer(file)
#     file_writer.writerow(list_barev)
#
# with open('example.csv', 'r') as file:
#     file = csv.reader(file)
#     for row in file:
#         print(row)


# import csv
#
#
# header = ['name', 'surname', 'age']
# dict1 = {'name': 'John', 'surname': 'Deer', 'age': '38'}
# with open('example.csv', 'w') as file:
#     writer = csv.DictWriter(file, header)
#     writer.writeheader()
#     writer.writerow(dict1)
#
# with open('example.csv', 'r') as file:
#     dict_reader = csv.DictReader(file)
#     for row in dict_reader:
#         print(dict(row))


# import json
# from pprint import pprint as pp
#
#
# employee = {'Job': 'Programmer', 'Age': 38, 'Full Name': 'Galagher, Fred', 'City': 'London', 'Surname': 'Galagher', 'Gender': 'Male', 'Name': 'Fred'}
#
# to_json = json.dumps(employee)
# with open('example.json', 'w') as file:
#     json.dump(to_json, file, indent=4, sort_keys=True)
#
# pp(to_json)
# print(type(to_json))
#
# from_json = json.loads(to_json)
# pp(from_json)
# print(type(from_json))

# ===== API ======
# import requests


# response = requests.post('https://httpbin.org/post', json={'key': 'toto je muj text'})
# print(response.json())

# import requests
# from pprint import pprint as pp
# import json
#
#
# url = 'https://api.openaq.org/v1/locations'
# r = requests.get(url)
# pp(type(eval(r.text)))

# yelp API pip install yelpapi

# import pandas as pd
# data = pd.DataFrame(vlozim treba list listu atd.)
# data.head()
# data.info()
# # pandas funguje podobne jako slovnik
# # object je v pd string
# data.describe()
# data.sort_values(by='hodnoceni', ascending=False)
# data.to_csv('name', header=True)


# from IPython.core.display import HTML

# ==== TWITER =====

# vybrat ucty a stahnout z nich data, ty pak analyzovat
# twitter potrebuje ctyri klice, ty si vygeneruju sam
import tweepy
from textblob import TextBlob


auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access)

api = tweeepy.API(auth)
public_tweets = api.search('Musk')
for tweet in public_tweets:
    print(tweet.text)
# analyza sentimentu
def tweet_sentiment()
def save_to_pandas_as_dict()
def clean_text()


