# pokus na volani dvou skryptu a vypsani spolecneho vysledku printem

import BMI
import person


def main(weight, height):
    status = BMI.bmi(weight, height)
    name_surname = person.id_person()
    name = name_surname[0]
    surname = name_surname[1]
    print(f'Person named {name} {surname} has {status} weight')


if __name__ == '__main__':
    main(80, 1.8)
