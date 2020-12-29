# Formátování stringů a textové soubory

# person_data = {'name': 'Bob', 'age': 37}
# print('My name is %(name)s and I am %(age)d years old.' % person_data)
# # nebo
#
#
# print('My name is {name} and I am {age} years old.'.format(name='Bob', age=37))
#
#
# name = 'Bob'
# age = 37
# print('My name is {name} and I am {age} years old.'.format(name=name, age=age))
#
#
# person_data = {'name': 'Bob', 'age': 37, 'job': 'freelancer'}
# print('My name is {name} and I am {age} years old.'.format(**person_data))


data = ('Bob', 37.123456789, 'freelancer')
print('|name: {0:->10}|age: {1:#>+10.5}|'.format(*data))  # index:fill|align|sign|width|.precision|
