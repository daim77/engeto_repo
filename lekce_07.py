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

def my_gcd(num1, num2):
    while num1 % num2 != 0:
        rest = num1 % num2
        num1, num2 = num2, rest
    return num2


print(my_gcd(78, 414))
