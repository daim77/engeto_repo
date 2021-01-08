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

# import random
# import string
# import time
#
#
# def vytvor_sileny_string(r, z, max_cislo):
#     celkovy_text = ''
#     for radek in range(r):
#         text_pro_radek = ''
#         for znak in range(z):
#             text_pro_radek += random.choice(string.ascii_lowercase) \
#                             + str(random.randint(0, max_cislo)) \
#                             + random.choice(string.punctuation)
#         celkovy_text += text_pro_radek + '\n'
#     return celkovy_text
#
#
# def count_num(my_string: str):
#     start_time = time.time()
#     total_sum = 0
#     while my_string:
#         number = '0'
#         while my_string[0].isdigit():
#             num = my_string[0]
#             number += num
#             my_string = my_string[1:]
#         total_sum += int(number)
#         my_string = my_string[1:]
#     total_time = time.time() - start_time
#     return total_sum, total_time
#
#
# def count_list(my_string):
#     start_time = time.time()
#     vysledek = 0
#     vysledny_text = ""
#     for znak in my_string:
#         if znak in string.ascii_lowercase or znak in string.ascii_uppercase:
#             pass
#         elif znak.isdigit():
#             vysledny_text += znak
#         elif znak in string.punctuation:
#             vysledny_text += ' '
#         else:
#             pass
#     for cislo in vysledny_text.split():
#         vysledek += int(cislo)
#     total_time = time.time() - start_time
#     return vysledek, total_time
#
#
# def count_my_list(my_string):
#     start_time = time.time()
#     string_list = [char if char.isdigit() else ' ' for char in my_string]
#     total_sum = sum([int(num) for num in ''.join(string_list).split()])
#     total_time = time.time() - start_time
#     return total_sum, total_time
#
#
# def main():
#     r = int(input('Pocet radku: '))
#     z = int(input('Pocet znaku v radku: '))
#     max_cislo = int(input('Rozsah pro generovani cisla int: '))
#     my_string = vytvor_sileny_string(r, z, max_cislo)
#     print(count_num(my_string), '|', count_list(my_string), '|', count_my_list(my_string))
#
#
# main()


# def my_sum(*args):
#     result = sum([num for num in args])
#     return result
#
#
# print(my_sum(*range(4)))

# === CALCULATOR ===
