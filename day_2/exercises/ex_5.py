name = input("Type your name: ")

# for letter in name:
#     print(name)
#     letters = [char for char in name]
#     letters.pop()
#     name = "".join(letters)

while name:
    print(name)
    name = name[:-1]
