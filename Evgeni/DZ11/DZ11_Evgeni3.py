class Car:
    """Класс автомобиля с атрибутами color, type и year."""

    def __init__(self, color: str, type_: str, year: int) -> None:
        """Инициализация автомобиля.

        Внимание: параметр конструктора назван type_ чтобы не скрывать
        встроенную функцию type(), но атрибут сохраняется как self.type.
        """
        if not isinstance(color, str):
            raise TypeError("color must be a str")
        if not isinstance(type_, str):
            raise TypeError("type must be a str")
        if not isinstance(year, int):
            raise TypeError("year must be an int")

        self.color: str = color
        self.type: str = type_
        self.year: int = year

    def start(self) -> None:
        """Запустить автомобиль (печатает сообщение)."""
        print("Автомобиль заведён")

    def stop(self) -> None:
        """Отключить автомобиль (печатает сообщение)."""
        print("Автомобиль заглушен")

    def set_year(self, year: int) -> None:
        """Присвоить год выпуска."""
        if not isinstance(year, int):
            raise TypeError("year must be an int")
        self.year = year

    def set_type(self, type_: str) -> None:
        """Присвоить тип автомобиля."""
        if not isinstance(type_, str):
            raise TypeError("type must be a str")
        self.type = type_

    def set_color(self, color: str) -> None:
        """Присвоить цвет автомобиля."""
        if not isinstance(color, str):
            raise TypeError("color must be a str")
        self.color = color


if __name__ == "__main__":
    car = Car("красный", "седан", 2020)
    car.start()
    car.stop()
    car.set_year(2021)
    car.set_type("купе")
    car.set_color("синий")
    print(car.color, car.type, car.year)
