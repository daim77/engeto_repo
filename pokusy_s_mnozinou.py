# definice mnozin
FIRST_SET = {'a', 's', 'd', 'f', 'g'}
SECOND_SET = {'l', 'k', 'j', 'h', 'g', 'f'}
''
# operace na mnozinach
print(FIRST_SET | SECOND_SET)
print(FIRST_SET.union(SECOND_SET))
print(FIRST_SET & SECOND_SET)
print(FIRST_SET.intersection(SECOND_SET))
print(FIRST_SET - SECOND_SET)
print(FIRST_SET <= SECOND_SET)
print('=' * 40)