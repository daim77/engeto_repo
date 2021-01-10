# # Errors
# def suma(lst):
#     # Vytváříme proměnou pro výsledek.
#     vysledek = 0
#     for num in lst:
#         vysledek += num
#     # Vracíme výsledek.
#     return vysledek
#
#
# def prvky(lst):
#     # Vytváříme proměnou pro výsledek.
#     pocet_prvku = 0
#     for i in lst:
#         # Načítáme počet prvků
#         pocet_prvku += 1
#     # Vracíme výsledek.
#     return pocet_prvku
#
#
# def prumer(lst):
#     # Vracíme výsledek předchozích funkcí.
#     return suma(lst) / prvky(lst)
#
#
# # Testovací listy.
# list1 = []
# list2 = [1, 2, 'a', 55]
# list3 = [1, 2, 3, 4, 5]
#
# # Zkoušíme to všechno spustit.
# try:
#     # Do nové proměné zkus postupně uložit průměr testovacích listů
#     prumer_listu = prumer(list3)
#     print(prumer_listu)
# # Odchytáváme dělení nulou.
# except TypeError:
#     # Vypisujeme zprávu.
#     print('neni cislo')
# # Odchytáváme chybu při sčítání.
# except ZeroDivisionError:
#     # Vypisujeme zprávu.
#     print('empty list')

# CSV conversion to dict
import pandas as pd

data_frame = pd.read_csv("/Users/martindanek/Documents/programovani/files/csv/citytemp.csv", header=None)
arr = data_frame.to_numpy()

result = {}
for item in arr:
    city = item[0]
    unit = item[2]
    temp = int(item[1])
    temp_list = []

    if city not in result:
        result.update({city: {unit: [temp]}})
    elif unit not in result[city]:
        result[city].update({unit: [temp]})
    else:
        temp_list = result[city][unit]
        temp_list.append(temp)
        result[city][unit] = temp_list


print(result)
