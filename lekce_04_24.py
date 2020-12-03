# kalkulacka
# Tvým úkolem v této části bude napsat jednoduchý skript, který bude umět provádět se dvěma zadanými hodnotami
# volitelné matematické operace (součet, odčítání, násobení, dělení) Řekněme, že si uživatel
# vybere cislo01 = 3 a cislo02 = 4. Dále si vybere, že chce provést operaci soucet. Výsledkem by měl
# vypsaný výpočet 3 + 4 = 7.
# Nejprve si ukážeme, jak bychom měli u tvorby takového kódu přemýšlet.
# Na začátek budeme chtít pozdravit uživatele a říct, aby vepsal dvě libovolná čísla.
# Další částí bude nadepsaný výběr operací, které může s čísly provádět.
# Nakonec budeme potřebovat spojit operaci, kterou uživatel vybral s výpočtem, který má provést a následně vypsat.
# Pomocí cyklu bychom chtěli zopakovat, aby se uživateli nabízely operace tak dlouho,
# dokud je nebude chtít příkazem ukončit.

# Pozdrav uživatele a umožni mu zapsat dvě vstupní proměnné
print('=' * 70)
print('Ahoj. Toto je velmi primitivni kalkulacka. Budes vyzvan k zadani dvou libovolnych cisel a k volbe vypoctu!')
print('=' * 70)
print('=' * 70)
a = int(input('Zadej prvni cislo: '))
b = int(input('Zadej druhe cislo: '))


# Zapiš nekonečnou smyčku



# Vypiš jaké operace může uživatel provádět a možnost zapsat input()
print('=' * 70)
print('Zvol jednu z nasledujicich operaci:')
print('1    |   soucet')
print('2    |   rozdil')
print('3    |   nasobeni')
print('4    |   deleni')
print('5    |   KONEC')



# Sem zapiš podmínky, které spojí tebou nabízené operace a následný print() výsledku