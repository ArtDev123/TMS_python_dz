from dataclasses import dataclass


@dataclass
class Pizza:
    """Класс пиццы."""

    size: str = ""
    cheese: bool = False
    pepperoni: bool = False
    mushrooms: bool = False
    onions: bool = False
    bacon: bool = False


class PizzaBuilder:
    """Строитель пиццы."""

    def __init__(self) -> None:
        self._pizza = Pizza()

    def set_size(self, size: str) -> "PizzaBuilder":
        self._pizza.size = size
        return self

    def add_cheese(self) -> "PizzaBuilder":
        self._pizza.cheese = True
        return self

    def add_pepperoni(self) -> "PizzaBuilder":
        self._pizza.pepperoni = True
        return self

    def add_mushrooms(self) -> "PizzaBuilder":
        self._pizza.mushrooms = True
        return self

    def add_onions(self) -> "PizzaBuilder":
        self._pizza.onions = True
        return self

    def add_bacon(self) -> "PizzaBuilder":
        self._pizza.bacon = True
        return self

    def build(self) -> Pizza:
        pizza = self._pizza
        self._pizza = Pizza()
        return pizza


class PizzaDirector:
    """Директор для создания пиццы."""

    def __init__(self, builder: PizzaBuilder) -> None:
        self._builder = builder

    def make_pizza(self) -> Pizza:
        return (
            self._builder
            .set_size("Large")
            .add_cheese()
            .add_pepperoni()
            .add_mushrooms()
            .build()
        )


def main() -> None:
    """Запуск программы."""
    builder = PizzaBuilder()
    director = PizzaDirector(builder)

    pizza = director.make_pizza()

    print(pizza)


if __name__ == "__main__":
    main()