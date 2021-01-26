# CSV a JSON

# import csv
# from pprint import pprint as pp
#
#
# prvni = ['Surname', 'Name', 'Full Name', 'Age', 'City', 'Job', 'Gender']
#
# obsah = [
#     ['Smith', 'John', 'Smith, John', '32', 'London', 'Programmer', ''],
#     ['Doe', 'Joe', 'Doe, Joe', '34', 'Liverpool', '', 'Male'],
#     ['Murphy', 'Ann', 'Murphy, Ann', '29', 'London', 'Admin', 'Female'],
#     ['Cook', 'Floyd', 'Cook, Floyd', '28', '', 'Tester', 'Male'],
#     ['Glenn', 'Taylor', 'Glenn, Taylor', '35', 'Birmingham', 'Manager', 'Female'],
#     ['Mills', 'Amanda', 'Mills, Amanda', '41', 'Leicester', 'Quality Assurance', 'Female']
#          ]
#
# f = open('/Users/martindanek/Documents/programovani/files/csv/names.csv', 'w')
# # f_writer = csv.writer(f) # objekt pro zapis csv dat
# csv.writer(f).writerow(prvni)
# csv.writer(f).writerows(obsah)
# f.close()
#
# file = open('/Users/martindanek/Documents/programovani/files/csv/names.csv', 'r')
# for item in csv.DictReader(file):
#     pp(item)
# file.close()
#
#
# import json
# from pprint import pprint as pp
#
#
# employee = {
#     'Job': 'Programmer',
#     'Age': 38,
#     'Full Name': 'Galagher, Fred',
#     'City': 'London',
#     'Surname': 'Galagher',
#     'Gender': 'Male',
#     'Name': 'Fred'
# }
#
# with open('/Users/martindanek/Documents/programovani/files/json/example1.json', 'w+') as file:
#     to_json = json.dumps(employee, indent=2, sort_keys=False)
#     # file.write(to_json)
#     json.dump(employee, file, indent=4, sort_keys=True)
#     print(to_json)
#
# # file = open('/Users/martindanek/Documents/programovani/files/json/example1.json')
# # file_csv = file.read()
# # from_json = json.loads(file_csv)
#
#     file.seek(0)
#     # file_json = file.read()
#     # from_json = json.loads(file_json)
#     from_json = json.load(file)
#     pp(from_json)
# # file.close()

# ===== Precteni prvnich sloupcu a tisk listu =====

import csv


def read_json_column(path: str, column=0):
    try:
        with open(path) as file:
            read_json = csv.reader(file)

            for row in read_json:
                if column == 0:
                    print(' '.join(row))
                else:
                    print(row[column - 1])

    except FileNotFoundError:
        print('File not found')
    except IndexError:
        print('Wrong column')


if __name__ == '__main__':
    read_json_column('/Users/martindanek/Documents/programovani/files/csv/pokus.csv', 0)
