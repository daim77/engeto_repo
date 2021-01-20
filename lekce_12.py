# # Debugger
#
# # assert, python -O script
#
# # assert podminka kterou cekam, 'string s chybovou hlaskou'
#
# import pdb
#
#
# def num_days(date1, date2):
#     days = 0
#     if date1 > date2:
#         days = -1
#     else:
#         while date1 < date2:
#             date1 = increase(date1)
#             days += 1
#     return days
#
#
# def increase(date):
#
#     y, m, d = date
#     # february
#     if m == 2 and d in [28, 29]:
#         if is_leap(y) and d == 28:
#             date = (y, m, d+1)
#         else:
#             date = (y, m+1, 1)
#
#     # month end
#     elif (m in [1, 3, 5, 7, 8, 10] and d == 31) \
#             or (m in [4, 6, 9, 11] and d == 30):
#         date = (y, m+1, 1)
#     # year end
#     elif m == 12 and d == 31:
#         date = (y+1, 1, 1)
#     # in month
#     else:
#         date = (y, m, d+1)
#     return date
#
#
# def is_leap(y):
#     result = False
#
#     if y % 400 == 0 \
#             or (y % 4 == 0 and y % 100 != 0):
#         result = True
#     return result
#
#
# if __name__ == '__main__':
#     pdb.set_trace()
#
#     date1 = (2013, 1, 1)
#     date2 = (2017, 1, 1)
#     num_days(date1, date2)

# ========= UKOL 52 =========
# prevadec rimskych cisel

NUMBERS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
           'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
           }


def to_arab(roman_num: str):
    valid_test(roman_num)

    result = NUMBERS[roman_num[-1]]
    value_before = NUMBERS[roman_num[-1]]

    for char in roman_num[-2::-1]:
        if value_before > NUMBERS[char]:
            result -= NUMBERS[char]
        else:
            result += NUMBERS[char]
        value_before = NUMBERS[char]

    return result


def valid_test(roman_num):
    not_valid = ('XXXX', 'VV', 'LL', 'DD', 'CCCC', 'IIII')

    for char in roman_num:
        if char not in NUMBERS:
            raise ValueError('Not valid number')

    for item in not_valid:
        if item in roman_num:
            raise ValueError('Not valid number')
    if len(roman_num) >= 3:
        one_before_one = NUMBERS[roman_num[-1]]
        one_before = NUMBERS[roman_num[-2]]
        for char in roman_num[-3::-1]:
            if NUMBERS[char] <= one_before_one and one_before != one_before_one:
                raise ValueError('Not valid number')
            else:
                one_before_one = one_before
                one_before = NUMBERS[char]
    return


def to_roman(arab_num: int):
    result = ''
    remaining = arab_num

    if remaining > 1000:
        result += 'M' * int(arab_num / 1000)
        remaining = int(str(arab_num)[1:])

    if remaining >= 900:
        result += 'CM'
        remaining -= 900

    if remaining >= 500:
        result += 'D' + 'C' * ((remaining - 500) // 100)
        remaining = int(str(remaining)[1:])
    elif remaining > 400:
        result += 'CD'
        remaining = int(str(remaining)[1:])
    elif 400 > remaining >= 100:
        result += 'C' * int(remaining / 100)
        remaining = remaining = int(str(remaining)[1:])

    if remaining > 90:
        result += 'XC'
        remaining -= 90

    if remaining >= 50:
        result += 'L' + 'X' * ((remaining - 50) // 10)
        remaining = int(str(remaining)[1:])
    elif remaining > 40:
        result += 'XL'
        remaining = int(str(remaining)[1:])
    elif 40 > remaining >= 10:
        result += 'X' * int(remaining / 10)
        remaining = remaining = int(str(remaining)[1:])

    if remaining == 9:
        result += 'IX'
        remaining = 0

    if remaining >= 5:
        result += 'V' + 'I' * (remaining - 5)
    elif remaining == 4:
        result += 'IV'
    elif 4 > remaining >= 1:
        result += 'I' * int(remaining / 1)

    print(remaining)

    return result


print(to_arab('MDCCCLVI'))
print(to_roman(1856))
