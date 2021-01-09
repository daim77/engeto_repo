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


