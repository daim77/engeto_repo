# a, b, c = 1, 2, 3
# print(a, b, c)
#
# # Prirazeni prvku lst do promennych
# l1, l2, l3, l4 = [1, 'pes', 2.3, ['vnoreny list']]
#
# # Tisk promennych z lst
# print(l4)

# # Nas list
# lst = [1, 'pes', 2.3, ['vnoreny list']]
#
# # Prirazeni prvku lst do promennych
# predposledni, posledni = lst[-2:]
#
# # Tisk
# print(predposledni)
# print(posledni)
#
# # Prirazeni znaku str do promennych
# p1, p2, p3, p4 = 'ahoj'
#
# # Tisk promennych ze str
# print(p1)
# print(p2)
# print(p3)
# print(p4)
#
# # Prirazeni promennych
# a, b = 1, 2
#
# # Tisk a,b
# print(a, b)
#
# # Prepsani promennych
# a, b = b, a + b
#
# # Opakovany tisk a,b
# print(a,b)
#
# # Prirazeni novych promennych
# a01, a02, a03 = [a, b, [1, 2, 3, ['x', 'y']]]
#
# # Tisk a03
# print(a03)
#
# # Rozlozeni promenne a03
# b01, b02, b03, b04 = a03
#
# # Tisk "x" a "y" z b04
# print(b04[0], b04[1])
#
# # Prirazeni pomoci range
# a, b = range(2)
#
# # Tisk promennych
# print (a, b)

# Slovnik
# d = {'name': 'Bob', 'surname': 'Francis'}
#
# # Prirazeni klicu
# kategorie1, kategorie2 = d  # hodnoty pak pres metodu .values(), d.items() vytvri tuple klic, hodnota
#
# # Tisk promennych
# print(kategorie1)
# print(kategorie2)

# Prirazeni hodnot
# d = {'name': 'Bob', 'surname': 'Francis'}
# item1, item2 = d.items()
#
# # Tisk promennych
# print(item1)
# print(item2)

# # Prirazeni prebytecnych hodnot
# prvni, *zbytek = 'AHOJ'
#
# # Tisk promennych
# print('Nejdrive', prvni, 'a potom', zbytek)


# # Oprav kod
# a, *b = 'Kolo'  # rozbalovani pomoci *
#
# # Tisk promennych
# print(a, b)

# # Použití rozbalovacího operátoru
# a, *b, c, d = 1, 2, 3
#
# # Tisk proměnných
# print(a,b,c,d)
# print(type(a))

# *a, = 'abcd'
# print(a)

# print(sum((1,2,4)))

# def secti_dve_cisla(a,b):
#     return a + b
# print(secti_dve_cisla(1, 2))

# def fce nemusi obsahovat returne
# def ukaz_sachovnici(rozmery):
#     for radek in range(rozmery):
#         print()
#         for sloupec in range(rozmery):
#             znak = '#' if (radek + sloupec) % 2 == 1 else ' '
#             print(znak, end='')
#     print()
# ukaz_sachovnici(10)

# # TASK na secteni cisel
# # Hlavicka funkce
# def soucet_rady(a, b):
#     vysledek = 0
#     for x in range(a, b+1):
#         vysledek += x
#     return vysledek
# print(soucet_rady(0, 200))

# def pozdrav():
#     print('Hello')
#
# def obal(abc):
#     return abc()
#
# obal(pozdrav)

# import random
# print(int(100*random.random()))

# # Nas list
# lst = [45, 21, 53, 1, 213, 43, 42, 85]
# print(lst)
# # Promichani a tisk listu
# random.shuffle(lst)
# print(lst)

# import random
# # Databaze
# ids = ['X5235', 'X6752']
#
# # Vygenerovani nahodnenho cisla mezi 1000 a 9999
# id_number = random.randint(1000, 9999)
#
# # Pridani nami vegenerovaneho id, pokud uz neni v databazi
# ids.append('X' + str(id_number)) if 'X' + str(id_number) not in ids else print('')
#
# # Tisk
# print(ids)
#
# # shuffle and sample
# print(random.sample(ids, len(ids)))
# print(random.shuffle(ids))
# print(ids)

# TEXT = 'Toto je muj text k zarovnani.'
# print(TEXT)
# print(TEXT.rjust(len(TEXT) + 10, '_'))  # jede od prava

# ========== ukol 34 ============
import random
list1 = []
for i in range(10):
    list1.append(random.randrange(0, 1000))
print(list1)


def fce_min(__iter):
    x = __iter.pop()
    for i in __iter:
        if i < x:
            x = i
    return x


print(fce_min(list1))
