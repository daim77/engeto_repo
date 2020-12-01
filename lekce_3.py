# #Napis kod, ktery bude testovat zda je krestni jmeno v listu. Pokud ne, tak ho prida.
# list_jmen = ["Petr","Karel","Ladislav", "Jarmil"]
# my_name = input('Zadej jmeno: ')
# if not my_name in list_jmen:
#     list_jmen.append(my_name)
# print(list_jmen)
# #Pokud zadane jmeno zacina na pismeno K, tak tohle jmeno vypis.
# if my_name[0] == 'K':
#     print(my_name)
# # my_name.startswith('K')
#
# #Pokud splnuje obe podminky, tak vypis toto jmeno, tak ze vsechna pismena jsou velka.
# if (my_name in list_jmen) and my_name[0] == 'K':
#     print('toto je jmeno z listu:', my_name.upper())


# # SLOVNIK DICTIONARY
# slovnk = dict() # pro prehlednost konstruktorem
# slovnik = {'jmeno':'Jakub', 'prijmeni':'Valenta'}
# print(slovnik['jmeno'][:2])
# slovnik['jazyky'] = ['Python', 'Java', 'C++']
# print(slovnik)
# # metody
# print(list(slovnik.keys()))
# print(list(slovnik.values()))
# print(list(slovnik.items())) # tuply
# print(len(slovnik))
# print(slovnik.get('adresa', "Klic neni ve slovniku")) # pokud tam klic je, vrati hodnotu
# print(slovnik.setdefault('prazdnej_list', []).append(slovnik['jazyky'])) # retezeni metod
# print(slovnik)

# predpripraveni DICT
film0 = dict()
film0['JMENO'] = None
film0['HODNOCENI'] = None
film0['ROK'] = None
film0['REZISER'] = None
film0['HRAJI'] = None
film0['STOPAZ'] = None

# naplneni slovniku
film0['JMENO'] = 'Shawshank redemption'
film0['HODNOCENI'] = 93

print(film0)
print(film0.pop('JMENO'))
print(film0)

# rozdil mezi DEL a .CLEAR

# # tvoreni databaze | jako klic nemuze byt menitelny datovy typ
# film1 = dict()
# film1 = {
# 'JMENO': 'Shawshank Redemption',
# 'HODNOCENI': 93,
# 'ROK': 1994,
# 'REZISER': 'Frank Darabont',
# 'HRAJI': ['Tim Robbins', 'Morgan Freeman'],
# 'STOPAZ': "144 min"
# }
# filmova_db = dict()
# # filmova_db[film1] # spatne
# filmova_db[film1['JMENO']] = film1
# print(filmova_db)

# type SET - mnoziny
# Promenne
PREDMETY = (
    'Premenovani',
    'Astronomie',
    'Obrana_proti_cerne_magii',
    'Bylinkarstvi',
    'Lektvary'
)

SKUP_PREMENOVANI = ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann', 'Ron', 'Hermiona']
SKUP_ASTRONOMIE = ['Marcus','Alex','Glenn','Samuel', 'Hermiona', 'Clara','Chelsea']
SKUP_OBRANA = ['Hermiona', 'Adam','Tyler', 'Alex','Clara']
SKUP_BYLINKARSTVI = ['Abraham','Marcus', 'Hermiona', 'Alex','Glenn','Clara']
SKUP_LEKTVARY = ['Alfred', 'Curt','Oliver','Tyler', 'Hermiona', 'Ann']

ROZVRH = dict()
ROZVRH['Premenovani'] = ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann', 'Ron', 'Hermiona']
print(ROZVRH)


