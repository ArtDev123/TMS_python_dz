class Car:
    def __init__(self,
                 car: str,
                 type: str,
                 year: int):
        self.car = car
        self.type = type
        self.year = year

    @staticmethod
    def start_auto() -> None:
        print("Автомобиль заведён")

    @staticmethod
    def stop_auto() -> None:
        print("Автомобиль заглушен")

    def set_auto_year(self, car_year: int) -> None:
        self.year = car_year

    def set_auto_type(self, car_type: str) -> None:
        self.type = car_type

    def set_auto_color(self, car_color: str) -> None:
        self.car = car_color


if __name__ == "__main__":
    car = Car("black", "sedan", 2020)

    car.start_auto()
    car.stop_auto()

    car.set_auto_color("красная")
    car.set_auto_type("купе")
    car.set_auto_year(2023)

    print(f"Ваша машина цвета {car.car.title()}"
          f" в кузове {car.type.title()}"
          f" сделана в {car.year}г.")
