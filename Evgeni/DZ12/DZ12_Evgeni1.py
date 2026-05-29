from __future__ import annotations

from types import NotImplementedType
from typing import Iterable, List, Optional, Sequence


class Tovar:
    """Товар с закрытыми полями: название, магазин, цена (в рублях)."""

    def __init__(self, name: str, shop: str, price: float) -> None:
        if not isinstance(name, str) or not isinstance(shop, str):
            raise TypeError("name и shop должны быть строками")
        if not isinstance(price, (int, float)):
            raise TypeError("price должен быть числом")
        if price < 0:
            raise ValueError("price не может быть отрицательным")

        self.__name: str = name
        self.__shop: str = shop
        self.__price: float = float(price)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def shop(self) -> str:
        return self.__shop

    @property
    def price(self) -> float:
        return self.__price

    def __add__(self, other: object) -> float | NotImplementedType:
        if isinstance(other, Tovar):
            return self.__price + other.__price
        if isinstance(other, (int, float)):
            return self.__price + float(other)
        return NotImplemented

    def __radd__(self, other: object) -> float | NotImplementedType:
        if isinstance(other, (int, float)):
            return float(other) + self.__price
        if isinstance(other, Tovar):
            return other.__price + self.__price
        return NotImplemented

    def __repr__(self) -> str:
        return (
            f"Tovar(name={self.__name!r}, shop={self.__shop!r}, "
            f"price={self.__price:.2f})"
        )

    def info(self) -> str:
        return f"Name: {self.__name}, Shop: {self.__shop}, Price: {self.__price:.2f} ₽"


class Sklad:
    """Склад, содержащий закрытый список товаров."""

    def __init__(self, items: Optional[Sequence[Tovar]] = None) -> None:
        self.__items: List[Tovar] = list(items) if items is not None else []

    def add_item(self, item: Tovar) -> None:
        if not isinstance(item, Tovar):
            raise TypeError("item должен быть экземпляром Tovar")
        self.__items.append(item)

    def info_by_index(self, index: int) -> str:
        try:
            item = self.__items[index]
        except IndexError as exc:
            raise IndexError("Индекс вне диапазона") from exc
        return item.info()

    def info_by_name(self, name: str) -> List[str]:
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        name_lower = name.lower()
        results: List[str] = [
            item.info() for item in self.__items if item.name.lower() == name_lower
        ]
        return results

    def get_by_name(self, name: str) -> List[Tovar]:
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        name_lower = name.lower()
        return [item for item in self.__items if item.name.lower() == name_lower]

    def sorted_by_name(self) -> List[Tovar]:
        return sorted(self.__items, key=lambda t: t.name.lower())

    def sorted_by_shop(self) -> List[Tovar]:
        return sorted(self.__items, key=lambda t: t.shop.lower())

    def sorted_by_price(self, reverse: bool = False) -> List[Tovar]:
        return sorted(self.__items, key=lambda t: t.price, reverse=reverse)

    def __len__(self) -> int:
        return len(self.__items)

    def __iter__(self) -> Iterable[Tovar]:
        return iter(self.__items)

    def __repr__(self) -> str:
        return f"Sklad({self.__items!r})"


if __name__ == "__main__":
    a = Tovar("Мёд", "Пчёлкин", 250.0)
    b = Tovar("Мёд", "Улучшенный", 320.5)
    c = Tovar("Слоновый корм", "Зоомаг", 199.9)

    sklad = Sklad([a, b])
    sklad.add_item(c)

    print("Все товары на складе:")
    for item in sklad:
        print(" ", item)

    print("\nДлина склада:", len(sklad))

    print("\nИнформация по индексу 1:")
    print(" ", sklad.info_by_index(1))

    print("\nПоиск по имени 'мёд':")
    for info in sklad.info_by_name("мёд"):
        print(" ", info)

    print("\nТовары, отсортированные по цене (по убыванию):")
    for item in sklad.sorted_by_price(reverse=True):
        print(" ", item.info())

    total_price = sum(sklad)
    print(f"\nОбщая стоимость всех товаров: {total_price:.2f} ₽")

    print("Мёд + 100 =", a + 100)
    print("100 + Мёд =", 100 + a)
