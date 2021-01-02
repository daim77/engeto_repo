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
    status = False
    my_path_list = path_decompose(my_path)
    filesystem_dict = read_filesystem()
    status = file_exists(my_path_list, filesystem_dict, status)
    print('status main(): ', status)


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


def file_exists(my_path_list, filesystem_dict, status):
    print(filesystem_dict['/'][1]['lib'][2]['systemd'][0]['system'][0])
    print('my_path_list: ', my_path_list)
    count = 0
    for char in my_path_list[::2]:
        count += 1
        print(filesystem_dict)
        print(count)
        print(char)
        # keys = filesystem_dict.keys()
        # if char in list(keys):
        filesystem_dict = filesystem_dict.get(char, -1)
        if filesystem_dict == -1:
            status = False
            return status
        for index in range(len(filesystem_dict) - 1):
            print(filesystem_dict[index])
            print(my_path_list[count])
            if my_path_list[count] in list(filesystem_dict[index].keys()):
                filesystem_dict = filesystem_dict[index].get(my_path_list[count])
                break
        if type(filesystem_dict) == list:
            filesystem_dict = next(k for k, v in filesystem_dict if k == my_path_list[count])
        status = True
    return status


# {'/'
main('/lib/systemd/system/sudo.service')
