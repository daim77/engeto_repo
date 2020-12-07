# Co se naučíš v tomto kurzu
# Datový typ Range,
# smyčka For,
# základy funkcí,
# formátování string,

# print('0-19:    ', list(range(20)))
# print('15-19:   ', tuple(range(15,20)))
# print('10-19:   ', tuple(range(10,20,3)))
#
# # Do proměnné nums vytvoř list pomocí range, který bude obsahovat každé číslo,
# # které je dělitelné 5 v rozmezí od 1-100.
# nums = list(range(5,101,5))
# print(nums)
#
# print(list(range(10)[2:6]))

# # For loop
# for num in range(10):
#     print(num)

# muj_str = 'Hello World'
# for i in range(len(muj_str)):
#     print(muj_str[i])
#
# for i in muj_str:
#     print(i)


# # Zadani tuplu
# data = (('Věk',43,True),('Jméno','John',True),('Příjmení','Smith',False))
#
# # For loop
# for category, value, indicator in data:
#     print(f"{category} : {value} : {indicator}")

# # DICT
# zamestnanci = {'Jméno': 'John', 'Příjmení': 'Smith', 'Věk': 43}
# # For loop
# for klic in zamestnanci:
#     print(klic)
# # To znamená, že procházení klíčů je nastavené u slovníku jako defaultní možnost.
#
# for hodnota in zamestnanci.values():
#     print(hodnota)
#
# for klic, hodnota in zamestnanci.items():
#     print(klic,hodnota)

# Promenna
# muj_str = 'Python'

# # For loop
# for index in range(len(muj_str)-1,-1,-1):
#     znak = muj_str[index]
#     print(znak, end='')

# Tabulka
tabulka = [['ID','NAME','PRICE','AMOUNT'],
         ['X131', 'Pipe', 2.05, 1000],
         ['XT12', 'Screw', 0.35, 1000],
         ['Z43', 'Nail', 0.95, 1000],
         ['P843', 'Tape', 1.39, 1000]
]

# # For loop
# for radek in tabulka:
#     for prvek in radek:
#         print(str(prvek) + "    ", end='')
#     print('')

# # enumerate()
# nejaky_string = 'For loops podporují iterační protokol'
# print(list(enumerate(nejaky_string)))
# for i, char in enumerate(nejaky_string):
#     if i % 2 == 0:
#         char = char.upper()
#     print(char, end='')