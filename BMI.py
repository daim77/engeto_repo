# Vstupni hodnoty
jmeno = input('Zadej sve jmeno: ')
vaha = int(input('Zadej tvoji vahu v kilogramech: '))
vyska = float(input('Zadej tvoji vysku v centimetrech: '))/100
print('=' * 40)
# Vypocet
bmi = round(vaha / vyska ** 2, 1)

# Vytvor promennou kategorie a prirad ji hodnoy pomoci podminek
if bmi < 18.5:
    kategorie = 'Podvyziva'
elif bmi < 25:
    kategorie = 'Zdrava vaha'
elif bmi < 30:
    kategorie = 'Mirna nadvaha'
elif bmi < 40:
    kategorie = 'Obezita'
else:
    kategorie = 'Tezka obezita'

# Vytiskni odpoved s vysledkem
print(jmeno, ' tve BMI je ', bmi, 'coz spada do kategorie', kategorie + '.')

