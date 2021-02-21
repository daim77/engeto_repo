# def my_range(start, stop, step=1):
#     test = (lambda x, y: x < y and step > 0,
#             lambda x, y: x > y and step < 0)[start > stop]
#
#     while test(start, stop):
#         yield start
#         start += step
#
#
# gen = my_range(0, 10)
# # for i in gen:
# #     print(i)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# text = 'vsvsvdv@bkdbcb.cz hjgsfgsag sgfsahgfag m@d.cy'
# r = list(
#     map(lambda x: x.rstrip('.,/\\; '),
#         map(lambda x: x.split('@')[-1],
#             filter(lambda x: '@' in x, text.split()
#                    )
#             )
#         )
# )
#
# print(r)


import random

# Vytvoříme list, který bude obsahovat všechny žolíkové karty.
deck = [
    suit + ' ' + str(number)
    for suit in ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    for number in ['Ace']+list(range(2, 11))+['Jack', 'Queen', 'King']
]

random.shuffle(deck)
print(deck)
