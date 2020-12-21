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
# import random
# list1 = []
# for i in range(10):
#     list1.append(random.randrange(0, 1000))
# print(list1)
#
#
# def my_min(__iter):
#     x_min = __iter[0]
#     for item in __iter[1:]:
#         if item < x_min:
#             x_min = item
#     return x_min
#
#
# def my_max(__iter):
#     x_max = __iter[0]
#     for item in __iter[1:]:
#         if item > x_max:
#             x_max = item
#     return x_max
#
#
# print(my_min(list1))
# print(my_max(list1))

# ========== ukol 37 ============
# funkce reversed

# def my_reversed(arg1):
#     seq = list()
#     index = len(arg1) - 1
#
#     for char in arg1[len(arg1)::-1]:
#         seq.append(char)
#         index -= 1
#     return seq
#
#
# list1 = 'Python'
# print(my_reversed(list1))

# ========== ukol 35 ============
# Funkce find


# def my_find(sequence, subchar):
#     result = []
#     for index, char in enumerate(sequence):
#         if char == subchar:
#             result.append(index)
#         continue
#     if result:
#         return result
#     else:
#         return -1


# def my_find(sequence, subchar):
#     return [i for i, x in enumerate(sequence) if x == subchar] or -1

# def my_find(seq, item):
#     for i, obj in enumerate(seq):
#         if obj == item:
#             return i
#     return -1


# print(my_find([3, 4, 5, 4], 4))
# print('ahojda'.find('a'))

# print([i for i, x in enumerate([1, 4, 'a', 3, 'a']) if x == 'a'] or -1)

# ========== ukol 36 ============
# Funkce all() a any()
# def my_all(seq):
#     for item in seq:
#         if not item:
#             return False
#     return True
#
# def my_any(seq):
#     for item in seq:
#         if item:
#             return True
#     return False
#
# print(my_all([43, 5, 87, 21, 23]))
# print(my_all([]))
# print(my_all([0, 12, 431, 3]))
# print('=' * 30)
# print(my_any([43, 45, 87, 21, 23]))
# print(my_any([]))
# print(my_any([0, 12, 431, 3]))
# print(my_any(['', [], (), 0]))

# ========== ukol 38 ============
# funkce sum()

# def my_sum(seq):
#     result = 0
#     for num in seq:
#         result += num
#     return result
#
#
# print(my_sum([32, 43, 54, 54, 76, 21, 62, 83, 52, 58]))

# ========== ukol 39 ============
# # funkce count()
# def my_count(sub, seq):
#     return len([i for i, x in enumerate(seq) if x == sub]) or None


names = [
    'Rob', 'Jim', 'Mark', 'Mark', 'Mark', 'Bob', 'Mark', 'Bob', 'Bob', 'Rob', 'Jim', 'Mark', 'Mark', 'Bob', 'Mark'
]
# print(my_count('Rob', names))
# print(my_count('Frank', names))

# ========== ukol 40 ============
# funkce mean()
# def my_mean(seq):
#     result = 0
#     for num in seq:
#         result += num
#     return float(result / len(seq))
#
#
# sequence = [32, 43, 54, 54, 76, 21, 62, 83, 52, 58]
# print(my_mean(sequence))
# data = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]
# print(my_mean(data))

# ========== ukol 41 ============
# funkce gcd()


# def my_gcd(num1, num2):
#     set1 = set()
#     set2 = set()
#     if not isinstance(num1, int) or not isinstance(num2, int):
#         print('TypeError')
#         exit()
#     devisor = 1
#     while devisor <= num1:
#         if num1 % devisor == 0:
#             set1.add(devisor)
#             devisor += 1
#             continue
#         devisor += 1
#
#     devisor = 1
#     while devisor <= num2:
#         if num2 % devisor == 0:
#             set2.add(devisor)
#             devisor += 1
#             continue
#         devisor += 1
#     return max(set1 & set2)

# def my_gcd(num1, num2):
#     while num1 % num2 != 0:
#         rest = num1 % num2
#         num1, num2 = num2, rest
#     return num2
#
#
# print(my_gcd(78, 414))

