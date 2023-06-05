def calc_combination(list):
    num_of_combinations = 0

    for index in range(1, len(list)):
        current_item = list[index]

        for sub_index in range(index):
            previous_item = list[sub_index]

            if current_item == previous_item:
                num_of_combinations += 1

    return num_of_combinations


print(calc_combination([1, 1, 2, 3]))
