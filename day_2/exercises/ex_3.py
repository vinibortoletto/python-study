file = open("students.txt", mode="w")

student_list = [
    "Marcos 10\n",
    "Felipe 4\n",
    "José 6\n",
    "Ana 10\n",
    "Maria 9\n",
    "Miguel 5\n",
]

file.writelines(student_list)

file.close()

print("File created")
