import sys
import os


def last_line_file():
    name_list = sys.argv[1:]
    for name in name_list:
        if os.path.isfile(os.getcwd() + '/' + name):
            with open(os.getcwd() + '/' + name, 'a+') as file:
                file.write('=' * 40)


if __name__ == '__main__':
    last_line_file()
