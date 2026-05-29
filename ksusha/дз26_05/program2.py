from enum import Enum


class Status(Enum):
    NECTAR = "nectar"
    GRASS = "grass"


class Beeelefant:
    def __init__(self, bee_part: int, elefant_part: int) -> None:
        self.bee_part = bee_part
        self.elefant_part = elefant_part

    def fly(self) -> bool:
        return self.bee_part > self.elefant_part

    def trumpet(self) -> str:
        if self.bee_part <= self.elefant_part:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal: Status, value: int) -> str:
        if not isinstance(meal, Status):
            raise ValueError
        if meal == Status.NECTAR:
            more = self.bee_part
            less = self.elefant_part
        else:
            less = self.bee_part
            more = self.elefant_part

        less -= value
        more += value

        if less < 0:
            less = 0
        if more > 100:
            more = 100

        if meal == Status.NECTAR:
            self.bee_part = more
            self.elefant_part = less
        else:
            self.bee_part = less
            self.elefant_part = more

        return f"Пчела: {self.bee_part}, Слон: {self.elefant_part}"


see = Beeelefant(5, 4)

print(see.trumpet())

print(see.eat(Status.NECTAR, 211))
