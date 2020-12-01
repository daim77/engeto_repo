# krabicka = 5 * 8
# # datový tip 5 a 8 INTEGER, FLOAT
# muj_type = type(krabicka)
# # zjistuje datovy typ
# # funkce print ... () volání funkce - bez mezery
# print(krabicka)
# print(muj_type)
# muj_float = 11/5

# def moje_funkce(a):
#     print(a)
# moje_funkce("toto je moje prvni funkce")
# print(type(moje_funkce))
# my_text = 'new_text'
# print(my_text[:5])

# klapka = 422
# print("Číslo na úřad práce je: 777 354", str(klapka))

# # Promenna
# prom = range(20)
#
# # Volání funkce type().
# typ = type(prom)
#
# # Tisk výstupu funkce type().
# print(typ)

# trojite_uvozovky = '''
# toto je pokusny dlouhy text'''
# print(len(trojite_uvozovky))

# Prevod stringu 'Hello' na list.
# novy_list = list('Martin')
# # Tisk noveho listu.
# print(novy_list)

# #metoda .append a dalsi
# shopping_list = []
# for i in range(1, 4):
#     new_item = input('zadej novou polozku :')
#     shopping_list.append(new_item)
#     i = i + 1
# print(shopping_list)
# shopping_list.insert(0, 'nakupni seznam do Lidlu')
# print(shopping_list)
# item_delete = shopping_list[1]
# shopping_list.remove(item_delete)
# print(shopping_list)
# del shopping_list[2]
# print(shopping_list)

# tuple a operace s nim
# my_list = [1, 'Jablko', 2, 'Máslo', 3, 'Chléb']
# print(type(my_list))
# #my_list = tuple() #proste pretipovani listu na tuple
# my_tuple = tuple(my_list) #vytvoreni nove promenne tuple z mz_list
# print(type(my_tuple))

# #indexing
# my_index = '987654321'
# print(my_index[0])
# my_tuple = 'jablko', 'hruska', 'mrkev'
# print(type(my_tuple))
# print(my_tuple[0])
# my_tuple_zero = my_tuple[0]
# print(type(my_tuple_zero))
# print(my_tuple_zero[0]) #jak vypsat prvni pismeno z puvodniho tuple

# zjisteni jakeho typu je fce len()
# my_list = ('a', 'b', 'c')
# print('=' * 20)
# print(my_list)
# print('=' * 20)
# print(type(my_list))
# a = len(my_list)
# print(a)
# print("delka tuple je typu: ", type(a))

# print(len([1,2,[3,4,5]]))

# max a min s typem string
muj_list_mm = ['ma', 'ma', 'ma']
print(min(muj_list_mm))