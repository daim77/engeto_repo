# Tvým úkolem bude napsat skript, který příjme od uživatele string s čísly, která jsou oddělena čárkou a
# vygeneruje list celých čísel ze zadaného stringu (datový typ integer). Program by měl následně list vypsat.
# Také budeš muset ošetřit kód tak, aby si uměl poradit se situací, kdy by součástí stringu byly mezery
# Hello, please write your numbers and press enter to confirm: '23, 54,  645, 76'
# List: [23, 54, 645, 76]

result = list()  # vlož čísla do listu bez mezer
# vstup
inpt = input('Insert numeric strings seperated by comma to be converted: ')

# vlož čísla do listu s mezerama
nums = inpt.split(',')
for number in nums:
    result.append(int(number.strip()))
print('nums', nums)
print(result)
