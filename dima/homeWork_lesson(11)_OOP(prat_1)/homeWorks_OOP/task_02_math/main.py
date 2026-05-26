class Math:
    @staticmethod
    def addition(a: int | float, b: int | float) -> None:
        print(a + b)

    @staticmethod
    def subtraction(a: int | float, b: int | float) -> None:
        print(a - b)

    @staticmethod
    def multiplication(a: int | float, b: int | float) -> None:
        print(a * b)

    @staticmethod
    def division(a: int | float, b: int | float) -> None:
        try:
            print(a / b)
        except ZeroDivisionError:
            print("На ноль делить нельзя")


if __name__ == "__main__":
    Math.addition(4, 5)
    Math.subtraction(4, 5)
    Math.multiplication(4, 5)
    Math.division(4, 5)
