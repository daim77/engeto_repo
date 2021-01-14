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

class SmartFridge:

    fridge_count = 0  # atribut tridy je pristupny vsem instancim

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        SmartFridge.fridge_count += 1  # instance.atribut = value

    def greet(self):
        print(f'Hello, I am your Smart Fridge :-) self = {self}')


