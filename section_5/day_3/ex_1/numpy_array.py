import numpy as np

# define an empty array of integers
my_array = np.array([], dtype=int)

my_array = np.insert(my_array, 0, 5)
my_array = np.insert(my_array, 1, 3)
my_array = np.insert(my_array, 2, 5)
print("After insert:", my_array)

my_array = np.insert(my_array, 1, 4)
print("after insert:", my_array)

my_array = np.delete(my_array, 0)
print("after delete:", my_array)
