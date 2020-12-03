# my_list = [1, 0, 0, 10]
# print(my_list.count(0))
# print(my_list.index(10))
# print(sum(my_list))

# my_true = bool(1)
# print(my_true)
# my_false = bool(0)
# print(my_false)
# print(my_false > my_true)

# operace s listem
# mylist = []
# mynewlist = []
# myls = [[3, 5], [3, 5], [3, 5]]
# mylist = [[]] * 3
# print(mylist)
# mylist[0].append(3)
# print(mylist)
# mylist[1].append(5)
# print(mylist)
# mylist[1:2] = [[7, 9]]
# print(mylist)
# mynewlist = mylist.pop(0)
# print('Tisk mylist a mynewlist po .pop na nulovem indexu')
# print(mylist)
# print(mynewlist)
# mynewlist.reverse()
# print('Tisk mynewlist po reversu')
# print(mynewlist)
# print('Tisk mylist po reversu mynewlist')
# print(mylist)
# mylist.append(1)
# print('Tisk mylist po .append se stringem 1')
# print(mylist)
# print(any(mylist))

# # Promenna
# mya = 11
# # If podminka
# if mya > 10:
#     print("mya je vetsi nez 10")
# elif mya > 5:
#     print("mya je vetsi nez 5")
# else:
#     print("mya je mensi nez 10 a nez 5")

# VEK = 10
# if  VEK: # chova se jako BOOLean
#   print("Jdi na pivo")
# else:
#   print("Jdi studovat")
#   exit()

# zadat znak a nahradit znak na indexu 5 znakem '@'
my_input = input('Insert any string with min 5 characters: ')
if len(my_input) < 5:
    print('the string has less than five characters')
    exit()
my_input = list(my_input)
my_input.pop(5)
my_input.insert(5, '@')
my_input = ''.join(my_input)
print(my_input)
