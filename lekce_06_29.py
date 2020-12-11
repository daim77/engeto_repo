# Skript na seřazení
# Vytvořme program, který nám seřadí abecedně jakýkoli list.
# Nemůžeme použít funkce jako je sort() nebo sorted().
# Toto cvičení slouží jako procvičení práce s for + break + else.
# Abychom otestovali náš program, použijeme následující seznam jmen:

names = [
    'Michal', 'Pepa', 'Honza',
    'Pavel', 'Lukas', 'Matej',
    'Iva', 'Klara', 'Jana',
    'Honza', 'Vasek', 'Milan',
    'Michal'
]
sorted_names = list(names.pop())
print(names)
for name in names:
    i = 0
    for sorted_name in sorted_names:
        if name <= sorted_name:
            sorted_names.insert(i, name)
            sorted_names.insert(i + 1, sorted_name)
            i +=1
            break
        else:
            sorted_names.append(name)
print(sorted_names)
