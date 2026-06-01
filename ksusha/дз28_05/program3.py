from typing import Self


class Pizza:
    def __init__(self, size: str = None, cheese: bool = False, pepperoni: bool = False,
                 mushrooms: bool = False, onions: bool = False, bacon: bool = False) -> None:
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self) -> str:
        toppings = []
        if self.cheese:
            toppings.append("сыр")
        if self.pepperoni:
            toppings.append("пепперони")
        if self.mushrooms:
            toppings.append("грибы")
        if self.onions:
            toppings.append("лук")
        if self.bacon:
            toppings.append("бекон")

        if not toppings:
            return f"Пицца {self.size}: без начинки"
        return f"Пицца {self.size}: {', '.join(toppings)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_size(self, size: str) -> Self:
        self.pizza.size = size
        return self

    def add_cheese(self) -> Self:
        self.pizza.cheese = True
        return self

    def add_pepperoni(self) -> Self:
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self) -> Self:
        self.pizza.mushrooms = True
        return self

    def add_onions(self) -> Self:
        self.pizza.onions = True
        return self

    def add_bacon(self) -> Self:
        self.pizza.bacon = True
        return self


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder) -> None:
        self.builder = builder

    def make_pizza(self, size: str,
                   cheese: bool = False,
                   pepperoni: bool = False,
                   mushrooms: bool = False,
                   onions: bool = False,
                   bacon: bool = False) -> Pizza:

        self.builder.add_size(size)
        if cheese:
            self.builder.add_cheese()
        if pepperoni:
            self.builder.add_pepperoni()
        if mushrooms:
            self.builder.add_mushrooms()
        if onions:
            self.builder.add_onions()
        if bacon:
            self.builder.add_bacon()

        return self.builder.pizza


builder = PizzaBuilder()
director = PizzaDirector(builder)
pizza1 = director.make_pizza(size="большая",
                             cheese=True,
                             pepperoni=True,
                             bacon=True)

print(pizza1)
