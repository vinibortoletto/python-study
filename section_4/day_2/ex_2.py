# Crie um algoritmo não recursivo para contar quantos
# números pares existem em uma sequência numérica (1 a n).
def count_even_number(number):
    counter = 0

    for number in range(number + 1):
        if number % 2 == 0 and number != 0:
            counter += 1

    print(counter)


# count_even_number(5)


# Transforme o algoritmo criado acima em recursivo.
def recursive_count_even_number(number):
    if number == 1:
        return 0
    elif number % 2 == 0:
        return 1 + recursive_count_even_number(number - 1)
    else:
        return recursive_count_even_number(number - 1)


# print(recursive_count_even_number(5))


# Crie um algoritmo recursivo que encontre, em uma lista, o
# maior número inteiro.
def find_greater_integer(number_list):
    list_length = len(number_list)

    if list_length == 1:
        return number_list[0]

    last_index = list_length - 1
    last_number = number_list[last_index]
    penultimate_number = number_list[last_index - 1]

    if last_number > penultimate_number:
        number_list.remove(penultimate_number)
        return find_greater_integer(number_list)
    else:
        number_list.remove(last_number)
        return find_greater_integer(number_list)


print(find_greater_integer([1, 21, 300, 4, 57]))
