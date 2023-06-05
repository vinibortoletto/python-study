class ArrayList:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def get(self, index):
        return self.data[index]

    def set(self, index, value):
        self.data.insert(index, value)

    def update(self, index, value):
        self.data[index] = value


array = ArrayList()
array.set(0, "Vinicius")
array.set(1, "Bortoletto")

print(array.get(0))
print(array.get(1))
print("----------")

index = 0

while index < len(array):
    print(array.get(index))
    index += 1
