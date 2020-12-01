# Naimportuj modul random
import random

# Vytvort list moznosti
moznosti = ['kamen', 'nuzky', 'papir']

# Vytvort promennou hrac
hrac = input('zadej svoji volbu: ')

# Vytvort promennou pocitac
pocitac = random.choice(moznosti)

# Vytiskni volbu cloveka a pocitace
print('Hrac: ', hrac)
print('Pocitac', pocitac)

# Vytvor podminku, zda hrac zvolil neplatnou volbu
if hrac != 'kamen' and hrac != 'nuzky' and hrac != 'papir':
    print('Neplatna volba')
    exit()

# Pokud je volba v poradku, muzeme provest zbytek programu


# Podimky zahrnujici ruzne kombinace voleb hrace a pocitace a tisk vysledku
if hrac == pocitac:
    print('remiza')
elif hrac == 'papir' and pocitac == 'nuzky':
    print('prohral jsi')
elif hrac == 'nuzky' and pocitac == 'kamen':
    print('prohral jsi')
elif hrac == 'kamen' and pocitac == 'papir':
    print('prohral jsi')
else:
    print('vyhral jsi')

