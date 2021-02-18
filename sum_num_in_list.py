import re


def count_only_num(data: list) -> float:
    suma = 0
    for item in data:

        if type(item) == int or type(item) == float or type(item) == bool:
            suma += item
            continue

        elif type(item) == str:
            b = re.findall(r'\d+', item)
            if b:
                for index, x in enumerate(b):
                    suma += float(b[index])
            continue
        elif type(item) == list:
            suma += count_only_num(item)
    return suma


if __name__ == '__main__':
    data = [4, 6, 8, 14, 900, "5", "ahoj", 34, True, "ddjj5", ["5", 7, True, "ddh5"]]

    print(count_only_num(data))