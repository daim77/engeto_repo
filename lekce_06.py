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

# analyza textu pro zahradniky
TEXT = """
Jedná se o ošetření stávajících vybraných stromů na vybraných lokalitách v obci Tuchoměřice (k.ú. Tuchoměřice a 
Kněžívka) a výsadba nových stromů na polní cestě od zemního vodojemu k ulici Ke Kovárně. V přiloženém dokumentu 
jsou mapy, ve kterých je území zakresleno Předmětem této zakázky je odborný řez stromů, včetně likvidace dřevního 
odpadu. Alej u tzv. Černé pěšiny - celkem 13 stromů (Populus nigra ´Italica´)
Řečanská alej - celkem 73 stromů (Tilia cordata, T. platyphylla) - provedení výsadby stromů v parcích dle specifikace
- výsadba 46 ks dřevin v parcích
- stromy budou normové školkařské výpěstky se zapěstovanou korunou s průběžným terminálem
- sázecí jáma bude mít objem minimálně 1 m3 a dno jámy vysypáno drenážní vrstvou
- na výsadbu dřevin bude použit certifikovaný kvalitní substrát tj. u listnatých dřevin zahradní substrát s kompostem 
u jehličnatých dřevin zahradní substrát s rašelinou
- listnaté dřeviny budou ukotveny 3 ks kůly včetně úvazků, 12 ks příček
- atd. Stručný popis předmětu:
Předmětem plnění veřejné zakázky v rámci tohoto výběrového řízení je provedení a obstarání veškerých prací a 
zhotovení děl nutných k úplnému dokončení a zprovoznění projektu revitalizace hřbitova a parku v Hranicích u Aše.
Revitalizace parku zahrnuje vegetační úpravy stávající zeleně, částečné odstranění současných povrchů a nahrazení 
navrženými vegetačními prvky – výsadba keřů, stromů a trvalek dle architektonického návrhu Ing. Lenky Červinkové.
Revitalizace hřbitova zahrnuje vegetační úpravy – odstranění a úpravy současné zeleně, novou výsadbu keřů, strom a 
trvalek, revitalizaci trvalého travního porostu dle architektonického návrhu Ing. Lenky Červinkové. V rámci 
revitalizace hřbitova dojde k částečným stavebním úpravám stávajících cest, doplnění mobiliáře a veřejného osvětlení.
Údržba travnatých ploch Jedná se o pravidelné provádění údržby travnatých ploch a ošetřování záhonů růží a trvalek. 
Zejména se jedná o jarní a podzimní vyhrabávání listí, běžné a občasné kosení, údržba záhonů růží a trvalek a výsadbové 
práce trvalek, cibulovin, letniček, růží a okrasných trav. Součástí zakázky je také vyčištění zelených ploch od všech 
nečistot rostlinného charakteru a rovněž od odpadků – papírů, plastových láhví apod. Část 2: Údržba dřevin Jedná se o 
pravidelné provádění odborné údržby dřevin a keřů. Zejména se jedná o ořezy stromů, odstranění pařezů, kácení stromů, 
instalaci bezpečnostních vazeb a jejich kontroly a výsadby stromů. Dále se jedná o pravidelnou údržbu keřů a keřových 
skupiny a výsadby keřů. Předmětem zakázky je také zajištění odvozu a odborné likvidace odpadů (např. uložení na 
skládku, odevzdání specializované firmě apod.) vč. úhrady poplatku za jeho uložení.
"""

# rozdeli, ocistit, vytvorit slovnik, sorted() a vypsat 5 nejcastejsich slov, ta pak ze seznamu vymazat cislovky a
# kratka slova, znova slovnik a vytisknout 20 NEJ
cisty_text = []
for char in TEXT.split():
    cisty_text.append(char.strip('.,!?()-_""/!=:'))
vyskyt_slov = {}
for char in set(cisty_text):
    vyskyt_slov[char] = cisty_text.count(char)
most_frequent = set(sorted(vyskyt_slov, key=vyskyt_slov.get, reverse=True)[:10])
words = list(set(vyskyt_slov.keys()) - most_frequent)
for x in words:
    if x.isdigit() or len(x) < 4:
        words.remove(x)
vyskyt_slov = {}
for char in set(words):
    vyskyt_slov[char] = words.count(char)
print(sorted(vyskyt_slov, key=vyskyt_slov.get, reverse=True)[:20])
