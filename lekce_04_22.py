# Napiš program, který z listu slova vybere nejdelší slovo.
# vytiskne do terminálu tuple s tímto nejdelším slovem a jeho délkou.
slova = [
    'Python', 'is', 'a', 'widely', 'used',
    'high-level', 'programming', 'language',
    'for', 'general-purpose', 'programming,',
    'created', 'by', 'Guido', 'van', 'Rossum',
    'and', 'first', 'released', 'in', '1991.'
]
pocet_slov = (len(slova))
my_char = None  # zkusit none
nejdelsi_slovo = ''  # musi mit '' protoze none nema delku!
final_tuple = None
while pocet_slov > 0:
    my_char = slova.pop()
    if len(my_char) > len(nejdelsi_slovo):
        nejdelsi_slovo = my_char
    pocet_slov -= 1
final_tuple = (nejdelsi_slovo, len(nejdelsi_slovo))
print(final_tuple)


# vzorove reseni
# nejdelsi_slovo = ('', 0)
# while slova:
#     slovo = slova.pop(0)
#     if len(slovo) > nejdelsi_slovo[1]:
#         nejdelsi_slovo = slovo, len(slovo)
# print(nejdelsi_slovo)