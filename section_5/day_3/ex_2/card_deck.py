import random


def shuffle_deck(deck):
    middle = len(deck) // 2
    first_half = deck[:middle]
    second_half = deck[middle:]

    random.shuffle(first_half)
    random.shuffle(second_half)

    return first_half + second_half


print(shuffle_deck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
