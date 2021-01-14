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

# OOP verze

class MyPoints:

    count_points = 0

    def __init__(self, x1, y1):
        self.axe_x = x1
        self.axe_y = y1
        MyPoints.count_points += 1

    def dist(self, nd_point):
        x1 = self.axe_x
        y1 = self.axe_y
        x2 = nd_point.axe_x
        y2 = nd_point.axe_y
        two_points_dist = ((x1 - x2)**2 + (y1 - y2) ** 2) ** (1/2)
        print(two_points_dist)


bod1 = MyPoints(1, 1)
bod2 = MyPoints(2, 2)

bod1.dist(bod2)
