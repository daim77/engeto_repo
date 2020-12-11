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
sorted_names = list()
sorted_names.append(names.pop())
for name in names:
    i = 0
    for sorted_name in sorted_names:
        if name <= sorted_name:
            sorted_names.insert(i, name)
            name = ''
            break
        else:
            i += 1
    sorted_names.append(name)
while '' in sorted_names:
    sorted_names.remove('')
print(sorted_names)
