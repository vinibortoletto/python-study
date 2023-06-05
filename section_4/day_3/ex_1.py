from random import shuffle


ordenados = list(range(100))
inversamente_ordenados = list(reversed(range(100)))
aleatorios = ordenados[:]  # copia dos ordenados
shuffle(aleatorios)  # embaralha eles


def selection_sort(array):
    for index in range(len(array)):
        minimum = index

        for sub_index in range(index + 1, len(array)):
            if array[sub_index] < array[minimum]:
                minimum = sub_index

        array[minimum], array[index] = array[index], array[minimum]

    return array


def insertion_sort(array):
    for i in range(len(array)):
        current_value = array[i]
        current_position = i

        while current_position > 0 and array[current_position - 1] > current_value:
            array[current_position] = array[current_position - 1]
            current_position = current_position - 1

        array[current_position] = current_value

    return array
