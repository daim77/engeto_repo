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


# zjisti pocet jednotlivych barev
# final = dict()
# colors = ['green', 'blue', 'black', 'red', 'red', 'yellow', 'blue', 'grey', 'black', 'red', 'green']
# while colors:
#     color_item = colors.pop()
#     # if color_item not in final:
#     #     final.setdefault(color_item, 0)
#     # final[color_item] += 1
#     final[color_item] = final.get(color_item, 0) + 1  # takto to je kratsi
#
# print(final)

# final = dict()
# colors = ['green', 'blue', 'black', 'red', 'red', 'yellow', 'blue', 'grey', 'black', 'red', 'green']
# for color_item in colors:  # nerozebere list a jede od predu
#     final[color_item] = final.get(color_item, 0) + 1
# print(final)

# colors = ['green', 'blue', 'black', 'red', 'red', 'yellow', 'blue', 'grey', 'black', 'red', 'green']
# for color in set(colors):
#     print(color, colors.count(color))

# colors = ['green', 'blue', 'black', 'red', 'red', 'yellow', 'blue', 'grey', 'black', 'red', 'green']
# print([(color, colors.count(color)) for color in set(colors)])

# colors = ['green', 'blue', 'black', 'red', 'red', 'yellow', 'blue', 'grey', 'black', 'red', 'green']
# # {color: colors.count(color) for color in colors}:

# veta = 'Toto ?je velmi, velmi kratká věta.!'
# cisty_list = []
# for slovo in veta.split():
#     ciste_slovo = slovo.strip(',.?!')
#     cisty_list.append(ciste_slovo)
# print(cisty_list)
#
# # list comprehension
# print([slovo.strip(",.?!") for slovo in veta.split()])  # na jeden radek

