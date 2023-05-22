import random


def generate_random_number_list(n):
    number_list = []

    for _ in range(100):
        average = 0

        for _ in range(n):
            average += random.randrange(1, n)

        average = average / n
        number_list.append(average)

    return number_list


print(generate_random_number_list(5))
