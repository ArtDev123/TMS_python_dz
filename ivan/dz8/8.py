def calculator() -> None:

    while True:
        try:
            num1_input = input(
                "\nВведите первое число (или 'exit' для выхода): "
            ).strip()

            if num1_input.lower() == "exit":
                print("Выход из программы. До свидания!")
                break

            num1 = float(num1_input)

            operation = input("Введите операцию (+, -, *, /, **, %, //): ").strip()

            valid_operations = ["+", "-", "*", "/", "**", "%", "//"]
            if operation not in valid_operations:
                raise ValueError(
                    f"Неизвестная операция {operation}."
                    "Используйте одну из: {', '.join(valid_operations)}"
                )

            num2_input = input("Введите второе число: ").strip()
            num2 = float(num2_input)

            result = None

            if operation == "+":
                result = num1 + num2
                operation_name = "Сложение"
            elif operation == "-":
                result = num1 - num2
                operation_name = "Вычитание"
            elif operation == "*":
                result = num1 * num2
                operation_name = "Умножение"
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно!")
                result = num1 / num2
                operation_name = "Деление"
            elif operation == "**":
                if abs(num2) > 1000:
                    raise ValueError("Степень слишком велика (максимум 1000)")
                result = num1**num2
                operation_name = "Возведение в степень"
            elif operation == "%":
                if num2 == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно!")
                result = num1 % num2
                operation_name = "Остаток от деления"
            elif operation == "//":
                if num2 == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно!")
                result = num1 // num2
                operation_name = "Целочисленное деление"
                print(operation_name)

            print(f"{num1} {operation} {num2} = {result}")

        except ValueError as e:
            print(f"\n ОШИБКА ВВОДА: {e}")
            print("Пожалуйста, введите корректные числовые значения.")
        except ZeroDivisionError as e:
            print(f"\n ОШИБКА ДЕЛЕНИЯ: {e}")
        except OverflowError:
            print("\n ОШИБКА: Результат слишком велик для вычисления!")
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем. До свидания!")
            break
        except Exception as e:
            print(f"\n НЕОЖИДАННАЯ ОШИБКА: {e}")
            print("Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    calculator()
