def decode(code):
    letter_to_number = {
        2: "ABC",
        3: "DEF",
        4: "GHI",
        5: "JKL",
        6: "MNO",
        7: "PQRS",
        8: "TUV",
        9: "WXYZ",
    }

    decoded_string = ""
    lower_code = code.lower()

    for index in range(0, len(lower_code)):
        for key, value in letter_to_number.items():
            lower_value = value.lower()

            if lower_code[index] in lower_value:
                decoded_string += str(key)
                break
        else:
            decoded_string += lower_code[index]

    return decoded_string


print(decode("vini"))
