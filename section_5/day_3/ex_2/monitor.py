def calc_max_working_time(collected_values):
    counter = 0
    max = 0

    for value in collected_values:
        if value == 1:
            counter += 1
        else:
            counter = 0

        if counter > max:
            max = counter

    return max


print(calc_max_working_time([0, 1, 1, 1, 0, 0, 1, 1]))
print(calc_max_working_time([1, 1, 1, 1, 1, 1, 0, 0, 1, 1]))
