# tento program pozna zda uzivatel zadal palyndrom
# header
# print('=' * 40)
# print('Tento program testuje zda zadany vyraz je PALYNDROM ci nikoliv')
# print('=' * 40)
# # zadani promene
# slovo = input('Zadej slovo: ')
# my_word_reverse = list(slovo)
# my_word_reverse.reverse()
# print('Slovo', slovo, ':')
# if my_word_reverse == list(slovo):
#     print("JE Palyndrom!")
# else:
#     print("NENI palyndrom!")

# a nebo jednoduseji
slovo = input('Zadej slovo: ')
if slovo == slovo[::-1]:
    print('je palyndrom')
else:
    print('neni palyndrom')
