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


# def all_anagrams(list_of_anagrams: list):
#     list_of_anagrams_decomposed = []
#     count = 0
#     if not list_of_anagrams:
#         return False
#     if len(list_of_anagrams) == 1:
#         return True
#     for item in list_of_anagrams:
#         list_of_anagrams_decomposed.append(sorted(list(item)))
#     last_word = list_of_anagrams_decomposed.pop()
#     for item in list_of_anagrams_decomposed:
#         if last_word == item:
#             count += 1
#     if count == len(list_of_anagrams) - 1:
#         return True
#     else:
#         return False
#
#
# words = ['ship', 'hips', 'name']
# print(all_anagrams(words))

# ========== UKOL 44 ==========
# email collection from txt

# # Funkce pro posbirani emailu ze stringu
# def collect_emails(text: str):
#     list_of_all_emails = []
#     collect_all = text.split(' ')
#     for item in collect_all:
#         char = item.strip('.!?\n')
#         if '@' and '.' in char:
#             list_of_all_emails.append(char)
#             continue
#     return list_of_all_emails
#
#
# # Funkce pro extrahovani emailu obsahujici cisla
# def select_num_emails(list_of_all_emails: list):
#     list_of_num_emails = []
#     for email_item in list_of_all_emails:
#         for number in range(10):
#             if str(number) in email_item:
#                 list_of_num_emails.append(email_item)
#                 break
#     return list_of_num_emails
#
#
# # Funkce pro extrahovani domen vsech emailu
# def select_domains(list_of_all_emails):
#     list_of_domains = []
#     for email_item in list_of_all_emails:
#         list_of_domains.append(email_item.split('@')[1])
#     return list_of_domains
#
#
# # def extract_domains(emails):
# # main func to generate dict
# def specemail(arg1: str):
#     my_dict = {'emails_with_nums': [], 'domains': []}
#     my_dict['emails_with_nums'] = select_num_emails(collect_emails(arg1))
#     my_dict['domains'] = select_domains(collect_emails(arg1))
#     return my_dict
#
#
# my_str = '''
#     Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#     Mauris vulputate lacus id eros consequat tempus. Nam viverra velit sit amet lorem lobortis,
#     at tincidunt nunc ultricies. Duis facilisis ultrices lacus, id tiger123@email.cz auctor massa molestie at.
#     Nunc tristique fringilla congue. Donec ante diam cnn@info.com, dapibus lacinia vulputate vitae,
#     ullamcorper in justo. Maecenas massa purus, ultricies a dictum ut, dapibus vitae massa.
#     Cras abc@gmail.com vel libero felis. In augue elit, porttitor nec molestie quis, auctor a quam.
#     Quisque b2b@money.fr pretium dolor et tempor feugiat. Morbi libero lectus, porttitor eu mi sed,
#     luctus lacinia risus. Maecenas posuere leo sit amet spam@info.cz. elit tincidunt maximus.
#     Aliquam erat volutpat. Donec eleifend felis at leo ullamcorper cursus. Pellentesque id dui viverra,
#     auctor enim ut, fringilla est. Maecenas gravida turpis nec ultrices aliquet.
# '''
#
# print(specemail(my_str))

# ========== UKOL 45 ==========
# # Eratosthenovo síto - prvocislo
#
# def list_primes(arg: int):
#     list_of_primes = []
#     list_numbers = [number for number in range(arg, 1, -1) if arg >= 2]
#     while list_numbers[0] ** (1/2) >= list_numbers[- 1]:
#         number = list_numbers.pop()
#         list_of_primes.append(number)
#         list_numbers = [x for x in list_numbers if x % number != 0]
#     list_numbers.reverse()
#     list_of_primes.extend(list_numbers)
#     return list_of_primes
#
#
# def is_prime(arg: int):
#     if arg in list_primes(arg):
#         return True
#     else:
#         return False
#
#
# print(is_prime(25))

# reseni z wikipedie
# https://cs.wikipedia.org/wiki/Eratosthenovo_s%C3%ADto


# def eratosthenovo_sito(do):
#     do += 1
#     sito = [True] * do
#
#     for i in range(2, do):
#         if sito[i]:
#             for j in range(i ** 2, do, i):
#                 sito[j] = False
#
#     prvocisla = []
#     for i in range(2, do):
#         if sito[i]:
#             prvocisla.append(i)
#     return prvocisla
#
#
# print(eratosthenovo_sito(5))

# # ========== UKOL 46 ==========
# # Caesarova šifra
#
#
# def caesar_cypher(text: str, shift: int):
#     abc_key = 'abcdefghijklmnopqrstuvwxyz'
#     text_modified = str()
#     for char in text:
#         if char in abc_key:
#             index = abc_key.find(char)
#             index = (index + shift) % 26
#             text_modified += abc_key[index]
#             continue
#         if char in abc_key.upper():
#             index = (abc_key.upper()).find(char)
#             index = (index + shift) % 26
#             text_modified += abc_key.upper()[index]
#             continue
#         else:
#             text_modified += char
#     return text_modified
#
#
# print(caesar_cypher('abcTd', 1))

# ========== UKOL 47 ==========
# word game sibenice
import random


def ask_letter():
    letter = input('Guess one letter: ')
    return letter


def sibenice(words: list):
    word = random.choice(words)
    count = len(word) + 5
    print('Welcome and explanations')
    while count:
        letter = ask_letter()
        print(letter, count)
        count -= 1
    return print(word)


sibenice(['weights', 'are', 'converted', 'cumulative', 'weights', 'before', 'making', 'selections'])
