# lekce s Jakubem Valentou z ENEGTO

# INPUT uvnitr funkce

# def f(k):
#     print(k)
#     input('insert: ')
#
# f(input('Insert anythink: '))

# def my_func(x, y=30):  # y je nastaveno defaultne
#     return x ** yef
#
#
# print(my_func(10, 50))  # pozicni argument
# print(my_func(y=50, x=10))  # klicovy argument
# print(my_func(20))  # vyuziti defaultniho param


# ==== MODULY ====
# secti vsechna cisla ve vygenerovanem silenem stringu

import random
import string
# import re

def vytvor_sileny_string(r, z, max_cislo):
    celkovy_text = ''
    for radek in range(r):
        text_pro_radek = ''
        for znak in range(z):
            text_pro_radek += random.choice(string.ascii_lowercase) \
                            + str(random.randint(0, max_cislo)) \
                            + random.choice(string.punctuation)
        celkovy_text += text_pro_radek + '\n'
    return celkovy_text


def count_num(my_string: str):
    total_sum = 0
    while my_string:
        number = '0'
        while my_string[0].isdigit():
            num = my_string[0]
            number += num
            my_string = my_string[1:]
        total_sum += int(number)
        my_string = my_string[1:]
    return total_sum


# def count_from_list(my_string: str):
#     sum_list = []
#     while my_string:
#         count = 0
#         char = my_string[0]
#         if char not in ('0987654321'):
#             my_string =
#
#     sum_list = my_string.split()


def main():
    r = int(input('Pocet radku: '))
    z = int(input('Pocet znaku v radku: '))
    max_cislo = int(input('Rozsah pro generovani cisla int: '))
    my_string = vytvor_sileny_string(r, z, max_cislo)
    print(my_string)
    print(count_num(my_string))


main()

