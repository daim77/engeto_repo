a, b = 0x21, 0x2f
my_punct = ''
for char in range(a, b + 1):
    my_punct += chr(char)
print(my_punct)


def verify_password(password):

    if len(password) < 8:
        raise ValueError('insufficient password length')

    count_char_categories = {(chr(num) for num in range(ord('A'), ord('Z') + 1)): 0,
                             (chr(num) for num in range(ord('a'), ord('z') + 1)): 0,
                             (chr(num) for num in range(ord('!'), ord('/') + 1)): 0,
                             (chr(num) for num in range(ord('0'), ord('9') + 1)): 0
                             }

    for category in count_char_categories:
        count_char_categories[category] = sum((char in password for char in category))

    return all(count_char_categories.values())
