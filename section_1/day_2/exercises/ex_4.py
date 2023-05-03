reproved_students = []

with open("students.txt") as grades_file:
    for line in grades_file:
        student_grade = line
        student_grade = student_grade.split(" ")

        if int(student_grade[1]) < 6:
            reproved_students.append(student_grade[0] + "\n")

with open("reproved_students.txt", mode="w") as reproved_students_file:
    print(reproved_students)
    reproved_students_file.writelines(reproved_students)
