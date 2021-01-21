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

import os


try:
    os.mkdir('test')
except FileExistsError:
    print()
finally:
    new_file = open('test/test_file.txt', 'w')
    new_file.close()

print(os.listdir('test'))
