# Vytvorte program na analyyovani textu .
# 1) ridici funkci main ve ktere se pomoci printu
# vypise pocet slov se zvolenou delkou slova a prvnich 5 slov s nejcastejsim vyskytem
# 2) Vytvorte 3 pomocne funkce:
# - text_cleaner, ktera zbavy text necistot a vraci list slov
# - number_of_words_with_specific_len, ktera rekne kolik slov s urcenou delkou mame v textu
# - most_frekquent_words, ktera vrati list slov s nejcastejsim vyskytem.

import string


def text_cleaner(text: str):
    # Tato funkce vraci list vycisteneho textu od punkci
    text = text.split()
    text_list = [word.strip(string.punctuation) for word in text]
    return text_list


def words_len(text_list: list, search_len: int):
    # vytvori list slov se specifickou delkou / vystup je list
    text_list_len = [word  for word in text_list if len(word) == search_len]
    return text_list_len


def most_frekquent_words(text_list: list):
    """Nejcastejsi slova"""
    counter = 0
    my_dict = {}
    top_list = []
    for word in text_list:
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] += 1

    top_list_values = my_dict.values()
    top_list_values = sorted(top_list_values)[:4]
    for word in my_dict:
        if my_dict[word] in top_list_values:
            top_list.append(word)
    return top_list


def main():

    text = input("Zadej text z internetu: ")
    search_len = int(input("Zadej delku slov, ktera hledas: "))
    text_list = text_cleaner(text)

    text_list_len = words_len(text_list, search_len)
    total_number = len(text_list_len)

    top_list = most_frekquent_words(text_list)

    print(f"Pocet slov s delkou: {search_len} je: {total_number}, Nejcastejsi slova: {top_list}")


if __name__ == '__main__':
    main()
