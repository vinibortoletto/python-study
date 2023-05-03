# # Lists
# fruits = ["orange", "apple", "grape", "pineapple"]
# print(fruits[0])
# print(fruits[-1])
# fruits.append("strawberry")
# fruits.remove("apple")
# fruits.extend(["pear", "kiwi"])
# fruits.index("banana")
# fruits.sort()

# trybe_course = ["Introdução", "Front-end", "Back-end"]
# trybe_course.append("Ciência da computação")
# trybe_course[0] = "Fundamentos"

# # Tuples
# user = ("Vinicius", "Bortoletto", 29)
# user[0]

# # Sets
# permissions = {"member", "group"}
# permissions.add("root")
# permissions.add("root")  # won't add duplicates
# permissions.union({"user"})
# permissions.intersection({"user"}, "member")
# permissions.difference({"user"})


# Dicts
# def ex_8_9():
#     info = {
#         "personagem": "Margarida",
#         "origem": "Pato Donald",
#         "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
#     }

#     info.update({"recorrente": "Sim"})
#     del info["origem"]
#     print(info)


# ex_8_9()

# Range
# print(list(range(5)))
# print(list(range(1, 6)))
# print(list(range(1, 11, 2)))
# print(list(range(10, 0, -1)))

# Loops
# number = 10
# counter = 1
# result = 1

# while counter <= number:
#     result *= counter
#     counter += 1
# result

# print(result)
# ----------------------------
# number = 10
# result = 1

# for factor in range(1, number + 1):
#     result *= factor

# print(result)

# ratings = [6, 8, 5, 9, 10]
# new_ratings = []

# for rating in ratings:
#     new_ratings.append(rating * 10)

# print(new_ratings)
# ----------------------------
# ratings = [6, 8, 5, 9, 10]
# new_ratings = [10 * rating for rating in ratings]
# print(new_ratings)
#
# for rating in new_ratings:
# if rating % 3 == 0:
# print(f"{rating} é múltiplo de 3")


# ----------------------------
# def get_greater_num(n1, n2):
#     if n1 > n2:
#         return n1
#     return n2


# print(get_greater_num(10, 20))
# ----------------------------
# def average_from_list(list):
#     return sum(list) / len(list)


# print(average_from_list([1, 2, 3, 4, 5]))
# ----------------------------
# def print_square(number):
# for row in range(number):
# print(number * "*")
#
#
# print_square(5)
# ----------------------------
# def print_longest_name(nameList):
#     longest_name = ""

#     for name in nameList:
#         if len(name) > len(longest_name):
#             longest_name = name

#     print(longest_name)


# print_longest_name(["Vinicius", "Felipe", "Isabela"])
# ----------------------------
# def calc_paint(area):
#     cover_area_by_liter = 3
#     required_liters = area / cover_area_by_liter
#     required_cans = required_liters // 18
#     can_price = 80

#     if required_liters % 18:
#         required_cans += 1

#     return required_cans, required_cans * can_price


# print(calc_paint(20))
# ----------------------------
# Exercício 1: Dada uma lista, descubra o menor elemento. Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2.


def print_lower_number(number_list):
    number_list.sort()
    print(number_list[0])


number_list = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]
print_lower_number(number_list)
