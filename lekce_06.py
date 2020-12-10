# opakovani while
# nakuni kosik chci naplnit potravinami

# kosik = {}
# oddelovac = '=' * 40
# potraviny = {
#     'mleko': 30,
#     'maso': 100,
# }
# print(oddelovac)
# for i in range(3):
#     vyber = input('vyber potravinu: ')
#     while vyber not in potraviny:
#         cena = int(input('zadej cenu: '))
#         potraviny.setdefault(vyber)
#         potraviny[vyber] = cena
#     kosik[vyber] = potraviny[vyber]
#
# print(kosik)


#zjisti pocet jednotlivych barev
final = dict()
colors = ['green', 'blue', 'black', 'red', 'red', 'yellow', 'blue', 'grey', 'black' , 'red', 'green']
color_item = colors.pop()
for i in range(len(set(colors))):
    color_item = colors.pop()
    if color_item not in final:
        final.setdefault(color_item, 0)
    final[color_item] += 1

print(final)
