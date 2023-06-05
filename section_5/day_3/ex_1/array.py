# Joining two arrays:
array = [1, 2, 3, 4]
other_array = [5, 6, 7, 8]
new_array = array + other_array

print(new_array)

print("-------")

print("Has number 5:", 5 in new_array)
print("Has number 9:", 9 in new_array)

print("Number of time the number 1 repeats:", new_array.count(1))


# Two dimensional array:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("----------")
print("index[1][1]:", matrix[1][1])
print("----------")

del matrix[2][2]
print("deleting index[2][2]:", matrix)
