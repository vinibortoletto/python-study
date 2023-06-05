import sys
from array import array

my_array = array("I")

my_array.insert(0, 5)
my_array.insert(1, 3)
my_array.insert(2, 5)

print("Items inserted:", my_array)

my_array.pop(0)
print("Items removed:", my_array)

elements = list(range(100))
print("List size:", sys.getsizeof(elements))
array_from_list = array("i", elements)
print("Array size:", sys.getsizeof(array_from_list))
