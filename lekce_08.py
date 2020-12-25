# import random
#
#
# def order_sequence(my_list):
#     for i in range(1, len(my_list)):
#         pos = i
#         while pos > 0 and my_list[pos-1] > my_list[pos]:
#             my_list[pos], my_list[pos-1] = my_list[pos-1], my_list[pos]
#             pos -= 1
#
# def generate_random_list(size):
#     lst = []
#     for i in range(size):
#         lst.append(random.randint(1, 100))
#     return lst
#
#
# list1 = generate_random_list(10)
# print('Before sorting:', list1)
# order_sequence(list1)
# print('After sorting:', list1)

# import random
#
# # Vnejsi fce
#
#
# def wrapper():
#     start = random.randint(1, 10)
#     end = random.randint(10, 100)
#     print('Původní hodnoty proměnných: start:', start, 'end:', end)
#     # Vnitrni fce
#
#     def inner():
#         # Deklarace nelokalnich promennych <-- ZDE
#         nonlocal start, end
#         start += 5
#         end += 5
#         return range(start, end)
#     # Zavolani fce inner
#     inner()
#     print('Funkce inner změnila hodnoty mých proměnných: start:', start, 'end:', end)
#     # Vraceni inner
#     return inner
# # Zavolani fce wrapper a ulozeni vysledku do promenne func
# func = wrapper()
# print(func)

# import time
# Definice fce


# def list_divisibles(start, stop, divisor):
#     divisibles = []
#     for num in range(start, stop):
#         if num % divisor == 0:
#             divisibles.append(num)
#     return divisibles

# Definice fce


# def timer(start, stop, divisor):
#
#     # Zjisteni casu pred vykonem fce
#     start_time = time.time()
#
#     # Vykonani fce func
#     list_divisibles(start, stop, divisor)
#
#     # Zjisteni casu vykonani fce
#     total_time = time.time() - start_time
#
#     # Vraceni dobu trvani vykonu fce func
#     return total_time
#
#
# print(timer(10, 100, 3))

# ========== UKOL 42 ==========
# luhn test


# def luhn(number):
#     sum_even = 0
#     sum_odd = 0
#     for order, num in enumerate(str(number)[::-1]):
#         if (order + 1) % 2 == 0 and (2 * int(num)) < 10:
#             sum_even += 2 * int(num)
#         elif (order + 1) % 2 == 0 and (2 * int(num)) >= 10:
#             sum_even += (2 * int(num) - 9)
#         else:
#             sum_odd += int(num)
#     if (sum_even + sum_odd) % 10 == 0:
#         return True
#     else:
#         return False
#
#
# my_card = luhn(5315336909269265)
# print(my_card)

# ========== UKOL 43 ==========
# ANAGRAM


def all_anagrams(list_of_anagrams: list):
    list_of_anagrams_decomposed = []
    count = 0
    if not list_of_anagrams:
        return False
    if len(list_of_anagrams) == 1:
        return True
    for item in list_of_anagrams:
        list_of_anagrams_decomposed.append(sorted(list(item)))
    last_word = list_of_anagrams_decomposed.pop()
    for item in list_of_anagrams_decomposed:
        if last_word == item:
            count += 1
    if count == len(list_of_anagrams) - 1:
        return True
    else:
        return False


words = ['ship', 'hips', 'name']
print(all_anagrams(words))
