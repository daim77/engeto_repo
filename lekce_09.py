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

# Funkce main
def main(my_path: str):
    my_path_list = path_decompose(my_path)
    filesystem_dict = read_filesystem()
    status = file_exists(my_path_list, filesystem_dict)
    print(f'{my_path}: ', status)


def read_filesystem():
    with open('/Users/martindanek/Documents/programovani/files/txt/filesystem.txt') as file:
        filesystem = file.read()
    filesystem = filesystem.replace(' ', '')
    filesystem = filesystem.replace('\n', '')
    filesystem_dict = eval(filesystem)
    return filesystem_dict


def path_decompose(my_path):
    my_path_list = my_path.split('/')
    if my_path[0] == '/':
        my_path_list[0] = '/'
    return my_path_list
# Funkce file_exists


def file_exists(my_path_list, filesystem_dict):

    for count, char in enumerate(my_path_list):

        while count == len(my_path_list) - 1:
            if my_path_list[-1] in filesystem_dict:
                status = True
                return status
            else:
                status = False
                return status

        if type(filesystem_dict) == dict:
            for item in filesystem_dict:
                if item == char:
                    filesystem_dict = filesystem_dict.get(char)
                    break
                else:
                    status = False
                    return status
            continue

        if type(filesystem_dict) == list:
            counter = 0
            for item in filesystem_dict:
                counter += 1
                if char == item:
                    status = True
                    return status
                elif type(item) == dict and char in item:
                    filesystem_dict = item.get(char)
                    break
                elif counter == len(filesystem_dict):
                    status = False
                    return status


# {'/'
main('/lib/systemd/system/sudo.service')
main('/bin/mkdir')
main('/lib/init/vars/vars.sh')
main('/lib/systemd/system/sudo.service')
main('/home/documents/reports/report1.xls')
