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

# ===========UKOL 2.2==========
# Phone class

from pprint import pprint as pp


class Phone:

    total_phone = 0
    phone_dict = {}

    def __init__(self, brand, emei):
        self.brand = brand
        self.emei = emei
        Phone.total_phone += 1
        Phone.phone_dict.update({self.brand: {self.emei: {'contacts': []}}})

    def add_contact(self, name, surname, phone_number):
        for c_list in Phone.phone_dict[self.brand][self.emei]['contacts']:
            if c_list == [name, surname, phone_number]:
                decision = input('This contact already exists. Would you like to save it? Y / N: ')
                if decision.lower() == 'n':
                    return
        Phone.phone_dict[self.brand][self.emei]['contacts'].append([name, surname, phone_number])

    def show_contact(self):
        print('contact list for: ', self.brand, 'with EMEI', self.emei)
        pp(Phone.phone_dict[self.brand][self.emei])
        print()

    def del_contact(self, name, surname):
        occurrence = 0
        for contact in Phone.phone_dict[self.brand][self.emei]['contacts']:
            if contact[0] == name and contact[1] == surname and occurrence == 0:
                occurrence += 1
                print('deleting contact {}, {}, {} '.format(name, surname, contact[2]))
                c_list = Phone.phone_dict[self.brand][self.emei]['contacts']
                c_list.remove([name, surname, contact[2]])
            if contact[0] == name and contact[1] == surname and occurrence > 0:
                decision = \
                    input('would you like to remove also duplicate contact with number {}? Y/N:'.format(contact[2]))
                if decision.lower() == 'y':
                    occurrence += 1
                    c_list = Phone.phone_dict[self.brand][self.emei]['contacts']
                    c_list.remove([name, surname, contact[2]])
        if occurrence == 0:
            print('No any contact for removal..')
        return

    def find_contact(self, name, surname):
        occurrence = 0
        for contact in Phone.phone_dict[self.brand][self.emei]['contacts']:
            if contact[0] == name and contact[1] == surname:
                occurrence += 1
                if occurrence == 1:
                    print('Contacts found:')
                print('{}, {}, {} '.format(name, surname, contact[2]))
        if occurrence == 0:
            print('No contact found...')
        return


mobile = Phone('iPhone 11', '123456789')
mobile.show_contact()

mobile.add_contact('name1', 'surname1', '123456789')
mobile.show_contact()

mobile.add_contact('name2', 'surname2', '987654321')
mobile.show_contact()

mobile.add_contact('name1', 'surname1', '1234567890')
mobile.show_contact()

office = Phone('Nokia', '0987654321ddhg547')
office.add_contact('office_name', 'office_surname', '1357913579')
office.show_contact()


mobile.find_contact('name1', 'surname1')

