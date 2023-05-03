# def get_number_list(number):
#     counter = 1
#     number_list = []

#     while counter <= number:
#         if counter % 3 == 0 and counter % 5 == 0:
#             number_list.append("FizzBuzz")
#         elif counter % 3 == 0:
#             number_list.append("Fizz")
#         elif counter % 5 == 0:
#             number_list.append("Buzz")
#         else:
#             number_list.append(counter)

#         counter += 1

#     return number_list


def get_number_list(number):
    number_list = []

    for counter in range(1, number + 1):
        if counter % 15 == 0:
            number_list.append("FizzBuzz")
        elif counter % 3 == 0:
            number_list.append("Fizz")
        elif counter % 5 == 0:
            number_list.append("Buzz")
        else:
            number_list.append(counter)

    return number_list
