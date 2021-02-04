# debugovani

# ===== ze zadane tabulky do txt a opacne =====
# pouzij aspon jednu vyjimku

# [["Jmeno", "Prijmeni", "Vek"], ["Petr","Novotny", 45], ["Hanka","Bila", 33], ["Sabina","Suchanova", 11]]

# TODO: nastudovat modul logging


import time
# import logging
# import sys
import os


def vytvor_file(data: list, cesta:str) -> None:
    with open(cesta + '/tabulka.txt', mode='w') as file:
        for item in data:
            file.write('.'.join([str(part) for part in item]) + '\n')


def precti_file_a_vytvor_list(cesta: str) -> list:
    try:
        # logging.basicConfig(level=logging.DEBUG, filename='myapp.log')
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
        return result
    except FileNotFoundError:
        print('soubor neexistuje')


def main():
    while True:
        mode = input('Zadej mod(w/r or any as QUIT): ').lower()
        if mode =='r':
            list_listu = precti_file_a_vytvor_list('/Users/martindanek/Documents/programovani/files/txt')
            print(list_listu)
        elif mode == 'w':
            tabulka = eval(input('Vloz svuj list listu: '))
            vytvor_file(tabulka, '/Users/martindanek/Documents/programovani/files/txt')
        else:
            return


if __name__ == '__main__':
    # print(sys.argv)
    print(os.getcwd())
    # os.chdir('/Users/martindanek/Documents/programovani/files/')
    # os.mkdir("textove_tabulky")
    start = time.time()
    main()
    end = time.time()
    print(end - start)
