# muj_string = 'a,u,t,o'
# rozdelen_do_listu = muj_string.split(',')
# print('muj string: ', muj_string)
# print(rozdelen_do_listu)
# muj_string = muj_string.strip('a,') # v promenne odstrani z leva do prvniho znaku, ktery neni argumentem. U stringu odstrani vse
# print(muj_string)

# Zadany string
muj_string = "Kdyby si Bruno nevšiml značky 'POZOR!', narazil by do zdi"
print(muj_string)
# Rozdel string do sekvence
muj_list = muj_string.split()
print(muj_list)
# Ziskej paty prvek
paty_prvek = muj_list[5]
print('paty prvek:', paty_prvek)
# Ocisti paty prvek
cisty_paty_prvek = paty_prvek.strip("',!")
print(cisty_paty_prvek)

# Over kapitalky promenne 'cisty_paty_prvek' - napis podminku za if a ukonci radek dvojteckou
if cisty_paty_prvek.isupper():
    print('jsou vsechna VELKA pismena')
else:
    print('alespon jedno je male pismena')
