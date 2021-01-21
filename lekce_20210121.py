# # Vytvorte program na analyyovani textu .
# # 1) ridici funkci main ve ktere se pomoci printu
# # vypise pocet slov se zvolenou delkou slova a prvnich 5 slov s nejcastejsim vyskytem
# # 2) Vytvorte 3 pomocne funkce:
# # - text_cleaner, ktera zbavy text necistot a vraci list slov
# # - number_of_words_with_specific_len, ktera rekne kolik slov s urcenou delkou mame v textu
# # - most_frekquent_words, ktera vrati list slov s nejcastejsim vyskytem.
#
# import string
#
#
# def text_cleaner(text: str):
#     # Tato funkce vraci list vycisteneho textu od punkci
#     return [word.strip(string.punctuation) for word in text.split()]
#
#
# def words_len(text_list: list, search_len: int):
#     # vytvori list slov se specifickou delkou / vystup je list
#     return len([word for word in text_list if len(word) == search_len])
#
#
# def most_frekquent_words(text_list: list):
#     """Nejcastejsi slova"""
#     my_dict, top_list = {}, []
#
#     for word in text_list:
#         if word not in my_dict:
#             my_dict[word] = 1
#         else:
#             my_dict[word] += 1
#
#     top_list_values = sorted(my_dict.values())[:4]
#
#     for word in my_dict:
#         if my_dict[word] in top_list_values:
#             top_list.append(word)
#     return top_list
#
#
# def main():
#
#     text = input("Zadej text z internetu: ")
#     search_len = int(input("Zadej delku slov, ktera hledas: "))
#     text_list = text_cleaner(text)
#
#     total_number = words_len(text_list, search_len)
#
#     top_list = most_frekquent_words(text_list)
#
#     print(f"Pocet slov s delkou: {search_len} je: {total_number}, Nejcastejsi slova: {top_list}")
#
#
# if __name__ == '__main__':
#     main()

# ======= hangman ========

import string
import random


def word_choice():
    text = input('Zedej text z ktereho vyberu slovo pro Hangmana: ')
    word = random.choice([word.strip(string.punctuation) for word in text.split() if len(word) >= 5])
    return word


def print_ui(state, your_name, counter):
    state = ''.join(state)
    print('-' * (len(state) + len(your_name) + 28))
    print(f'HRAC: {your_name} | STAV: {state} | ZBYVA: {counter} |')
    print('-' * (len(state) + len(your_name) + 28))
    return


def game(word, state, letter):
    for index, char in enumerate(word):
        if char == letter:
            state[index] = letter + ' '
    return state


def main():
    word = word_choice().lower()
    word_list = [char + ' ' for char in word]
    state = ['_ ' for i in range(len(word))]
    counter = int(len(word) * 1.5)

    your_name = input('ZADEJ TVE JMENO: ')
    print_ui(state, your_name, counter)
    while counter:
        letter = input('Zadej pismeno: ')
        state = game(word, state, letter)
        if word_list == state:
            print('winner')
            exit()
        counter -= 1
        print_ui(state, your_name, counter)
    print('looser', word)


if __name__ == '__main__':
    main()
