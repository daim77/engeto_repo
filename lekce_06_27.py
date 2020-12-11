# # CHESS
# # Napiš program, který vytiskne šachovnici daných rozměrů.
# # Program musí používat proměnné:
# # size - délka hrany šachovnice
# # symbols - znaky potřebné pro černá a bílá pole
# # desk - reprezentace šachovnice, tuple, list, dict
#
# desk = list()
# desk_row = []
# # Zadej rozměry šachovnice
# size = int(input('Zadej rozmer sachovnice: '))
#
# # Zadej dva symboly
# symbols = [' ', ' ', ' ']
# while len(symbols) != 2:
#     symbols = list(input('Zadej dva symboly sachovnice repre B&W: '))
#
# # Vytvoř šachovnici
#
# # Doplň smyčky for, které by měly postupně nahrát celou
# # šachovnici do proměnné 'desk'
# for row in range(1, size + 1):
#     for item in range(1, size + 1):
#         if row % 2 != 0 and item % 2 != 0:
#             desk_row.append(symbols[0])
#         elif row % 2 != 0 and item % 2 == 0:
#             desk_row.append(symbols[1])
#         elif row % 2 == 0 and item % 2 != 0:
#             desk_row.append(symbols[1])
#         else:
#             desk_row.append(symbols[0])
#     desk.append(desk_row)
#     desk_row = []
# # Vytiskni šachovnici.
# for row in range(size):
#     for item in range(size):
#         print(desk[row][item], end='')
#     print('')

# kratsi verze
# Zadej rozměry šachovnice
size = 10

# Zadej symboly
symbols = ['#', ' ']

# Vytvoř šachovnici
desk = []

# Doplň smyčky for, které by měly postupně nahrát celou šachovnice do proměnné 'desk'
for row in range(size):
    line = []

    for cell in range(size):
        i = (row+cell) % len(symbols)
        line.append(symbols[i])

    desk.append(''.join(line))

# Vytiskni šachovnici
print('\n'.join(desk))
