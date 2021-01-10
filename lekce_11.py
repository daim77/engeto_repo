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

# # CSV conversion to dict
# import pandas as pd
#
# data_frame = pd.read_csv("/Users/martindanek/Documents/programovani/files/csv/citytemp.csv", header=None)
# arr = data_frame.to_numpy()
#
# result = {}
# for item in arr:
#     city = item[0]
#     unit = item[2]
#     temp = int(item[1])
#     temp_list = []
#
#     if city not in result:
#         result.update({city: {unit: [temp]}})
#     elif unit not in result[city]:
#         result[city].update({unit: [temp]})
#     else:
#         temp_list = result[city][unit]
#         temp_list.append(temp)
#         result[city][unit] = temp_list
#
# print(result)

# ========
# try:
#     #Místo kde vznikne chyba.
#     produkt = 123 / (23 * 0)
#
# #Urči typ chyby a vytvoř alias.
# except ZeroDivisionError as my_error:
#     #Ulož vyjímku.
#     my_error_var = my_error
#     #Nech vypsat proměnou.
#     print('========================')
#     print(my_error.__class__.__name__)
#     print(my_error.__class__)
#     print(my_error)
#     print(my_error.args)
#     print(my_error_var)
#     print('========================')
#     # Získej typ / jméno chyby.
#     typ = type(my_error_var).__name__
#     # Získej zprávu.
#     zprava = my_error_var.args[0]
#     # Poskládej jméno a zprávu tak, aby vytvořily požadovaný text.
#     radek = typ + ': ' + zprava
#     # Nech složený text vypsat.
#     print(radek)

# ==========
# try:
#     num = [1,2,3,4][4]
#     print(num*4)
# except LookupError:
#     print('Zachytávám lookup error')
# except IndexError:
#     print('Zachytávám index error')
# finally:
#     print('Konec')

# # =====TASK 49=====
# # line reader
#
# def line_reader(path: str):
#     try:
#         with open(path, 'r') as txtfile:
#             my_text = txtfile.read()
#             my_text = my_text.split('\n')
#             for part in my_text:
#                 if part == '':
#                     continue
#                 print(part)
#     except FileNotFoundError:
#         file_name = path.split('/')[-1].upper()
#         print('File {} not found!'.format(file_name))
#
#
# line_reader('/Users/martindanek/Documents/programovani/files/txt/lesson_11_line_readerr.txt')

# =====TASK 50=====
# sum up dirty list
def sum_list(list_seq: list):
    result = 0
    try:
        for num in list_seq:
            result += num
        return print(result)
    except (TypeError, ValueError):
        print('Only numbers could be sumed up')
    finally:
        print('Thank you ENGETO :-)')


test = [1, 'asda', {'zvire': 'kocka'}, '3.0', 2.0, [], '\n', '4']
sum_list(test)