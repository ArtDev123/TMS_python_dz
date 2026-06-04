from __future__ import annotations
from typing import Literal

Meal = Literal["nectar", "grass"]


class BeeElephant:
    """Пара: первая часть — пчела, вторая — слон.

    Значения хранятся в диапазоне [0, 100]. При инициализации и при
    изменениях происходит валидация и приведение к этому диапазону.
    """

    def __init__(self, bee: int, elephant: int) -> None:
        if not isinstance(bee, int) or not isinstance(elephant, int):
            raise TypeError("bee и elephant должны быть целыми числами")
        self.__bee: int = self.__clamp(bee)
        self.__elephant: int = self.__clamp(elephant)

    @staticmethod
    def __clamp(value: int) -> int:
        """Ограничить значение в диапазоне [0, 100]."""
        if value < 0:
            return 0
        if value > 100:
            return 100
        return value

    @property
    def bee(self) -> int:
        """Текущая часть пчелы (readonly)."""
        return self.__bee

    @property
    def elephant(self) -> int:
        """Текущая часть слона (readonly)."""
        return self.__elephant

    def fly(self) -> bool:
        """True, если часть пчелы не меньше части слона, иначе False."""
        return self.__bee >= self.__elephant

    def trumpet(self) -> str:
        """Возвращает звук трубы в зависимости от отношения частей."""
        if self.__elephant >= self.__bee:
            return "tu-tu-doo-doo"
        return "wzzzz"

    def eat(self, meal: Meal, value: int) -> None:
        """Съесть meal с величиной value.

        meal может быть только "nectar" или "grass".
        Если meal == "nectar": value вычитается из слона и добавляется пчеле.
        Если meal == "grass": наоборот.
        Значения всегда остаются в диапазоне [0, 100].
        """
        if not isinstance(value, int):
            raise TypeError("value должен быть целым числом")
        if value < 0:
            raise ValueError("value не может быть отрицательным")

        if meal == "nectar":
            self.__elephant = self.__clamp(self.__elephant - value)
            self.__bee = self.__clamp(self.__bee + value)
            return

        if meal == "grass":
            self.__bee = self.__clamp(self.__bee - value)
            self.__elephant = self.__clamp(self.__elephant + value)
            return

        raise ValueError("meal должен быть 'nectar' или 'grass'")

    def __repr__(self) -> str:
        return f"BeeElephant(bee={self.__bee}, elephant={self.__elephant})"


if __name__ == "__main__":
    be = BeeElephant(40, 30)
    print(be)
    print("fly:", be.fly())
    print("trumpet:", be.trumpet())

    be.eat("nectar", 20)
    print(be)

    be.eat("grass", 200)
    print(be)
