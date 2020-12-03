# Ziskani nahodneho slova z listu 'ovoce'
import random

ovoce = ['Jablko', 'Banán', 'Hruška']
print("Máme košík a v něm máme nasledující ovoce:", ovoce)
print("Z košíku náhodně vybírame jedno ovoce. Tvým úkolem je uhodnout, které ovoce bylo vybráno. Máš 2 pokusy")

slovo = random.choice(ovoce)

# Pocet pokusu na uhodnuti
pocet_pokusu = 2

# Nastaveni pocitadla
i = 0

# While smycka s podminkou - napis podminku za while a před dvoujčeku
while i < 2:

    # Zadani tipu
    tip = input('Vlož svůj tip: ')

    # Kontrola spravnosti slova - nastav podminku za if
    if slovo == tip:
        break

    # Zvetseni pocitadla
    i += 1

# Podminka pro vyhru
if i == 2:
    print("Prohrál jsi")
else:
    print('Správně! Počet pokusů:', )
