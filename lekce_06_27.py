# CHESS
# Napiš program, který vytiskne šachovnici daných rozměrů.
# Program musí používat proměnné:
# size - délka hrany šachovnice
# symbols - znaky potřebné pro černá a bílá pole
# desk - reprezentace šachovnice, tuple, list, dict

desk = list()
# Zadej rozměry šachovnice
size = int(input('Zadej rozmer sachovnice: '))

# Zadej symboly
symbols = input('Zadej dva symboly sachovnice repre B&W: ')

# Vytvoř šachovnici

# Doplň smyčky for, které by měly postupně nahrát celou
# šachovnici do proměnné 'desk'
for a in range(size): # enumerate
    for b in range(size):
        desk_row[b] = symbols
    desk[a].append(desk_row)
# Vytiskni šachovnici.
print(symbols)
