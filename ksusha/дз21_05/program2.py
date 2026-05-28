class Math:
    def addition(self, x: float, y: float) -> None:
        print(x+y)

    def subtraction(self, x: float, y: float) -> None:
        print(x-y)

    def multiplication(self, x: float, y: float) -> None:
        print(x*y)

    def division(self, x: float, y: float) -> float:
        try:
            res = x/y
        except ZeroDivisionError as mistake:
            print(f"Ошибка {mistake}")
        return res


math_obj = Math()

while (True):
    print("Меню\n1. Сложить два числа\n"
    "2.Вычесть одно число из другого\n"
    "3.Перемножить два числа\n"
    "4.Разделить одно число на другое\n"
    "5.Выход из программы")
    choice = input("Введите номер того, что хотите сделать: ")

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Неверный ввод, введите целое число от 1 до 5")
        continue

    x = int(input("Введите x"))
    y = int(input("Введите y"))
    print("Результат работы программы: ", end="")
    match choice:
        case "1":

            math_obj.addition(x, y)

        case "2":
            math_obj.subtraction(x, y)

        case "3":
            math_obj.multiplication(x, y)

        case "4":
            math_obj.division(x, y)

        case "5":
            break
    print("\n")
