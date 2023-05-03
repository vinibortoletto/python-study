number_list = input("Type your numbers. Add a space to separate them: ")


number_list = number_list.split(" ")
sum = 0

for number in number_list:
    if number == "":
        number_list.remove(number)

    elif number != "" and number.isdigit() == False:
        print(f"Number {number} is invalid")

    else:
        sum += int(number)


print(sum)
