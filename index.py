# Extrahuj a vytiskni prvních 5 písmen
print('=' * 20)
my_index = "indexování"
prvnich_pet = my_index[:5] # petku lze nahradit promennou INT
print('first five letters: ', prvnich_pet)


# Extrahuj a vytiskni posledních 5 písmen
print('=' * 20)
poslednich_pet = my_index[5:]
print('last five letters: ', poslednich_pet)


# Extrahuj a vytiskni každé 3 písmeno
print('=' * 20)
kazde_treti = my_index[::3]
print('every 3rd letter (first included): ', kazde_treti)