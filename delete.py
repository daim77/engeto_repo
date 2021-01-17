from datetime import date


class Person:

    def __init__(self, name, address, nationality, birthdate):
        self.name = name
        self.address = address
        self.nationality = nationality
        self.birthdate = birthdate
        self.__age = self.calculate_age()
        self.__is_adult = self.__age >= 18
        self.choose_beverage = 'beer' if self.__is_adult else 'water'

    @property
    def birthdate(self):
        return self.birthdate

    @birthdate.setter
    def birthdate(self, new_birthday):
        self._birthdate = new_birthday  # protected variable
        self.__age = self.calculate_age()
        self.__is_adult = self.__age > 18
        self.choose_beverage = 'beer' if self.__is_adult else 'water'

    @birthdate.deleter
    def birthdate(self):
        del self._birthdate
        del self.choose_beverage
        del self.__age
        del self.__is_adult

    def calculate_age(self):
        diff = date.today() - self._birthdate  # Přistupujeme přímo k `_birthdate`
        return round(diff.days / 365, 1)


anna = Person("Ana", "Svobodova 3", "Czech", date(2000, 1, 20))
print(anna.choose_beverage)

anna.birthdate = date(2018, 12, 31)
print(anna.choose_beverage)
