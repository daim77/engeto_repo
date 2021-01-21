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

# funkce na vypis slozky
import os


def list_folder(path: str):
    if os.path.isdir(path):
        