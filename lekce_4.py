# muj_string = 'a,u,t,o'
# rozdelen_do_listu = muj_string.split(',')
# print('muj string: ', muj_string)
# print(rozdelen_do_listu)
# muj_string = muj_string.strip('a,') # v promenne odstrani z leva do prvniho znaku, ktery neni argumentem. U stringu odstrani vse
# print(muj_string)

# # Zadany string
# muj_string = "Kdyby si Bruno nevšiml značky 'POZOR!', narazil by do zdi"
# print(muj_string)
# # Rozdel string do sekvence
# muj_list = muj_string.split()
# print(muj_list)
# # Ziskej paty prvek
# paty_prvek = muj_list[5]
# print('paty prvek:', paty_prvek)
# # Ocisti paty prvek
# cisty_paty_prvek = paty_prvek.strip("',!")
# print(cisty_paty_prvek)
#
# # Over kapitalky promenne 'cisty_paty_prvek' - napis podminku za if a ukonci radek dvojteckou
# if cisty_paty_prvek.isupper():
#     print('jsou vsechna VELKA pismena')
# else:
#     print('alespon jedno je male pismena')

# List zeleniny
zelenina = ['brokolice', 'petrzel', 'celer', 'redkev', 'rajce', 'petrzel',
                'okurka', 'salat', 'cervena_repa', 'paprika', 'petrzel']

# # Zjisti pocet pro 'petrzel'
# pocet_Petr = zelenina.count('petrzel')
# print('Amount of parsley:', pocet_Petr)
# # Zjisti index pro 'rajce'
# rajce_Index = zelenina.index('rajce')
# print('Rajce je na pozici: ', rajce_Index)
#
# # 'zelenina' bez 'okurka'
# zelenina.remove('okurka')
# print("zelenina bez okurky", zelenina)
#
# # ZDE NIC NEPIS. Jde o kontrolu tveho zapisu :)
# if pocet_Petr == 3 and rajce_Index == 4 and 'okurka' not in zelenina:
# 	print('Skvělá práce, v metodách listů jsi přeborník!')
# else:
# 	print('Ještě si to jednou projdi, někde se vloudila chybka :(\nPokud si nejsi jistý, mrkni ještě jednou na tabulku s metodami')

# # #smycka WHILE
# muj_string = 'while smyčky můžou býT neKonečné'
# while muj_string:
#     if muj_string[0].isupper():
#         print('Našel jsem velké písmeno:',muj_string[0])
# #        break
#     muj_string = muj_string[1:]
# print('muj_string po while:_' + muj_string + '_')

# barvy = ['zelena', 'modra', 'cerna', 'cervena', 'cervena', 'zluta', 'modra', 'seda', 'cerna' , 'cervena', 'zelena']
# pocet_barev = {}
# while barvy:
#     barva = barvy.pop()
#     pocet_barev[barva] = pocet_barev.get(barva,0) + 1 # NULA je defaultni hodnota if key is missing
# print(pocet_barev)

# # my example with .get, while nad counting the characters in one full sentence
# sentence = input('Zedej vetu nebo slovo. Spocitam vyskyt znaku!: ')
# characters = {}
# # convert string to list
# sentence = list(sentence)
#
# while sentence:
#     character = sentence.pop()
#     characters[character] = characters.get(character,0) + 1
# print(characters)

# odpocet po jedne sekunde
from time import sleep
my_sec = int(input('Zadej pocet sekund: '))
while my_sec:
    sleep(1)
    print('Pocet sekund:', my_sec)
    my_sec = my_sec - 1

