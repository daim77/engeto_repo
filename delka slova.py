# Zadani slova
slovo = input('Zadej jakekoliv slovo: ')

# Zjisteni delky
delka_slova = len(slovo)

# Podminka a tisk delky slova
if delka_slova > 5:
    print(slovo, 'obsahuje', delka_slova, 'znaku.')
elif delka_slova > 1:
    print(slovo, 'obsahuje', delka_slova, 'znaky.')
elif delka_slova == 1:
    print(slovo, 'obsahuje', delka_slova, 'znak.')
else:
    print('Nebylo zadano zadne slovo!')