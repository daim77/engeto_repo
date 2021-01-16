from datetime import date


class Person:

    def __init__(self, name, address, nationality, birth_date):
        self.name = name
        self.address = address
        self.nationality = nationality
        self.birth_date = birth_date
        self.__age = self.calculate_age()
        self.__is_adult = self.__age >= 18

    def set_is_adult(self):
        self.__is_adult = self.__age >= 18

    def set_birth_date(self, new_birth_date):
        self.birth_date = new_birth_date
        self.__age = self.calculate_age()
        self.__is_adult = self.__age >= 18

    def del_birth_date(self):
        del self.birth_date
        del self.__is_adult
        del self.__age

    def get_birt_date(self):
        return self.birth_date

    def calculate_age(self):
        delta = date.today() - self.birth_date
        return round(delta.days / 365, 1)


def choose_beverage(person):
    return "Take a beer!" if person.calculate_age() >= 18 else 'Sorry, water for you'


ana = Person("Ana", "Svobodova 3", "Czech", date(2010, 1, 4))
print(ana.birth_date)
print(ana.__age)
print(choose_beverage(ana))

print()

ana.set_birth_date(date(2000, 1, 4))
print(ana.__age)
print(choose_beverage(ana))
print(ana.__is_adult)

print()

ana.set_birth_date(date(2019, 1, 4))
print(ana.__is_adult)
