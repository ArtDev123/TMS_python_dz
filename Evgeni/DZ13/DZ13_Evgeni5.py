from abc import ABC, abstractmethod


class Strategy(ABC):
    """Абстрактная стратегия."""

    @abstractmethod
    def execute(self, first: float, second: float) -> float:
        """Выполняет математическую операцию."""


class Addition(Strategy):
    """Стратегия сложения."""

    def execute(self, first: float, second: float) -> float:
        return first + second


class Subtraction(Strategy):
    """Стратегия вычитания."""

    def execute(self, first: float, second: float) -> float:
        return first - second


class Multiplication(Strategy):
    """Стратегия умножения."""

    def execute(self, first: float, second: float) -> float:
        return first * second


class Division(Strategy):
    """Стратегия деления."""

    def execute(self, first: float, second: float) -> float:
        if second == 0:
            raise ValueError("Деление на ноль невозможно.")

        return first / second


class Calculator:
    """Калькулятор, использующий паттерн 'Стратегия'."""

    def __init__(self) -> None:
        self._strategy: Strategy | None = None

    def set_strategy(self, strategy: Strategy) -> None:
        """Устанавливает стратегию вычисления."""
        self._strategy = strategy

    def calculate(self, first: float, second: float) -> float:
        """Выполняет вычисление с помощью выбранной стратегии."""
        if self._strategy is None:
            raise ValueError("Стратегия не выбрана.")

        return self._strategy.execute(first, second)


def main() -> None:
    """Запуск программы."""
    calculator = Calculator()

    calculator.set_strategy(Addition())
    print(calculator.calculate(10, 5))

    calculator.set_strategy(Subtraction())
    print(calculator.calculate(10, 5))

    calculator.set_strategy(Multiplication())
    print(calculator.calculate(10, 5))

    calculator.set_strategy(Division())
    print(calculator.calculate(10, 5))


if __name__ == "__main__":
    main()
