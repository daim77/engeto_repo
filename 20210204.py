# debugovani

# ===== ze zadane tabulky do txt a opacne =====
# pouzij aspon jednu vyjimku

tabulka = [
    ["Jmeno", "Prijmeni", "Vek"], ["Petr","Novotny", 45],
    ["Hanka","Bila", 33], ["Sabina","Suchanova", 11]
]


def vytvor_file(data: list, cesta:str) -> None:
    with open(cesta + '/tabulka.txt', mode='w') as file:
        for item in tabulka:
            file.write('.'.join([str(part) for part in item]) + '\n')


def precti_file_a_vytvor_list(cesta: str) -> list:
    try:
        with open(cesta + '/tabulka.txt', mode='r') as file:
            result = []
            while True:
                row = file.readline()
                if not row:
                    break
                row = row.replace('\n', '').split('.')
                try:
                    row[2] = int(row[2])
                except ValueError:
                    pass
                result.append(row)
        print(result)
    except FileNotFoundError:
        print('soubor neexistuje')


# def main()
#     pass

if __name__ == '__main__':
    vytvor_file(tabulka, '/Users/martindanek/Documents/programovani/files/txt')
    precti_file_a_vytvor_list('/Users/martindanek/Documents/programovani/files/txt')