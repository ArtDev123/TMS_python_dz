from homeWorks.patterns.builder.pizza import Pizza
from typing import Any, Self


class PizzaBuilder:
    def __init__(self) -> None:
        self.pizza = Pizza()

    def set_size(self, size: Any) -> Self:
        self.pizza.size = size
        return self

    def set_cheese(self, cheese: Any) -> Self:
        self.pizza.cheese = cheese
        return self

    def set_pepperoni(self, pepperoni: Any) -> Self:
        self.pizza.pepperoni = pepperoni
        return self

    def set_mushrooms(self, mushrooms: Any) -> Self:
        self.pizza.mushrooms = mushrooms
        return self

    def set_onions(self, onions: Any) -> Self:
        self.pizza.onions = onions
        return self

    def set_beacon(self, bacon: Any) -> Self:
        self.pizza.bacon = bacon
        return self

    def build(self) -> Pizza:
        return self.pizza
