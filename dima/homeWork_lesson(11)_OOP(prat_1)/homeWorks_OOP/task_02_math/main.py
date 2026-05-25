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
    math_obj = Math()

    math_obj.addition(4, 5)
    math_obj.subtraction(4, 5)
    math_obj.multiplication(4, 5)
    math_obj.division(4, 5)
