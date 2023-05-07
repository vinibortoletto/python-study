class Calculator:
    def sum(self, x, y):
        return x + y


class CalculatorDecorator:
    def __init__(self, calculator):
        self.calculator = calculator

    def convert_number_to_int(self, number):
        if not isinstance(number, str):
            return number

        number_dict = {
            "um": 1,
            "dois": 2,
            "três": 3,
            "quatro": 4,
            "cinco": 5,
            "seis": 6,
            "sete": 7,
            "oito": 8,
            "nove": 9,
            "dez": 10,
        }

        return number_dict.get(number.lower())

    def sum(self, x, y):
        int_x = self.convert_number_to_int(x)
        int_y = self.convert_number_to_int(y)
        return self.calculator.sum(int_x, int_y)


class CalculatorDecoratorEnglish:
    def __init__(self, calculator):
        self.calculator = calculator

    def convert_number_to_int(self, number):
        if not isinstance(number, str):
            return number

        number_dict = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
        }

        return number_dict.get(number)

    def sum(self, x, y):
        int_x = self.convert_number_to_int(x)
        int_y = self.convert_number_to_int(y)
        return self.calculator.sum(int_x, int_y)


if __name__ == "__main__":
    calculator = Calculator()
    print("10 + 20 = ", calculator.sum(10, 20))

    calculator_decorator = CalculatorDecorator(calculator)
    print("oito + dois = ", calculator_decorator.sum("oito", "dois"))

    calculator_decorator_english = CalculatorDecoratorEnglish(calculator)
    print("nine + one = ", calculator_decorator_english.sum("nine", "one"))
