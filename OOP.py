# OOP v Puthonu, class, methods atc...

# class SmartFridge:
#
#     def greet(self):
#         print(f'Hello, I am your Smart Fridge :-) self = {self}')
#
#
# my_fridge = SmartFridge()  # instance
# print(my_fridge)
# my_fridge.greet()
#
# # atributy instance
# my_fridge.brand = 'Bosh'
# print(my_fridge.brand)

# # metoda __init__()
# class SmartFridge:
#     def __init__(self, brand, model):
#
#         self.brand = brand
#         self.model = model
#
#     def greet(self):
#         print(f'Hello from {self.brand} Fridge!')
#
#
# my_fridge = SmartFridge('Bosch', 'built-in')
# print(my_fridge.brand)
# my_fridge.brand = 'Miele'
# print(my_fridge.brand)
#
# my_fridge_home = SmartFridge('Liebher', 'classic')
# my_fridge_home.greet()
# my_fridge_home.greet()

# atributy class

# # ===========UKOL 1==========
# # pridani metody stari lednice
# from datetime import date
#
#
# class SmartFridge:
#
#     fridge_count = 0  # atribut tridy je pristupny vsem instancim
#
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.creation = date.today()
#         SmartFridge.fridge_count += 1  # instance.atribut = value
#
#     def greet(self):
#         print(f'Hello, I am your Smart Fridge :-) self = {self}')
#
#     def age_fridge(self):
#         age = date.today() - self.creation
#         print(age.days)
#
#
# home_fridge = SmartFridge('Bosch', 'small')
# office_fridge = SmartFridge('Miele', 'vine')
#
# print(SmartFridge.fridge_count)
#
# print(home_fridge)
# print(home_fridge.creation)
# home_fridge.age_fridge()

# ===========UKOL 2==========
# souradnice verze OOP a verze proceduralni
# ===========UKOL 2.1==========
# # proceduralni verze
#
# def my_dist(x1, y1, x2, y2):
#     dist = ((x1 - x2)**2 + (y1 - y2) ** 2) ** (1/2)
#     return dist
#
#
# print(my_dist(1,1,2,2))

# # ===========UKOL 2.2==========
# # OOP verze
#
# class MyPoints:
#
#     count_points = 0
#
#     def __init__(self, x1, y1):
#         self.axe_x = x1
#         self.axe_y = y1
#         MyPoints.count_points += 1
#
#     def dist(self, nd_point):
#         x1 = self.axe_x
#         y1 = self.axe_y
#         x2 = nd_point.axe_x
#         y2 = nd_point.axe_y
#         two_points_dist = ((x1 - x2)**2 + (y1 - y2) ** 2) ** (1/2)
#         print('{:<.6}'.format(two_points_dist))
#
#
# bod1 = MyPoints(1, 1)
# bod2 = MyPoints(11, 11)
#
# bod1.dist(bod2)

