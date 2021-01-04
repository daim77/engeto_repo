# Formátování stringů a textové soubory

# person_data = {'name': 'Bob', 'age': 37}
# print('My name is %(name)s and I am %(age)d years old.' % person_data)
# # nebo
#
#
# print('My name is {name} and I am {age} years old.'.format(name='Bob', age=37))
#
#
# name = 'Bob'
# age = 37
# print('My name is {name} and I am {age} years old.'.format(name=name, age=age))
#
#
# person_data = {'name': 'Bob', 'age': 37, 'job': 'freelancer'}
# print('My name is {name} and I am {age} years old.'.format(**person_data))

# format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# fill            ::=  <any character>
# align           ::=  "<" | ">" | "=" | "^"
# sign            ::=  "+" | "-" | " "
# width           ::=  digit+
# grouping_option ::=  "_" | ","
# precision       ::=  digit+
# type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

# data = ('car', 1037.123456789, 'freelancer')
# print('|word: {0:*^11}|number: {1:#>+15,.7E}|'.format(*data))
# print('|{0:*<6c}|'.format(90))
#
# # %[(klic)][zarovnani_vypln][sirka][.presnost][typecode]
# print('|%#5x|' % (54,))

# # Hodnoty a sirky
# num1 = 45 / 3
# width1 = len(str(num1)) + 2
# num2 = 45 * 3
# width2 = len(str(num2)) + 2
# num3 = 45 % 3
# width3 = len(str(num3)) + 2
#
# # Dynamicke formatovani sirky
# print('|%-*d|%0*d|%-*d|%+*d|% *d|' % (width1, num1, width1, num2, width2, num3, width3, 45678, width2, 45))


# import sys
#
#
# file = open(r'/Users/martindanek/Documents/programovani/files/txt/test_text.txt')
# print(file.tell())
# text = file.read()
# print(file.tell())
# file.seek(0)
# print(file.tell())  # possible read again. cursor position = 0
# text_list = []
# for char in text.split('\n'):
#     text_list.append(char.split())
# print(text_list)
# print(sys.getsizeof(file))  # vraci velikost spotrebovane pameti, ne velikost souboru...
# file.close()

# # kontext automaticky zavre soubor
# with open(r'/Users/martindanek/Documents/programovani/files/txt/test_text.txt', 'r+') as file:
#     number_openning = file.readline()
#     number_openning = int(number_openning.strip('\n'))
#     number_openning += 1
#     file.seek(0)
#     file.write(str(number_openning))
#     file.seek(0, 2)
#     file.write(f'\nThis file were opened {number_openning} times')

# filesystem path existence

# # Funkce main
# def main(paths: dict):
#     paths_list = paths.keys()
#     for my_path in paths_list:
#         my_path_list = path_decompose(my_path)
#         filesystem_dict = read_filesystem()
#         paths[my_path] = file_exists(my_path_list, filesystem_dict)
#     from pprint import pprint as pp
#     pp(paths)
#
#
# def read_filesystem():
#     with open('/Users/martindanek/Documents/programovani/files/txt/filesystem.txt') as file:
#         filesystem = file.read()
#     filesystem = filesystem.replace(' ', '')
#     filesystem = filesystem.replace('\n', '')
#     filesystem_dict = eval(filesystem)
#     from pprint import pprint as pp
#     pp(filesystem_dict)
#     return filesystem_dict
#
#
# def path_decompose(my_path):
#     my_path_list = my_path.split('/')
#     if my_path[0] == '/':
#         my_path_list[0] = '/'
#     return my_path_list
#
#
# # Funkce file_exists
# def file_exists(my_path_list, filesystem_dict):
#
#     for count, char in enumerate(my_path_list):
#
#         while count == len(my_path_list) - 1:
#             if my_path_list[-1] in filesystem_dict:
#                 status = True
#                 return status
#             else:
#                 status = False
#                 return status
#
#         if type(filesystem_dict) == dict:
#             for item in filesystem_dict:
#                 if item == char:
#                     filesystem_dict = filesystem_dict.get(char)
#                     break
#                 else:
#                     status = False
#                     return status
#             continue
#
#         if type(filesystem_dict) == list:
#             counter = 0
#             for item in filesystem_dict:
#                 counter += 1
#                 if char == item:
#                     status = True
#                     return status
#                 elif type(item) == dict and char in item:
#                     filesystem_dict = item.get(char)
#                     break
#                 elif counter == len(filesystem_dict):
#                     status = False
#                     return status
#
#
# # {'/'
# paths = {'/bin/mkdir': None,
#          '/lib/init/vars/vars.sh': None,
#          '/lib/init/vars.sh': None,
#          '/home/documents/reports/report1.xls': None,
#          '/home/music/album3/song2.mp3': None,
#          '/home/music/album1/song2.mp3': None,
#          '/lib/systemd/system/sudo.service': None,
#          '/lib/udev/ata_id': None
#          }
# main(paths)


