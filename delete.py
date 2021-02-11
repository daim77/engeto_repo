
friendships = [
    ('A', 'B'),
    ('B', 'C'),
    ('A', 'C'),
    ('C', 'D'),
    ('B', 'F'),
    ('D', 'E'),
    ('F', 'E'),
    ('F', 'J'),
    ('E', 'H'),
    ('E', 'G'),
    ('G', 'H'),
    ('H', 'I'),
    ('I', 'J'),
    ('I', 'L'),
    ('L', 'M'),
    ('M', 'N'),
    ('N', 'O')
]

def get_friends(person):
    my_set = set()
    for item in friendships:
        if person in item:
            my_set.update(set(item).difference(person))
    return my_set


def common_friends(person1, person2):
    set1 = get_friends(person1)
    set2 = get_friends(person2)
    return set1 & set2


def is_friendship(person1, person2):
    for item in friendships:
        if item == (person1, person2) or item == (person2, person1):
            return True
        else:
            return False


if __name__ == '__main__':
    print(common_friends('G', 'H'))
    print(is_friendship('A', 'D'))
