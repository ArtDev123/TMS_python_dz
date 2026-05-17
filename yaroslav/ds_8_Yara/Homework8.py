# 1

try:
    weight = float(input("Введите вес(кг)"))
    heaght_cm = float(input("введите рост(см)"))

    heaght_m = heaght_cm / 100  # перевод роста в метры

    imt = weight / (heaght_m**2)
    print(f"ваш ИМТ =", imt)

    if imt < 18.9:
        print("недостаточная масса тела")
    elif 18.9 < imt < 24.9:
        print("нормальный вес")
    elif 25 < imt < 29.9:
        print("избыточная масса тела")
    elif imt > 30:
        print("ожирение")

except ZeroDivisionError as e:
    print(f"делить на ноль нельзя, ошибка: {e}")
except ValueError as e:
    print(f"введите число, ошибка: {e}")
except Exception as e:
    print(f"ошибка", {e})

    # 2


def calculate():
    print("калькулятор для операций с двумя числами")


try:

    a = float(input("первое число = "))
    operator = input("введите операцию(+, -, /, *)")
    b = float(input("второе число = "))

    if operator == "+":
        print(a + b)
    if operator == "-":
        print(a - b)
    if operator == "/":
        print(a / b)
    if operator == "*":
        print(a * b)

except ValueError as e:
    print(f"введите число, ошибка: {e}")
except ZeroDivisionError as e:
    print(f"делить на ноль нельзя", {e})
except Exception as e:
    print(f"другая ошибка", {e})

calculate()