# # LIST of DIVISORS
# def main_divisors(number_from, number_to, divisor_min, divisor_max):
#     sorted_list = sorted([divisor_min, divisor_max])
#     if 0 in sorted_list:
#         print('Division by zero not possible')
#     divisor_min = int(sorted_list[0])
#     divisor_max = int(sorted_list[1])
#
#     divisors_dict = result_create(number_from, number_to, divisor_min, divisor_max)
#     divisors_print(divisors_dict, number_from, number_to, divisor_min, divisor_max)
#
#
# def result_create(number_from, number_to, divisor_min, divisor_max):
#     divisors_dict = {}
#     for divisor in range(divisor_min, divisor_max + 1):
#         div_list = [str(number) for number in range(number_from, number_to + 1) if number % divisor == 0]
#         divisors_dict[divisor] = div_list
#     return divisors_dict
#
#
# def divisors_print(divisors_dict, number_from, number_to, divisor_min, divisor_max):
#     max_l = len(', '.join(divisors_dict[divisor_min]))  # max lenght
#
#     print('''\nSTART point: {2:>4}\nEND point: {3:>6}\ndivisors: {0:>7} till {1}\n{4}
#     '''.format(divisor_min, divisor_max, number_from, number_to, '=' * (17 + max_l))
#           )
#     print('|{0:^12}|{1:^{width}}|'.format('DIVISORS', 'NUMBERS DIVIDED', width=2 + max_l))
#
#     for i in range(divisor_min, divisor_max + 1):
#         print('|{0:^11} | {1:^{width}} |'.format(i, ', '.join(divisors_dict[i]), width=max_l))
#
#
# main_divisors(2, 30, 2, 9)

# Generovani smluv


def contract_change():
    contract_files_name = ['salary_change.txt', 'job_change.txt', 'contract_prolongation.txt']
    print()
    print('{:^60}'.format('CONTRACT CHANGE MODUL'))
    print('=' * 60)
    print('''
    0 - salary change
    1 - position change
    2 - contract prolongation
    ''')

    option = 'employees.txt'
    data_id_dict = eval(read_data(option))
    id_dict_list = list(data_id_dict.keys())

    option = input('Select your option or press Q for quit: ')
    if option not in [str(i) for i in range(3)]:  # due to Three contract templates
        exit()

    contract_template_txt = read_data(contract_files_name[int(option)])

    print()
    print('{:^60}'.format('EMPLOYEE SELECTION'))
    print('=' * 60)
    print('{:^20}{:^20}{:^20}'.format('order', 'NAME', 'BIRTHDATE'))
    print('.' * 60)
    for number, item in enumerate(id_dict_list):
        print('{:^20}{:^20}{:^20}'.format(number, data_id_dict[item]['full_name'], data_id_dict[item]['birthdate']))

    option = input('Select employee: ')
    if option not in [str(i) for i in range(len(id_dict_list))]:
        exit()
    option_id = id_dict_list[int(option)]

    contract_changed_txt = data_change(option_id, data_id_dict, contract_template_txt)
    contract_write(contract_changed_txt)


def read_data(option: str):
    with open(f'/Users/martindanek/Documents/programovani/files/txt/{option}') as file:
        data_id = file.read()
    return data_id


def data_change(option_id, data_id_dict, contract_template_txt):
    # for item in list(data_id_dict[option_id].keys()):
    #     if item in contract_template_txt:
    #         contract_template_txt = contract_template_txt.replace('{' + item + '}', str(data_id_dict[option_id][item]))
    # return contract_template_txt
    return contract_template_txt.format(**data_id_dict[option_id])


def contract_write(contract_changed_txt):
    with open('/Users/martindanek/Documents/programovani/files/txt/contract_changed.txt', mode='w') as file:
        file.write(contract_changed_txt)
    return print('\n\nCHECK YOUR FILE contract_changed.txt')


contract_change()
