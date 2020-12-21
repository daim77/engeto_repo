import random
def order_sequence(my_list):
    for i in range(1,len(my_list)):
        pos = i
        while pos > 0 and my_list[pos-1] > my_list[pos]:
            my_list[pos],my_list[pos-1] =  my_list[pos-1], my_list[pos]
            pos -= 1


def generate_random_list(size):
    lst = []
    for i in range(size):
        lst.append(random.randint(1,100))
    return lst

l = generate_random_list(10)
print('Before sorting:',l)
order_sequence(l)
print('After sorting:', l)