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

# jeden radek
# colors = ['green', 'blue', 'black', 'red', 'red', 'yellow', 'blue', 'grey', 'black', 'red', 'green']
# print({color: colors.count(color) for color in colors})

# veta = 'Toto ?je velmi, velmi kratká věta.!'
# cisty_list = []
# for slovo in veta.split():
#     ciste_slovo = slovo.strip(',.?!')
#     cisty_list.append(ciste_slovo)
# print(cisty_list)
#
# # list comprehension
# print([slovo.strip(",.?!") for slovo in veta.split()])  # na jeden radek

# oddelovac = '=' * 20
# for number in range(0, 5):
#     print(oddelovac)
#     print(f'radek cislo: {number}')
#     print(oddelovac)
#     for cislo_bunky in range(1, 5):
#         print(f'bunka cislo {cislo_bunky}')
#
# slovnik = {}
# veta = 'Toto ?je velmi, velmi kratká věta.!'
# for slovo in veta.split()
#     slovnik[slovo] = {}
#     print(slovo)
#     for char in slovo:
#         print(char)
#         slovnik[slovo][char] = char


# # enumerate()
# JMENA = ["Helmut", "Helga", "Harold", "Hammet", "Hetfield"]
# ocislovane = enumerate(JMENA, 1)  # bude pocitat od jedna
# print(list(ocislovane))
#
# for cislo, jmeno in enumerate(JMENA, 1):  # default je nula
#     print(f'{cislo}.: {jmeno}')

# analyza textu
TEXT = """
Affronting imprudence do he he everything. Sex lasted dinner wanted indeed
wished out law. Far advanced settling say finished raillery. Offered
chiefly farther of my no colonel shyness. Such on help ye some door if in.
Laughter proposal laughing any son law consider. Needed except up piqued
an. Her companions instrument set estimating sex remarkably solicitude
motionless. Property men the why smallest graceful day insisted required.
Inquiry justice country old placing sitting any ten age. Looking venture
justice in evident in totally he do ability. Be is lose girl long of up give.
Trifling wondered unpacked ye at he. In household certainty an on tolerably
smallness difficult. Many no each like up be is next neat. Put not enjoyment
behaviour her supposing. At he pulled object others. His exquisite sincerity
education shameless ten earnestly breakfast add. So we me unknown as improve
hastily sitting forming. Especially favourable compliment but thoroughly
unreserved saw she themselves. Sufficient impossible him may ten insensible
put continuing. Oppose exeter income simple few joy cousin but twenty. Scale
began quiet up short wrong in in. Sportsmen shy forfeited engrossed may can.
Remain valley who mrs uneasy remove wooded him you. Her questions favourite
him concealed. We to wife face took he. The taste begin early old why since
dried can first. Prepared as or humoured formerly. Evil mrs true get post.
Express village evening prudent my as ye hundred forming. Thoughts she why not
directly reserved packages you. Winter an silent favour of am tended mutual. 
"""

# rozdeli, ocistit, vytvorit slovnik, sorted() a vypsat 5 nejcastejsich slov, ta pak ze seznamu vymazat
rozdeleny_TEXT = TEXT.split()
cisty_TEXT = rozdeleny_TEXT.strip('.,!?')
vyskyt_slov = {}
# for char in set(cisty_TEXT):
#    vyskyt_slov[char] = cisty_TEXT.count[char]
# nejcastejsi = sorted(vyskyt_slov, key = vyskyt_slov.get, reverse = true)[:5]
print(cisty_TEXT)
