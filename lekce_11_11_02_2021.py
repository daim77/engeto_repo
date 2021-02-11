# #vytvorte slovnik poctu jednotlivych barev
# list_barev = ["cervena", "cervena", "modra", "bila", "cerna", "zluta", "modra"]
#
# slovnik = {}
# list_barev = ['cervena', 'cervena', 'modra', 'cerna', 'zluta', 'modra']
# for i in list_barev:
#   slovnik[i] = slovnik.get(i, 0) + 1
# print(slovnik)
#
# slovnik = {}
# list_barev = ['cervena', 'cervena', 'modra', 'cerna', 'zluta', 'modra']
# for i in list_barev:
#   slovnik[i] = slovnik.setdefault(i, 0) + 1
# print(slovnik)
#
# def barvy(sekvence:list) -> dict:
#     slovnik = dict()
#     for item in list_barev:
#         slovnik[item] = slovnik.get(item, 0) + 1
#     return slovnik
# list_barev = ["cervena", "cervena", "modra", "bila", "cerna", "zluta", "modra"]
# print(barvy(list_barev))
#
# colors = ["cervena", "cervena", "modra", "bila", "cerna", "zluta", "modra"]
# vysledky = dict()
# for i in colors:
#     if i in vysledky:
#         vysledky[i] = vysledky[i]+1
#     else:
#         vysledky.update({i:1})
# print(vysledky)
#
# list_barev = ["cervena", "cervena", "modra", "bila", "cerna", "zluta", "modra"]
# pocet_barev = {}
# while list_barev:
#     barva = list_barev.pop()
#     if barva not in pocet_barev:
#         pocet_barev[barva]= 0
#     pocet_barev[barva] += 1
# print(pocet_barev)
#
# list_barev = ["cervena", "cervena", "modra", "bila", "cerna", "zluta", "modra"]
# {key : list_barev.count(key) for key in list_barev}
#
# import csv
# file = open('example.csv', "w")
# file_writer = csv.writer(file)
# file_writer.writerow(list_barev)
# file.close()
#
# with open('exampleI.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Surname','Name','Age','City','Job', 'Gender'])
#     writer.writerow(['Smith','John',32,'London','Programmer',])
#     writer.writerow(['Doe', 'Joe',34,'Liverpool',"",'Male'])
#
# with open('exampleI.csv', 'r') as file:
#     file_reader = csv.reader(file)
#     for row in file_reader:
#       print(row)
#
# dict1 = {'Job': 'Programmer', 'Age': 38, 'Full Name': 'Galagher, Fred', 'City': 'London', 'Surname': 'Galagher', 'Gender': 'Male', 'Name': 'Fred'}
# header = ['Surname', 'Name', 'Full Name', 'Age', 'City', 'Job', 'Gender']
#
# file = open("file.csv", "w")
# writer = csv.DictWriter(file, header)
# writer.writeheader()
# writer.writerow(dict1)
# file.close()
#
# with open('salary.csv', 'w') as file:
#     fieldnames = ['name', 'salary']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'name': 'Ronaldo', 'salary': 2870})
#     writer.writerow({'name': 'Buffon', 'salary': 2822})
#     writer.writerow({'name': 'Pietro', 'salary': 2801})
#
# with open('salary.csv', 'r') as file:
#   dict_reader = csv.DictReader(file)
#   for row in dict_reader:
#     print(dict(row))
#
# def csv_to_pytho(filename):
#   with open(filename, 'r') as file:
#     dict_reader = csv.DictReader(file)
#     return [dict(row) for row in dict_reader]
# filename = "salary.csv"
# csv_to_pytho(filename)
#
# hlavicka = ['Surname', 'Name', 'Full Name', 'Age', 'City', 'Job', 'Gender'] #Hlavička(jména sloupců)
#
# obsah = [['Smith', 'John', 'Smith, John', '32', 'London', 'Programmer', ''], #Data ( list listů)
#
# ['Doe', 'Joe', 'Doe, Joe', '34', 'Liverpool', '', 'Male'],
#
# ['Murphy', 'Ann', 'Murphy, Ann', '29', 'London', 'Admin', 'Female'],
#
# ['Cook', 'Floyd', 'Cook, Floyd', '28', '', 'Tester', 'Male'],
#
# ['Glenn', 'Taylor', 'Glenn, Taylor', '35', 'Birmingham', 'Manager', 'Female'],
#
# ['Mills', 'Amanda', 'Mills, Amanda', '41', 'Leicester', 'Quality Assurance', 'Female']]
#
#
# with open("newfile.csv", "w") as file:
#   writer = csv.writer(file)
#   writer.writerow(hlavicka)
#   writer.writerows(obsah)
#
#   # for row in obsah:
#   # writer.writerow(row)
#
# """# Json"""
#
# import json
# employee = {'Job': 'Programmer', 'Age': 38, 'Full Name': 'Galagher, Fred', 'City': 'London', 'Surname': 'Galagher', 'Gender': 'Male', 'Name': 'Fred'}
# to_json = json.dumps(employee, indent= 5)
# print(to_json, type(to_json))
#
# with open("test.json", "w") as file:
#   file.write(to_json)
#
# with open("test.json", "r") as file:
#   data = file.read()
#   data = json.loads(data)
#   print(data, type(data))
#
# dict1 = {'Name': 'Fred', 'Job': 'Programmer', 'Full Name': 'Galagher, Fred', 'Surname': 'Galagher', 'City': 'London', 'Gender': 'Male', 'Age': 38}
# json_string_sorted = json.dumps(dict1, indent=4, sort_keys=True)
# json_string_sorted
#
# employee = {
#             "Name": "Fred",
#             "Job": "Programmer",
#             "Full Name": "Galagher, Fred",
#            }
#
# with open("emloyees.json", "w") as file:
#   json.dump(employee, file, indent=4, sort_keys=True)
#
# with open("emloyees.json", "r") as file:
#   data = json.load(file)
#   print(data, type(data))
#
# HTTP Protokol
# -1xx Proces stále pokračuje -2xx Přístup povolen(200) -3xx Přesměrování -4xx Přístup odepřen (404) -5xx Server Error
#
# Metody HTTP
# GET - vyžádá daný dokument nebo video - obecně zdroj - tato metoda se používá k načtení dat
# POST - metoda používaná k odesílání dat na server, např. pro autentizaci nebo registraci atd.
# PUT - podobně jako metoda POST v tom, že posíláme některá data na server, ale server by měl aktualizovat daný (existující) záznam nebo jiný zdroj na novou hodnotu, posíláme jej
# DELETE - odebere daný prostředek
# HEAD - požaduje odpověď totožnou s odpovědí na požadavek GET, ale bez těla odpovědi
# OPTIONS - zeptá se serveru, jaké metody daný zdroj podporuje - daná webová stránka atd.
#
# Pro naše účely (stahování dat a odesílání dat) nás bude zajímat metoda GET a POST.
#
# <body>
#     <h1>This is a heading</h1>
#     <p>And this is the paragraph number 1</p>
#
#     <p> This is the paragraph number 2</p>
# </body>
#
# <a href="https://www.google.com/" target="_blank">Go to Google</a>
#
# import requests
# response = requests.post('https://httpbin.org/post', json={'key':'Tohle je muj text'})
# response
#
# dir(response)
#
# response.json()
#
# response.status_code
#
# r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Brno')
# r.status_code
#
# r.text
#
# r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=d7fbd888f435c075cdd7d5a28ed0c899')
# r.status_code
#
# r.json()
#
# pocasi_slovnik = r.json()
#
# pocasi_slovnik.keys()
#
# pocasi_slovnik["weather"][0]["id"]
#
# import requests
# from pprint import pprint
# import json
#
# url = "https://api.openaq.org/v1/locations"
# r = requests.get(url)
# print(r.status_code)
# data = r.json()
# pprint(data, indent=4)
#
# data.keys()
#
# for i in data["results"]:
#   print(i['city'])
#
# city = input("Name of the city you want: ").upper().title()
# country = input("Country sign: ")
# appi_key = "0ed495ca49c2ade2cfc4b47bf6456878"
# url = "https://samples.openweathermap.org/data/2.5/forecast?q={},{}&appid={}".format(city,country,appi_key)
# res = requests.get(url)
# data= res.json()
# data
#
# """# Yelp"""
#
# #@title
# Client_ID = "3qHY6E4NeBeyZsY3pWwtpg"
# API_Key = "fd2CIcawCrcE59KSeyecCXm4ajbUSaXorT9ms-g7oufDYftDSPGaheCto0nSsESjDwBB7m32M9X17ELjiLmuTUitT-Cb2jsgVbwm0ECxFdYxEjZd2AtU2rwb5pcDX3Yx"
#
# !pip install yelpapi
#
# from yelpapi import YelpAPI
# yelp_api = YelpAPI(API_Key)
#
# dir(yelp_api)
#
# term = 'czech cuisine'
# location = 'Prague, Pg'
# search_limit = 50
# response = yelp_api.search_query(term = term,
#                                  location = location,
#                                  limit = search_limit
#                                  )
#
# dir(response)
#
# response
#
# response.keys()
#
# type(response["businesses"])
#
# response["businesses"][0].keys()
#
# for d in response["businesses"]:
#   print(d["name"], d["rating"], d["location"]["address1"], d["phone"])
#
# import pandas as pd
# data = pd.DataFrame([ (d["name"], d["rating"], d["location"]["address1"], d["phone"]) for d in response["businesses"]], columns=["jmeno_restaurace", "hodnoceni", "adresa", "telefon"])
#
# data.head()
#
# data.info()
#
# data["hodnoceni"].mean()
#
# data.describe()
#
# serazena_data = data.sort_values(by="hodnoceni", ascending=False)
#
# dir(serazena_data)
#
# serazena_data.to_csv("yelp_restaurace_praha.csv", header=True)
#
# with_pictures = pd.DataFrame([(i["name"], i["rating"], i["location"]["address1"], i["phone"], i["image_url"]) for i in response["businesses"]], columns=["jmeno_restaurace", "hodnoceni", "adresa", "telefon", "obrazek"])
#
# from IPython.core.display import HTML
#
#
# # convert your links to html tags
# def path_to_image_html(path):
#     return '<img src="'+ path + '" width="60" >'
#
# pd.set_option('display.max_colwidth', -1)
# HTML(with_pictures.to_html(escape=False ,formatters=dict(picture=path_to_image_html)))
#
#
#
# import tweepy
# from textblob import TextBlob
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# dir(tweepy)
#
# api = tweepy.API(auth)
#
# public_tweets = api.search("Musk")
#
# for tweet in public_tweets:
#   print(tweet.text)
#
# def tweet_sentiment(tweets,vote=None):
# 	for tweet in tweets:
# 		print(tweet.text)
# 		if vote =="user":
# 			analysis = TextBlob(tweet)
# 		else:
# 			analysis = TextBlob(tweet.text)
# 		print(analysis.sentiment)
# 		if analysis.sentiment[0]>0:
# 			print ('Positive')
# 		else:
# 			print ('Negative')
# 		print("")
# tweet_sentiment(public_tweets)