# # ===========UKOL 3==========
# # Phone class
#
# from pprint import pprint as pp
#
#
# class Phone:
#
#     phone_dict = {}
#
#     def __init__(self, brand, emei):
#         self.brand = brand
#         self.emei = emei
#         self.phone_dict = {brand: {emei: {'contacts': []}}}
#
#     def add_contact(self, name, surname, phone_number):
#         for c_list in self.phone_dict[self.brand][self.emei]['contacts']:
#             if c_list == [name, surname, phone_number]:
#                 decision = input('This contact already exists. Would you like to save it? Y / N: ')
#                 if decision.lower() == 'n':
#                     return
#         self.phone_dict[self.brand][self.emei]['contacts'].append([name, surname, phone_number])
#
#     def show_contact(self):
#         print('contact list for: ', self.brand, 'with EMEI', self.emei)
#         pp(self.phone_dict[self.brand][self.emei])
#         print()
#
#     def del_contact(self, name, surname):
#         occurrence = 0
#         for contact in self.phone_dict[self.brand][self.emei]['contacts']:
#             if contact[0] == name and contact[1] == surname and occurrence == 0:
#                 occurrence += 1
#                 print('deleting contact {}, {}, {} '.format(name, surname, contact[2]))
#                 c_list = self.phone_dict[self.brand][self.emei]['contacts']
#                 c_list.remove([name, surname, contact[2]])
#             if contact[0] == name and contact[1] == surname and occurrence > 0:
#                 decision = \
#                     input('would you like to remove also duplicate contact with number {}? Y/N:'.format(contact[2]))
#                 if decision.lower() == 'y':
#                     occurrence += 1
#                     c_list = self.phone_dict[self.brand][self.emei]['contacts']
#                     c_list.remove([name, surname, contact[2]])
#         if occurrence == 0:
#             print('No any contact for removal..')
#         return
#
#     def find_contact(self, name, surname):
#         occurrence = 0
#         for contact in self.phone_dict[self.brand][self.emei]['contacts']:
#             if contact[0] == name and contact[1] == surname:
#                 occurrence += 1
#                 if occurrence == 1:
#                     print('Contacts found:')
#                 print('{}, {}, {} '.format(name, surname, contact[2]))
#         if occurrence == 0:
#             print('No contact found...')
#         return
#
#
# mobile = Phone('iPhone 11', '123456789')
# mobile.show_contact()
#
# mobile.add_contact('name1', 'surname1', '123456789')
# mobile.show_contact()
#
# mobile.add_contact('name2', 'surname2', '987654321')
# mobile.show_contact()
#
# mobile.add_contact('name1', 'surname1', '1234567890')
# mobile.show_contact()
#
# office = Phone('Nokia', '0987654321ddhg547')
# office.add_contact('office_name', 'office_surname', '1357913579')
# office.show_contact()
#
#
# mobile.find_contact('name1', 'surname1')


# getter, setter a deleter

# class Person:
#
#     def __init__(self, name, address, nationality, age):
#         self.name = name
#         self.address = address
#         self.nationality = nationality
#         self.age = age
#         self.is_adult = self.age >= 18
#
#     def get_age(self):                      # Nový getter
#         return self.age
#
#     def set_is_adult(self):
#         self.is_adult = self.age >= 18
#         return
#
#     def del_age(self):
#         del self.age
#         del self.is_adult
#         return
#
#
# ana = Person("Ana", "Svobodova 3", "Czech", 17)
# print(ana.get_age())
# print(ana.is_adult)
#
# ana.age = 20
# print(ana.get_age())
# ana.set_is_adult()
# print(ana.is_adult)
#
# ana.del_age()
# print(ana.get_age())
# print(ana.is_adult)

# from datetime import date
#
#
# class Person:
#
#     def __init__(self, name, address, nationality, birth_date):
#         self.name = name
#         self.address = address
#         self.nationality = nationality
#         self.birth_date = birth_date
#         self.age = self.calculate_age()
#         self.is_adult = self.age >= 18
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, new_age):
#         self.age = new_age
#         self.is_adult = self.age >= 18
#
#     def del_age(self):
#         del self.age
#
#     def set_is_adult(self):
#         self.is_adult = self.age >= 18
#
#     def set_birth_date(self, new_birth_date):
#         self.birth_date = new_birth_date
#         self.age = self.calculate_age()
#         self.is_adult = self.age >= 18
#
#     def del_birth_date(self):
#         del self.birth_date
#         del self.is_adult
#         del self.age
#
#     def get_birt_date(self):
#         return self.birth_date
#
#     def calculate_age(self):
#         delta = date.today() - self.birth_date
#         return round(delta.days / 365, 1)
#
# def choose_beverage(person):
#     return "Take a beer!" if person.calculate_age() >= 18 else 'Sorry, water for you'
#
#
# ana = Person("Ana", "Svobodova 3", "Czech", date(2010, 1, 4))
# print(ana.birth_date)
# print(ana.age)
# print(choose_beverage(ana))
#
# print()
#
# ana.set_birth_date(date(2000, 1, 4))
# print(ana.age)
# print(choose_beverage(ana))
# print(ana.is_adult)
#
# print()
#
# ana.set_birth_date(date(2019, 1, 4))
# print(ana.is_adult)


