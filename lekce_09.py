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

# format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# fill            ::=  <any character>
# align           ::=  "<" | ">" | "=" | "^"
# sign            ::=  "+" | "-" | " "
# width           ::=  digit+
# grouping_option ::=  "_" | ","
# precision       ::=  digit+
# type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

data = ('car', 1037.123456789, 'freelancer')
print('|word: {0:*^11}|number: {1:#>+15,.7E}|'.format(*data))
print('|{0:*<6c}|'.format(90))

# %[(klic)][zarovnani_vypln][sirka][.presnost][typecode]
print('|%#5x|' % (54,))
