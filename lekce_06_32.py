# Napiš program, který bude mít 3 vstupy a všechny budou celá čísla:
#
# start
# stop
# divisor (dělitel)
# Všechny by měly být poskytnuty uživatelem.
#
# Program by měl:
#
# vygenerovat sbírku celých čísel v rozmezí mezi start (včetně) a stop (včetně)
# vytisknout list v rozmezí čísel start - stop, která jsou dělitelná vstupem divisor
# Pokud je dělitel 0, program by měl vytisknout string Cannot divide by zero.

list_of_quotients = list()
start = int(input('Insert beginning of interval: '))
end = int(input('Insert beginning of interval: '))

if end < start:
    print('Wrong interval!')
    exit()

divisor = int(input('Insert divisor: '))

while divisor == 0:
    print('Cannot divide by zero. Insert divisor once again!')
    divisor = int(input('Insert divisor: '))

for i in range(start, end + 1):
    if i % divisor == 0:
        list_of_quotients.append(i)
print('Numbers in', range(start, end), 'divisible by', divisor, ':\n', list_of_quotients)

# reseni by ENGETO

# start = int(input('START: '))
# stop = int(input('STOP: '))
# divisor = int(input('DIVISOR: '))
# result = []
# if divisor:
#     for num in range(start, stop+1):
#         if num % divisor == 0:
#             result.append(num)
#     print('Numbers in range(' + str(start) +', ' + str(stop) + ') divisible by ' + str(divisor) + ':')
#     print(result)
# else:
#     print('Cannot divide by zero')