# # chranene atribut tridy
#
# from datetime import date
#
#
# class Person:
#
#     def __init__(self, name, address, nationality, birth_date):
#         self.name = name
#         self.address = address
#         self.nationality = nationality
#         self.birth_date = birth_date
#         self._age = self.calculate_age()
#         self._is_adult = self._age >= 18
#
#     def get_age(self):
#         return self._age
#
#     def set_age(self, new_age):
#         self._age = new_age
#         self._is_adult = self._age >= 18
#
#     def del_age(self):
#         del self._age
#
#     def set_is_adult(self):
#         self._is_adult = self._age >= 18
#
#     def set_birth_date(self, new_birth_date):
#         self.birth_date = new_birth_date
#         self._age = self.calculate_age()
#         self._is_adult = self._age >= 18
#
#     def del_birth_date(self):
#         del self.birth_date
#         del self._is_adult
#         del self._age
#
#     def get_birt_date(self):
#         return self.birth_date
#
#     def calculate_age(self):
#         delta = date.today() - self.birth_date
#         return round(delta.days / 365, 1)
#
#
# def choose_beverage(person):
#     return "Take a beer!" if person.calculate_age() >= 18 else 'Sorry, water for you'
#
#
# ana = Person("Ana", "Svobodova 3", "Czech", date(2010, 1, 4))
# print(ana.birth_date)
# print(ana._age)
# print(choose_beverage(ana))
#
# print()
#
# ana.set_birth_date(date(2000, 1, 4))
# print(ana._age)
# print(choose_beverage(ana))
# print(ana._is_adult)
#
# print()
#
# ana.set_birth_date(date(2019, 1, 4))
# print(ana._is_adult)

# # data hiding - lze pristupovat pres name._Person__age
#
# from datetime import date
#
#
# class Person:
#
#     def __init__(self, name, address, nationality, birth_date):
#         self.name = name
#         self.address = address
#         self.nationality = nationality
#         self.birth_date = birth_date
#         self.__age = self.calculate_age()
#         self.__is_adult = self.__age >= 18
#
#     def set_is_adult(self):
#         self.__is_adult = self.__age >= 18
#
#     def set_birth_date(self, new_birth_date):
#         self.birth_date = new_birth_date
#         self.__age = self.calculate_age()
#         self.__is_adult = self.__age >= 18
#
#     def del_birth_date(self):
#         del self.birth_date
#         del self.__is_adult
#         del self.__age
#
#     def get_birth_date(self):
#         return self.birth_date
#
#     def calculate_age(self):
#         delta = date.today() - self.birth_date
#         return round(delta.days / 365, 1)
#
#
# def choose_beverage(person):
#     return "Take a beer!" if person.calculate_age() >= 18 else 'Sorry, water for you'
#
#
# ana = Person("Ana", "Svobodova 3", "Czech", date(2010, 1, 4))
# print(ana.birth_date)
# print(choose_beverage(ana))
# print(ana._Person__age)
#
# print()
#
# ana.set_birth_date(date(2000, 1, 4))
# print(choose_beverage(ana))
# print(ana.__is_adult)
#
#
# print()
#
# ana.set_birth_date(date(2019, 1, 4))
# print(ana.__is_adult)

# dekorator PROPERTY

# from datetime import date
#
#
# class Person:
#
#     def __init__(self, name, address, nationality, birthdate):
#         self.name = name
#         self.address = address
#         self.nationality = nationality
#         self.birthdate = birthdate
#         self.__age = self.calculate_age()
#         self.__is_adult = self.__age >= 18
#
#     @property
#     def birthdate(self):
#         return self.birthdate
#
#     @birthdate.setter
#     def birthdate(self, new_birthday):
#         """
#         Tato metoda nám pomohá zachovat soulad mezi birthday, age a is_adult.
#         """
#         self._birthdate = new_birthday  # protected variable
#         self.__age = self.calculate_age()
#         self.__is_adult = self.__age > 18
#
#     @birthdate.deleter
#     def birthdate(self):
#         """
#         Tato metoda nám pomohá zachovat soulad mezi birthdate, age a is_adult.
#         """
#         del self._birthdate
#         del self.__age
#         del self.__is_adult
#
#     def calculate_age(self):
#         """
#         Tato metoda vypočítá věk osoby na základě data narození.
#         """
#         diff = date.today() - self._birthdate  # Přistupujeme přímo k `_birthdate`
#         return round(diff.days / 365, 1)
#
#
# def choose_beverage(person):
#     return "Take a beer!" if person.calculate_age() >= 18 else 'Sorry, water for you'
#
#
# anna = Person("Ana", "Svobodova 3", "Czech", date(2003, 1, 20))
# print(choose_beverage(anna))
#
# anna.birthdate = date(2019, 12, 31)
# print(choose_beverage(anna))