# ========== ukol zmena prirazeni v databazi ==========
# I. KROK
# Vlozime zadani
# UDAJE = """
# byt 0001,55 m2,Olomouc,ul.Heyrovského,
# byt 0003,65 m2,Olomouc,ul.Novosadský dvůr,
# byt 0004,75 m2,Olomouc,ul.Wolkerova,
# byt 0004,68 m2,Olomouc,ul.Zikova,
# byt 0001,36 m2,Olomouc,ul.Nová Ulice,
# byt 0003,46 m2,Olomouc,ul.Nové sady,
# byt 0004,75 m2,Olomouc,ul.Nová Ulice,
# byt 0003,42 m2,Olomouc,ul.Nová Ulice,
# byt 0005,107 m2,Olomouc,ul.Nová Ulice,
# byt 0003,74 m2,Olomouc,ul.Uničovská,
# byt 0003,42 m2,Olomouc,ul.Nešverova,
# byt 0002,55 m2,Olomouc,ul.Dělnická,
# byt 0004,59 m2,Olomouc,ul.Zirmova,
# byt 0007,92 m2,Olomouc,ul.Nová Ulice,
# byt 0002,52 m2,Olomouc,ul.Nová Ulice,
# byt 0004,76 m2,Olomouc,ul.Nová Ulice,
# byt 0002,81 m2,Olomouc,ul.Nová Ulice,
# byt 0003,64 m2,Olomouc,ul.Za vodojemem,
# byt 0007,113 m2,Olomouc,ul.Jihoslovanská,
# byt 0005,94 m2,Olomouc,ul.Uničovská,
# byt 0003,42 m2,Olomouc,ul.Rošického,
# byt 0003,75 m2,Olomouc,ul.Rošického,
# byt 0004,48 m2,Olomouc,ul.Handského,
# byt 0004,68 m2,Olomouc,ul.Komenského,
# byt 0003,61 m2,Olomouc,ul.Jarmily Glazarové,
# byt 0004,39 m2,Olomouc,ul.Přichystalova,
# byt 0003,70 m2,Olomouc,ul.Foerstova,
# byt 0005,61 m2,Olomouc,ul.Nová Ulice,
# byt 0007,88 m2,Olomouc,ul.Nová Ulice,
# byt 0003,92 m2,Olomouc,ul.U cukrovaru,
# byt 0003,56 m2,Olomouc,ul.U cukrovaru,
# byt 0004,56 m2,Olomouc,ul.Paseka,
# byt 0002,74 m2,Olomouc,ul.Rokycanova,
# byt 0007,116 m2,Olomouc,ul.U cukrovaru,
# byt 0004,59 m2,Olomouc,ul.Řezáčova,
# byt 0004,100 m2,Olomouc,ul.Libušina,
# byt 0003,64 m2,Olomouc,ul.Řezáčova,
# byt 0001,33 m2,Olomouc,ul.Libušina,
# byt 0006,87 m2,Olomouc,ul.Černá cesta,
# byt 0007,95 m2,Olomouc,ul.Kaštanová,
# byt 0003,74 m2,Olomouc,ul.Nová Ulice,
# byt 0003,75 m2,Olomouc,ul.Nová Ulice,
# byt 0004,86 m2,Olomouc,ul.Hněvotínská,
# byt 0002,67 m2,Olomouc,ul.Polská,
# byt 0007,120 m2,Olomouc,ul.Dvořákova,
# byt 0004,90 m2,Olomouc,ul.Dvořákova,
# byt 0004,86 m2,Olomouc,ul.Nová Ulice,
# byt 0003,75 m2,Olomouc,ul.Nešverova,
# byt 0001,45 m2,Olomouc,ul.Zirmova,
# byt 0010,114 m2,Olomouc,ul.Přichystalová,
# """
#
# PREVOD_UDAJU = {
#     "byt 0001": "1+1",
#     "byt 0002": "2+1",
#     "byt 0003": "2+kk",
#     "byt 0004": "3+1",
#     "byt 0005": "3+kk",
#     "byt 0006": "4+1",
#     "byt 0007": "4+kk",
# }
# result = []
# count = 0
# result_sublist = []
#
# udaje_list = UDAJE.split(',')
#
# for item in udaje_list:
#     item = item.strip('\n')
#     result_sublist.append(item)
#     count += 1
#     if count == 4:
#         result.append(result_sublist)
#         result_sublist = []
#         count = 0
#
# for item in result:
#     if item[0] in PREVOD_UDAJU:
#         item[0] = PREVOD_UDAJU.get(item[0])
#     else:
#         item[0] = 'None'
#     print(item)
#
#
# # vysledek
# #  ['2+kk', '65 m2', 'Olomouc', 'ul.Novosadský dvůr'],
# #  ['3+1', '75 m2', 'Olomouc', 'ul.Wolkerova'],
# #  ['3+1', '68 m2', 'Olomouc', 'ul.Zikova'],
# #  ['1+1', '36 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['2+kk', '46 m2', 'Olomouc', 'ul.Nové sady'],
# # [['1+1', '55 m2', 'Olomouc', 'ul.Heyrovského'],
# #  ['3+1', '75 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['2+kk', '42 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['3+kk', '107 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['2+kk', '74 m2', 'Olomouc', 'ul.Uničovská'],
# #  ['2+kk', '42 m2', 'Olomouc', 'ul.Nešverova'],
# #  ['2+1', '55 m2', 'Olomouc', 'ul.Dělnická'],
# #  ['3+1', '59 m2', 'Olomouc', 'ul.Zirmova'],
# #  ['4+kk', '92 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['2+1', '52 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['3+1', '76 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['2+1', '81 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['2+kk', '64 m2', 'Olomouc', 'ul.Za vodojemem'],
# #  ['4+kk', '113 m2', 'Olomouc', 'ul.Jihoslovanská'],
# #  ['3+kk', '94 m2', 'Olomouc', 'ul.Uničovská'],
# #  ['2+kk', '42 m2', 'Olomouc', 'ul.Rošického'],
# #  ['2+kk', '75 m2', 'Olomouc', 'ul.Rošického'],
# #  ['3+1', '48 m2', 'Olomouc', 'ul.Handského'],
# #  ['3+1', '68 m2', 'Olomouc', 'ul.Komenského'],
# #  ['2+kk', '61 m2', 'Olomouc', 'ul.Jarmily Glazarové'],
# #  ['3+1', '39 m2', 'Olomouc', 'ul.Přichystalova'],
# #  ['2+kk', '70 m2', 'Olomouc', 'ul.Foerstova'],
# #  ['3+kk', '61 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['4+kk', '88 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['2+kk', '92 m2', 'Olomouc', 'ul.U cukrovaru'],
# #  ['2+kk', '56 m2', 'Olomouc', 'ul.U cukrovaru'],
# #  ['3+1', '56 m2', 'Olomouc', 'ul.Paseka'],
# #  ['2+1', '74 m2', 'Olomouc', 'ul.Rokycanova'],
# #  ['4+kk', '116 m2', 'Olomouc', 'ul.U cukrovaru'],
# #  ['3+1', '59 m2', 'Olomouc', 'ul.Řezáčova'],
# #  ['3+1', '100 m2', 'Olomouc', 'ul.Libušina'],
# #  ['2+kk', '64 m2', 'Olomouc', 'ul.Řezáčova'],
# #  ['1+1', '33 m2', 'Olomouc', 'ul.Libušina'],
# #  ['4+1', '87 m2', 'Olomouc', 'ul.Černá cesta'],
# #  ['4+kk', '95 m2', 'Olomouc', 'ul.Kaštanová'],
# #  ['2+kk', '74 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['2+kk', '75 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['3+1', '86 m2', 'Olomouc', 'ul.Hněvotínská'],
# #  ['2+1', '67 m2', 'Olomouc', 'ul.Polská'],
# #  ['4+kk', '120 m2', 'Olomouc', 'ul.Dvořákova'],
# #  ['3+1', '90 m2', 'Olomouc', 'ul.Dvořákova'],
# #  ['3+1', '86 m2', 'Olomouc', 'ul.Nová Ulice'],
# #  ['2+kk', '75 m2', 'Olomouc', 'ul.Nešverova'],
# #  ['1+1', '45 m2', 'Olomouc', 'ul.Zirmova'],
# #  [None, '114 m2', 'Olomouc', 'ul.Přichystalová']]


