file = open("new_file.txt", mode="w")

file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")

print("Line from print", file=file)

lines = ["Line 1 from array\n", "Line 2 from array\n"]
file.writelines(lines)

print("File created")

file.close()
