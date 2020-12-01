#program for unit conversion
# Prevodni pomery
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

# Pocet jednotek, ktery ma byt preveden.
print('=' * 20)
print('insert your values for unit conversion...')
print('=' * 20)
kg_pocet = input('how many kilograms do you have? :')
km_pocet = input('how many kilometers do you have? :')
l_pocet = input('how many litres do you have? :')

# Vypocty pro prevod
kg_vysledek = int(kg_pocet) * kg_lb
km_vysledek = int(km_pocet) * km_mile
l_vysledek = int(l_pocet) * l_gal
# Vysledne odpovedi
print('=' * 20)
print('Here is your required conversion...')
print('=' * 20)
print(f'{kg_pocet} kg is {kg_vysledek} galons')
print(f'{km_pocet} km is {km_vysledek} galons')
print(f'{l_pocet} l is {l_vysledek} galons')