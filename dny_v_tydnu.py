# Vytvor list 'tyden' a uloz dny v tydnu v podobe stringu
tyden = ('pondeli', 'utery', 'streda', 'ctvrtek', 'patek', 'sobota', 'nedele')

# Ziskej vyber dne od uzivatele
cislo_dne = int(input('Vyber den v tydnu (1 - pondeli) atd.: '))

# Ziskej den z listu na zaklade hodnoty ziskane od uzivatele
prvni_pismeno_dne = tyden[cislo_dne-1][0]

# Ziskej tip na prvni pismeno dne od uzivatele
tip_prvniho_pismena = input('Zadej prvni pismeno tveho vybraneho dne: ')

# Zjistit vysledek
if prvni_pismeno_dne == tip_prvniho_pismena:
    print("OK")
else:
    print('spatne :-(')

# Vytiskni vysledek