# # ============== UKOL 4 ===============
# # integrace func do class
# from datetime import date
#
#
# class Person:
#
#     def __init__(self, name, address, nationality, birthdate):
#         self.name = name
#         self.address = address
#         self.nationality = nationality
#         self.birthdate = birthdate
#         self.__age = self.calculate_age()
#         self.__is_adult = self.__age >= 18
#         self.choose_beverage = 'beer' if self.__is_adult else 'water'
#
#     @property
#     def birthdate(self):
#         return self.birthdate
#
#     @birthdate.setter
#     def birthdate(self, new_birthday):
#         self._birthdate = new_birthday  # protected variable
#         self.__age = self.calculate_age()
#         self.__is_adult = self.__age > 18
#         self.choose_beverage = 'beer' if self.__is_adult else 'water'
#
#     @birthdate.deleter
#     def birthdate(self):
#         del self._birthdate
#         del self.choose_beverage
#         del self.__age
#         del self.__is_adult
#
#     def calculate_age(self):
#         diff = date.today() - self._birthdate  # Přistupujeme přímo k `_birthdate`
#         return round(diff.days / 365, 1)
#
#
# anna = Person("Ana", "Svobodova 3", "Czech", date(2000, 1, 20))
# print(anna.choose_beverage)
#
# anna.birthdate = date(2018, 12, 31)
# print(anna.choose_beverage)

# # ============= UKOL 5 =================
# # Zamestnanec
#
# from datetime import date
# import string
#
#
# class Employee:
#
#     def __init__(self, ident, department, contract_from, contract_to, password):
#         self.ident = ident
#         self.department = department
#         self.contract_from = contract_from
#         self.contract_to = contract_to
#         self.__password = password
#         self.password_test = self.password_test()
#
#     @property
#     def password(self):
#         raise ValueError('Password is not readable')
#
#     @password.setter
#     def password(self, new_password):
#         # self._password_test = self.password_test(new_password)
#         # if not self.password_test:
#         #     raise ValueError
#         self.__password = new_password
#
#     @password.deleter
#     def password(self):
#         raise AttributeError('Password can not be deleted')
#
#     def password_test(self):
#         if len(self.__password) >= 8:
#
#             for char in self.__password:
#                 if char in string.ascii_lowercase:
#
#                     for sub_char in self.__password:
#                         if sub_char in string.ascii_uppercase:
#
#                             for sub_sub_char in self.__password:
#                                 if sub_sub_char in '''!"#$%&'()*+,-./''':
#
#                                     for num in self.__password:
#                                         if num in str(range(0, 10)):
#
#                                             return True
#         raise ValueError('wrong password format')
#
#
# honza = Employee('QX123', 'logistics', date(2000, 1, 1), date(2020, 12, 31), 'Hellotdk8/di')
# # honza.password = 'ahoj'
# print(honza._Employee__password)

# ========= UKOL 6 =========
# class Account

from datetime import datetime


class Account:

    def __init__(self, initial_deposit=0):
        self.deposits = initial_deposit
        self.withdrawals = 0
        self._balance = initial_deposit
        self._history = {datetime.now(): self._balance}

    @property
    def balance(self):
        return self._balance

    @property
    def history(self):
        return self._history

    def formated_history(self):
        print('.' * 35)
        for item in self._history:
            print('|{:^22}|{:^10}|'.format(item.strftime('%Y-%b-%d %H:%M:%S'), self._history[item]))
        print('.' * 35)

    def deposit(self, deposit):
        self._history.update({datetime.now(): deposit})
        self._balance += deposit
        self.deposits += deposit

    def withdrawal(self, withdrawal):
        self._history.update({datetime.now(): -1 * withdrawal})
        self._balance -= withdrawal
        self.withdrawals += withdrawal


rb_bank = Account(100)
print(rb_bank.deposits)
print(rb_bank.balance)
print(rb_bank.history)

rb_bank.deposit(50)
print(rb_bank.deposits)
print(rb_bank.balance)
print(rb_bank.history)

rb_bank.withdrawal(25)
print(-1 * rb_bank.withdrawals)
print(rb_bank.balance)
print(rb_bank.history)

rb_bank.formated_history()

rb_bank.balance = 100
