# # Skript na seřazení
# # Vytvořme program, který nám seřadí abecedně jakýkoli list.
# # Nemůžeme použít funkce jako je sort() nebo sorted().
# # Toto cvičení slouží jako procvičení práce s for + break + else.
# # Abychom otestovali náš program, použijeme následující seznam jmen:
#
# names = [
#     'Michal', 'Pepa', 'Honza',
#     'Pavel', 'Lukas', 'Matej',
#     'Iva', 'Klara', 'Jana',
#     'Honza', 'Vasek', 'Milan',
#     'Michal'
# ]
# sorted_names = list()
# sorted_names.append(names.pop())
# for name in names:
#     i = 0
#     for sorted_name in sorted_names:
#         if name <= sorted_name:
#             sorted_names.insert(i, name)
#             name = ''
#             break
#         else:
#             i += 1
#     sorted_names.append(name)
# while '' in sorted_names:
#     sorted_names.remove('')
# print(sorted_names)
# =========================================
# names = [
#     'Michal', 'Pepa', 'Honza',
#     'Pavel', 'Lukas', 'Matej',
#     'Iva', 'Klara', 'Jana',
#     'Honza', 'Vasek', 'Milan',
#     'Michal'
# ]
#
# # Vytvoř list, do kterého vložíš jeden prvek z list `names`. Zároveň ho z listu `names` odstraň.
# # Tento krok se ti bude hodit, když budeš chtít přidávat a seřazovat další jméno z listu `names` do listu `sorted_names`
# sorted_names = [names.pop()]
#
# # Začni vnější for loop, kterým budeš procházet seznam `names` (měl by mít už o jeden prvek méně)
# for name in names:
#     # Zační vnitřní for loop, kterým budeš procházet seznam `sorted_names` a pomocí podmínkového výrazu,
#     # `break` a `else` vlož jméno z `names` buď na pozici, nebo za pozici daného jméno v listu `sorted_names`
#     for i, s_name in enumerate(sorted_names):
#         if name < s_name:
#             sorted_names.insert(i, name)
#             break
#     else:
#         sorted_names.append(name)
#
# # Vytiskni seřazená jména
# print(sorted_names)

# =================================
# # v2.0
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
    i = -1
    for sorted_name in sorted_names:
        if name < sorted_name:
            i += 1
            sorted_names.insert(i, name)
            break
    else:
        sorted_names.append(name)
print(sorted_names)

