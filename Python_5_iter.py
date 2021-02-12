# # social media who is friend...
#
# friendships = [
#     ('A', 'B'),
#     ('B', 'C'),
#     ('A', 'C'),
#     ('C', 'D'),
#     ('B', 'F'),
#     ('D', 'E'),
#     ('F', 'E'),
#     ('F', 'J'),
#     ('E', 'H'),
#     ('E', 'G'),
#     ('G', 'H'),
#     ('H', 'I'),
#     ('I', 'J'),
#     ('I', 'L'),
#     ('L', 'M'),
#     ('M', 'N'),
#     ('N', 'O')
# ]
#
#
# def get_friends(person):
#     my_set = set(
#         map(
#             lambda friend: ''.join(friend).replace(person, ''
#                                                    ),
#             filter(
#                 lambda pairs: person in pairs, friendships
#             )
#         )
#     )
#     # my_set = set()
#     # for pairs in friendships:
#     #     if person in pairs:
#     #         my_set.update(set(pairs).difference(person))
#     return my_set
#
#
# def common_friends(person1, person2):
#     return get_friends(person1) & get_friends(person2)
#
#
# def is_friendship(person1, person2):
#     for item in friendships:
#         if item == (person1, person2) or item == (person2, person1):
#             return True
#         else:
#             return False
#
#
# if __name__ == '__main__':
#     print(common_friends('M', 'O'))
#     print(is_friendship('A', 'B'))


# # ==========
# recursive func
# def sum_rec(num):
#     if num == 0:
#         return 0
#     return num + sum_rec(num-1)
#
#
# print(sum_rec(5))

# ==========
# factory func


# def factory():
#
#     def add_num(n):
#         return n + 5
#
#     return add_num
#
#
# a = factory()
# print(a(5))


# def factory():
#     const = 5
#     abc = 'd'
#
#     def add_num(n):
#         print(abc)
#         return n + const
#
#     return add_num
#
#
# a = factory()
# print(a(6))
# print(a.__closure__[0].cell_contents)
# print(dir(factory.__closure__))


# def factory(m):
#
#     def add_num(n):
#         return n + m
#
#     return add_num
#
#
# a54 = factory(54)
# print(a54(32))


# def actions_generator(start, stop):
#     actions = []
#     for i in range(start, stop+1):
#         actions.append(lambda x: x+i)
#     return actions
#
#
# for part in actions_generator(1, 5):
#     print(part(0))


# import datetime
#
#
# today = datetime.date.today()
# today = today - datetime.timedelta(10, weeks=1)
#
# print(today)
# print(datetime.datetime.today().weekday())

# # rekurze faktodial
# import time
#
#
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
#
#
# def factorial_for(n):
#     result = 1
#     for number in range(1, n + 1):
#         result *= number
#     return result
#
#
# start = time.time()
# factorial(900)
# print(time.time() - start)
#
# start = time.time()
# factorial_for(900)
# print(time.time() - start)


# # ==== Fibonacci =====
# # INPUT = 'n' member of fibonacci row
# # OUTPU = value of 'n' member
#
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# if __name__ == '__main__':
#     print(fibonacci(20))

# # ==== nejvetsi spolecny delitel s rekurzi =====
#
# def gcd(a, b):
#     r = a % b
#     if r == 0:
#         return b
#     return gcd(b, r)
#
#
# print(gcd(30, 22))


