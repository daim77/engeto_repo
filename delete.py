import os


def search(start_dir, searched_name):
    # Vytvoříme proměnou, které se bude vracet.
    paths = []
    # Vytvoříme proměnou, do které se ukládají složky, které je nutné prohledat.
    dirs_to_search = [start_dir]

    # Dokud máme složky, které je potřeba prohledat, tak prohledáváme.
    while dirs_to_search:
        current_dir = dirs_to_search.pop(0)

        # Procházíme všechny položky ve složce.
        for item in os.listdir(current_dir):

            # Vytváříme cestu ke každému souboru ve složce.
            item_path = os.path.join(current_dir, item)

            # Pokud během prohledávání narazíme na složku, přidáme jí do listu složek k prohledání
            if os.path.isdir(item_path):
                dirs_to_search.append(item_path)

            # Pokud narazíme na hledané jmeno, přidáváme do výsledného listu
            elif item.split('.')[0] == searched_name:
                paths.append(item_path)

    return paths


if __name__ == '__main__':
    print(search('/Users/martindanek/Documents', 'text1'))
