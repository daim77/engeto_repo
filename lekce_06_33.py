# Vytvoř program, který vytiskne, kolikrát se každý objekt nachází v daném listu, tuplu, nebo stringu
# (u stringu chceme počet jednotlivých znaků).
# Výstupem programu by měl být slovník, který se skládá z následující dvojice klíč - hodnota:
# klíč - string reprezentace počítaného objektu,
# hodnota - celé číslo, které značí počet výskytu daného objektu.
# Příklad vstupu:
# seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]
# Výstup:
# {'1': 4, '8': 1, '321': 1, '4': 1, '3': 2, '6': 2, '21': 1, '32': 1, '5': 2, '2': 3, '9': 1}

# vstup
seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]

numerosity = {}
for i in seq:
    if i not in numerosity:
        numerosity.setdefault(i, 0)
    numerosity[i] += 1
print(numerosity)

# reseni by ENGETO
seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]
counts = {}
for num in seq:
    counts[str(num)] = counts.setdefault(str(num),0) + 1
print(counts)