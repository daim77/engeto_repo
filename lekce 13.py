# import delete
#
# if __name__ == '__main__':
#     print(delete.day_today())
#     print(delete.__name__)

# import os
# from pprint import pprint as pp
#
#
# pp(os.listdir())
# print(os.getcwd())
# pp(os.listdir('/'.join(os.getcwd().split('/')[:3])))
# print('/'.join(os.getcwd().split('/')[:4]))

# import os
#
#
# try:
#     os.mkdir('test')
# except FileExistsError:
#     pass
# try:
#     os.mkdir('test/TestDir1')
# except FileExistsError:
#     pass
# try:
#     os.mkdir('test/TestDir2')
# except FileExistsError:
#     pass
# try:
#     os.mkdir('test/TestDir3')
# except FileExistsError:
#     pass
# finally:
#     new_file = open('test/test_file.txt', 'w')
#     new_file.close()
#     new_file = open('test/TestDir1/config.txt', 'w')
#     new_file.close()
#     new_file = open('test/TestDir1/tasks.txt', 'w')
#     new_file.close()
#     new_file = open('test/TestDir1/test.txt', 'w')
#     new_file.close()
#
# print(os.listdir('test/TestDir1'))
#
# os.rename('test/TestDir1/tasks.txt', 'test/TestDir1/tasks.txt')
#
# print(os.listdir('test/TestDir1'))

# import os
#
#
# def delete_folder(path: str):
#     files_folder = os.listdir(path)
#     for item in files_folder:
#         os.remove(path + '/' + item)
#     os.rmdir(path)
#
#
# if __name__ == '__main__':
#
#     # os.mkdir('test')
#     file_list = ['tasks', 'config', 'test']
#
#     try:
#         for i in range(1, 4):
#             os.mkdir('test/TestDir' + str(i))
#     except FileExistsError:
#         pass
#
#     for file_name in file_list:
#         file = open('test/TestDir1/' + file_name + '.txt', 'w')
#         file.close()
#
#     print(os.sep)
#     print(os.name)
#     print(os.getcwd())
#     print(os.getcwdb())
#
#     my_path = '/Users/martindanek/Documents/programovani/engeto_repo/engeto_repo/test/TestDir1/config.txt'
#     only_path = '/Users/martindanek/Documents/programovani/engeto_repo/engeto_repo/test/TestDir1'
#     print(os.path.basename(my_path))
#     print(os.path.dirname(my_path))
#     print(os.path.split(my_path))  # tuple
#     print(os.path.splitext(my_path))
#
#     print(os.path.exists(my_path))
#     print(os.path.isfile(only_path))
#     print(os.path.isdir(only_path))
#
#     print(os.path.getsize(my_path))
#     print(os.path.getsize(only_path))
#
#
#     # delete_folder('test/TestDir1')

# import sys
# import os
#
#
# def last_line_file():
#     name_list = sys.argv[1:]
#     for name in name_list:
#         if os.path.isfile(os.getcwd() + '/' + name):
#             with open(os.getcwd() + '/' + name, 'a+') as file:
#                 file.write('=' * 40)
#
#
# if __name__ == '__main__':
#     last_line_file()
#
#
# import os
#
#
# def dir_or_file(arg: str):
#     if os.path.isdir(arg):
#         return 'dir'
#     elif os.path.isfile(arg):
#         return 'file'
#     else:
#         return 'PathNotFound'
#
#
# def file_creator(names: list):
#     result = []
#     for name in names:
#         if type(name) != str:
#             result.append(False)
#             continue
#         file = open(name + '.txt', 'w')
#         file.close()
#         result.append(True)
#     return result
#
#
# if __name__ == "__main__":
#     dir_or_file('/Users/martindanek/Desktop')
#     print(file_creator(['a', 'aa', 'aaa', 1]))
#
#
# import sys
# import os
# from pprint import pprint as pp
#
#
# print(sys.getdefaultencoding())
# print(sys.getrecursionlimit())
# print(sys.maxsize)
# print(2**63)
# pp(sys.modules)
# print(sys.platform)
#
# print(os.getcwd())
# os.chdir('/Users/martindanek/Documents/programovani')
# pp(os.listdir())
# pp(os.times())

# # ========= UKOL Vyhledavac souboru =========
# import os
# from datetime import datetime
#
#
# def search_file(file_name: str, path: str):
#     start = datetime.now()
#     for subdir, dirs, files in os.walk(path):
#         if file_name in files:
#             print(datetime.now() - start)
#             return subdir + os.sep + file_name
#     return False
#
#
# if __name__ == '__main__':
#     print(search_file('text1.txt', '/Users/martindanek/Documents'))

# # nebo engeto upravene reseni
#
import os
from time import time


def search(start_dir: str, searched_name: str):
    start_time = time()
    paths = []
    dirs_to_search = [start_dir]

    while dirs_to_search:
        current_dir = dirs_to_search.pop()

        for item in os.listdir(current_dir):
            item_path = os.path.join(current_dir, item)
            if os.path.isdir(item_path):
                dirs_to_search.append(item_path)
            elif item == searched_name:
                paths.append(item_path)
    end = time()
    print(end - start_time)
    return paths


if __name__ == '__main__':
    print(search('/Users/martindanek/Documents', 'text1.txt'))
