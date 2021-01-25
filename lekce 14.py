# CSV a JSON

import csv

prvni = ['Surname', 'Name', 'Full Name', 'Age', 'City', 'Job', 'Gender']

obsah = [
    ['Smith', 'John', 'Smith, John', '32', 'London', 'Programmer', ''],
    ['Doe', 'Joe', 'Doe, Joe', '34', 'Liverpool', '', 'Male'],
    ['Murphy', 'Ann', 'Murphy, Ann', '29', 'London', 'Admin', 'Female'],
    ['Cook', 'Floyd', 'Cook, Floyd', '28', '', 'Tester', 'Male'],
    ['Glenn', 'Taylor', 'Glenn, Taylor', '35', 'Birmingham', 'Manager', 'Female'],
    ['Mills', 'Amanda', 'Mills, Amanda', '41', 'Leicester', 'Quality Assurance', 'Female']
         ]

f = open('/Users/martindanek/Documents/programovani/files/csv/names.csv', 'w')
# f_writer = csv.writer(f) # objekt pro zapis csv dat

csv.writer(f).writerow(prvni)
csv.writer(f).writerows(obsah)

f.close()
