from typing import Tuple, Union, Any

Numeric = Union[int, float]


class Math:
    """Класс для простых арифметических операций с печатью результата."""

    def __init__(self) -> None:
        """Инициализация без атрибутов."""
        return None

    def _validate(self, a: Any, b: Any) -> Tuple[Numeric, Numeric]:
        """Проверяет, что a и b — числа (int или float).

        Raises:
            TypeError: если любой из аргументов не является числом.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Аргументы должны быть int или float")
        return a, b

    def addition(self, a: Numeric, b: Numeric) -> None:
        """Сложение a и b и печать результата."""
        x, y = self._validate(a, b)
        result = x + y
        print(f"Результат сложения: {result}")

    def subtraction(self, a: Numeric, b: Numeric) -> None:
        """Вычитание b из a и печать результата."""
        x, y = self._validate(a, b)
        result = x - y
        print(f"Результат вычитания: {result}")

    def multiplication(self, a: Numeric, b: Numeric) -> None:
        """Умножение a на b и печать результата."""
        x, y = self._validate(a, b)
        result = x * y
        print(f"Результат умножения: {result}")

    def division(self, a: Numeric, b: Numeric) -> None:
        """Деление a на b и печать результата; обрабатывает деление на ноль."""
        x, y = self._validate(a, b)
        if y == 0:
            print("Ошибка: деление на ноль")
            return
        result = x / y
        print(f"Результат деления: {result}")


if __name__ == "__main__":
    m = Math()
    m.addition(3, 2)
    m.subtraction(3.5, 1)
    m.multiplication(4, 2.5)
    m.division(10, 2)
    m.division(1, 0)
