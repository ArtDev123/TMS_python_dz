class Operation:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Addition(Operation):

    def execute(self) -> float:
        return self.x + self.y


class Subtraction(Operation):

    def execute(self) -> float:
        return self.x - self.y


class Multiplication(Operation):

    def execute(self) -> float:
        return self.x * self.y


class Division(Operation):

    def execute(self) -> float:
        if self.y == 0:
            raise ZeroDivisionError("Ошибка! Деление на ноль")
        return self.x / self.y


class Calculator:
    def __init__(self) -> None:
        self.strategy = None

    def set_strategy(self, strategy: 'Operation') -> None:
        self.strategy = strategy

    def calculate(self) -> float:
        if self.strategy:
            return self.strategy.execute()
        raise ValueError("Стратегия не выбрана")


Calcula = Calculator()
Calcula.set_strategy(Division(2, 3))
print(Calcula.calculate())
