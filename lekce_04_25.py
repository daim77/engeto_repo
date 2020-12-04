# Vytvořte program, který vytiskne každý pár klíč-hodnota ve formátu: "Klíč: <key> | Hodnota: <value>"

film = {'name': 'Forrest Gump',
        'made': 1994,
        'director': 'Robert Zemeckis',
        'soundtrack': 'Multiple',
        'starring': 'Tom Hanks',
        'fun_fact': 'The house used in Forrest Gump is the same house used in The Patriot (2000). Some paneling was changed for interior shots  in the latter film.'}
count = 0
my_pairs = tuple(film.items())
while count < len(film):
        print(f"key:    {my_pairs[count][0]}        |  value:    {my_pairs[count][1]}")
        count += 1

# vzorove reseni
# while film:
#     info = film.popitem()
#     print('Key: ' + str(info[0]) + ' | Value: ' + str(info[1]))