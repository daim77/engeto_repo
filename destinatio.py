# Pozdrav klienta
print('=' * 40)
print('WELCOME to Destinatio')
print('=' * 40)
# Nabídni mu destinace
print('We can offer you the flw DEST')
print('.' * 40)
print('''
1 - Prague   | 1000
2 - Wien.    | 1100
3 - Brno     | 2000
4 - Svitavy  | 1500
5 - Zlin     | 2300
6 - Ostrava  | 3400
''')
print('.' * 40)

# Získej vstup uživatele o destinaci
dest_choice = int(input('Insert DEST No: '))

# Zkontroluj, zde byl vložen vhodný vstup
if dest_choice < 1 or dest_choice > 6:
    print('Wrong destination')
    exit()

# Přiřaď proměnným příslušná data
city_tuple = ('Prague', 'Wien', 'Brno', 'Svitavy', 'Zlin', 'Ostrava')
price_tuple = (1000, 1100, 2000, 1500, 2300, 3400)
discount = ('Svitavy', 'Ostrava')
# Získej data z proměnných podle vstupu uživatele
city_index = city_tuple[dest_choice - 1]
price_index = float(price_tuple[dest_choice - 1])

# Začni registraci
print('In order to complete your reservations, please share few details about yourself with us.')
print('.' * 40)

# Získej vstup uživatele o jeho osobních datech
name = input('NAME: ')
print('=' * 40)
surname = input('SURNAME: ')
print('=' * 40)
birth = int(input('Year of Birth: '))
print('=' * 40)
email = input('EMAIL: ')
print('=' * 40)
password = input('PASSWORD: ')
print('=' * 40)

# cond discount
# if city_index == 'Svitavy' or city_index == 'Ostrava':
#    price_index = price_index * 0.75
if city_index in discount:
    price_index = price_index * 0.75

# cond age
if 2020 - birth < 15:
    print('You are too young, ask your parents for a ticket :-)')
    exit()

# cond @
# elif ('@' in email) == bool():
#     print('Invalid format email')
#     exit()
elif not ('@' in email) and not ('.' in email):
    print('invalid email!')
    exit()

# cond length 8 char
elif len(password) < 8:
    print('Your password must contain at least 8 characters')
    exit()

# cond no numbers at beginning or end
elif password[0].isnumeric():
    print('Your password must not begin with any numbers')
    exit()
elif password[len(password) - 1].isnumeric():
    print('Your password must not end with any numbers')
    exit()

# cond at least one letter and one number
elif (password.isnumeric() or password.isalpha()):
    print('Password must contain at least one letter and one number')
    exit()

else:
    print('THX', name + '!')
    print('We have processed your reservation to', city_index, ".")
    print('Total price is', price_index)
